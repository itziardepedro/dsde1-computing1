'''
question3.py

Fix the errors so that this code runs when called
from the commandline.
'''

def count_words(input_string):
    '''Counts the number of words between spaces'''
    words = input_string.split()
    return len(word)



def main():
    '''Main function to be run first.'''

    my_string = 'Imperial College London'

    # count number of words in string
    num_words = len(my_string)

    # print how many words were counted
    print('There are ' + str(num_words) + ' words in the string: ' + my_string)

if __name__ == '__main__':
    main()