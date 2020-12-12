class Shape:
    def __init__(self,color = "Green",filled = True):
        self.color = color
        self.filled = filled
    def getColor(self):
        return f"The color is {self.color}"
    def setColor(self,color):
        self.color = color
    def isFilled(self):
        if self.color == "":
            self.filled = False
            return "not filled"
        else:
            self.filled = True
            return "filled"
    def toString(self):
        return f"a shape with color of {self.color} and {Shape.isFilled(self)}"

class Circle(Shape):
    def __init__(self,radius=1.0):
        super().__init__("Green",True)
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        self.radius = radius
    def getArea(self):
        a = 3.14 * (self.radius ** 2)
        return "The Area is",a
    def getPerimeter(self):
        a = 2 * 3.14 * self.radius
        return "The Perimeter is",a
    def toString(self):
        a= Shape.toString(self)
        return f"A Circle with radius {self.radius} which is a subclass of {a}"

class Rectangle(Shape):
    def __init__(self,width = 1.0,length = 1.0):
        super().__init__("Green",True)
        self.width = width
        self.length = length
    def getWidth(self):
        return "The Width is",self.width
    def setWidth(self, width):
        self.width = width
    def getLength(self):
        return "The Length is",self.length
    def setLength(self, length):
        self.length = length
    def getArea(self):
        a = self.width * self.length
        return "The Area is",a
    def getPerimeter(self):
        a = (2 * self.width) + (2 * self.length)
        return "The Perimeter is",a
    def toString(self):
        a = Shape.toString(self)
        return f"A Rectangle with {self.width} and {self.length}, which is a subclass of",a

class Square(Rectangle):
    def __init__(self):
        super().__init__(1.0,1.0)
        side = (self.width + self.length)/2
        self.side = side
    def getSide(self):
        return "The Length is",self.side
    def setSide(self,side):
        self.side = side
    def getArea(self):
        a = self.side**2
        return "The Area is",a
    def getPerimeter(self):
        a = self.side*4
        return "The Perimeter is", a
    def toString(self):
        a = Shape.toString(self)
        return f"A Square with {self.side}, which is a subclass of {a}"

if __name__ == "__main__":
    Shape("Blue",True)
    Rectangle(2.0,2.0)
    shape = Square().toString()
    print(Shape)