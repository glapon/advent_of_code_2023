calibration_strings = []
# open file and add each line to calibrations_strings
with open('input.txt') as input:
    for item in input.readlines():
        calibration_strings.append(item.strip('\n'))

nums = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

# digits / numbers spelled out converted to digits as list
converted_calibration_strings = []

for calibration_string in calibration_strings:
    new_string = ''
    for i in range(len(calibration_string)):
            # for each element, if it's a digit, add it
        if calibration_string[i].isdigit():
            new_string += calibration_string[i]
            continue
        else:
            # if it's a digit spelled out, add actual number
            for word, num in nums.items():
                if calibration_string[i:].find(word) == 0:
                    new_string += num
    converted_calibration_strings.append(new_string)
                
def get_calibration_value(calibration_string):
    """
    For a given string, concatenate the first and last digit in the
    string, and return as integer.
    """
    digits = [ x for x in calibration_string if x.isdigit() ]
    return int(digits[0] + digits[-1])

sum = 0
for calibration_string in converted_calibration_strings:
    sum += get_calibration_value(calibration_string)

print(sum)