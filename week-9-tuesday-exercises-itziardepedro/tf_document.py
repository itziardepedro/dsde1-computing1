'''tf_document_solution.py
Solution file for TFDocument class of the TF-IDF exercise.'''

import string
import math

class TFDocument:
    def __init__(self, location):
        '''Given a text file location, populates the instance
        attribute tf with the Term Frequency of that file.'''

        # save location in attribute
        # parse string and populate the tf attribute
        g = self.read_file(location)
        h = self.string_to_list(g)
        e = self.compute_tf(h)
        print(e)
        self.tf = e


    def read_file(self, storage_string):
        '''Opens a text file at the given location and returns 
        a string of its contents.'''

        with open(storage_string, 'r') as s: 
            contents = s.readlines()
            s_contents = ''  #empty string
        
        return (s_contents.join(contents)) #this inserts s_contents between each word in contents
        #its empty so it will return it with no spaces        


    def string_to_list(self, input_string):
        '''Takes in a string and returns a list of strings with all whitespace removed 
        along with any edge punctuation. Inner punctuation such as "that's" will remain.'''
        # ensure everything is lowercase
        # split into words at whitespace
        # remove any non-alpha characters at the beginning or end of each word
        
        sentence = input_string.lower()
        for char in sentence:
            if char in input_string.punctuation:
                sentence = sentence.replace(char, '')
        
        list1 = sentence.split()
        return list1
 

    def compute_tf(self, words):
        '''Given a list of strings, return a dictionary where each key is
        a string and the corresponding value is the Term Frequency for that
        string normalised to number of unique strings in the original list.'''
        # remove any repeated words
        # calculate total number of words
        dictionary = dict()
        for word in words:
            if word not in dictionary.keys():
                dictionary[word] = 1
            else:
                dictionary[word] += 1

        return dictionary

    def get_tfidf(self, word, idf):
        '''Given a word and its IDF value, return the TFIDF value for that word.'''
        return 