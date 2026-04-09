"""
Task 2: More Dunder Methods Examples - Advanced Use Cases
Demonstrating: __call__, __new__, __del__, __hash__, __slots__, __getattr__, __setattr__, __delattr__, __dir__, __instancecheck__, __subclasscheck__
"""

# ========== EXAMPLE 1: __call__ - Make Objects Callable ==========

class Multiplier:
    """A callable object that multiplies"""
    
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, *args):
        """Enable: object() like a function"""
        result = 1
        for arg in args:
            result *= arg
        return result * self.factor
    
    def __repr__(self):
        return f"Multiplier(factor={self.factor})"


print("=" * 60)
print("EXAMPLE 1: __call__ - Callable Objects")
print("=" * 60)

double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5) = {double(5)}")           # 2 * 5 = 10
print(f"double(3, 4) = {double(3, 4)}")     # 2 * 3 * 4 = 24
print(f"triple(2, 3, 4) = {triple(2, 3, 4)}")  # 3 * 2 * 3 * 4 = 72
print(f"double: {double}")


# ========== EXAMPLE 2: __new__ vs __init__ ==========

class Singleton:
    """Singleton pattern using __new__"""
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        """Create instance only once"""
        if cls._instance is None:
            print("__new__ called - Creating new instance")
            cls._instance = super().__new__(cls)
        else:
            print("__new__ called - Returning existing instance")
        return cls._instance
    
    def __init__(self, value):
        """Initialize instance (called every time)"""
        print(f"__init__ called with value={value}")
        self.value = value
    
    def __repr__(self):
        return f"Singleton(value={self.value})"


print("\n" + "=" * 60)
print("EXAMPLE 2: __new__ - Singleton Pattern")
print("=" * 60)

s1 = Singleton(10)
print(f"s1 = {s1}")
s2 = Singleton(20)
print(f"s2 = {s2}")
print(f"s1 is s2: {s1 is s2}")  # True - same instance
print(f"s1.value: {s1.value}")  # 20 (overwritten by s2's __init__)


# ========== EXAMPLE 3: __del__ - Destructor ==========

class Resource:
    """Demonstrating resource cleanup"""
    
    def __init__(self, name):
        self.name = name
        print(f"Resource '{name}' created")
    
    def __del__(self):
        """Called when object is about to be destroyed"""
        print(f"Resource '{self.name}' is being destroyed")
    
    def use(self):
        print(f"Using resource '{self.name}'")


print("\n" + "=" * 60)
print("EXAMPLE 3: __del__ - Destructor")
print("=" * 60)

def create_resource():
    r = Resource("Database Connection")
    r.use()
    # r will be destroyed when function ends

create_resource()
print("Function ended, resource should be destroyed now")


# ========== EXAMPLE 4: __hash__ & __eq__ - Make Objects Hashable ==========

class Point:
    """A hashable point for use in sets and dicts"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        """Two points are equal if coordinates match"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __hash__(self):
        """Enable: Point in sets and as dict keys"""
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"


print("\n" + "=" * 60)
print("EXAMPLE 4: __hash__ - Hashable Objects")
print("=" * 60)

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

# Use in sets
points_set = {p1, p2, p3}
print(f"Set of points: {points_set}")  # p1 and p2 are same, so only 2 items
print(f"p1 == p2: {p1 == p2}")
print(f"hash(p1) == hash(p2): {hash(p1) == hash(p2)}")

# Use as dict keys
point_data = {
    p1: "First point",
    p3: "Third point"
}
print(f"point_data[p1]: {point_data[p1]}")
print(f"point_data[p2]: {point_data[p2]}")  # Same as p1


# ========== EXAMPLE 5: __slots__ - Memory Optimization ==========

class VectorWithSlots:
    """Using __slots__ to save memory"""
    __slots__ = ['x', 'y']  # Only these attributes allowed
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"VectorWithSlots({self.x}, {self.y})"


print("\n" + "=" * 60)
print("EXAMPLE 5: __slots__ - Memory Optimization")
print("=" * 60)

v1 = VectorWithSlots(3, 4)
print(f"v1 = {v1}")
print(f"v1.x = {v1.x}")
# v1.z = 5  # This would raise AttributeError (not in __slots__)

import sys
print(f"Size with __slots__: {sys.getsizeof(v1)} bytes")


class VectorWithoutSlots:
    """Normal class with __dict__"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


v2 = VectorWithoutSlots(3, 4)
print(f"Size without __slots__: {sys.getsizeof(v2.__dict__)} bytes")


# ========== EXAMPLE 6: __getattr__, __setattr__, __delattr__ ==========

class SmartObject:
    """Dynamic attribute handling"""
    
    def __init__(self):
        self._data = {}
        self._protected = "can't delete me"
    
    def __getattr__(self, name):
        """Called when attribute NOT found"""
        print(f"__getattr__ called for '{name}'")
        return self._data.get(name, f"Attribute '{name}' not found")
    
    def __setattr__(self, name, value):
        """Called for ALL attribute assignments"""
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print(f"__setattr__ called: {name} = {value}")
            self._data[name] = value
    
    def __delattr__(self, name):
        """Called when deleting attributes"""
        if name == '_protected':
            raise AttributeError("Cannot delete protected attribute")
        print(f"__delattr__ called for '{name}'")
        if name in self._data:
            del self._data[name]
    
    def __repr__(self):
        return f"SmartObject({self._data})"


print("\n" + "=" * 60)
print("EXAMPLE 6: Dynamic Attribute Handling")
print("=" * 60)

obj = SmartObject()
obj.name = "Mahad"      # __setattr__
obj.age = 25            # __setattr__
print(f"obj = {obj}")
print(f"obj.name: {obj.name}")
print(f"obj.salary: {obj.salary}")  # __getattr__ (not found)

del obj.age             # __delattr__
print(f"After del obj.age: {obj}")


# ========== EXAMPLE 7: __dir__ - Customize dir() ==========

class CustomClass:
    """Custom dir() output"""
    
    def __init__(self):
        self.public_attr = 1
        self._private_attr = 2
        self.__very_private = 3
    
    def public_method(self):
        pass
    
    def _private_method(self):
        pass
    
    def __dir__(self):
        """Return custom list of attributes"""
        return ['public_attr', 'public_method', 'custom_added']


print("\n" + "=" * 60)
print("EXAMPLE 7: __dir__ - Customize dir()")
print("=" * 60)

cc = CustomClass()
print(f"dir(cc): {dir(cc)}")


# ========== EXAMPLE 8: __instancecheck__ & __subclasscheck__ ==========

class Meta(type):
    """Metaclass with custom instance/subclass checks"""
    
    def __instancecheck__(cls, instance):
        """Custom isinstance() behavior"""
        print(f"__instancecheck__ called for {instance}")
        return hasattr(instance, 'validate')
    
    def __subclasscheck__(cls, subclass):
        """Custom issubclass() behavior"""
        print(f"__subclasscheck__ called for {subclass}")
        return hasattr(subclass, 'validate')


class Validator(metaclass=Meta):
    pass


class GoodValidator:
    def validate(self):
        return True


class BadValidator:
    def invalid(self):
        return True


print("\n" + "=" * 60)
print("EXAMPLE 8: Metaclass - __instancecheck__ & __subclasscheck__")
print("=" * 60)

gv = GoodValidator()
bv = BadValidator()

print(f"isinstance(gv, Validator): {isinstance(gv, Validator)}")
print(f"isinstance(bv, Validator): {isinstance(bv, Validator)}")
print(f"issubclass(GoodValidator, Validator): {issubclass(GoodValidator, Validator)}")


# ========== EXAMPLE 9: __missing__ - Default Dict Behavior ==========

class MyDict(dict):
    """Dictionary with custom missing key behavior"""
    
    def __missing__(self, key):
        """Called when key is not found"""
        print(f"Key '{key}' not found, returning default")
        self[key] = 0  # Set default
        return 0
    
    def __repr__(self):
        return f"MyDict({super().__repr__()})"


print("\n" + "=" * 60)
print("EXAMPLE 9: __missing__ - Custom Missing Key Behavior")
print("=" * 60)

d = MyDict({'a': 1, 'b': 2})
print(f"d = {d}")
print(f"d['a']: {d['a']}")
print(f"d['z']: {d['z']}")  # __missing__ called
print(f"After accessing 'z': {d}")


# ========== EXAMPLE 10: __get__, __set__, __delete__ (Descriptors) ==========

class ValidatedAttribute:
    """Descriptor for validated attributes"""
    
    def __init__(self, min_value=0, max_value=100):
        self.min_value = min_value
        self.max_value = max_value
        self.data = {}
    
    def __get__(self, obj, objtype=None):
        """Called when getting attribute"""
        if obj is None:
            return self
        return self.data.get(id(obj), self.min_value)
    
    def __set__(self, obj, value):
        """Called when setting attribute"""
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Value must be between {self.min_value} and {self.max_value}")
        self.data[id(obj)] = value
        print(f"ValidatedAttribute set to {value}")
    
    def __delete__(self, obj):
        """Called when deleting attribute"""
        if id(obj) in self.data:
            del self.data[id(obj)]
            print("ValidatedAttribute deleted")


class Student:
    age = ValidatedAttribute(0, 150)
    grade = ValidatedAttribute(0, 100)
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def __repr__(self):
        return f"Student({self.name}, age={self.age}, grade={self.grade})"


print("\n" + "=" * 60)
print("EXAMPLE 10: Descriptors - __get__, __set__, __delete__")
print("=" * 60)

student = Student("Ali", 20, 85)
print(f"student = {student}")
print(f"student.age: {student.age}")
print(f"student.grade: {student.grade}")

try:
    student.age = 200  # Will raise ValueError
except ValueError as e:
    print(f"Error: {e}")


# ========== EXAMPLE 11: __prepare__, __init_subclass__ ==========

class BaseClass:
    """Base class tracking subclasses"""
    subclasses = []
    
    def __init_subclass__(cls, **kwargs):
        """Called when class is subclassed"""
        super().__init_subclass__(**kwargs)
        BaseClass.subclasses.append(cls)
        print(f"New subclass created: {cls.__name__}")


class Child1(BaseClass):
    pass


class Child2(BaseClass):
    pass


print("\n" + "=" * 60)
print("EXAMPLE 11: __init_subclass__ - Track Subclasses")
print("=" * 60)

print(f"BaseClass.subclasses: {BaseClass.subclasses}")


# ========== EXAMPLE 12: Comprehensive Dunder Methods Summary ==========

print("\n" + "=" * 60)
print("DUNDER METHODS QUICK REFERENCE")
print("=" * 60)

dunder_methods = {
    "Lifecycle": ["__new__", "__init__", "__del__"],
    "String Representation": ["__str__", "__repr__", "__format__"],
    "Comparison": ["__eq__", "__ne__", "__lt__", "__le__", "__gt__", "__ge__"],
    "Arithmetic": ["__add__", "__sub__", "__mul__", "__truediv__", "__floordiv__", "__mod__", "__pow__"],
    "Unary": ["__neg__", "__pos__", "__abs__", "__invert__"],
    "Augmented Assignment": ["__iadd__", "__isub__", "__imul__", "__itruediv__"],
    "Container/Sequence": ["__len__", "__getitem__", "__setitem__", "__delitem__", "__contains__", "__iter__"],
    "Callable": ["__call__"],
    "Attribute Access": ["__getattr__", "__setattr__", "__delattr__", "__dir__"],
    "Context Manager": ["__enter__", "__exit__"],
    "Descriptors": ["__get__", "__set__", "__delete__"],
    "Hashing": ["__hash__"],
    "Type Conversion": ["__int__", "__float__", "__bool__", "__round__"],
    "Metaclass": ["__prepare__", "__instancecheck__", "__subclasscheck__", "__init_subclass__"],
    "Memory": ["__slots__"],
    "Dict Missing": ["__missing__"],
}

for category, methods in dunder_methods.items():
    print(f"\n{category}:")
    for method in methods:
        print(f"  • {method}")
