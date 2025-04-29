#!/usr/bin/env python3
"""
File Read & Write Challenge
This program reads a file, modifies its content, and writes the result to a new file.
"""

import os
import sys


def read_file(filename):
    """
    Read content from a file.
    
    Args:
        filename (str): Path to the file to read
        
    Returns:
        str: Content of the file if successful
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        PermissionError: If the file can't be read due to permissions
        Exception: For other unexpected errors
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
        return None
    except Exception as e:
        print(f"Unexpected error reading '{filename}': {str(e)}")
        return None


def write_file(filename, content):
    """
    Write content to a file.
    
    Args:
        filename (str): Path to the file to write
        content (str): Content to write to the file
        
    Returns:
        bool: True if successful, False otherwise
        
    Raises:
        PermissionError: If the file can't be written due to permissions
        Exception: For other unexpected errors
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"Error: You don't have permission to write to '{filename}'.")
        return False
    except Exception as e:
        print(f"Unexpected error writing to '{filename}': {str(e)}")
        return False


def modify_content(content, modification_type="uppercase"):
    """
    Modify the content based on the specified modification type.
    
    Args:
        content (str): Content to modify
        modification_type (str): Type of modification to apply
        
    Returns:
        str: Modified content
    """
    if not content:
        return ""
        
    if modification_type == "uppercase":
        return content.upper()
    elif modification_type == "lowercase":
        return content.lower()
    elif modification_type == "capitalize_lines":
        return "\n".join([line.capitalize() for line in content.split("\n")])
    elif modification_type == "reverse_lines":
        return "\n".join([line for line in content.split("\n")][::-1])
    else:
        # Default modification
        return content.upper()


def get_modification_choice():
    """
    Prompt the user to choose a modification type.
    
    Returns:
        str: The chosen modification type
    """
    print("\nChoose a modification type:")
    print("1. Convert to UPPERCASE")
    print("2. Convert to lowercase")
    print("3. Capitalize each line")
    print("4. Reverse the order of lines")
    
    choice = input("Enter your choice (1-4): ")
    
    options = {
        "1": "uppercase",
        "2": "lowercase",
        "3": "capitalize_lines",
        "4": "reverse_lines"
    }
    
    return options.get(choice, "uppercase")


def main():
    """Main function that orchestrates the file operations."""
    print("=== File Read & Write Challenge ===")
    
    # Get input filename
    input_filename = input("Enter the name of the file to read: ")
    
    # Read the file
    content = read_file(input_filename)
    if content is None:
        return
    
    # Get modification choice
    mod_type = get_modification_choice()
    
    # Modify the content
    modified_content = modify_content(content, mod_type)
    
    # Get output filename
    output_filename = input("Enter the name of the file to write the modified content to: ")
    
    # Check if output file already exists
    if os.path.exists(output_filename):
        overwrite = input(f"File '{output_filename}' already exists. Overwrite? (y/n): ")
        if overwrite.lower() != 'y':
            print("Operation cancelled.")
            return
    
    # Write the modified content
    if write_file(output_filename, modified_content):
        print(f"Successfully wrote modified content to '{output_filename}'.")
        print(f"Modified {len(content)} characters using '{mod_type}' modification.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)