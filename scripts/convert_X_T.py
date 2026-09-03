# modo python
# EMAG
# import .x_t format to modo, process geometry, save as .lxo scene file
# ================================

import lx
import modo

from h3d_batch_xt_lxo.scripts.convert_cad_to_lxo import FileFormat, process_files
from h3d_batch_xt_lxo.scripts.set_dir_ui_command import CAD_FILES_DIR_USER_VALUE_NAME

from h3d_utilites.scripts.h3d_utils import execution_time_alarm, get_user_value


X_T_EXTENSIONS = ('.x_t', '.x_b',)


def open_x_t(file: str) -> None:
    lx.eval('loaderOptions.PowerTranslators Mesh Copy "Use Settings Below" 0.0 false "128 um" "0 mm" "0 mm" 0.01 0.0 0.0 Z "0 mm" false false true')
    lx.eval(f'!scene.open "{file}" normal')


@execution_time_alarm('Converting .x_t files to .lxo')
def main():
    file_format = FileFormat(extensions=X_T_EXTENSIONS, open_file_func=open_x_t)
    dir_path = get_user_value(CAD_FILES_DIR_USER_VALUE_NAME)

    global numfiles
    numfiles = process_files(dir_path, file_format)

    print(f'{numfiles} files processed.')


numfiles = 0
if __name__ == '__main__':
    main()
    modo.dialogs.alert('Conversion Complete', f'{numfiles} files processed.', 'OK')
