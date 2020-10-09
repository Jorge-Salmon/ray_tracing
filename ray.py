class Ray:
    '''Ray of light'''
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()
