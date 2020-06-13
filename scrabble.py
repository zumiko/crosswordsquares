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


    def starts_with(self,letter): 
        for line in file: 
            word = line.strip()
            for i in range(len(word)): 
                if letter == word[0]: 
                    print(word)

    def check_match(self, letter, spot): 
        possible = []
        for line in file: 
            word = line.strip()
            for i in range(len(word)): 
                if letter == word[spot]: 
                    possible.append(word)
        print(possible)

    def starts_with2(self, string,length): 
        possible = []
        for line in file: 
            word = line.strip()
            good = True
            if len(word) >= len(string) and check_len(word,length): 
                for i in range(len(word)):
                    for j in range(len(string)):
                        if string[j] != word[j]: 
                            good = False 
                if good == True: 
                    possible.append(word)
                good = True 
        print(possible)
        return possible

    def check_len(self, word): 
        if len(word) == self.length: 
            return True
        else: 
            return False

    def choose_random_word(self):   #takes list of possible words and tries them out to initialize feed whole list of words
        ls = []
        for line in file: 
            word = line.strip()
            if self.check_len(word) == True: 
                ls.append(word) 
        start = random.choice(ls)
        return start

    def add_to_array(self, word, rownum): #this adds the word to the array based on the rownumber 
        for i in range(len(word)): 
            self.array[rownum, i] = word[i]

    def print_array(self): 
        print(self.array.decode('utf8'))


    def make_puzzle(self): 
        start = self.choose_random_word()
        print(start)
        self.add_to_array(start, 0)
        self.print_array()

    def is_possible(self): 
        i = 0 
        while i < self.length: #need to sum the letter spots, so outer loop for column number and inner loop up to row 


        return True 

        return False 


    def make_puzzle2(self): 
        if self.done == False: 
            neword = self.choose_random_word()
            print(neword)
            if self.is_possible(neword): 
                self.add_to_array(neword)
                self.row += 1
                self.print_array()
            self.make_puzzle2()
            
            






g1 = Grid(4)
#g1.choose_random_word()
g1.make_puzzle2()


#starts_with("b")
#starts_with2("by")
#start_up(5)
#add_to_array("hater", 1)
#add_to_array("lemur", 0)

#choose_random_start() 

