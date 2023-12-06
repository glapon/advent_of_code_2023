calibration_strings = []
# open file and add each line to calibrations_strings
with open('input.txt') as input:
    for item in input.readlines():
        calibration_strings.append(item.strip('\n'))

def get_calibration_value(calibration_string):
    """
    For a given string, concatenate the first and last digit in the
    string, and return as integer.
    """
    digits = [ x for x in calibration_string if x.isdigit() ]
    return int(digits[0] + digits[-1])

sum = 0
for calibration_string in calibration_strings:
    sum += get_calibration_value(calibration_string)

print(sum)