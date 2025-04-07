# Python-Data-structures
# Python Assignment 5

This Python script includes two tasks:

1. **Student Marks Lookup using a Dictionary**
2. **List Slicing and Manipulation**

## Task 1: Student Marks Lookup

This task creates a dictionary of student names and their corresponding marks. The user can input a student's name to retrieve their marks.

### How it works:
- A dictionary named `students` stores student names as keys and their marks as values.
- The program prompts the user to enter a name.
- It capitalizes the input to ensure proper formatting and then checks if the name exists in the dictionary.
- If found, it prints the marks; otherwise, it notifies the user that the student was not found.

### Example:
```bash
Enter the student's name: Harry
Harry's marks: 99
```

## Task 2: List Slicing and Reversing

This task demonstrates list slicing by:
- Creating a list of numbers from 1 to 10.
- Extracting the first five elements.
- Reversing those extracted elements.

### Output:
```
Original list:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Extracted five elements:  [1, 2, 3, 4, 5]

Reversed extracted elements:  [5, 4, 3, 2, 1]
```

## Notes

- Make sure to capitalize the first letter of the student’s name when prompted (e.g., "Alice", not "alice").
- The list manipulation part runs automatically after the dictionary lookup.

