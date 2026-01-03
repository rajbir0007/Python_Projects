def caesar(message, shift, mode):
    shift = shift % 26
    temp = list(message)

    for i in range(len(temp)):
        if 97 <= ord(temp[i]) <= 122:
            if mode == "encode":
                temp[i] = chr((ord(temp[i]) - 97 + shift) % 26 + 97)
            else:
                temp[i] = chr((ord(temp[i]) - 97 - shift) % 26 + 97)

    return "".join(temp)


def main():
    ans = 'yes'
    while ans == 'yes':
        option = input('Enter "ENCODE" or "DECODE":\n').lower()
        message = input('Enter text:\n').lower()
        shift = int(input('Enter the shift number:\n'))

        if option in ['encode', 'decode']:
            print(caesar(message, shift, option))
        else:
            print("Invalid option")

        ans = input('Enter "yes" for more operations otherwise "no":\n').lower()


if __name__ == '__main__':
    main()
