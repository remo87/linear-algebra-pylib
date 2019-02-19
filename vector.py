import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def sum(self, v):
        
        if(self.dimension != v.dimension):
            raise ValueError('Vectors must be of the same dimension')
        sumVector = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(sumVector)
    
    def substract(self, v):
        
        if(self.dimension != v.dimension):
            raise ValueError('Vectors must be of the same dimension')
        
        substract = [x-y for (x,y) in zip(self.coordinates, v.coordinates)]
        
        substractVector = Vector (substract)
        return substractVector

    def scale(self, c):
        scale = [c*x for x in self.coordinates]
        scaleVector = Vector (scale)
        return scaleVector

    def magnitude(self):
        magnitude = math.sqrt(sum([v*v for v in self.coordinates]))
        return magnitude

    def normalize(self):
        normalization = self.scale(1/self.magnitude())
        return normalization

    def dotProduct(self, v):
        dot = sum(x*y for x,y in zip(self.coordinates, v.coordinates))
        return dot

    def getRad(self, v):
        dot = self.dotProduct(v)
        rad = math.acos(dot/(self.magnitude()*v.magnitude()))
        return rad 

    def getDeg(self, v):
        degrees = math.degrees(self.getRad(v))
        return degrees 

# vec1 = Vector([8.218,-9.341])
# vec2 = Vector([-1.129,2.111])
# print(vec1.sum(vec2))

# vec1 = Vector([7.119,8.215])
# vec2 = Vector([-8.223,0.878])
# print(vec1.substract(vec2))

# vec1 = Vector([1.671,-1.012,-0.318])
# scalar = 7.41
# print(vec1.scale(scalar))

# vec1 = Vector([-0.221,7.437])
# print(vec1.magnitude())

# vec2 = Vector([8.813,-1.331,-6.247])
# print(vec2.magnitude())

# vec1 = Vector([5.581,-2.136])
# print(vec1.normalize())

# vec2 = Vector([1.996,3.108,-4.554])
# print(vec2.normalize())

vec1 = Vector([7.887,4.138])
vec2 = Vector([-8.802,6.776])
print(vec1.dotProduct(vec2))

vec1 = Vector([3.183,-7.627])
vec2 = Vector([-2.668,5.319])
print(vec1.getRad(vec2))

vec1 = Vector([7.35,0.221,5.188])
vec2 = Vector([2.751,8.259,3.985])
print(vec1.getDeg(vec2))



