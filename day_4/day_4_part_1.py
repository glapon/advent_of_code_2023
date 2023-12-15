lines = []
# open file and add each line to lines
with open('input.txt') as input:
    for item in input.readlines():
        lines.append(item.strip('\n'))

class Card:
    def __init__(self, line):
        line_split = line.split(': ')
        nums_split = line_split[1].split(' | ')
        self.winning_nums = nums_split[0].split()
        self.your_nums = nums_split[1].split()
        self.winners = self.check_winners()
        
    def check_winners(self):
        winners = []
        for num in self.your_nums:
            if num in self.winning_nums:
                winners.append(num)
        return winners
    
    def get_score(self):
        win_count = len(self.winners)
        if win_count == 0:
            return 0
        else:
            return 2 ** (win_count - 1)

cards = []
for line in lines:
    cards.append(Card(line))

print(sum([ card.get_score() for card in cards ]))