from unittest import TestCase, mock
from unittest.mock import Mock

from library_reference.unittest_.demo import tar_file, A


class TestDemo(TestCase):

    @mock.patch('tarfile.TarFile')
    def test_tar_file(self, mocker):
        tar_file()

    @mock.patch('library_reference.unittest_.demo.A')
    def test_add(self, mocker):
        mocker.add = Mock(return_value=10)
        a = A()
        res = a.add(1, 1)
        self.assertEqual(res, 10)
