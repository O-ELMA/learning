class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        if self.__class__.__name__ == 'Square':
            return f'{self.__class__.__name__}(side={self.side})'
        else:
            return f'{self.__class__.__name__}(width={self.width}, height={self.height})'
        
    def set_width(self, width):
        if self.__class__.__name__ == 'Square':
            self.side = width
        else:
            self.width = width
        
    def set_height(self, height):
        if self.__class__.__name__ == 'Square':
            self.side = height
        else:
            self.height = height

    def get_area(self):
        if self.__class__.__name__ == 'Square':
            return self.side * self.side
        else:
            return self.width * self.height

    def get_perimeter(self):
        if self.__class__.__name__ == 'Square':
            return 4 * self.side
        else:
            return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        if self.__class__.__name__ == 'Square':
            return self.side * (2 ** 0.5)
        else:
            return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        result = ''

        if self.__class__.__name__ == 'Square':
            result = '\n'.join('*' * self.side for _ in range(self.side))
        else:
            result = '\n'.join('*' * self.width for _ in range(self.height))
        return result + '\n'

    def get_amount_inside(self, shape):
        if self.width < shape.width or self.height < shape.height:
            return 0

        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        self.side = side

Rectangle(4,8).get_amount_inside(Rectangle(3, 6))