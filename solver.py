from jumble_map import build_map
import json

class JumbleSolver:
    def __init__(self, jumble_list, circle_list, final_list, word_list=None):
        self.jumbles = jumble_list
        self.circles = circle_list
        self.final = final_list
        self.pool = word_list
        self.map = None

    def _start(self):
        try:
            file = open('jumble_table.txt', 'r')
            self.map = json.loads(file)
        except:
            if self.pool == None: # if no specific word pool, we pull from local dictionary
                with open('/usr/share/dict/words', 'r') as words:
                    self.pool = words.read().lower().split()

            self.map = self._build_map(self.pool)
            print(self.map)
            with open('jumble_table.txt', 'w') as file:
                file.write(json.dumps(self.map))

        circle_indexes = [] # gets a list of list of indexes which the circles are
        for circle_arry in self.circles:
            circle_indexes = []
            for index, char in enumerate(circle_arry):
                if char == 'O':
                    circle_indexes.append(index)

        solved_jumbles = [] # solves all the jumbles as a list of list of solutions
        for jumble in self.jumbles:
            solved_jumbles.append(self._solve(jumble))

        return solved_jumbles

    def _build_map(self, word_list):
        '''Builds a map from sorted word to unsorted word'''
        map = {}
        for word in word_list:
            sorted_word = ''.join(sorted(word))
            map.setdefault(sorted_word, []).append(word)
        return map

    def _solve(self, word):
        sorted_word = ''.join(sorted(word))
        solution = self.map[sorted_word]
        return solution

if __name__ == 'main':
    pass