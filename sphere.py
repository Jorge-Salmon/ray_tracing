from math import sqrt

class Sphere:
    '''Sphere has a center, radius and material'''

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        '''Checks if ray intersects sphere. Returns distance or None'''
        sphere_to_ray = ray.origin - self.center

        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 *c

        if discriminant >= 0:
            dist = (-b -sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None

    def normal(self, surface_point):
        '''Returns normal to a pont'''
        return (surface_point - self.center).normalize()
