def count_truth(lst, ch_type):
    total = 0
    for item in lst:
        if item == ch_type:
            total += 1
    return total


'''def abs(x):
    if x < 0:
        x = -x
    return x

if __name__ == '__main__':
    assert abs(-2) == 2
    assert abs(-0) == 0
    #assert abs(2) == 2
    print('ok')'''
