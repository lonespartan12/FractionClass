def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
      common = gcd(top,bottom)      #1.17.2  
      self.num = (top//common)#1.17.2 
      self.den = (bottom//common)#1.17.2 

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
    
    def __sub__(self, otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)#helper function
        # use integer division on num and den to return the simplified fraction
        return Fraction(newnum // common, newden // common) 

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)#helper function to find the greatest common denominator
        return Fraction(newnum//common, newden//common)#use integer division to show the simplified fraction

    def __truediv__(self, other):
        """performs true division, it will return floating points"""
        #would it be more efficient to treat the __mul__ method
        #that we created above and just swtich the inputs than to creat an entire div method?
        #A: I guess not because of we don't have any way to switch the numerator and the denominator,
        # A: only which fraction is loaded first in the method
        newnum = self.num*other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)#helper function to find greatest common denominator
        # use integer devision on num and den to return the simplified fraction
        return Fraction(newnum // common, newden // common)

    def __gt__(self, other):
        """performs greater than comparison, and returns true or false"""
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum
    
    def __lt__(self, other):
        """performs greater than comparison, and returns true or false"""
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    
    def getNum(self):
      return self.num


    def getDen(self):
      return self.den

#def main():
x = Fraction(2, 4)
y = Fraction(2, 3)
print(f"Fraction x: {x}")
print(f"Fraction y: {y}")
print(f'addition {x}+{y}: ')
print(x + y)
print(f'subraction {x}+{y}: ')
print(x - y)
print(f'Multiply {x}+{y}: ')
print(x * y)
print(f'Divide {x}+{y}: ')
print(x / y)
print(f'Greater Than {x}+{y}: ')
print(x > y)
print(f'Less Than {x}+{y}: ')
print(x < y)
print(f'equals {x}+{y}: ')
print(x == y)
print(x.getNum())
print(x.getDen())
