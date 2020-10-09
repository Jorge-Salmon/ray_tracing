from color import Color

class Light:
    '''Punctual light source'''
    def __init__(self, position, color=Color.from_hex("#FFFFFF")):
        self.position = position
        self.color = color
