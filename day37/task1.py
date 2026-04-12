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