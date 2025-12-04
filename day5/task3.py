# to determine wheter the number is perfect square or not
import math

def is_perfect_square(number: int) -> bool:
    """
    Return True if `number` is a perfect square, otherwise False.
    Negative numbers are never perfect squares in the set of real numbers.
    """
    if number < 0:
        return False

    # Use integer square root to avoid floating point inaccuracies.
    root = math.isqrt(number)
    return root * root == number

    
numb = 9
print(f"{'Perfect square' if is_perfect_square(numb) else 'Not a Perfect square'}")    
    
  
    



