# modo python
# EMAG
# set directory for cad files UI command
# ================================

import os

import modo

from h3d_utilites.scripts.h3d_utils import (
    get_user_value,
    set_user_value,
)

CAD_FILES_DIR_USER_VALUE_NAME = 'h3d_cxtl_cad_files_dir'


def set_directory_ui_value(user_value_name: str) -> None:
    old_path = get_user_value(user_value_name)
    path = get_files_directory('Set directory for cad files', old_path)
    if path == old_path:
        return
    set_user_value(user_value_name, path)


def get_files_directory(title: str, old_path: str) -> str:
    result = modo.dialogs.fileOpen('', title, True, old_path)

    if not result:
        return old_path

    dir_path = os.path.dirname(result[0])

    return dir_path


def main():
    set_directory_ui_value(CAD_FILES_DIR_USER_VALUE_NAME)


if __name__ == "__main__":
    main()
