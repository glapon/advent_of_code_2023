lines = []
# open file and add each line to lines
with open('input.txt') as input:
    for item in input.readlines():
        lines.append(item.strip('\n'))

class Number:
    def __init__(self, num, line, start, end):
        self.num=num
        self.line=line
        self.start=start
        self.end=end

    def check_right(self):
        """
        Return True if symbol is to the right of number
        """
        string = lines[self.line]
        if self.end == (len(string) - 1):
            return False

        if string[self.end + 1] != '.':
            return True
        else:
            return False
        
    def check_left(self):
        """
        Return True if symbol is to the left of number
        """
        string = lines[self.line]
        if self.start == 0:
            return False

        if string[self.start - 1] != '.':
            return True
        else:
            return False
        
    def check_same_line(self):
        line_string = lines[self.line]
        return (self.check_right() or self.check_left())
        
    def check_other_line(self, line_index):
        line_string = lines[line_index]
        first = max(self.start - 1, 0)
        last = min(self.end + 1, len(line_string) - 1)

        for i in range(first, last + 1):
            char = line_string[i]
            if not char.isdigit() and char != '.':
                return True
        return False
    
    def check_if_symbol_adjacent(self):
        if self.check_same_line():
            return True
        elif self.line > 0 and self.check_other_line(self.line - 1):
            return True
        elif self.line < len(lines) - 1 and self.check_other_line(self.line + 1):
            return True
        else:
            return False
    
    def get_num(self):
        return self.num

numbers = []

for i in range(len(lines)):
    line = lines[i]
    current_num = ''
    for j in range(len(line)):
        character = line[j]
        if character.isdigit():
            current_num += character
        elif current_num:
            numbers.append(Number(int(current_num), i, j - (len(current_num)), j - 1))
            current_num = ''

nums_to_sum = []

for num in numbers:
    if num.check_if_symbol_adjacent():
        nums_to_sum.append(num.get_num())

print(sum(nums_to_sum))
