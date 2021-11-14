import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.C = complex(self.real, self.imaginary)
        
    def __add__(self, no):
        self.D = complex(no.real, no.imaginary)
        res = self.C + self.D
        return format(res, '.2f').replace('j', 'i')
    
    def __sub__(self, no):
        self.D = complex(no.real, no.imaginary)
        res = self.C - self.D
        return format(res, '.2f').replace('j', 'i')
    
    def __mul__(self, no):
        self.D = complex(no.real, no.imaginary)
        res = self.C * self.D
        return format(res, '.2f').replace('j', 'i')
        
    def __truediv__(self, no):
        self.D = complex(no.real, no.imaginary)
        res = (self.C * self.D.conjugate()) / (self.D * self.D.conjugate())
        return format(res, '.2f').replace('j', 'i')
    
    def mod(self):
        return format(abs(self.C), '.2f') + '+0.00i'
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
