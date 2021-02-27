def bubble_sort(inputlist):
    # swap pairs of elements in order, such that after one iteration an element is in its correct place
    print('Original list: ', inputlist)
    for i in range(0, len(inputlist), 1):
        for j in range(len(inputlist)-2, i-1, -1):
            # print('i-{} | j-{}'.format(i, j))
            print('{} > {} ???'.format(inputlist[j], inputlist[j + 1]), end=' ')
            if inputlist[j] > inputlist[j + 1]:
                print('Yes', inputlist)
                temp = inputlist[j]
                inputlist[j] = inputlist[j + 1]
                inputlist[j + 1] = temp
            else:
                print('No ', inputlist)
        # for j in range(i):
        #     print('i-{} | j-{}'.format(i, j))
        print(inputlist)


def sorting():
    input_list = [2, 17, 6, 7, 0, 453, 26, 10, 70]
    bubble_sort(input_list)


sorting()
