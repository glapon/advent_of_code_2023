lines = []
# open file and add each line to lines
with open('input.txt') as input:
    for item in input.readlines():
        lines.append(item.strip('\n'))

class Asterisk:
    def __init__(self, line, index):
        self.line = line
        self.index = index
        self.left = max(0, self.index - 1)
        self.right = min(self.index + 1, len(lines[line]) - 1)
        self.numbers=[]
        self.get_nums_on_line(lines[line], self.index, self.index)
        if line > 0:
            self.get_nums_on_line(lines[line - 1], self.left, self.right)
        if line < (len(lines) - 1):
            self.get_nums_on_line(lines[line + 1], self.left, self.right)
        if len(self.numbers) == 2:
            self.product = self.numbers[0] * self.numbers[1]
        else:
            self.product = 0

    def get_nums_on_line(self, line, start, end):
        current_num = ''
        for j in range(len(line)):
            character = line[j]
            if character.isdigit():
                current_num += character
            elif current_num:
                if self.check_overlap(j - (len(current_num)), j - 1):
                    self.numbers.append(int(current_num))
                current_num = ''
    
    def check_overlap(self, start, end):
        if self.index >= start and self.index <= end:
            return True
        elif self.index == start -1:
            return True
        elif self.index == end + 1:
            return True
        else:
            return False

    def get_product(self):
        return self.product

asterisks = []
for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        character = line[j]
        if character == '*':
            asterisks.append(Asterisk(i, j))

print(sum([ a.get_product() for a in asterisks]))

for a in asterisks:
    print(a.numbers)