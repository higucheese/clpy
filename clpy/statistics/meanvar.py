# TODO(okuta): Implement median


# TODO(okuta): Implement average


def mean(a, axis=None, dtype=None, out=None, keepdims=False):
    """Returns the arithmetic mean along an axis.

    Args:
        a (clpy.ndarray): Array to compute mean.
        axis (int): Along which axis to compute mean. The flattened array is
            used by default.
        dtype: Data type specifier.
        out (clpy.ndarray): Output array.
        keepdims (bool): If ``True``, the axis is remained as an axis of
            size one.

    Returns:
        clpy.ndarray: The mean of the input array along the axis.

    .. seealso:: :func:`numpy.mean`

    """
    # TODO(okuta): check type
    return a.mean(axis=axis, dtype=dtype, out=out, keepdims=keepdims)


def var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False):
    """Returns the variance along an axis.

    Args:
        a (clpy.ndarray): Array to compute variance.
        axis (int): Along which axis to compute variance. The flattened array
            is used by default.
        dtype: Data type specifier.
        out (clpy.ndarray): Output array.
        keepdims (bool): If ``True``, the axis is remained as an axis of
            size one.

    Returns:
        clpy.ndarray: The variance of the input array along the axis.

    .. seealso:: :func:`numpy.var`

    """
    # TODO(okuta): check type
    return a.var(axis=axis, dtype=dtype, out=out, ddof=ddof,
                 keepdims=keepdims)


def std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False):
    """Returns the standard deviation along an axis.

    Args:
        a (clpy.ndarray): Array to compute standard deviation.
        axis (int): Along which axis to compute standard deviation. The
            flattened array is used by default.
        dtype: Data type specifier.
        out (clpy.ndarray): Output array.
        keepdims (bool): If ``True``, the axis is remained as an axis of
            size one.

    Returns:
        clpy.ndarray: The standard deviation of the input array along the axis.

    .. seealso:: :func:`numpy.std`

    """
    # TODO(okuta): check type
    return a.std(axis=axis, dtype=dtype, out=out, ddof=ddof,
                 keepdims=keepdims)


# TODO(okuta): Implement nanmean


# TODO(okuta): Implement nanstd


# TODO(okuta): Implement nanvar
