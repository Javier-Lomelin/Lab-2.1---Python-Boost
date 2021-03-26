string_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def int_to_str(number):
    str_number = ""
    if number == 0:
        return "0"

    while number > 0:
        digit = number % 10
        number = int(number / 10)
        str_number = string_array[digit] + str_number

    return str_number


def str_to_int(string_num):
    number = 0
    for char in string_num:
        number = number * 10
        digit = string_array.index(char)
        number = number + digit

    return number


int_test_cases = [0, 2, 4, 1234, 6789, 15766654, 666, 453154, 118624, 4841]
print("")
print("int_to_str Function:")
i = 0
for value in int_test_cases:
    i = i + 1
    result = int_to_str(value)
    print("Case {0}: From {1} to '{2}'".format(i, value, result))

print("")

str_test_cases = ["0", "2", "123", "456", "789", "54131684", "654318", "161381358", "841818", "147258"]
print("")
print("str_to_int Function:")
i = 0
for value in str_test_cases:
    i = i + 1
    result = str_to_int(value)
    print("Case {0}: From '{1}' to {2}".format(i, value, result))