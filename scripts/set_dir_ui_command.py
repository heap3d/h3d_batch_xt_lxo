# modo python
# EMAG
# set directory for cad files UI command
# ================================

from h3d_utilites.scripts.h3d_utils import (
    get_user_value,
    set_user_value,
    get_directory,
)

CAD_FILES_DIR_USER_VALUE_NAME = 'h3d_cxtl_cad_files_dir'


def set_directory_ui_value(user_value_name: str) -> None:
    old_path = get_user_value(user_value_name)
    path = get_directory('Set directory for cad files', old_path)
    if path == old_path:
        return
    set_user_value(user_value_name, path)


def main():
    set_directory_ui_value(CAD_FILES_DIR_USER_VALUE_NAME)


if __name__ == "__main__":
    main()
