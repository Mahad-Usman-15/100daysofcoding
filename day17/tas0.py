"""
Dunder Methods Quick Reference Guide
Print this file for a comprehensive cheat sheet of Python dunder methods
"""

print("""
╔══════════════════════════════════════════════════════════╗
║          PYTHON DUNDER METHODS COMPLETE GUIDE            ║
╚══════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────┐
│ 1. OBJECT LIFECYCLE                                     │
├─────────────────────────────────────────────────────────┤
│ __new__(cls, ...)      → Create instance (before init)  │
│ __init__(self, ...)    → Initialize instance            │
│ __del__(self)          → Destructor (cleanup)           │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 2. STRING REPRESENTATION                                │
├─────────────────────────────────────────────────────────┤
│ __str__(self)          → str(obj), print(obj)           │
│ __repr__(self)         → repr(obj), obj in REPL         │
│ __format__(self, fmt)  → format(obj, 'spec')            │
│ __bytes__(self)        → bytes(obj)                     │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 3. COMPARISON OPERATORS                                 │
├─────────────────────────────────────────────────────────┤
│ __eq__(self, other)    → obj1 == obj2                   │
│ __ne__(self, other)    → obj1 != obj2                   │
│ __lt__(self, other)    → obj1 < obj2                    │
│ __le__(self, other)    → obj1 <= obj2                   │
│ __gt__(self, other)    → obj1 > obj2                    │
│ __ge__(self, other)    → obj1 >= obj2                   │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 4. ARITHMETIC OPERATORS                                 │
├─────────────────────────────────────────────────────────┤
│ __add__(self, other)     → obj1 + obj2                  │
│ __sub__(self, other)     → obj1 - obj2                  │
│ __mul__(self, other)     → obj1 * obj2                  │
│ __truediv__(self, other) → obj1 / obj2                  │
│ __floordiv__(self, oth)  → obj1 // obj2                 │
│ __mod__(self, other)     → obj1 % obj2                  │
│ __pow__(self, other)     → obj1 ** obj2                 │
│ __matmul__(self, other)  → obj1 @ obj2 (matrix mult)    │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 5. REVERSED ARITHMETIC (when obj is right operand)      │
├─────────────────────────────────────────────────────────┤
│ __radd__(self, other)    → other + obj                  │
│ __rsub__(self, other)    → other - obj                  │
│ __rmul__(self, other)    → other * obj                  │
│ __rtruediv__(self, oth)  → other / obj                  │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 6. AUGMENTED ASSIGNMENT                                 │
├─────────────────────────────────────────────────────────┤
│ __iadd__(self, other)    → obj1 += obj2                 │
│ __isub__(self, other)    → obj1 -= obj2                 │
│ __imul__(self, other)    → obj1 *= obj2                 │
│ __itruediv__(self, oth)  → obj1 /= obj2                 │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 7. UNARY OPERATORS                                      │
├─────────────────────────────────────────────────────────┤
│ __neg__(self)            → -obj                         │
│ __pos__(self)            → +obj                         │
│ __abs__(self)            → abs(obj)                     │
│ __invert__(self)         → ~obj                         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 8. TYPE CONVERSION                                      │
├─────────────────────────────────────────────────────────┤
│ __int__(self)            → int(obj)                     │
│ __float__(self)          → float(obj)                   │
│ __bool__(self)           → bool(obj)                    │
│ __complex__(self)        → complex(obj)                 │
│ __round__(self, n)       → round(obj, n)                │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 9. CONTAINER/SEQUENCE METHODS                           │
├─────────────────────────────────────────────────────────┤
│ __len__(self)            → len(obj)                     │
│ __getitem__(self, key)   → obj[key]                     │
│ __setitem__(self, k, v)  → obj[key] = value             │
│ __delitem__(self, key)   → del obj[key]                 │
│ __contains__(self, item) → item in obj                  │
│ __iter__(self)           → iter(obj), for x in obj      │
│ __reversed__(self)       → reversed(obj)                │
│ __missing__(self, key)   → dict[key] when missing       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 10. ATTRIBUTE ACCESS                                    │
├─────────────────────────────────────────────────────────┤
│ __getattr__(self, name)  → obj.name (not found)         │
│ __getattribute__(s, n)   → obj.name (always)            │
│ __setattr__(self, n, v)  → obj.name = value             │
│ __delattr__(self, name)  → del obj.name                 │
│ __dir__(self)            → dir(obj)                     │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 11. CALLABLE OBJECTS                                    │
├─────────────────────────────────────────────────────────┤
│ __call__(self, *args)    → obj() like function          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 12. CONTEXT MANAGERS (with statement)                   │
├─────────────────────────────────────────────────────────┤
│ __enter__(self)          → with obj as var:             │
│ __exit__(self, *args)    → exit with block              │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 13. DESCRIPTORS (Advanced OOP)                          │
├─────────────────────────────────────────────────────────┤
│ __get__(self, obj, cls)  → Get attribute from class     │
│ __set__(self, obj, val)  → Set attribute                │
│ __delete__(self, obj)    → Delete attribute             │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 14. HASHING & IDENTITY                                  │
├─────────────────────────────────────────────────────────┤
│ __hash__(self)           → hash(obj), set, dict keys    │
│ __index__(self)          → obj as int index             │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 15. METACLASS METHODS                                   │
├─────────────────────────────────────────────────────────┤
│ __prepare__(cls, ...)    → Prepare class namespace      │
│ __instancecheck__(cls)   → isinstance(obj, cls)         │
│ __subclasscheck__(cls)   → issubclass(sub, cls)         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 16. CLASS CREATION                                      │
├─────────────────────────────────────────────────────────┤
│ __init_subclass__(cls)   → When subclass created        │
│ __class_getitem__(cls)   → Class[Type] generics         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 17. MEMORY OPTIMIZATION                                 │
├─────────────────────────────────────────────────────────┤
│ __slots__                → Restrict attributes          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 18. ASYNCHRONOUS METHODS                                │
├─────────────────────────────────────────────────────────┤
│ __await__(self)          → await obj                    │
│ __aenter__(self)         → async with obj               │
│ __aexit__(self, *args)   → exit async with              │
│ __aiter__(self)          → async for x in obj           │
│ __anext__(self)          → Next async iteration         │
└─────────────────────────────────────────────────────────┘

╔══════════════════════════════════════════════════════════╗
║                    BEST PRACTICES                        ║
╠══════════════════════════════════════════════════════════╣
║ 1. Return NotImplemented (not NotImplementedError)      ║
║    when operation not supported for type                ║
║                                                         ║
║ 2. __str__ should be user-friendly                      ║
║    __repr__ should be developer-friendly (unambiguous)   ║
║                                                         ║
║ 3. If you define __eq__, also define __hash__           ║
║    (or set __hash__ = None)                             ║
║                                                         ║
║ 4. Use @property instead of __getattr__ when possible   ║
║                                                         ║
║ 5. __slots__ saves memory but prevents dynamic attrs    ║
║                                                         ║
║ 6. Always call super() in __init_subclass__             ║
║                                                         ║
║ 7. __del__ is not guaranteed to be called               ║
║    Use context managers for cleanup                     ║
╚══════════════════════════════════════════════════════════╝
""")
