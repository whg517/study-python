import os
import tarfile
from _stat import filemode
from datetime import datetime
from tarfile import TarFile, TarInfo
from typing import Optional
from zipfile import ZipFile


def zip2tar(zip_file: str, tar_file, tar_mode: Optional[str] = 'w:gz'):
    """

    :param zip_file: zip file path
    :param tar_file:
                      IO(_io.IOBase): file obj
    :param tar_mode:  ref `tarfile.TarFile.open`
    :return:
    """
    zip_file = ZipFile(file=zip_file, mode='r')
    tar_file = TarFile.open(fileobj=tar_file, mode=tar_mode)

    try:
        for zip_info in zip_file.infolist():
            tar_info = TarInfo(name=zip_info.filename)
            tar_info.size = zip_info.file_size
            tar_info.mtime = datetime.now().timestamp()
            # https://stackoverflow.com/a/434689/11722440
            tar_info.mode = zip_info.external_attr >> 16

            # https://stackoverflow.com/a/18432983/11722440
            # https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
            # TODO whg fix other file (like symbolic link) in zip to regular file in tar file
            if zip_info.filename.endswith('/'):
                tar_info.type = tarfile.DIRTYPE
            else:
                tar_info.type = tarfile.REGTYPE

            infile = zip_file.open(zip_info.filename)
            tar_file.addfile(tar_info, infile)
    except Exception as e:
        raise
    finally:
        tar_file.close()
        zip_file.close()


if __name__ == '__main__':
    base_dir = '/tmp/test'
