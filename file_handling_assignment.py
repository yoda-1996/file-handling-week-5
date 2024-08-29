

def main():
    try:
        
        with open('my_file.txt', 'w') as file:
            file.write("Hello, World!\n")
            file.write("This is a Python file handling example.\n")
            file.write("123456\n")

        
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File Contents:")
            print(content)

       
        with open('my_file.txt', 'a') as file:
            file.write("Appending some new lines.\n")
            file.write("Another line.\n")
            file.write("And one more.\n")

       
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nUpdated File Contents:")
            print(content)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nExecution finished.")

if __name__ == "__main__":
    main()
