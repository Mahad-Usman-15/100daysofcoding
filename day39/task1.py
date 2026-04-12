def lovefunc(flower1, flower2):
    """
    Checks if Timmy and Sarah are in love based on petal counts.
    Condition: One must be even and the other must be odd.
    """
    try:
        # Check if the sum of petals is odd. 
        # (Even + Odd always equals Odd. Even + Even or Odd + Odd always equals Even).
        if (flower1 + flower2) % 2 != 0:
            return "They Are in Love"
        else:
            return "They Are Not in Love"
    except TypeError:
        # This catches cases where flower1 or flower2 are not integers/floats
        return "Error: Please provide valid numbers for the petal counts."
    except Exception as e:
        # Catch-all for any other unexpected issues
        return f"An unexpected error occurred: {e}"

# --- Test Cases ---

# Case 1: One Even, One Odd (In Love)
print(f"Test 1: {lovefunc(1, 4)}") 

# Case 2: Both Even (Not in Love)
print(f"Test 2: {lovefunc(2, 2)}") 

# Case 3: Invalid Input (Handled by except block)
print(f"Test 3: {lovefunc(None, 'five')}")