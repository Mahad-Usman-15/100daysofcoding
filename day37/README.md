# ⏰ Time-Based Greeting Script

## 📌 Overview

This example demonstrates:

* Headings
* Lists
* Code blocks

It uses Python to print greetings based on the current time.

---

## 🧠 How It Works

* Fetches current time using `datetime`
* Checks hour range
* Prints appropriate greeting

---

## 📋 Conditions

* 🌅 Morning → 6 AM – 12 PM
* 🌞 Afternoon → 12 PM – 5 PM
* 🌇 Evening → 5 PM – 7 PM
* 🌙 Night → 7 PM – 6 AM

---

## 💻 Python Code

```python
from datetime import datetime

hour = datetime.now().hour

if 6 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 17:
    print("Good Afternoon!")
elif 17 <= hour < 19:
    print("Good Evening")
else:
    print("Good Night")
```

---

## ⚠️ Issues in Your Original Code

* ❌ `datetime.now().time().hour` is unnecessarily repeated
* ❌ `hour > 19 and hour < 6` → impossible condition
* ❌ Edge values (like exactly 12, 17) were excluded

---

## ✅ Improvements Made

* ✔ Stored hour in a variable (`hour`)
* ✔ Fixed logical ranges
* ✔ Covered all 24 hours properly using `else`

---

## 🚀 Tip

Always simplify conditions and avoid repeating function calls—it makes code cleaner and faster.
