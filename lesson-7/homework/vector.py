import math

class Vector:

    def __init__(self, *components):
        self.component = list(components)

    def __repr__(self):
        return f"Vector({",".join(map(str, self.component))})"
    
    def __len__(self):
        return len(self.component)

    def __add__(self, v2):

        if len(self) != len(v2):
            raise ValueError("Vectors of the same magnitude can be added!")
        return Vector(*(a+b for a, b in zip(self.component, v2.component)))
        
    def __sub__(self, v2):
        if len(self) != len(v2):
            raise ValueError("Vectors of the same magnitude can be subtracted!")
        return Vector(*(a-b for a, b in zip(self.component, v2.component)))

    def __mul__(self, scalar):
        return Vector(*(a*scalar for a in self.component))

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __mul__(self, v2):
        if len(self) != len(v2):
            raise ValueError("Vectors of the same magnitude can have a dor product!")
        elem = list(a*b for a, b in zip(self.component, v2.component))
        return sum(elem)

    def magnitude(self):
        return round(math.sqrt(sum(a**2 for a in self.component)), 5)
    
    def normalize(self):
        return Vector(*(round(a/self.magnitude(), 3) for a in self.component))


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

dot_product = v1 * v2
print(dot_product)

