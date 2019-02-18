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

vec1 = Vector([8.218,-9.341])
vec2 = Vector([-1.129,2.111])
print(vec1.sum(vec2))

vec1 = Vector([7.119,8.215])
vec2 = Vector([-8.223,0.878])
print(vec1.substract(vec2))

vec1 = Vector([1.671,-1.012,-0.318])
scalar = 7.41
print(vec1.scale(scalar))