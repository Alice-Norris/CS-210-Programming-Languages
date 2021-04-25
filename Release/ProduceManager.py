 # Author: Alice Norris
 # Class: CS-210-T4249 Programming Languages 21EW4
 # Professor: Eric Gregori, MSCS
 # Main file, completed 04/23/2021
 #
 # The code in this file attempts to follow Python.org's PEP8 Styyle Guide.
 #(https://www.python.org/dev/peps/pep-0008/).
 # Comments are used extensively, even when code is obvious, to present an
 # understanding of the code, and for corrections or clarifications in
 # execution and concept. In accordance with the PEP8 style guide, all
 # lines have been wrapped as neatly as possible to 79 characters, and
 # all naming conventions have been followed to the best of my ability

import os # imported to use the getcwd() function, which allows the 
          # writeFrequencyFile function to print the directory the file was 
          # created in.


#produce manager created as a class in order to cut down on work having to 
#be redone as data that requires persistence can be stored with the class 
#instance
class ProduceManager:

    #parameterized constructor. As everything depends on this one python 
    #class, a default constructor was not given. takes two strings as 
    #arguments, both should be file names, ideally with file extensions.
    def __init__(self, input_file_name, output_file_name): 

        #set instance's data_file_name to input file name given by C++
        self.data_file_name = input_file_name 
        
        #set instance's output_file_name to output file name given by C++
        self.output_file_name = output_file_name 

        #dictionary to be used to hold produce data from data file
        self.produce_dict = {} 

    #this method returns no data, and populates the instances produce 
    #dictionary with items sold today along with the quantity of each item 
    #sold. 
    def total_produce_frequencies(self):
        #open a file whose name matches that given upon instantiation, 
        #in read mode.
        produce_record = open(self.data_file_name, 'r') 
        #iterate over open file stream, line by line. For loop automatically
        #stops when EOF is reached
        for item_line in produce_record:
            #strip whitespace from both ends of string on each line
            produce_item = item_line.strip() 
            #search this instance's produce_dict for a key matching the word 
            #retrieved from the file. If it is not there...
            if (produce_item not in self.produce_dict): 
                #include it in the dictionary by giving it a value of one
                self.produce_dict[produce_item] = 1 
            else: #if it's already in there...
                self.produce_dict[produce_item] += 1 #increment its value by one.
        produce_record.close() #always clean up after yourself! file closed!
    
    #this method returns no data, and prints a prettified list of all items 
    #sold today, followed by the quantity of the items sold today
    def print_all_produce_frequencies(self):
        print(" ======================= ") #this is just the list header

        #print formatted title line, with the "Produce Name" left justified in
        # a 12-character-width field, followed by a right-justified "Quantity"
        # header, in an 8-character-width field
        print("|%(produceName)-12s\t%(item_qty)8s|" % {
            "produceName" : "Produce Name", "item_qty" : "Quantity"})
        print("|=======================|") #also just a header

        #iterate over each item in this instance's dictionary of item names/qtys
        for item in self.produce_dict.items(): 
            print("|%(produceName)-12s\t%(item_qty)8s|" % {
                "produceName" : item[0], "item_qty" : item[1]})

        print("|-----------------------|") #just a footer!
        input("Press any key to continue...") #pause program, prompt user


    #this method is used to return a single item's quantity sold today, as 
    #found in the instance's produce dictionary. Takes one string, item_name,
    #as a search key
    def return_produce_frequency(self, item_name):
        match = False #set booolean match to false as a defualt state
        for item in self.produce_dict.items(): #iterate over produce dictionary
            if item[0] == item_name: #if key (item[0]) matches item_name...
                return item[1] #...return the value, its quantity (item[1])
                match = True #turn match to true
        #if 'quit' is given or no match found...
        if (match == False or item_name == 'quit'): 
           return -1 #...return -1.
    
    #This method is used to put the data that was parsed from the given input file
    # in the given output file name, following the format:
    # <item_name> <item_qty>\n  
    # (notice the *single* space between item_name and item_qty.)
    def write_frequency_file(self):
        #create a file of the given output name, open the stream in write mode
        output_file = open(self.output_file_name, 'w') 

        #print the filename so the user knows what to look for
        print("File Name: ", self.output_file_name)

        #iterate over each item in the instance's produce dictionary
        for produce_item in self.produce_dict.items(): 
            #create a line to write to the file 
            file_line = produce_item[0] + " " + str(produce_item[1]) + "\n" 
            #write line to file
            output_file.write(file_line)    
        #print a message to user showing the location of the file as created.
        print("Output location: " + os.getcwd() + "\\" + self.output_file_name)