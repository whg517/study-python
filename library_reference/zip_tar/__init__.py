import os
from tarfile import TarFile
from tempfile import TemporaryDirectory
from zipfile import ZipFile
import stat

base_dir = '/tmp/test'

with ZipFile(os.path.join(base_dir, 'demo.zip'), mode='r') as myzip:
    tmp_dir = TemporaryDirectory('-spiderkeeper')
    myzip.extractall(tmp_dir.name)
    print('xxx')
# tar_file = os.path.join(base_dir, 'py', 'demo_with_dir.tar.gz')
tar_file = os.path.join(base_dir, 'tools', 'demo_with_dir.tar.gz')

# with TarFile.open(tar_file, 'r:gz') as tarfile:
#     tar_files = [i for i in tarfile]
