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
            file.close()
        except:
            if self.pool == None: # if no specific word pool, we pull from local dictionary
                with open('/usr/share/dict/words', 'r') as words:
                    self.pool = words.read().lower().split()

            self.map = self._build_map(self.pool)
            with open('jumble_table.txt', 'w') as file:
                json.dump(self.map, file)

        print("MAP SIZE " + str(len(self.map)))

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
        sorted_word = ''.join(sorted(word)).lower()
        print(sorted_word)
        return self.map[sorted_word]
        # if word in self.map:
        #     return self.map[sorted_word]
        # else:
        #     return "No Solution"

if __name__ == "__main__":
    # Cartoon prompt for final jumble:
    # "Farley rolled on the barn floor because of his __-______."
    letters = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    circles = ['__O_O', 'OO_O_', '____O_', '___OO_']
    final = ['OO', 'OOOOOO']
    print(JumbleSolver(letters, circles, final)._start())
    # Cartoon prompt for final jumble: "What a dog house is: A ____ ___."
    letters = ['TARFD', 'JOBUM', 'TENJUK', 'LETHEM']
    circles = ['____O', '_OO__', '_O___O', 'O____O']
    final = ['OOOO', 'OOO']
    print(JumbleSolver(letters, circles, final)._start())
    # Cartoon prompt for final jumble:
    # "A bad way for a lawyer to learn the criminal justice system: _____ and _____."
    letters = ['LAISA', 'LAURR', 'BUREEK', 'PROUOT']
    circles = ['_OOO_', 'O_O__', 'OO____', '__O_OO']
    final = ['OOOOO', 'OOOOO']
    print(JumbleSolver(letters, circles, final)._start())