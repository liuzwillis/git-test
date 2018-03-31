def get_num():
    while True:
        num = input("input a number between [0, 100), quit with \'quit\' or \'exit\':  ")
        if num in ('quit','exit'):
            break
        try:
            num = int(num)
        except ValueError:
            print('not a number')
        else:
            if num in range(100):
                print('number: {}'.format(num))
            else:
                print('number {} out range'.format(num))
    return num


if __name__ == '__main__':
    get_num()

