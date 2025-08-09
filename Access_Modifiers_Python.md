# Access Modifiers in Python

Python does not have strict access modifiers like C#. Instead, it uses naming conventions to indicate the intended level of access for class members.

---

## 1. Public
- **Description:** Accessible from anywhere.
- **Syntax Example:**
    ```python
    class MyClass:
        def __init__(self):
            self.my_var = 10  # public attribute

        def my_method(self):  # public method
            pass
    ```

---

## 2. Protected (Convention)
- **Description:** Intended to be accessed only within the class and its subclasses. Indicated by a single underscore `_`.
- **Syntax Example:**
    ```python
    class MyClass:
        def __init__(self):
            self._my_var = 20  # protected attribute

        def _my_method(self):  # protected method
            pass
    ```

---

## 3. Private (Name Mangling)
- **Description:** Intended to be accessed only within the class. Indicated by a double underscore `__`. Python performs name mangling to make it harder to access from outside.
- **Syntax Example:**
    ```python
    class MyClass:
        def __init__(self):
            self.__my_var = 30  # private attribute

        def __my_method(self):  # private method
            pass
    ```

---

**Note:**  
These are conventions and do not enforce strict access control. All members can still