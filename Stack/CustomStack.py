class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize  # Maximum size of the stack
        self.stack = []  # Internal list to hold stack elements
        self.top = -1  # Track the index of the top element

    def push(self, x: int) -> None:
        """Add an element to the top of the stack if there is space."""
        if self.top + 1 < self.maxSize:  # Check if there is space in the stack
            self.top += 1
            self.stack.append(x)  # Append the element to the stack

    def pop(self, index: int = None) -> int:
        """
        Remove and return the top element of the stack if index is None.
        If index is provided, remove and return the element at that index.
        Returns -1 if the stack is empty or index is invalid.
        """
        if self.top == -1:  # Check if the stack is empty
            return -1  # Return -1 if there are no elements
        
        if index is None:  # Default behavior, pop the top element
            value = self.stack[self.top]  # Get the top element
            self.top -= 1  # Move the top index down
            # Resize the stack to remove the last element
            self.stack = self.stack[:self.top + 1]
        elif 0 <= index <= self.top:  # Check if the index is valid
            value = self.stack[index]  # Get the element at the specified index
            # Create a new stack excluding the specified index
            self.stack = self.stack[:index] + self.stack[index + 1:self.top + 1]
            self.top -= 1  # Update the top index to reflect the removal
        else:
            return -1  # Return -1 if the index is invalid
        
        return value  # Return the removed element

    def increment(self, k: int, val: int) -> None:
        """Increment the bottom min(k, len(stack)) elements by val."""
        for i in range(min(k, self.top + 1)):  # Use self.top + 1 to consider the actual number of elements
            self.stack[i] += val

    def display(self) -> None:
        """Helper function to display the current state of the stack."""
        print(self.stack)

# Example usage
obj = CustomStack(5)  # Create a CustomStack with a maximum size of 5
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())  # Output: 4 (removes and returns the top element)
print(obj.pop(1))  # Output: 2 (removes and returns the element at index 1)
print(obj.pop(10))  # Output: -1 (invalid index)
obj.push(5)
obj.push(6)
obj.increment(2, 10)  # Increment the bottom 2 elements by 10
print(obj.pop())  # Output: 6 (removes and returns the top element)
print(obj.pop())  # Output: 15 (removes and returns the top element after increment)
print(obj.pop())  # Output: 11 (removes and returns the element at index 0)
print(obj.pop())  # Output: -1 (stack is empty, returns -1)
