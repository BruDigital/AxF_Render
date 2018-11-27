import platform
import os

import axfrender_common as funcs
import axfrender_config as conf

def check_system():
    '''
    checks current os 
    '''
    if platform.system() is not 'Windows' and platform.release() is not 10:
        return 'Operating system is not win 10.\n'

    return ''

def check_project_path():
    '''
    checks is project dir exists
    '''
    if not os.path.isdir(conf.BRU_DGTL):
        return 'Project directory "{path}" is not exists.\n'.format(path = conf.BRU_DGTL)
    return ''

def check_3dmax():
    '''
    checks is 3d max installed
    '''
    if os.environ.get('ADSK_3DSMAX_x64_2018', '').replace('\\','/') != conf.MAX_SHEll.rsplit('/',1)[0] and\
        not os.path.isfile(conf.MAX_SHEll) :
            return 'It`s seems that Autodesk 3D studio max is not installed.\n'
    return ''

def check_template_file():
    '''
    checks is max template file exists
    '''
    if not os.path.isfile(conf.DEFAULT_MAX_TEMPLATE) :
        return 'File "{file_name}" is not exists.\n'.format(file_name = conf.DEFAULT_MAX_TEMPLATE)
    return ''

def check_RPM_loaded():
    '''
    cheks is RPManager plugin loaded
    '''
    import MaxPlus
    
    rpm_files = (r'c:\program files\autodesk\3ds max 2018\plugins\rpmpropholder.dlo',
                    r'c:\program files\autodesk\3ds max 2018\plugins\rpmmaterial.dlt',
                    r'c:\program files\autodesk\3ds max 2018\plugins\rpmframeinfo.dlv',)
    
    intersections = 0
    pluginsDlls_path = MaxPlus.PluginManager.PluginDlls

    for pd in pluginsDlls_path:
        if (pd.FilePath in rpm_files) and pd.Loaded:
            intersections+=1
        if intersections == len(rpm_files):
            return ''

    return 'It`s seems that RPManager plugin is not instulled.\n'

def check_VRay_loaded():
    '''
    cheks is VRay plugin loaded
    '''
    import MaxPlus
    
    vray_dll = r'c:\program files\autodesk\3ds max 2018\plugins\vrender2018.dlr'
    
    pluginsDlls_path = MaxPlus.PluginManager.PluginDlls

    for pd in pluginsDlls_path:
        
        if (pd.FilePath == vray_dll) and pd.Loaded :
            return ''
    
    return 'It`s seems that VRay plugin is not instulled.\n'

def check_PySide_installed():
    '''
    cheks is PySide 1 installed
    '''
    try:
        from PySide import QtCore, QtGui
        from PySide import __version__

    except ImportError:
        return 'PySide 1 is not installed.\n'

    return ''

def check_deadline_installed():
    '''
    cheks is Deadline installed
    '''
    if os.environ.get('DEADLINE_PATH', '').replace('\\','/') != conf.MAX_SHEll.rsplit('/',1)[0] and\
        not os.path.isfile(conf.DEDLINE_SHELL) :
            return 'It`s seems that Deadline is not installed.\n'
    return ''

def check_render_object():
    '''
    cheks is rendered object present in the scene
    is object has right material
    '''
    import MaxPlus
    
    err = ''
    node = MaxPlus.INode.GetINodeByName(conf.MAX_OBJECT_NAME)
    
    if not node:
        err = 'The object "{name}" not presents in the scene.\n'.format(name=conf.MAX_OBJECT_NAME)
        return err
    
    node_material = node.GetMaterial()

    if node_material.GetName() != conf.MATERIAL_NAME:
        err = 'The material "{name}" not presents on the object "{obj}".\n'.format(name=conf.MATERIAL_NAME, obj=conf.MAX_OBJECT_NAME)
        return err

    material_submat = node_material.GetSubMtl(0)
    if material_submat.GetNumSubMtls() != 50:
        err = 'The count of axfmaterials is not 50.\n'
        return err

    for m in range(material_submat.GetNumSubMtls()):
        if not material_submat.GetSubMtl(m) or material_submat.GetSubMtl(m).GetName() != conf.SUB_MATS_NAME + str(m+1):
            err = 'The name of some axfmaterials is not "{name}" or some slots are empty.\n'.format(name=conf.SUB_MATS_NAME)
            return err
    return err

def check_render_object_modifier():
    '''
    cheks does "material" modifire prethent in stack of the rendered object
    '''
    import MaxPlus
    
    node = MaxPlus.INode.GetINodeByName(conf.MAX_OBJECT_NAME)

    if not node:
        return ''

    for m in range(0,node.GetNumModifiers()):
        if node.GetModifier(m).GetName() == conf.MATERIAL_MODIFIER:
            return ''
            
    return 'The render object has not "{name}" modifier.\n'.format(name=conf.MATERIAL_MODIFIER)

def check_rpasses():
    '''
    cheks does scene render passes have standart names
    '''
    import MaxPlus
    
    rpasses = {}
    rpass_count = MaxPlus.Core.EvalMAXScript('rpmdata.getpasscount()').Get()
    if not rpass_count:
        return "Render passes are not present in the scene.\n"
    
    for i in range(1, rpass_count+1):
        pass_name = MaxPlus.Core.EvalMAXScript('RPMdata.GetPassName {}'.format(i)).Get()

        if pass_name not in conf.RENDER_PASS_NAMES:
            return 'Some of render pass does have not valid name.\n'
    return ''

def check_initial_state():
    err = ''
    err += check_system()
    err += check_project_path()
    err += check_3dmax()
    err += check_template_file()
    err += check_PySide_installed()
    err += check_deadline_installed()
    return err

def check_max_file_scene():
    err = ''
    err += check_RPM_loaded()
    if not err:
        err += check_rpasses()
    err += check_VRay_loaded()
    err += check_render_object()
    err += check_render_object_modifier()
    return err