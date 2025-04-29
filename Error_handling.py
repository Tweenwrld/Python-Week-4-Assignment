#!/usr/bin/env python3
"""
Error Handling Lab
This program demonstrates comprehensive error handling
when working with files in Python.
"""

import os
import sys
import time


class FileError(Exception):
    """Base class for file operation exceptions in this program."""
    pass


class FileReadError(FileError):
    """Exception raised when a file cannot be read."""
    pass


class FileWriteError(FileError):
    """Exception raised when a file cannot be written."""
    pass


def validate_filename(filename):
    """
    Validate that a filename is properly formatted.
    
    Args:
        filename (str): The filename to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # Check if filename is empty
    if not filename.strip():
        print("Error: Filename cannot be empty.")
        return False
    
    # Check for invalid characters in different operating systems
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        if char in filename:
            print(f"Error: Filename contains invalid character '{char}'.")
            return False
    
    return True


def check_file_access(filename, mode='r'):
    """
    Check if a file can be accessed in the specified mode.
    
    Args:
        filename (str): The filename to check
        mode (str): The access mode to check ('r' for read, 'w' for write)
        
    Returns:
        tuple: (bool, str) - Success flag and message
    """
    if mode == 'r':
        # Check if file exists
        if not os.path.exists(filename):
            return False, f"The file '{filename}' does not exist."
        
        # Check if it's a file (not a directory)
        if not os.path.isfile(filename):
            return False, f"'{filename}' is not a file."
        
        # Check if file is readable
        if not os.access(filename, os.R_OK):
            return False, f"You don't have permission to read '{filename}'."
    
    elif mode == 'w':
        # If file exists, check if it's writable
        if os.path.exists(filename):
            if not os.access(filename, os.W_OK):
                return False, f"You don't have permission to write to '{filename}'."
        else:
            # Check if directory is writable
            directory = os.path.dirname(filename) or '.'
            if not os.access(directory, os.W_OK):
                return False, f"You don't have permission to write to the directory containing '{filename}'."
    
    return True, "File access check passed."


def read_file_with_retries(filename, max_retries=3, retry_delay=1):
    """
    Read a file with retry logic.
    
    Args:
        filename (str): The file to read
        max_retries (int): Maximum number of retry attempts
        retry_delay (int): Delay between retries in seconds
        
    Returns:
        str: The content of the file
        
    Raises:
        FileReadError: If the file cannot be read after all retries
    """
    attempts = 0
    last_error = None
    
    while attempts < max_retries:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise FileReadError(f"The file '{filename}' was not found.")
        except PermissionError:
            raise FileReadError(f"Permission denied when trying to read '{filename}'.")
        except UnicodeDecodeError:
            raise FileReadError(f"The file '{filename}' contains characters that cannot be decoded. Try a different encoding.")
        except IsADirectoryError:
            raise FileReadError(f"'{filename}' is a directory, not a file.")
        except (IOError, OSError) as e:
            # These are potentially transient errors, so we can retry
            last_error = str(e)
            attempts += 1
            print(f"Error reading file (attempt {attempts}/{max_retries}): {last_error}")
            
            if attempts < max_retries:
                print(f"Retrying in {retry_delay} second(s)...")
                time.sleep(retry_delay)
                continue
            else:
                raise FileReadError(f"Failed to read '{filename}' after {max_retries} attempts. Last error: {last_error}")
        except Exception as e:
            # Unexpected error
            raise FileReadError(f"Unexpected error reading '{filename}': {str(e)}")


def display_file_info(filename):
    """
    Display information about a file.
    
    Args:
        filename (str): The file to display information about
    """
    try:
        file_size = os.path.getsize(filename)
        mod_time = os.path.getmtime(filename)
        
        # Convert size to human-readable format
        size_units = ["B", "KB", "MB", "GB", "TB"]
        size_index = 0
        size_value = file_size
        
        while size_value > 1024 and size_index < len(size_units) - 1:
            size_value /= 1024
            size_index += 1
        
        human_size = f"{size_value:.2f} {size_units[size_index]}"
        
        # Convert modification time to readable format
        mod_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mod_time))
        
        print("\nFile Information:")
        print(f"Filename: {os.path.basename(filename)}")
        print(f"Size: {human_size} ({file_size} bytes)")
        print(f"Last modified: {mod_time_str}")
        print(f"Full path: {os.path.abspath(filename)}")
        
    except OSError as e:
        print(f"Error retrieving file information: {str(e)}")


def main():
    """Main function that demonstrates file error handling."""
    print("=== Error Handling Lab ===")
    print("This program demonstrates comprehensive error handling with files.")
    
    # Get filename from user
    while True:
        filename = input("\nEnter the name of a file to read: ")
        
        # Validate filename format
        if not validate_filename(filename):
            continue
        
        # Check file accessibility
        access_ok, message = check_file_access(filename, 'r')
        if not access_ok:
            print(f"Error: {message}")
            retry = input("Try another file? (y/n): ")
            if retry.lower() != 'y':
                print("Exiting program.")
                return
            continue
        
        break
    
    # Try to read the file with retry logic
    try:
        start_time = time.time()
        content = read_file_with_retries(filename)
        end_time = time.time()
        
        # Display file information
        display_file_info(filename)
        
        # Display file statistics
        line_count = content.count('\n') + 1 if content else 0
        word_count = len(content.split()) if content else 0
        char_count = len(content) if content else 0
        
        print("\nFile Content Statistics:")
        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Characters: {char_count}")
        print(f"Read time: {(end_time - start_time):.4f} seconds")
        
        # Ask if user wants to see the content
        show_content = input("\nWould you like to see the file content? (y/n): ")
        if show_content.lower() == 'y':
            print("\n--- File Content Start ---")
            # Show first 500 characters with ellipsis if longer
            if len(content) > 500:
                print(content[:500] + "...\n[Content truncated]")
            else:
                print(content)
            print("--- File Content End ---")
        
    except FileReadError as e:
        print(f"File reading error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    finally:
        print("\nProgram finished.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        sys.exit(0)