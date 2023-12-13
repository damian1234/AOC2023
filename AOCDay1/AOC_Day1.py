
def get_calibration_digit(coded_value):
    for index, character in enumerate(coded_value):
        if character.isdigit():
            coded_value = coded_value[0:index] + coded_value[index+1:]
            return (coded_value, character)

    return ('', '')


def main():
    file_path = 'AOC_Day1_input'
    total_calibration = 0
    second_digit = ''
    with open(file_path, 'r') as file:
        for line in file:
            value = line.rstrip()
            new_value, first_digit = get_calibration_digit(value)
            if new_value:
                _, second_digit = get_calibration_digit(new_value[::-1])
            num = first_digit + second_digit
            total_calibration = total_calibration + int(num)

    print(total_calibration)

if __name__ == '__main__':
    main()
