import random
import numpy as np

file = open('words.txt')

#you need to make a temporary list of the possible words using the matches thing

#TODO: 
#fix matching function (DONE)
#make compare funciton 
#retry previous word if none 


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
        for line in file: 
            word = line.strip()
            if len(word) == self.length: 
                self.lswords.append(word)


    def choose_random_word(self):   #choose random word from list
        start = random.choice(self.lswords)
        print(start)
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
                print(word)
                #checklist = self.starts_with(word)             
                #templs.append(checklist)  #the temp list is what need
                j+= 1
            checklist = self.starts_with(word)             
            templs.append(checklist) 
            i+= 1
        print("this is temp")
        print(templs)
        return templs

    def clean_lsols(self, lsos): #clean the new list so its only last letter in column words
        final = [] 
        for el in lsos: 
            first = []
            for w in el: 
                first.append(w[self.row]) 
            final.append(first)
        print("this is clean temp")
        print(final)
        return final

    def find_new_list(self, lsos): #this gets the new list of possibilites 
        lists = self.lswords
        l = len(lsos)
        count = 0 
        while count <= 5: 
            for word in self.lswords: 
                if not self.check_match2(word, lsos): 
                    print('remove' + word)
                    self.lswords.remove(word)
            count +=1
  
        print(self.lswords)

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
        neword = self.choose_random_word() #get random word of right length
        self.add_to_array(str(neword), self.row) #add it to the array 
        self.row += 1
        if self.row == self.length: 
            self.print_array()
        else: 

            self.print_array()
            
            lsols = self.is_possible() #get list of column words
            lsolsc = self.clean_lsols(lsols) #clean list
            self.find_new_list(lsolsc) #get new possibilites 

            if len(self.lswords) != 0: 
                print(self.row)
                self.make_puzzle()

            else: #start over 
                self.make_list()
                self.make_puzzle()



            
        


g1 = Grid(2)
#g1.choose_random_word()
g1.make_list()
g1.make_puzzle()


#starts_with("b")
#starts_with2("by")
#start_up(5)
#add_to_array("hater", 1)
#add_to_array("lemur", 0)

#choose_random_start() 

