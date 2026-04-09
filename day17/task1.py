"""
Task 1: Magic/Dunder Methods - Comprehensive Examples
Create a Vector2D class implementing __add__, __sub__, __mul__, __eq__, __len__, __repr__, __str__, __getitem__, __setitem__

Python magic (dunder) methods are special methods with double underscores __ that enable operator overloading and custom object behavior.
"""

class Vector2D:
    """A 2D vector class demonstrating dunder methods"""
    
    def __init__(self, x=0, y=0):
        """Initialize vector coordinates"""
        self.x = x
        self.y = y
    
    # ========== ARITHMETIC OPERATORS ==========
    
    def __add__(self, other):
        """Enable: vector1 + vector2"""
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Enable: vector1 - vector2"""
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Enable: vector * number (scalar multiplication)"""
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __truediv__(self, scalar):
        """Enable: vector / number"""
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector2D(self.x / scalar, self.y / scalar)
        return NotImplemented
    
    def __floordiv__(self, scalar):
        """Enable: vector // number (floor division)"""
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector2D(self.x // scalar, self.y // scalar)
        return NotImplemented
    
    def __pow__(self, power):
        """Enable: vector ** n (each component to the power)"""
        if isinstance(power, (int, float)):
            return Vector2D(self.x ** power, self.y ** power)
        return NotImplemented
    
    # ========== COMPARISON OPERATORS ==========
    
    def __eq__(self, other):
        """Enable: vector1 == vector2"""
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False
    
    def __ne__(self, other):
        """Enable: vector1 != vector2"""
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """Enable: vector1 < vector2 (compare by magnitude)"""
        if isinstance(other, Vector2D):
            return self.magnitude() < other.magnitude()
        return NotImplemented
    
    def __le__(self, other):
        """Enable: vector1 <= vector2"""
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        """Enable: vector1 > vector2"""
        if isinstance(other, Vector2D):
            return self.magnitude() > other.magnitude()
        return NotImplemented
    
    def __ge__(self, other):
        """Enable: vector1 >= vector2"""
        return self.__gt__(other) or self.__eq__(other)
    
    # ========== STRING REPRESENTATION ==========
    
    def __str__(self):
        """Enable: str(vector) or print(vector) - User-friendly"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Enable: repr(vector) or vector in REPL - Developer-friendly"""
        return f"Vector2D(x={self.x}, y={self.y})"
    
    def __format__(self, format_spec):
        """Enable: format(vector, '.2f')"""
        if format_spec == 'polar':
            import math
            magnitude = self.magnitude()
            angle = math.degrees(math.atan2(self.y, self.x))
            return f"r={magnitude:.2f}, θ={angle:.2f}°"
        return f"({self.x}, {self.y})"
    
    # ========== CONTAINER/INDEXING ==========
    
    def __len__(self):
        """Enable: len(vector) - Returns magnitude"""
        return int(self.magnitude())
    
    def __getitem__(self, index):
        """Enable: vector[0], vector[1], vector['x'], vector['y']"""
        if index == 0 or index == 'x':
            return self.x
        elif index == 1 or index == 'y':
            return self.y
        elif isinstance(index, slice):
            return [self.x, self.y][index]
        raise IndexError(f"Index must be 0, 1, 'x', or 'y', got {index}")
    
    def __setitem__(self, index, value):
        """Enable: vector[0] = 5, vector['x'] = 10"""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        
        if index == 0 or index == 'x':
            self.x = value
        elif index == 1 or index == 'y':
            self.y = value
        else:
            raise IndexError(f"Index must be 0, 1, 'x', or 'y', got {index}")
    
    def __delitem__(self, index):
        """Enable: del vector[0]"""
        if index == 0 or index == 'x':
            self.x = 0
        elif index == 1 or index == 'y':
            self.y = 0
        else:
            raise IndexError(f"Index must be 0, 1, 'x', or 'y', got {index}")
    
    def __contains__(self, value):
        """Enable: value in vector"""
        return value in (self.x, self.y)
    
    def __iter__(self):
        """Enable: for coord in vector"""
        yield self.x
        yield self.y
    
    # ========== NUMERIC CONVERSION ==========
    
    def __int__(self):
        """Enable: int(vector)"""
        return int(self.magnitude())
    
    def __float__(self):
        """Enable: float(vector)"""
        return float(self.magnitude())
    
    def __bool__(self):
        """Enable: bool(vector) - False if zero vector"""
        return self.x != 0 or self.y != 0
    
    def __abs__(self):
        """Enable: abs(vector) - Returns magnitude"""
        return self.magnitude()
    
    def __round__(self, n=0):
        """Enable: round(vector, 2)"""
        return Vector2D(round(self.x, n), round(self.y, n))
    
    # ========== UNARY OPERATORS ==========
    
    def __neg__(self):
        """Enable: -vector"""
        return Vector2D(-self.x, -self.y)
    
    def __pos__(self):
        """Enable: +vector"""
        return Vector2D(+self.x, +self.y)
    
    def __invert__(self):
        """Enable: ~vector (swap x and y)"""
        return Vector2D(self.y, self.x)
    
    # ========== AUGMENTED ASSIGNMENT ==========
    
    def __iadd__(self, other):
        """Enable: vector1 += vector2"""
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
            return self
        return NotImplemented
    
    def __isub__(self, other):
        """Enable: vector1 -= vector2"""
        if isinstance(other, Vector2D):
            self.x -= other.x
            self.y -= other.y
            return self
        return NotImplemented
    
    def __imul__(self, scalar):
        """Enable: vector *= number"""
        if isinstance(scalar, (int, float)):
            self.x *= scalar
            self.y *= scalar
            return self
        return NotImplemented
    
    # ========== CONTEXT MANAGER ==========
    
    def __enter__(self):
        """Enable: with vector as v"""
        print(f"Entering context with {self}")
        self._original_x = self.x
        self._original_y = self.y
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager"""
        print(f"Exiting context, restoring original values")
        self.x = self._original_x
        self.y = self._original_y
        return False  # Don't suppress exceptions
    
    # ========== HELPER METHODS ==========
    
    def magnitude(self):
        """Calculate vector magnitude"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def dot(self, other):
        """Calculate dot product"""
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        return NotImplemented
    
    def normalize(self):
        """Return normalized vector"""
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / mag, self.y / mag)


# ========== EXAMPLES & TESTS ==========

if __name__ == "__main__":
    print("=" * 60)
    print("DUNDER METHODS EXAMPLES - Vector2D Class")
    print("=" * 60)
    
    # Create vectors
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    
    print(f"\nv1 = {v1}")
    print(f"v2 = {v2}")
    
    # Arithmetic Operations
    print("\n--- ARITHMETIC OPERATIONS ---")
    print(f"v1 + v2 = {v1 + v2}")  # __add__
    print(f"v1 - v2 = {v1 - v2}")  # __sub__
    print(f"v1 * 3 = {v1 * 3}")    # __mul__
    print(f"v1 / 2 = {v1 / 2}")    # __truediv__
    print(f"v1 // 2 = {v1 // 2}")  # __floordiv__
    print(f"v1 ** 2 = {v1 ** 2}")  # __pow__
    
    # Comparison Operations
    print("\n--- COMPARISON OPERATIONS ---")
    print(f"v1 == v2: {v1 == v2}")  # __eq__
    print(f"v1 != v2: {v1 != v2}")  # __ne__
    print(f"v1 < v2: {v1 < v2}")    # __lt__
    print(f"v1 > v2: {v1 > v2}")    # __gt__
    print(f"v1 <= v2: {v1 <= v2}")  # __le__
    print(f"v1 >= v2: {v1 >= v2}")  # __ge__
    
    # String Representation
    print("\n--- STRING REPRESENTATION ---")
    print(f"str(v1): {str(v1)}")      # __str__
    print(f"repr(v1): {repr(v1)}")    # __repr__
    print(f"format(v1, 'polar'): {format(v1, 'polar')}")  # __format__
    
    # Container/Indexing
    print("\n--- CONTAINER/INDEXING ---")
    print(f"len(v1): {len(v1)}")      # __len__
    print(f"v1[0]: {v1[0]}")          # __getitem__
    print(f"v1[1]: {v1[1]}")
    print(f"v1['x']: {v1['x']}")
    print(f"v1['y']: {v1['y']}")
    print(f"3 in v1: {3 in v1}")     # __contains__
    print(f"Iterate v1: {list(v1)}")  # __iter__
    
    # Modify using __setitem__
    print("\n--- MODIFYING VECTORS ---")
    v3 = Vector2D(5, 6)
    print(f"Before: v3 = {v3}")
    v3[0] = 10
    print(f"After v3[0] = 10: v3 = {v3}")
    v3['y'] = 20
    print(f"After v3['y'] = 20: v3 = {v3}")
    
    # Numeric Conversion
    print("\n--- NUMERIC CONVERSION ---")
    print(f"int(v1): {int(v1)}")      # __int__
    print(f"float(v1): {float(v1)}")  # __float__
    print(f"bool(v1): {bool(v1)}")    # __bool__
    print(f"abs(v1): {abs(v1)}")      # __abs__
    print(f"round(Vector2D(3.14159, 2.71828), 2): {round(Vector2D(3.14159, 2.71828), 2)}")
    
    # Unary Operators
    print("\n--- UNARY OPERATORS ---")
    print(f"-v1: {-v1}")             # __neg__
    print(f"+v1: {+v1}")             # __pos__
    print(f"~v1 (swap): {~v1}")      # __invert__
    
    # Augmented Assignment
    print("\n--- AUGMENTED ASSIGNMENT ---")
    v4 = Vector2D(1, 1)
    print(f"Before: v4 = {v4}")
    v4 += Vector2D(2, 3)
    print(f"After v4 += Vector2D(2, 3): v4 = {v4}")
    v4 *= 2
    print(f"After v4 *= 2: v4 = {v4}")
    
    # Context Manager
    print("\n--- CONTEXT MANAGER ---")
    v5 = Vector2D(10, 20)
    with v5 as v:
        print(f"Inside context: {v}")
        v[0] = 99
        print(f"Modified inside context: {v}")
    print(f"After context (restored): {v5}")
    
    # Helper Methods
    print("\n--- HELPER METHODS ---")
    print(f"v1.magnitude(): {v1.magnitude():.2f}")
    print(f"v1.dot(v2): {v1.dot(v2)}")
    print(f"v1.normalize(): {v1.normalize()}")
    
    # Zero vector test
    print("\n--- ZERO VECTOR TEST ---")
    zero = Vector2D(0, 0)
    print(f"zero = {zero}")
    print(f"bool(zero): {bool(zero)}")
    print(f"len(zero): {len(zero)}")
