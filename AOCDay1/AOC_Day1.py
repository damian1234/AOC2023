
def get_calibration_digit(coded_value):
    for index, character in enumerate(coded_value):
        if character.isdigit():
            return character

    return ''


def main():
    file_path = 'AOC_Day1_input'
    total_calibration = 0
    with open(file_path, 'r') as file:
        for line in file:
            value = line.rstrip()
            first_digit = get_calibration_digit(value)
            second_digit = get_calibration_digit(value[::-1])
            total_calibration = total_calibration + int(first_digit + second_digit)

    print(total_calibration)

if __name__ == '__main__':
    main()
