# modo python
# EMAG
# open .lxo format to modo, process geometry, save as .obj scene file
# ================================

import lx
import modo

from h3d_utilites.scripts.h3d_utils import execution_time_alarm, get_user_value

from h3d_batch_xt_lxo.scripts.convert_cad_to_lxo import FileFormat, convert_scene
from h3d_batch_xt_lxo.scripts.set_dir_ui_command import CAD_FILES_DIR_USER_VALUE_NAME


LOAD_LXO_EXT = ('.lxo',)
SAVE_OBJ_EXT = '.obj'


def open_lxo(file: str) -> None:
    lx.eval(f'!scene.open "{file}" normal')


def save_obj(file: str) -> None:
    lx.eval(f'scene.saveAs "{file}" wf_OBJ true')


@execution_time_alarm('Converting .lxo files to .obj')
def main():
    lxo_obj_handler = FileFormat(load_ext=LOAD_LXO_EXT, open_scene=open_lxo, save_ext=SAVE_OBJ_EXT, save_scene=save_obj)
    dir_path = get_user_value(CAD_FILES_DIR_USER_VALUE_NAME)

    global numfiles
    numfiles = convert_scene(dir_path, lxo_obj_handler)

    print(f'{numfiles} files processed.')


numfiles = 0
if __name__ == '__main__':
    main()
    modo.dialogs.alert('Conversion Complete', f'{numfiles} files processed.', 'OK')
