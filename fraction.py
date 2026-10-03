class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        
    def __str__(self):  # This __str__ is also a special method auto invoked when object is placed inside print(x)
        return "{}/{}".format(self.n, self.d)
      
    def __add__(self, other): # This is also a special method auto invoked if print(x + y) here need two objects as x will come to self and y will come to other self will contain both num and den also other will contain both num and den
        final_num = self.n * other.d + self.d * other.n
        final_den = self.d * other.d
        return "{}/{}".format(final_num, final_den)          

    def __sub__(self, other): # This is also a special method auto invoked if print(x + y) here need two objects as x will come to self and y will come to other self will contain both num and den also other will contain both num and den
        final_num = self.n * other.d - self.d * other.n
        final_den = self.d * other.d
        return "{}/{}".format(final_num, final_den)
    
    def __mul__(self, other): # This is also a special method auto invoked if print(x + y) here need two objects as x will come to self and y will come to other self will contain both num and den also other will contain both num and den
        final_num = self.n * other.n
        final_den = self.d * other.d
        return "{}/{}".format(final_num, final_den)
    
    def __truediv__(self, other): # This is also a special method auto invoked if print(x + y) here need two objects as x will come to self and y will come to other self will contain both num and den also other will contain both num and den
        final_num = self.n * other.d
        final_den = self.d * other.n
        return "{}/{}".format(final_num, final_den)
    
# Similarly we have mod pow ge lt lte gte and many more 
# We also have typeConversion special methods 
