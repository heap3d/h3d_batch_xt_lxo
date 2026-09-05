# modo python
# EMAG
# import .obj format to modo, process geometry, save as .lxo scene file
# ================================

import lx
import modo

from h3d_utilites.scripts.h3d_utils import execution_time_alarm, get_user_value

from h3d_batch_xt_lxo.scripts.convert_cad_to_lxo import FileFormat, convert_scene
from h3d_batch_xt_lxo.scripts.set_dir_ui_command import CAD_FILES_DIR_USER_VALUE_NAME


LOAD_OBJ_EXT = ('.obj',)
SAVE_LXO_EXT = '.lxo'


def open_obj(file: str) -> None:
    lx.eval('loaderOptions.wf_OBJ true false true millimeters')
    lx.eval(f'!scene.open "{file}" normal')


def save_lxo(file: str) -> None:
    lx.eval(f'scene.saveAs "{file}" $LXOB false')


@execution_time_alarm('Converting .obj files to .lxo')
def main():
    dir_path = get_user_value(CAD_FILES_DIR_USER_VALUE_NAME)
    obj_lxo_handler = FileFormat(load_ext=LOAD_OBJ_EXT, open_scene=open_obj, save_ext=SAVE_LXO_EXT, save_scene=save_lxo)

    global numfiles
    numfiles = convert_scene(dir_path, obj_lxo_handler)

    print(f'{numfiles} files processed.')


numfiles = 0
if __name__ == '__main__':
    main()
    modo.dialogs.alert('Conversion Complete', f'{numfiles} files processed.', 'OK')
