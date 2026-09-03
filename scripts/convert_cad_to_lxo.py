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


@dataclass
class FileFormat:
    extensions: Iterable[str]
    open_file_func: Callable[[str], None]


def get_dir_files(path: str, ext: Iterable[str]) -> list[str]:
    return [f for f in os.listdir(path) if f.endswith(tuple(ext))]


def process_files(dir_path: str, file_format: FileFormat) -> int:
    files = get_dir_files(dir_path, file_format.extensions)

    print(f'Current directory: {dir_path}')
    if not files:
        print('No files found.')
        return 0

    for file in files:
        process_file(file, file_format, dir_path)

    return len(files)


def process_file(file: str, file_format: FileFormat, dir_path: str) -> None:
    print(f'Processing file: {file}')
    file_format.open_file_func(os.path.join(dir_path, file))

    meshref_cleanup(suppress_vmap_normals_check=True)
    check_vmap_normal_health(supress_warnings=True)
    mesh_islands_cleanup(supress_final_cleanup=True)

    lxo_scene_path = os.path.join(dir_path, os.path.splitext(file)[0] + '.lxo')
    lx.eval(f'scene.saveAs "{lxo_scene_path}" $LXOB false')
    lx.eval('scene.close')
