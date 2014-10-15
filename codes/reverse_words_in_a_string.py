# coding=utf8
#

'''
created at: 2014-10-15

'''

__AUTHOR__ = 'seraphln'


def reverse_words(sentense):
    '''
    >>> reverse_words("the sky is blue")
    'blue is sky the'
    >>> reverse_words("wow in the sky")
    'sky the in wow'
    '''
    return ' '.join(sentense.split(' ')[::-1])

