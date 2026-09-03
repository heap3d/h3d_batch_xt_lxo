# modo python
# EMAG
# import .obj format to modo, process geometry, save as .lxo scene file
# ================================

import lx
import modo

from h3d_batch_xt_lxo.scripts.convert_cad_to_lxo import FileFormat, process_files
from h3d_batch_xt_lxo.scripts.set_dir_ui_command import CAD_FILES_DIR_USER_VALUE_NAME

from h3d_utilites.scripts.h3d_utils import execution_time_alarm, get_user_value


OBJ_EXTENSIONS = ('.obj',)


def open_obj(file: str) -> None:
    lx.eval('loaderOptions.wf_OBJ true false true millimeters')
    lx.eval(f'!scene.open "{file}" normal')


@execution_time_alarm('Converting .obj files to .lxo')
def main():
    file_format = FileFormat(extensions=OBJ_EXTENSIONS, open_file_func=open_obj)
    dir_path = get_user_value(CAD_FILES_DIR_USER_VALUE_NAME)

    global numfiles
    numfiles = process_files(dir_path, file_format)

    print(f'{numfiles} files processed.')


numfiles = 0
if __name__ == '__main__':
    main()
    modo.dialogs.alert('Conversion Complete', f'{numfiles} files processed.', 'OK')
