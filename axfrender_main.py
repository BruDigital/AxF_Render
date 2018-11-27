# -*- coding: utf-8 -*-
import sys
import os
from subprocess import Popen, PIPE

try:
    from PySide2 import QtCore, QtGui, QtWidgets
    from PySide2 import __version__
except ImportError:
    from PySide import QtCore, QtGui
    from PySide import __version__
    #QtWidgets = QtGui

from gui import mainWindowUI_PS
from os import path

import axfrender_config as conf
import axfrender_common as funcs
import axfrender_check as check

class mainWindow(QtGui.QMainWindow, mainWindowUI_PS.Ui_MainWindow):
    '''
    ui elements definition
    '''
    def __init__(self):
        super(mainWindow,self).__init__()
        
        self.setupUi(self)
        
        self.SecretButton.toggled.connect(self.hide_unhide_MAX_file_field)
        
        self.MaxFileName.editingFinished.connect(self.check_start_activity)
        self.MaxFileName.hide()
        self.MaxFileName.setAcceptDrops(1)
        self.MaxFileName.dragEnterEvent = self.MaxFileName_dragEnterEvent
        self.MaxFileName.dragMoveEvent = self.MaxFileName_dragMoveEvent
        self.MaxFileName.dropEvent = self.MaxFileName_dropEvent
        self.MaxFileName.setText(conf.DEFAULT_MAX_TEMPLATE)

        self.rpass_objects = []
        self.set_rpass_check_boxes(conf.RENDER_PASS_NAMES)

        self.axf_files_common_size = 0
        self.AxfFileList.setAcceptDrops(1)
        self.AxfFileList.itemDoubleClicked.connect(self.delete_AxfFileList_sel_item)
        self.AxfFileList.dragEnterEvent = self.AxfFileList_dragEnterEvent
        self.AxfFileList.dragMoveEvent = self.AxfFileList_dragMoveEvent
        self.AxfFileList.dropEvent = self.AxfFileList_dropEvent
        
        self.process = None
        self.StartRenderButton.setEnabled(0)
        self.StartRenderButton.clicked.connect(self.send_to_render)
    
    def hide_unhide_MAX_file_field(self):
        if self.SecretButton.isChecked():
            self.MaxFileName.show()
            self.SecretButton.setText('-')
        else:
            self.MaxFileName.hide()
            self.SecretButton.setText('+')

    def set_rpass_check_boxes(self, rpass_list):
        for i in rpass_list:
            check_btn = RPassCheckBox(str(i))
            check_btn.for_out_connection = self.check_start_activity
            self.rpass_objects.append(check_btn)
            self.RenderPassLayOut.addWidget(check_btn)

    def check_max_file_wgt(self):
        file_name = self.MaxFileName.text()
        if os.path.isfile(file_name) and file_name.endswith('.max'):
            return True
    
    def check_rpass_ch_boxes(self):
        for i in self.rpass_objects:
            if i.isChecked():
                return True

    def check_axf_files_list(self):
        return bool(self.AxfFileList.count())

    def check_start_activity(self):
        cond_result = self.check_max_file_wgt() and self.check_rpass_ch_boxes() and self.check_axf_files_list()
        if cond_result:
            self.StartRenderButton.setEnabled(1)
        else:
            self.StartRenderButton.setEnabled(0)

    def MaxFileName_dragEnterEvent(self, e):
        file_name = e.mimeData().urls()[0].toLocalFile()
        if e.mimeData().hasUrls() and\
            file_name.startswith('Z:') and\
            os.path.isfile(file_name) and\
            file_name.endswith('.max'):
            e.accept()
        else:
            e.ignore()

    def MaxFileName_dragMoveEvent(self, e):
        self.MaxFileName_dragEnterEvent(e)

    def MaxFileName_dropEvent(self, e):
        self.MaxFileName.setText(e.mimeData().urls()[0].toLocalFile())
        self.check_start_activity()

    def delete_AxfFileList_sel_item(self):
        self.AxfFileList.takeItem(self.AxfFileList.currentRow())
        self.check_start_activity()


    def AxfFileList_dragEnterEvent(self, e):
        for i in e.mimeData().urls():
            file_name = i.toLocalFile()
            # add chek for axf_file.rsplit('/',3)[0]
            if not (e.mimeData().hasUrls() and\
                    file_name.startswith(conf.BRU_DGTL) and\
                    os.path.isfile(file_name) and\
                    file_name.endswith('.axf')):
                e.ignore()
                return
        e.accept()

    def AxfFileList_dragMoveEvent(self, e):
        self.AxfFileList_dragEnterEvent(e)

    def AxfFileList_dropEvent(self, e):
        for i in e.mimeData().urls():
            file_name = i.toLocalFile()
            if self.AxfFileList.findItems(file_name.split('/')[-1], 1):
                continue
            
            file_size = os.path.getsize(file_name)
            self.axf_files_common_size += file_size
            if self.axf_files_common_size > conf.AXF_SIZE_LIMIT:
                self.axf_files_common_size -= file_size
                funcs.message_out('WARNING!\nAXF files size limit has exceeded\nsome files are not inserted.')
                return

            self.AxfFileList.addItem(file_name)
            if self.axf_is_rendered(file_name):
                self.AxfFileList.item(self.AxfFileList.count()-1).setForeground(QtGui.QColor('red'))

        self.check_start_activity()
    
    def axf_is_rendered(self, file_name):
        pass

    def run_max_file(self, name):
        self.process = Popen([conf.MAX_SHEll, '-u', 'PythonHost', name])

    def send_to_render(self):
        '''
        gets the data from UI and sends them to MAX
        '''
        list_of_axf = [self.AxfFileList.item(elem).text() for elem in range(self.AxfFileList.count())]
        list_of_rpases = [elem.text() for elem in self.rpass_objects if elem.isChecked()]
        templete_max_file = self.MaxFileName.text()

        funcs.write_data_to_file([list_of_axf, list_of_rpases, templete_max_file], conf.BUFFER_FILE)
        self.run_max_file(conf.MAX_PYTHON_FILE)

        self.StartRenderButton.setEnabled(0)
        
        self.process.wait()

        self.StartRenderButton.setEnabled(1)


class RPassCheckBox(QtGui.QCheckBox):
    '''
    '''
    def __init__(self, rpass_name):
        super(RPassCheckBox,self).__init__()
        self.setText(rpass_name)
        self.setChecked(0)
        self.toggled.connect(self.for_out_connection)

    def for_out_connection(self):
        '''
        must be reordered in main script
        '''
        pass

def main():
    app = QtGui.QApplication(sys.argv)
    err = check.check_initial_state()

    if err:
        funcs.message_out(err)
        return
    
    window = mainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()