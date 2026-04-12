# The Logic Blueprint: The Smart Parking Garage

In this task, you aren't just calculating a number; you are managing a physical space using logic. You have to track **slots** and **time**.

## 1. The Setup (Data Structures)

- **Total Slots**: Start with a fixed number of parking spots (e.g., 10).
- **Occupied Slots**: Start this at `0`.
- **Rate**: Set a price (e.g., $5 per hour).

## 2. The Logic Gates (The Core Challenges)

Your program should handle three main **events**. This is where your brain has to work through the sequences:

### Event A: Vehicle Entry

- **Logic Check**: Is `Occupied Slots` less than `Total Slots`?
  - **Yes**: Increment `Occupied Slots` by 1. Record the "Entry Time" (you can just ask the user to input the hour, e.g., `14` for 2 PM).
  - **No**: Print `"Garage Full"` and deny entry.

### Event B: Vehicle Exit (The Math Logic)

This is the hardest part. You need to:

1. Ask for the **"Exit Time."**
2. **Calculate Duration**: `Exit Time - Entry Time`
3. **Apply Logic Rule**: What if the duration is less than 1 hour? (Usually, garages still charge for a full hour).
4. **Calculate Total**: `Duration * Rate`
5. **Free the Space**: Decrement `Occupied Slots` by 1.

### Event C: System Status

Show the user exactly how many spots are left and the total revenue collected so far.

## Why This Builds Logic

- **Capacity Management**: You are learning how to prevent a system from "overflowing" (adding more than the limit).
- **Time Handling**: Working with time (even just simple integers) forces you to think about how data changes over an interval.
- **Running Totals**: You have to maintain a `"Revenue"` variable that survives even after a car leaves.

## The "Edge Case" Challenge

Once you get the basics down, try to solve this logical puzzle:

> What happens if a car enters at 11 PM (23) and leaves at 2 AM (2)? If your code simply does `2 - 23`, you'll get a negative number!

Solving that **rollover logic** is what separates a beginner from a real programmer.
