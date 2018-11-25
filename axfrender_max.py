import MaxPlus
import sys
import json
import os

sys.path.append('F:/!!_WORK_!!/!!__VV__!!/scripts/BruDigital/Scripts/axfrender/project')

import axfrender_common as funcs
import axfrender_config as conf

data = []
log_out = []
axf_numbers = []
texunitsize = 10.0
displacement = 'on'
displacement_scale_factor = 1.0

funcs.wait_file_open(conf.BUFFER_FILE)

err, readed_data = funcs.read_data_from_file(conf.BUFFER_FILE)

if err:
    log_out.append(str(err))

if not readed_data:
   log_out.append('not output data in buffer file')
    
if log_out:
    funcs.write_data_to_file('\n'.join(log_file), LOG_FILE)

MaxPlus.Core.EvalMAXScript ('loadMaxFile "{file_name}"'.format(file_name = readed_data[2]))

#funcs.remove_file(conf.BUFFER_FILE)

axf_numbers = [int(elem.split('_')[-1].split('-')[0]) for elem in readed_data[0]]
rfile_base_name = readed_data[0][0].rsplit('_',1)[0].split('/')[-1] + '_.jpg'
rfile_base_dir = readed_data[0][0].rsplit('/',3)[0] + '/' + conf.RENDER_DIR_NAME

# Add keyframes to MaterialID modifier
def create_keys(axf_numbers):
    #Delete keys from Material modifier animation curve first
    cmd = 'deleteKeys {}.modifiers[#Material].materialID.controller #allKeys'.format(conf.MAX_OBJECT_NAME)
    MaxPlus.Core.EvalMAXScript(cmd)

    for i, val in enumerate(axf_numbers):
        # form maxscript command
        cmd = 'with animate on at time {time} setControllerValue {obj} {ind} true #absolute \n' \
                  '{obj}.keys.inTangentType = #step'
        MaxPlus.Core.EvalMAXScript(cmd.format(time=val,
                                                obj=conf.MAX_OBJECT_NAME+'.modifiers[#Material].materialID.controller',
                                                ind=i + 1))

# Adjust scene materials according to the existing axf files inside axf_directory
def adjust_mats(axf_list):

    for i, val in enumerate(axf_list):
        mat_name = 'Material_{}____XriteAxFMtl'.format(str(i+1)) 
        cmd = 'rootScene[#SME][(#View1)][#{material}].Properties.reference.filename = "{axf}" \n' \
                  'rootScene[#SME][(#View1)][#{material}].Properties.reference.texunitsize = {tex} \n' \
                  'rootScene[#SME][(#View1)][#{material}].Properties.reference.displacement = {disp} \n' \
                  'rootScene[#SME][(#View1)][#{material}].Properties.reference.displacement_scale_factor = {disp_rate}'
        command = cmd.format(material=mat_name,
                                axf=val,
                                tex=texunitsize,
                                disp=displacement,
                                disp_rate=displacement_scale_factor)

        MaxPlus.Core.EvalMAXScript(command)

# Adjust RP Manager passes - frames, output path
# for more information regarding RPManager maxscript commands, check Help and forum
# http://www.rpmanager.com/documentation/dokuwiki/doku.php?id=mxs:maxscript_access
# http://www.jellybiscuits.com/phpBB3rpm/viewtopic.php?f=6&t=54
def adjust_rp_passes(pass_list, frames_string):
    rpass_count = MaxPlus.Core.EvalMAXScript('rpmdata.getpasscount()').Get()
    for i in range(1,rpass_count+1):
        pass_name = MaxPlus.Core.EvalMAXScript('RPMdata.GetPassName {}'.format(i)).Get()

        if pass_name not in pass_list:
          continue

        output_path = rfile_base_dir + '/' + pass_name
        if not os.path.exists(output_path):
            # creating dir check must be present
            os.makedirs(output_path)

        output_file = output_path + '/' + rfile_base_name
        cmd = ('rpmdata.rmopenfloater() \n'\
                'RPMdata.SetPassOutputPath {index} "{path}" \n'\
                'RPMData.RMModifyValues 46 numbarray: #({index}) input: "{frames}" \n'\
                'RPMData.RMModifyValues 2 numbarray: #({index}) input: 4 \n'\
                'RPMdata.RMrefresh()').\
                format(index=i, path=output_file, frames=frames_string)
        # add start render
        MaxPlus.Core.EvalMAXScript(cmd)

create_keys(axf_numbers)

adjust_mats(readed_data[0])

adjust_rp_passes(readed_data[1], str(axf_numbers).strip('[]'))

#MaxPlus.Core.EvalMAXScript ('quitMAX #noPrompt')








