# читает числа до символа конца файла и выводит их квадраты

def interact():
    print('hello stream world')   # выводит в sys.stdout

    while True:
        try:
            reply = input('Enter a number >')   # выводит в sys.stdin
        except EOFError:
            break           # исключение при встрече символа eof
        else:
            num = int(reply)
            print('%d squared is %d' % (num, num ** 2))
    print('Bye')

if __name__ == '__main__':
    interact()