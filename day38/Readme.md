# ATM Simulator

A simple command-line ATM simulation built with Python's object-oriented programming features.

![ATM Simulator](/images/images.jpg)

## Features

### PIN Authentication

Secure access to the ATM system using a 4-digit PIN code. Users must enter the correct PIN before performing any transactions.

```python
pin = int(input("Enter the pin"))
if pin == bankaccount.pin:
    # Access granted
```

### Withdraw Funds

Withdraw cash from your account with automatic balance checking. The system prevents withdrawals that exceed available balance.

```python
def withdraw(self, amount):
    if self.amount > self.balance:
        print("insuffiencient balance")
    else:
        self.balance -= self.amount
        print("Amount withraw successfully")
```

### Deposit Funds

Add funds to your account with validation to prevent invalid (zero or negative) deposits.

```python
def deposit(self, amount):
    if self.amount <= 0:
        print("Invalid amount")
    else:
        self.balance += self.amount
        print("Amount deposited successfully")
```

### Check Balance

View your current account balance in real-time.

```python
def showbalance(self):
    print(f"Your Balance:{self.balance}")
```

### Session Management

Interactive menu system with graceful logout functionality, including a brief delay for realism.

```python
elif userchoice == 4:
    print("Logging Out...")
    time.sleep(1)
    condition = False
```

## How to Run

1. Navigate to the `day38` directory in your terminal
2. Run the script: `python task1.py`
3. Enter the PIN: `123`
4. Choose an option from the menu (1–4)
5. Follow the prompts to complete your transaction
6. Select "Log out" to exit safely

## Modules Used in the Program

- [Time Module](https://docs.python.org/3/library/time.html) — Provides the `sleep()` function for realistic logout delay




