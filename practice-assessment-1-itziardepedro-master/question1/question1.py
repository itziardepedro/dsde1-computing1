'''
question1.py

Implementation of the flowchart in question1.png.
'''

def flowchart(input_value):
    if input_value == 0: 
        return 0
    
    elif input_value > 0:
        if input_value % 2 == 0: 
            return 'positive-even'
        elif input_value % 2 != 0:
            return 'positive-odd'
    
    elif input_value < 0: 
        if input_value % 2 == 0: 
            return 'negative-even'
        elif input_value % 2 != 0:
            return 'negative-odd'

