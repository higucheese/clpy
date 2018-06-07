import unittest

import itertools
import numpy

import clpy
from clpy import testing


def perm(iterable):
    return list(itertools.permutations(iterable))


@testing.parameterize(
    *testing.product({
        'shape': [(4, 4, 4)],
        'indexes': (
            perm(([1, 0], slice(None))) +
            perm(([1, 0], Ellipsis)) +
            perm(([1, 2], None, slice(None))) +
            perm(([1, 0], 1, slice(None))) +
            perm(([1, 2], slice(0, 2), slice(None))) +
            perm((1, [1, 2], 1)) +
            perm(([[1, -1], [0, 3]], slice(None), slice(None))) +
            perm(([1, 0], [3, 2], slice(None))) +
            perm((slice(0, 3, 2), [1, 2], [1, 0])) +
            perm(([1, 0], [2, 1], [3, 1])) +
            perm(([1, 0], 1, [3, 1])) +
            perm(([1, 2], [[1, 0], [0, 1], [-1, 1]], slice(None))) +
            perm((None, [1, 2], [1, 0])) +
            perm((numpy.array(0), numpy.array(-1))) +
            perm((numpy.array(0), None)) +
            perm((1, numpy.array(2), slice(None)))
        )
    })
)
@testing.gpu
class TestArrayAdvancedIndexingGetitemPerm(unittest.TestCase):

    @testing.for_all_dtypes()
    @testing.numpy_clpy_array_equal()
    def test_adv_getitem(self, xp, dtype):
        a = testing.shaped_arange(self.shape, xp, dtype)
        return a[self.indexes]


@testing.parameterize(
    {'shape': (2, 3, 4), 'indexes': numpy.array(-1)},
    {'shape': (2, 3, 4), 'indexes': (None, [1, 0], [0, 2], slice(None))},
    {'shape': (2, 3, 4), 'indexes': (None, [0, 1], None, [2, 1], slice(None))},
    {'shape': (2, 3, 4), 'indexes': numpy.array([1, 0])},
    {'shape': (2, 3, 4), 'indexes': [1, -1]},
    {'shape': (2, 3, 4), 'indexes': ([0, 1], slice(None), [[2, 1], [3, 1]])},
    # mask
    {'shape': (10,), 'indexes': (numpy.random.choice([False, True], (10,)),)},
    {'shape': (2, 3, 4),
     'indexes': (numpy.random.choice([False, True], (2, 3, 4)),)},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), numpy.array([True, False, True]))},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), slice(None),
                 numpy.array([True, False, False, True]))},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), numpy.random.choice([False, True], (3, 4)))},
    {'shape': (2, 3, 4),
     'indexes': numpy.random.choice([False, True], (2, 3))},
    # empty arrays
    {'shape': (2, 3, 4), 'indexes': []},
    {'shape': (2, 3, 4), 'indexes': numpy.array([], dtype=numpy.int32)},
    {'shape': (2, 3, 4), 'indexes': [[]]},
    {'shape': (2, 3, 4), 'indexes': numpy.array([[]], dtype=numpy.int32)},
    {'shape': (2, 3, 4), 'indexes': [[[]]]},
    {'shape': (2, 3, 4), 'indexes': [[[[]]]]},
    {'shape': (2, 3, 4, 5), 'indexes': [[[[]]]]},
    {'shape': (2, 3, 4, 5), 'indexes': [[[[[]]]]]},
    {'shape': (2, 3, 4), 'indexes': (slice(None), [])},
    {'shape': (2, 3, 4), 'indexes': ([], [])},
    {'shape': (2, 3, 4), 'indexes': ([[]],)},
    {'shape': (2, 3, 4), 'indexes': numpy.array([], dtype=numpy.bool)},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), numpy.array([], dtype=numpy.bool))},
    {'shape': (2, 3, 4), 'indexes': numpy.array([[], []], dtype=numpy.bool)},
    # list indexes
    {'shape': (2, 3, 4), 'indexes': [1]},
    {'shape': (2, 3, 4), 'indexes': [1, 1]},
    {'shape': (2, 3, 4), 'indexes': [[1]]},
    {'shape': (2, 3, 4), 'indexes': [[1, 1]]},
    {'shape': (2, 3, 4), 'indexes': [[1], [1]]},
    {'shape': (2, 3, 4), 'indexes': [[1, 1], 1]},
    {'shape': (2, 3, 4), 'indexes': [[1], slice(1, 2)]},
    {'shape': (2, 3, 4), 'indexes': [[[1]], slice(1, 2)]},
    # zero-dim and zero-sized arrays
    {'shape': (), 'indexes': Ellipsis},
    {'shape': (), 'indexes': ()},
    {'shape': (), 'indexes': None},
    # TODO(niboshi): pass the following commented out tests
    # {'shape': (), 'indexes': True},
    # {'shape': (), 'indexes': (True,)},
    # {'shape': (), 'indexes': (False, True, True)},
    # {'shape': (), 'indexes': numpy.array([True])},
    # {'shape': (), 'indexes': numpy.array([False, True, True])},
    {'shape': (), 'indexes': numpy.ones((), dtype=numpy.bool_)},
    {'shape': (), 'indexes': numpy.zeros((), dtype=numpy.bool_)},
    {'shape': (0,), 'indexes': None},
    {'shape': (0,), 'indexes': ()},
    # TODO(niboshi): pass the following commented out tests
    # {'shape': (0,), 'indexes': True},
    # {'shape': (0,), 'indexes': (True,)},
    # {'shape': (0,), 'indexes': (False, True, True)},
    # {'shape': (0,), 'indexes': numpy.array([True])},
    # {'shape': (0,), 'indexes': numpy.array([False, True, True])},
    # {'shape': (0,), 'indexes': numpy.ones((), dtype=numpy.bool_)},
    # {'shape': (0,), 'indexes': numpy.zeros((), dtype=numpy.bool_)},
)
@testing.gpu
class TestArrayAdvancedIndexingGetitemParametrized(unittest.TestCase):

    @testing.for_all_dtypes()
    @testing.numpy_clpy_array_equal()
    def test_adv_getitem(self, xp, dtype):
        a = testing.shaped_arange(self.shape, xp, dtype)
        return a[self.indexes]


@testing.parameterize(
    {'shape': (2, 3, 4), 'transpose': (1, 2, 0),
     'indexes': (slice(None), [1, 0])},
    {'shape': (2, 3, 4), 'transpose': (1, 0, 2),
     'indexes': (None, [1, 2], [0, -1])},
)
@testing.gpu
class TestArrayAdvancedIndexingGetitemParametrizedTransp(unittest.TestCase):

    @testing.for_all_dtypes()
    @testing.numpy_clpy_array_equal()
    def test_adv_getitem(self, xp, dtype):
        a = testing.shaped_arange(self.shape, xp, dtype)
        if self.transpose:
            a = a.transpose(self.transpose)
        return a[self.indexes]


@testing.gpu
class TestArrayAdvancedIndexingGetitemCupyIndices(unittest.TestCase):

    shape = (2, 3, 4)

    def test_adv_getitem_clpy_indices1(self):
        a = clpy.zeros(self.shape)
        index = clpy.array([1, 0])
        original_index = index.copy()
        b = a[index]
        b_cpu = a.get()[index.get()]
        testing.assert_array_equal(b, b_cpu)
        testing.assert_array_equal(original_index, index)

    def test_adv_getitem_clpy_indices2(self):
        a = clpy.zeros(self.shape)
        index = clpy.array([1, 0])
        original_index = index.copy()
        b = a[(slice(None), index)]
        b_cpu = a.get()[(slice(None), index.get())]
        testing.assert_array_equal(b, b_cpu)
        testing.assert_array_equal(original_index, index)

    def test_adv_getitem_clpy_indices3(self):
        a = clpy.zeros(self.shape)
        index = clpy.array([True, False])
        original_index = index.copy()
        b = a[index]
        b_cpu = a.get()[index.get()]
        testing.assert_array_equal(b, b_cpu)
        testing.assert_array_equal(original_index, index)

    def test_adv_getitem_clpy_indices4(self):
        a = clpy.zeros(self.shape)
        index = clpy.array([4, -5])
        original_index = index.copy()
        b = a[index]
        b_cpu = a.get()[index.get() % self.shape[1]]
        testing.assert_array_equal(b, b_cpu)
        testing.assert_array_equal(original_index, index)

    def test_adv_getitem_clpy_indices5(self):
        a = clpy.zeros(self.shape)
        index = clpy.array([4, -5])
        original_index = index.copy()
        b = a[[1, 0], index]
        b_cpu = a.get()[[1, 0], index.get() % self.shape[1]]
        testing.assert_array_equal(b, b_cpu)
        testing.assert_array_equal(original_index, index)


@testing.parameterize(
    {'shape': (), 'indexes': (-1,)},
    {'shape': (), 'indexes': (0,)},
    {'shape': (), 'indexes': (1,)},
    {'shape': (), 'indexes': ([0],)},
    {'shape': (), 'indexes': (numpy.array([0]),)},
    {'shape': (), 'indexes': (numpy.array(0),)},
    {'shape': (), 'indexes': ([False],)},
    {'shape': (0,), 'indexes': (-1,)},
    {'shape': (0,), 'indexes': (0,)},
    {'shape': (0,), 'indexes': (1,)},
    # TODO(niboshi): pass the following commented out tests
    # {'shape': (0,), 'indexes': ([0],)},
    # {'shape': (0,), 'indexes': (numpy.array([0]),)},
    # {'shape': (0,), 'indexes': (numpy.array(0),)},
    # {'shape': (0,), 'indexes': ([False],)},
    {'shape': (0, 1), 'indexes': (0, Ellipsis)},
    {'shape': (2, 3), 'indexes': (slice(None), [1, 2], slice(None))},
    {'shape': (2, 3), 'indexes': numpy.array([], dtype=numpy.float)},
    {'shape': (2, 3, 4), 'indexes': [1, [1, [1]]]},
)
@testing.gpu
class TestArrayInvalidIndexAdvGetitem(unittest.TestCase):

    @testing.for_all_dtypes()
    @testing.numpy_clpy_raises()
    def test_invalid_adv_getitem(self, xp, dtype):
        a = testing.shaped_arange(self.shape, xp, dtype)
        a[self.indexes]


@testing.parameterize(
    # array only
    {'shape': (2, 3, 4), 'indexes': numpy.array(-1), 'value': 1},
    {'shape': (2, 3, 4), 'indexes': numpy.array([1, 0]), 'value': 1},
    {'shape': (2, 3, 4), 'indexes': [1, -1], 'value': 1},
    {'shape': (2, 3, 4), 'indexes': (slice(None), [1, 2]), 'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), [[1, 2], [0, -1]],), 'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), slice(None), [[1, 2], [0, 2]]), 'value': 1},
    # slice and array
    {'shape': (2, 3, 4),
     'indexes': (slice(None), slice(1, 2), [[1, 2], [0, 2]]), 'value': 1},
    # None and array
    {'shape': (2, 3, 4),
     'indexes': (None, [1, -1]), 'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (None, [1, -1], None), 'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (None, None, None, [1, -1]), 'value': 1},
    # None, slice and array
    {'shape': (2, 3, 4),
     'indexes': (slice(0, 1), None, [1, -1]), 'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (slice(0, 1), slice(1, 2), [1, -1]), 'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (slice(0, 1), None, slice(1, 2), [1, -1]), 'value': 1},
    # mask
    {'shape': (2, 3, 4),
     'indexes': numpy.array([True, False]), 'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), numpy.array([True, False, True])), 'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), slice(None),
                 numpy.random.choice([False, True], (4,))),
     'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (numpy.random.choice([False, True], (2, 3)),), 'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), numpy.random.choice([False, True], (3, 4)),),
     'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (numpy.random.choice([False, True], (2, 3, 4)),), 'value': 1},
    # multiple arrays
    {'shape': (2, 3, 4), 'indexes': ([0, -1], [1, -1]), 'value': 1},
    {'shape': (2, 3, 4),
     'indexes': ([0, -1], [1, -1], [2, 1]), 'value': 1},
    {'shape': (2, 3, 4), 'indexes': ([0, -1], 1), 'value': 1},
    {'shape': (2, 3, 4), 'indexes': ([0, -1], slice(None), [1, -1]),
     'value': 1},
    {'shape': (2, 3, 4), 'indexes': ([0, -1], 1, 2), 'value': 1},
    {'shape': (2, 3, 4), 'indexes': ([1, 0], slice(None), [[2, 0], [3, 1]]),
     'value': 1},
    # multiple arrays and basic indexing
    {'shape': (2, 3, 4), 'indexes': ([0, -1], None, [1, 0]), 'value': 1},
    {'shape': (2, 3, 4), 'indexes': ([0, -1], slice(0, 2), [1, 0]),
     'value': 1},
    {'shape': (2, 3, 4), 'indexes': ([0, -1], None, slice(0, 2), [1, 0]),
     'value': 1},
    {'shape': (1, 1, 2, 3, 4),
     'indexes': (None, slice(None), slice(None), [1, 0], [2, -1], 1),
     'value': 1},
    {'shape': (1, 1, 2, 3, 4),
     'indexes': (None, slice(None), 0, [1, 0], slice(0, 2, 2), [2, -1]),
     'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), [0, -1], [[1, 0], [0, 1], [-1, 1]]), 'value': 1},
    # empty arrays
    {'shape': (2, 3, 4), 'indexes': [], 'value': 1},
    {'shape': (2, 3, 4), 'indexes': [],
     'value': numpy.array([1, 1, 1, 1])},
    {'shape': (2, 3, 4), 'indexes': [],
     'value': numpy.random.uniform(size=(3, 4))},
    {'shape': (2, 3, 4), 'indexes': numpy.array([], dtype=numpy.int32),
     'value': 1},
    {'shape': (2, 3, 4), 'indexes': [[]],
     'value': 1},
    {'shape': (2, 3, 4), 'indexes': numpy.array([[]], dtype=numpy.int32),
     'value': numpy.random.uniform(size=(3, 4))},
    {'shape': (2, 3, 4), 'indexes': [[[]]],
     'value': 1},
    {'shape': (2, 3, 4), 'indexes': [[[[]]]],
     'value': 1},
    {'shape': (2, 3, 4, 5), 'indexes': [[[[]]]],
     'value': 1},
    {'shape': (2, 3, 4, 5), 'indexes': [[[[[]]]]],
     'value': 1},
    {'shape': (2, 3, 4), 'indexes': (slice(None), []),
     'value': 1},
    {'shape': (2, 3, 4), 'indexes': ([], []),
     'value': 1},
    {'shape': (2, 3, 4), 'indexes': numpy.array([], dtype=numpy.bool),
     'value': 1},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), numpy.array([], dtype=numpy.bool)),
     'value': 1},
    {'shape': (2, 3, 4), 'indexes': numpy.array([[], []], dtype=numpy.bool),
     'value': numpy.random.uniform(size=(4,))},
    # list indexes
    {'shape': (2, 3, 4), 'indexes': [1, 0], 'value': 1},
    {'shape': (2, 3, 4), 'indexes': [[1]], 'value': 1},
    {'shape': (2, 3, 4), 'indexes': [[1, 0]], 'value': 1},
    {'shape': (2, 3, 4), 'indexes': [[1], [0]], 'value': 1},
    {'shape': (2, 3, 4), 'indexes': [[1, 0], 2], 'value': 1},
    {'shape': (2, 3, 4), 'indexes': [[1], slice(1, 2)], 'value': 1},
    {'shape': (2, 3, 4), 'indexes': [[[1]], slice(1, 2)], 'value': 1},
    # zero-dim and zero-sized arrays
    {'shape': (), 'indexes': Ellipsis, 'value': 1},
    {'shape': (), 'indexes': (), 'value': 1},
    {'shape': (), 'indexes': None, 'value': 1},
    # TODO(niboshi): pass the following commented out tests
    # {'shape': (), 'indexes': True, 'value': 1},
    # {'shape': (), 'indexes': (True,), 'value': 1},
    # {'shape': (), 'indexes': (False, True, True), 'value': 1},
    # {'shape': (), 'indexes': numpy.array([True]), 'value': 1},
    # {'shape': (), 'indexes': numpy.array([False, True, True]), 'value': 1},
    {'shape': (), 'indexes': numpy.ones((), dtype=numpy.bool_), 'value': 1},
    {'shape': (), 'indexes': numpy.zeros((), dtype=numpy.bool_), 'value': 1},
    {'shape': (0,), 'indexes': None, 'value': 1},
    {'shape': (0,), 'indexes': (), 'value': 1},
    # TODO(niboshi): pass the following commented out tests
    # {'shape': (0,), 'indexes': True, 'value': 1},
    # {'shape': (0,), 'indexes': (True,), 'value': 1},
    # {'shape': (0,), 'indexes': (False, True, True), 'value': 1},
    # {'shape': (0,), 'indexes': numpy.array([True]), 'value': 1},
    # {'shape': (0,), 'indexes': numpy.array([False, True, True]), 'value': 1},
    # {'shape': (0,), 'indexes': numpy.ones((), dtype=numpy.bool_),
    #  'value': 1},
    # {'shape': (0,), 'indexes': numpy.zeros((), dtype=numpy.bool_),
    #  'value': 1},
)
@testing.gpu
class TestArrayAdvancedIndexingSetitemScalarValue(unittest.TestCase):

    @testing.for_all_dtypes()
    @testing.numpy_clpy_array_equal()
    def test_adv_setitem(self, xp, dtype):
        a = xp.zeros(self.shape, dtype=dtype)
        a[self.indexes] = self.value
        return a


@testing.parameterize(
    {'shape': (2, 3, 4), 'indexes': numpy.array(1),
     'value': numpy.array([1])},
    {'shape': (2, 3, 4), 'indexes': numpy.array(1),
     'value': numpy.array([1, 2, 3, 4])},
    {'shape': (2, 3, 4), 'indexes': (slice(None), [0, -1]),
     'value': numpy.arange(2 * 2 * 4).reshape(2, 2, 4)},
    {'shape': (2, 3, 4), 'indexes': (slice(None), [[0, 1], [2, 0]]),
     'value': numpy.arange(2 * 2 * 2 * 4).reshape(2, 2, 2, 4)},
    # mask
    {'shape': (2, 3, 4), 'indexes': numpy.random.choice([False, True], (2, 3)),
     'value': numpy.arange(4)},
    {'shape': (2, 3, 4),
     'indexes': (slice(None), numpy.array([True, False, True])),
     'value': numpy.arange(2 * 2 * 4).reshape(2, 2, 4)},
    {'shape': (2, 3, 4),
     'indexes': (numpy.array([[True, False, False], [False, True, True]]),),
     'value': numpy.arange(3 * 4).reshape(3, 4)},
    {'shape': (2, 2, 2),
     'indexes': (slice(None), numpy.array([[True, False], [False, True]]),),
     'value': numpy.arange(2 * 2).reshape(2, 2)},
    {'shape': (2, 2, 2),
     'indexes': (numpy.array(
         [[[True, False], [True, False]], [[True, True], [False, False]]]),),
     'value': numpy.arange(4)},
    {'shape': (5,),
     'indexes': numpy.array([True, False, False, True, True]),
     'value': numpy.arange(3)},
    # multiple arrays
    {'shape': (2, 3, 4), 'indexes': ([1, 0], [2, 1]),
     'value': numpy.arange(2 * 4).reshape(2, 4)},
    {'shape': (2, 3, 4), 'indexes': ([1, 0], slice(None), [2, 1]),
     'value': numpy.arange(2 * 3).reshape(2, 3)},
    {'shape': (2, 3, 4), 'indexes': ([1, 0], slice(None), [[2, 0], [3, 1]]),
     'value': numpy.arange(2 * 2 * 3).reshape(2, 2, 3)},
    {'shape': (2, 3, 4),
     'indexes': ([[1, 0], [1, 0]], slice(None), [[2, 0], [3, 1]]),
     'value': numpy.arange(2 * 2 * 3).reshape(2, 2, 3)},
    {'shape': (2, 3, 4),
     'indexes': (1, slice(None), [[2, 0], [3, 1]]),
     'value': numpy.arange(2 * 2 * 3).reshape(2, 2, 3)},
    # list indexes
    {'shape': (2, 3, 4), 'indexes': [1],
     'value': numpy.arange(3 * 4).reshape(3, 4)},
)
@testing.gpu
class TestArrayAdvancedIndexingVectorValue(unittest.TestCase):

    @testing.for_all_dtypes()
    @testing.numpy_clpy_array_equal()
    def test_adv_setitem(self, xp, dtype):
        a = xp.zeros(self.shape, dtype=dtype)
        a[self.indexes] = self.value.astype(a.dtype)
        return a


@testing.gpu
class TestArrayAdvancedIndexingSetitemCupyIndices(unittest.TestCase):

    shape = (2, 3)

    def test_clpy_indices_integer_array_1(self):
        a = clpy.zeros(self.shape)
        index = clpy.array([0, 1])
        original_index = index.copy()
        a[:, index] = clpy.array(1.)
        testing.assert_array_equal(
            a, clpy.array([[1., 1., 0.], [1., 1., 0.]]))
        testing.assert_array_equal(index, original_index)

    def test_clpy_indices_integer_array_2(self):
        a = clpy.zeros(self.shape)
        index = clpy.array([3, -5])
        original_index = index.copy()
        a[:, index] = clpy.array(1.)
        testing.assert_array_equal(
            a, clpy.array([[1., 1., 0.], [1., 1., 0.]]))
        testing.assert_array_equal(index, original_index)

    def test_clpy_indices_integer_array_3(self):
        a = clpy.zeros(self.shape)
        index = clpy.array([3, -5])
        original_index = index.copy()
        a[[1, 1], index] = clpy.array(1.)
        testing.assert_array_equal(
            a, clpy.array([[0., 0., 0.], [1., 1., 0.]]))
        testing.assert_array_equal(index, original_index)

    def test_clpy_indices_boolean_array(self):
        a = clpy.zeros(self.shape)
        index = clpy.array([True, False])
        original_index = index.copy()
        a[index] = clpy.array(1.)
        testing.assert_array_equal(
            a, clpy.array([[1., 1., 1.], [0., 0., 0.]]))
        testing.assert_array_almost_equal(original_index, index)


@testing.gpu
class TestArrayAdvancedIndexingSetitemDifferetnDtypes(unittest.TestCase):

    @testing.for_all_dtypes_combination(names=['src_dtype', 'dst_dtype'],
                                        no_complex=True)
    @testing.numpy_clpy_array_equal()
    def test_differnt_dtypes(self, xp, src_dtype, dst_dtype):
        shape = (2, 3)
        a = xp.zeros(shape, dtype=src_dtype)
        indexes = xp.array([0, 1])
        a[:, indexes] = xp.array(1, dtype=dst_dtype)
        return a

    @testing.for_all_dtypes_combination(names=['src_dtype', 'dst_dtype'],
                                        no_complex=True)
    @testing.numpy_clpy_array_equal()
    def test_differnt_dtypes_mask(self, xp, src_dtype, dst_dtype):
        shape = (2, 3)
        a = xp.zeros(shape, dtype=src_dtype)
        indexes = xp.array([True, False])
        a[indexes] = xp.array(1, dtype=dst_dtype)
        return a


@testing.gpu
class TestArrayAdvancedIndexingSetitemTranspose(unittest.TestCase):

    @testing.numpy_clpy_array_equal()
    def test_adv_setitem_transp(self, xp):
        shape = (2, 3, 4)
        a = xp.zeros(shape).transpose(0, 2, 1)
        slices = (numpy.array([1, 0]), slice(None), numpy.array([2, 1]))
        a[slices] = 1
        return a
