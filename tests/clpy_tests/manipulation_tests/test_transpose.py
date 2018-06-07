import unittest

import clpy
from clpy import testing


@testing.gpu
class TestTranspose(unittest.TestCase):

    _multiprocess_can_split_ = True

    @testing.numpy_clpy_array_equal()
    def test_rollaxis(self, xp):
        a = testing.shaped_arange((2, 3, 4), xp)
        return xp.rollaxis(a, 2)

    def test_rollaxis_failure(self):
        a = testing.shaped_arange((2, 3, 4))
        with self.assertRaises(ValueError):
            clpy.rollaxis(a, 3)

    @testing.numpy_clpy_array_equal()
    def test_swapaxes(self, xp):
        a = testing.shaped_arange((2, 3, 4), xp)
        return xp.swapaxes(a, 2, 0)

    def test_swapaxes_failure(self):
        a = testing.shaped_arange((2, 3, 4))
        with self.assertRaises(ValueError):
            clpy.swapaxes(a, 3, 0)

    @testing.numpy_clpy_array_equal()
    def test_transpose(self, xp):
        a = testing.shaped_arange((2, 3, 4), xp)
        return a.transpose(-1, 0, 1)

    @testing.numpy_clpy_array_equal()
    def test_transpose_empty(self, xp):
        a = testing.shaped_arange((2, 3, 4), xp)
        return a.transpose()

    @testing.numpy_clpy_array_equal()
    def test_transpose_none(self, xp):
        a = testing.shaped_arange((2, 3, 4), xp)
        return a.transpose(None)

    @testing.numpy_clpy_array_equal()
    def test_external_transpose(self, xp):
        a = testing.shaped_arange((2, 3, 4), xp)
        return xp.transpose(a, (-1, 0, 1))

    @testing.numpy_clpy_array_equal()
    def test_external_transpose_all(self, xp):
        a = testing.shaped_arange((2, 3, 4), xp)
        return xp.transpose(a)
