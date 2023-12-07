class Game:
    def __init__(self, cube_sets):
        totals = {
            'red': 12,
            'green': 13,
            'blue': 14
        }
        colors = ['red', 'green', 'blue']
        
        self.cube_sets = cube_sets.split(': ')
        self.game_id = self.get_id()
        self.possible_game = True

        for color in colors:
            if self.get_max(color) > totals[color]:
                self.possible_game = False
        
    def get_id(self):
        """
        Extract game ID from cube_sets string
        """
        id_string = self.cube_sets[0]
        return int(id_string.lstrip('Game '))
    
    def get_count(self, count_string):
        return int(count_string.split()[0])
    
    def get_max(self, color):
        """
        Return maximum count of a given color in a given game
        """
        combos = [ x.split(', ') for x in self.cube_sets[1].split('; ')]
        counts = []
        for combo in combos:
            for count_string in combo:
                if color in count_string:
                    counts.append(self.get_count(count_string))
        return max(counts)
    
    def return_id(self):
        return self.game_id
    
    def return_possible_game(self):
        return self.possible_game

cube_sets = []
# open file and add each line to calibrations_strings
with open('input.txt') as input:
    for item in input.readlines():
        cube_sets.append(item.strip('\n'))

games = [ Game(cube_set) for cube_set in cube_sets ]
possible_ids = [ game.return_id() for game in games if game.return_possible_game()]

print(sum(possible_ids))