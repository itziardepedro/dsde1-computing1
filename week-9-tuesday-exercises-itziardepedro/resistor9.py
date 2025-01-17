class Resistor:

    colours = {'black': 0,
                   'brown': 1,
                   'red': 2,
                   'orange': 3,
                   'yellow': 4,
                   'green': 5,
                   'blue': 6,
                   'violet': 7,
                   'grey': 8,
                   'white': 9, 
                   'silver': 0.1,
                   'gold':0.01}

    tol_colours = {'brown': 0.01,
                       'red': 0.02,
                       'green': 0.005,
                       'blue': 0.0025,
                       'violet': 0.001,
                       'grey': 0.0005,
                       'silver': 0.05,
                       'gold': 0.1}

    def __add__(self, other): 
        return self.value() + other.value() 

    '''Resistor class representing 4 or 5 band resistors.'''
    def __init__(self, band1, band2, band3, band4, band5=None):
        self.b1 = band1.lower()
        self.b2 = band2.lower()
        self.b3 = band3.lower()


        # 4 band resistor 
        if band5 is None:
            self.tolerance = band4
            self.num_bands = 4
        # 5 band resistor
        else:
            self.b4 = band4
            self.tolerance = band5
            self.num_bands = 5

    def value(self):
        '''Returns the calculated value of the resistor in Ohms.'''
        
        # 4-band value = <band1 band2> (each a digit) x 10^band3
        if self.num_bands == 4:
            value = (Resistor.colours[self.b1] * 10 + Resistor.colours[self.b2]) * 10**Resistor.colours[self.b3]
        
        # 5-band value = <band1 band2 band3> (each a digit) x 10^band4
        if self.num_bands == 5:
            value = (Resistor.colours[self.b1] * 100 + Resistor.colours[self.b2] * 10 + Resistor.colours[self.b3]) * 10** Resistor.colours[self.b4]
       
        return value
    
    def min_value(self):
        '''Return the minimum value within the tolerance of the resistor value.'''
        return self.value - self.value * (Resistor.tol_colours(self.tolerance))
    
    def max_value(self):
        '''Return the maximium value within the tolerance of the resistor value.'''
        return self.value + self.value * (Resistor.tol_colours(self.tolerance))