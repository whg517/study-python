from tarfile import TarFile
from tempfile import NamedTemporaryFile


def tar_file():
    tmp_file = NamedTemporaryFile()
    tar_op = TarFile.open(mode='w:gz', fileobj=tmp_file)
    tar_op.add('demo.py')
    tar_op.close()
    tmp_file.close()


def sum_(x, y):
    return x + y


class A:

    def add(self, x, y):
        print(f'Add: {x}, {y}')
        return sum_(x, y)
