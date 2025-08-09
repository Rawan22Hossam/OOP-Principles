# Access Modifiers in C#

Access modifiers in C# define the visibility and accessibility of classes, methods, and other members. Here are the main access modifiers:

---

## 1. `public`
- **Description:** Accessible from any other code.
- **Syntax Example:**
    ```csharp
    public class MyClass
    {
        public int MyProperty { get; set; }
    }
    ```

---

## 2. `private`
- **Description:** Accessible only within the containing class.
- **Syntax Example:**
    ```csharp
    class MyClass
    {
        private int myField;
    }
    ```

---

## 3. `protected`
- **Description:** Accessible within the containing class and by derived classes.
- **Syntax Example:**
    ```csharp
    class MyClass
    {
        protected void MyMethod() { }
    }
    ```

---

## 4. `internal`
- **Description:** Accessible only within the same assembly (project).
- **Syntax Example:**
    ```csharp
    internal class MyClass
    {
        internal void MyMethod() { }
    }
    ```

---

## 5. `protected internal`
- **Description:** Accessible within the same assembly or from derived classes in other assemblies.
- **Syntax Example:**
    ```csharp
    protected internal void MyMethod() { }
    ```

---

## 6. `private protected`
- **Description:** Accessible within the containing class or derived classes, but only within the same assembly.
- **Syntax Example:**
    ```csharp
    private protected void MyMethod() {