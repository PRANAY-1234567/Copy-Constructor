# 🔁 Copy Constructor Simulation in Python (Sample Class)

## 📌 Description

This Python program demonstrates how to simulate a **copy constructor** using a class. It creates a new object by copying values from an existing object and modifying them.

---

## 🚀 Features

* Defines a `Sample` class
* Supports:

  * Parameterized constructor
  * Copy constructor (using object as argument)
* Automatically modifies copied values (+5)
* Displays object data

---

## 🛠️ How It Works

1. The constructor `__init__(self, x=None, y=None, z=None)` checks:

   * If `x` is an object of `Sample` → copy constructor is used
   * Otherwise → normal parameterized constructor

2. **Copy Constructor Logic**:

   * Copies values from another object
   * Adds `+5` to each value

3. Objects created:

   * `s1` → initialized with values `(53, 66, 68)`
   * `s2` → copy of `s1` (+5 added)
   * `s3` → copy of `s2` (+5 added again)

---

## 💻 Code

```python id="m4x9pt"
class Sample:
    def __init__(self, x=None, y=None, z=None):
        # Parameterized constructor
        if isinstance(x, Sample):   # copy constructor case
            t = x
            self.x = t.x + 5
            self.y = t.y + 5
            self.z = t.z + 5
        else:
            self.x = x
            self.y = y
            self.z = z

    def display(self):
        print(f"x = {self.x}\ty = {self.y}\tz = {self.z}")


s1 = Sample(53, 66, 68)
s2 = Sample(s1)   # copy constructor
s3 = Sample(s2)   # copy constructor again

s1.display()
s2.display()
s3.display()
```

---

## ▶️ Example Output

```id="y8q2nv"
x = 53	y = 66	z = 68
x = 58	y = 71	z = 73
x = 63	y = 76	z = 78
```

---

## 📚 Concepts Used

* Class and Object
* Constructor (`__init__`)
* Copy constructor (simulation in Python)
* `isinstance()` function
* Method definition

---

## 🎯 Use Case

This program helps beginners understand:

* How object copying works in Python
* Difference between normal constructor and copy constructor
* How values can be modified during copying

---

## 🔧 Future Improvements

* Create an exact copy (without modifying values)
* Add deep copy vs shallow copy examples
* Use `copy` module for advanced copying
* Add input-based object creation

--

## 📄 License

This project is open-source and free to use.
![Uploading image.png…]()
