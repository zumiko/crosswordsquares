import random
import numpy as np

file = open('words.txt')


class Grid:

    def __init__(self, length):
        self.length = length
        self.array = np.chararray((length, length))
        self.array[:] =  None
        self.done = False
        self.row = 0 
        self.lswords = []

    def make_list(self): 
        for line in file: 
            word = line.strip()
            if len(word) == self.length: 
                self.lswords.append(word)

    def check_match(self, letter, spot): 
        possible = []
        for line in file: 
            word = line.strip()
            for i in range(len(word)): 
                if letter == word[spot]: 
                    possible.append(word)
        print(possible)

    def starts_with(self, string): 
        possible = []
        for w in self.lswords: 
            good = True  
            for j in range(len(string)):  #goes through pieces of string
                if string[j] != w[j]: 
                    good = False 
            if good == True: 
                possible.append(w)
        return possible

    def check_len(self, word): 
        if len(word) == self.length: 
            return True
        else: 
            return False

    def choose_random_word(self):   #takes list of possible words and tries them out to initialize feed whole list of words
        start = random.choice(self.lswords)
        print(start)
        return start

    def add_to_array(self, word, rownum): #this adds the word to the array based on the rownumber 
        for i in range(len(word)): 
            self.array[rownum, i] = word[i]

    def print_array(self): 
        print(self.array.decode('utf8'))
        print(self.row)


    def make_puzzle(self): 
        start = self.choose_random_word()
        print(start)
        self.add_to_array(start, 0)
        self.print_array()

    def is_possible(self): # checks if we are good so far
        i = 0 
        begin = []
        possible = True
        while i < self.length: #need to sum the letter spots, so outer loop for column number and inner loop up to row 
            j = 0 
            word = ''
            while j < self.row: 
                word += self.array[j, i].decode('utf8')
                print(word)
                checklist = self.starts_with(word)
                print(checklist)
                if len(checklist) <= 2: 
                    possible = False
                j+= 1
            i+= 1
        return possible


    def make_puzzle2(self): 
        if self.row == self.length: 
            self.print_array()

        else: 
            neword = self.choose_random_word() 
            self.add_to_array(str(neword), self.row)
            self.print_array()
            if self.is_possible() == True: 
                self.row += 1
                print(self.row)

            self.make_puzzle2()

            
            






g1 = Grid(2)
#g1.choose_random_word()
g1.make_list()
g1.make_puzzle2()


#starts_with("b")
#starts_with2("by")
#start_up(5)
#add_to_array("hater", 1)
#add_to_array("lemur", 0)

#choose_random_start() 

