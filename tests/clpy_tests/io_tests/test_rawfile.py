import unittest

from clpy import testing


@testing.gpu
class TestRawfile(unittest.TestCase):

    _multiprocess_can_split_ = True
