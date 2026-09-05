# modo python
# EMAG
# import cad format to modo, process geometry, save as .lxo scene file
# ================================

import os
from dataclasses import dataclass
from typing import Callable, Iterable

import lx

from h3d_cad2modo.scripts.meshref_cleanup import meshref_cleanup
from h3d_cad2modo.scripts.mesh_islands_cleanup import mesh_islands_cleanup
from h3d_merge_tools.scripts.check_vmap_normal_health import check_vmap_normal_health


EXPORT_DIR = '__Converted'


@dataclass
class FileFormat:
    load_ext: Iterable[str]
    open_scene: Callable[[str], None]
    save_ext: str
    save_scene: Callable[[str], None]


def get_dir_files(path: str, ext: Iterable[str]) -> list[str]:
    return [f for f in os.listdir(path) if f.endswith(tuple(ext))]


def convert_scene(dir_path: str, file_format: FileFormat) -> int:
    files = get_dir_files(dir_path, file_format.load_ext)

    print(f'Current directory: {dir_path}')
    if not files:
        print('No files found.')
        return 0

    monitor = lx.Monitor(len((files)))
    for file in files:
        process_scene(file, file_format, dir_path)
        monitor.step()

    return len(files)


def process_scene(file: str, file_format: FileFormat, dir_path: str) -> None:
    print(f'Processing file: {file}')
    file_format.open_scene(os.path.join(dir_path, file))

    meshref_cleanup(suppress_vmap_normals_check=True)
    check_vmap_normal_health(supress_warnings=True)
    mesh_islands_cleanup(supress_final_cleanup=True)

    save_dir = os.path.join(dir_path, EXPORT_DIR)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, os.path.splitext(file)[0] + file_format.save_ext)
    print(f'Saving file: {file_path}')
    file_format.save_scene(file_path)

    lx.eval('!scene.close')
