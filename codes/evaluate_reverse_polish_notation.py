# coding=utf8
#

'''
created at: 2014-10-15

'''

__AUTHOR__ = 'seraphln'


def evaluate_reverse_polish_notation(lst):
    '''
    >>> evaluate_reverse_polish_notation(["2", "1", "+", "3", "*"])
    9
    >>> evaluate_reverse_polish_notation(["4", "13", "5", "/", "+"])
    6
    '''
    stack = []

    for x in lst:
        if x.isdigit():
            stack.append(x)
        else:
            a1 = stack.pop(-1) 
            a2 = stack.pop(-1)

            s = eval('%s%s%s' % (a2, x, a1))
            stack.insert(len(stack), s)

    return stack[0]


if __name__ == '__main__':
    evaluate_reverse_polish_notation(["4", "13", "5", "/", "+"])