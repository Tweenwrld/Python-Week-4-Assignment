# Python File Handling Assignment

## Overview

This repository contains two Python programs that demonstrate advanced file handling techniques with comprehensive error handling. These programs are designed to showcase best practices for reading, modifying, and writing files in Python.

## Programs Included

### 1. File Read & Write Challenge

A program that reads a file, applies transformations to its content, and writes the modified content to a new file.

**Key Features:**
- Reading from and writing to files using proper resource management
- Multiple content transformation options (uppercase, lowercase, capitalize, reverse lines)
- User interaction for selecting files and transformation methods
- Overwrite protection for existing files
- Comprehensive error handling

### 2. Error Handling Lab

A program that demonstrates robust error handling techniques when working with files.

**Key Features:**
- Custom exception classes for file operations
- Filename validation and format checking
- File access permission verification
- Retry logic for transient errors
- Detailed file information display (size, modification time, etc.)
- File content statistics (line count, word count, character count)

## Core Concepts Covered

### File Operations
- Opening and closing files properly using context managers (`with` statement)
- Reading file content into memory
- Writing content to files
- Checking file existence and permissions

### Error Handling
- Using try/except blocks to catch specific exceptions
- Creating custom exception classes
- Implementing retry mechanisms for transient errors
- Graceful degradation when errors occur
- User-friendly error messages

### Input Validation
- Validating user input
- Checking filename format
- Verifying file accessibility before operations

### User Interface
- Clear, informative prompts and messages
- Operation status updates
- Confirmation before destructive operations
- Program flow control

### Code Organization
- Modular design with well-defined functions
- Comprehensive docstrings
- Logical flow of operations
- Clean code structure

## Best Practices Demonstrated

1. **Resource Management**: Proper handling of file resources using context managers
2. **Defensive Programming**: Anticipating and handling potential errors
3. **User Experience**: Clear communication with the user throughout operations
4. **Input Validation**: Verifying user input before performing operations
5. **Code Documentation**: Thorough docstrings and comments explaining functionality
6. **Exception Handling**: Catching specific exceptions and providing helpful error messages
7. **Modularity**: Breaking functionality into logical, reusable components

## Running the Programs

Both programs can be run directly from the command line:

```bash
# For the File Read & Write Challenge
python Read_write.py

# For the Error Handling Lab
python Error_handling.py
```

Follow the on-screen prompts to interact with each program.

## Learning Outcomes

Working with these programs I understand:
- How to safely handle file operations in Python
- Proper error handling techniques for file I/O
- How to create user-friendly interfaces for file operations
- Best practices for working with user input and file paths
- Techniques for providing informative feedback during operations

