def print_formatted(num):

    width = len(bin(num))-2
    for i in range(1, num + 1):
        dec = str(i).rjust(width)
        binary = bin(num)[2:].rjust(width)
        octal = oct(num)[2:].rjust(width)
        hexa_decimal = hex(num)[2:].rjust(width)
        print(f'{dec}{octal}{hexa_decimal} {binary}')

num = int(input("Enter the num: "))

print_formatted(num)