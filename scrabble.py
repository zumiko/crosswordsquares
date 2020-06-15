import random
import numpy as np



file = open('words.txt')

#you need to make a temporary list of the possible words using the matches thing

#TODO: 
#looks like your co


class Grid:

    def __init__(self, length):
        self.length = length
        self.array = np.chararray((length, length))
        self.array[:] =  None
        self.done = False
        self.row = 0 
        self.lswords = []
        self.templs = []

    def make_list(self): #make a list of all the words
        file = open('words.txt')
        for line in file: 
            word = line.strip()
            if len(word) == self.length: 
                self.lswords.append(word)
        self.templs = self.lswords


    def choose_random_word(self, list):   #choose random word from list
        start = random.choice(list)
        return start

    def check_match(self, letter, spot): #find words that match letter in certain spot 
        possible = []
        for w in self.lswords: 
            for i in range(len(w)): 
                if letter == w[spot]: 
                    possible.append(w)
        return possible

    def check_match2(self, word, lsos): #find words that match letter in certain spot (GOOD)
        b = True
        i = 0 
        while i < len(lsos): 
            if word[i] not in lsos[i]: 
                b = False
            i +=1
        return b

    def is_possible(self): #gets list of column words so far 
        i = 0 
        templs = []
        while i < self.length: #need to sum the letter spots, so outer loop for column number and inner loop up to row USED TO BE LEN
            j = 0 
            word = ''
            while j < self.row: 
                word += self.array[j, i].decode('utf8')
                #checklist = self.starts_with(word)             
                #templs.append(checklist)  #the temp list is what need
                j+= 1
            checklist = self.starts_with(word)             
            templs.append(checklist) 
            i+= 1
        return templs

    def clean_lsols(self, lsos): #clean the new list so its only last letter in column words
        final = [] 
        for el in lsos: 
            first = []
            for w in el: 
                first.append(w[self.row]) 
            final.append(first)
        #print(final)
        return final

    def empty_list(self, lsos): 
        b = False
        for ls in lsos: 
            if len(ls) == 0: 
                b = True 
        return b 



    def find_new_list(self, lsos): #this gets the new list of possibilites 
        self.templs = self.lswords
        if self.empty_list(lsos) == True: 
            self.lswords.clear()

        else: 
            count = 0 
            while count <= 10: 
                for word in self.templs: 
                    if not self.check_match2(word, lsos): 
                        self.templs.remove(word)
                count += 1
        #print(self.templs)

                    #need to get the last letters off of the lsols

    def starts_with(self, string): #this get all words that start with some string
        possible = []
        for w in self.lswords: 
            good = True  
            for j in range(len(string)):  #goes through pieces of string
                if string[j] != w[j]: 
                    good = False 
            if good == True: 
                possible.append(w)
        return possible

    #more little stuff length check, adding to array, and printing

    def check_len(self, word): 
        if len(word) == self.length: 
            return True
        else: 
            return False

    def add_to_array(self, word, rownum): #by row number adding
        for i in range(len(word)): 
            self.array[rownum, i] = word[i]

    def print_array(self): 
        print(self.array.decode('utf8'))
        print(self.row)


    #overall fuction

    def make_puzzle(self): 
        neword = self.choose_random_word(self.templs) #get random word of right length
        self.add_to_array(str(neword), self.row) #add it to the array 
        self.row += 1
        if self.row == self.length: 
            self.make_list()
            self.print_array()
        else: 

            #self.print_array()
            
            lsols = self.is_possible() #get list of column words
            lsolsc = self.clean_lsols(lsols) #clean list
            self.find_new_list(lsolsc) #get new possibilites 

            if len(self.lswords) != 0: 
                self.make_puzzle()

            else: #start over 
                self.make_list()
                self.row = 0 
                self.make_puzzle()
       

g1 = Grid(3)
#g1.choose_random_word()
g1.make_list()
g1.make_puzzle()



