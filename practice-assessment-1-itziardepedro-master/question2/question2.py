'''
question2.py

Draw the corresponding flowchart to describe
the algorithm implemented below.
'''

def flowchart(input_list):
    '''Takes in list and returns a new list of the numbers 3, 2, or 0 
    corresponding with what number the original list was divisble by 
    (3, 2, or neither).'''

    # create an empty list to fill and return
    common_denominators = []

    for i in input_list:
        # if the item is divisble by three
        if not i%3:
            # add the value 3 to the list
            common_denominators.append(3)

        # if the item is divisible by two
        elif not i%2:
            # add the value 2 to the list
            common_denominators.append(2)

        # otherwise
        else:
            # append the value 0
            common_denominators.append(0)

    return common_denominators
