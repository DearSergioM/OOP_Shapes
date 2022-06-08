from abc import ABC, abstractmethod
from math import pi
import math

class Shape(ABC):

    def __init__(self, color = 'Red', filled = True):
        self._color = color
        self._filled = filled

    def getColor(self):
        return self._color

    def setColor(self, newColor):
        self._color = newColor
    
    def isFilled(self):
        return self._filled
    
    def setFilled(self, value):
        self._filled = value
    
    @abstractmethod
    def getArea(self):
        ...
    
    @abstractmethod
    def getPerimeter(self):
        ...
    
    def toString(self):
        return print("Color: "+self._color+", Filled: "+str(self._filled))

class Circle(Shape):

    def __init__(self, radius, color = 'Red', filled = True):
        self._color = color
        self._filled = filled
        self.radius = radius
    
    def getRadius(self):
        return self.radius

    def setRadius(self, value):
        value = 1.0
        self.radius = value

    def getArea(self):
        pi
        r = self.radius
        a = pi*(r*r)
        return a
    
    def getPerimeter(self):
        pi
        p = self.radius + self.radius
        perimeter = pi * p
        return perimeter

    def toString(self):
        return "Color: "+self._color+'\n'+" Filled: "+str(self._filled)

class Rectangle(Shape):

    def __init__(self, width, length, color = 'Red', filled = True):
        self._color = color
        self._filled = filled
        self.width = width
        self.length = length
    
    def getWidth(self):
        return self.width

    def setWidth(self, value):
        value = 1.0
        self.width = value

    def getLength(self):
        return self.length

    def setLength(self, value):
        value = 1.0
        self.length = value

    def getArea(self):
        w = self.width
        l = self.length
        a = w * l
        return a
    
    def getPerimeter(self):
        w = self.width * 2
        l = self.length * 2
        p = w + l
        return p

    def toString(self):
        return "Color: "+self._color+'\n'+" Filled: "+str(self._filled)

class Square(Shape):

    def __init__(self, side, color = 'Red', filled = True):
        self._color = color
        self._filled = filled
        self._side = side
    
    def getSide(self):
        return self._side

    def setWidth(self, value):
        value = 1.0
        self._side = value

    def getArea(self):
        a = self._side * self._side
        return a
    
    def getPerimeter(self):
        p = self._side * 4
        return p

    def toString(self):
        return "Color: "+self._color+'\n'+" Filled: "+str(self._filled)

class EquilateralTriangle(Shape):

    def __init__(self, sideLength, color = 'Red', filled = True):
        self._color = color
        self._filled = filled
        self._side = sideLength
    
    def getSideLength(self):
        return self._side

    def setSideLength(self, value):
        value = 1.0
        self._side = value

    def getArea(self):
        b = self._side
        h = math.sqrt(3)
        a = ((b*b) * (h))/4
        return a
    
    def getPerimeter(self):
        p = self._side * 3
        return p

    def toString(self):
        return "Color: "+self._color+'\n'+" Filled: "+str(self._filled)

sh1 = Circle(5)
print('Circle')
print(' Radius: ',sh1.getRadius(),'\n',
        'Pi: ', pi,'\n',
        'Area: ',sh1.getArea(),'\n',
        'Perimeter: ',sh1.getPerimeter(),'\n',
        sh1.toString())
print('-------------------')

sh2 = Rectangle(5,10)
print('Rectangle')
print(' Width: ',sh2.getWidth(),'\n',
        'Length: ',sh2.getLength(),'\n',
        'Area: ',sh2.getArea(),'\n',
        'Perimeter: ',sh2.getPerimeter(),'\n',
        sh2.toString())
print('-------------------')

sh3 = Square(5)
print('Square')
print(' Side: ',sh3.getSide(),'\n',
        'Area: ',sh3.getArea(),'\n',
        'Perimeter: ',sh3.getPerimeter(),'\n',
        sh3.toString())
print('-------------------')

sh4 = EquilateralTriangle(2)
print('Equilateral Triangle')
print(' Side: ',sh4.getSideLength(),'\n',
        'Area: ',sh4.getArea(),'\n',
        'Perimeter: ',sh4.getPerimeter(),'\n',
        sh4.toString())
print('-------------------')