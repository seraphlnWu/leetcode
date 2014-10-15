# coding=utf8
#

'''
created at: 2014-10-15

'''

__AUTHOR__ = 'seraphln'


def make_slice(lst):
    ''' split list by 0 or minus numbers '''
    result = []
    tmp_lst = []
    for x in lst:
        if x > 0:
            tmp_lst.append(x)
        else:
            result.append(tmp_lst)
            tmp_lst = []

    return result


def product(lst):
    return reduce(lambda x, y: x*y, lst)


def max_product_subarray(array):
    '''
    >>> max_product_subarray([2, 3, -2, 4]) 
    [2, 3]
    >>> max_product_subarray([2, 0, 3, 4, -2])
    [3, 4]
    '''
    return sorted([(x, product(x)) for x in make_slice(array)], key=lambda x: x[1], reverse=True)[0][0]


if __name__ == '__main__':
    max_product_subarray([2, 0, 3, 4, -2])