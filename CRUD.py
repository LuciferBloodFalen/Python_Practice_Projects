def create_file(filename):
    with open(filename, 'w') as file:
        print(f"File created successfully.")

def overwrite_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
        print(f"File overwritten.")

def read_data(filename):
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")

def add_data(filename, data):
    with open(filename, 'a') as file:
        file.write(data)
        print(f"Data added successfully.")

def delete_data(filename, data):
    with open(filename, 'r') as file:
        full_data = file.read()
    with open(filename, 'w') as file:
        if data in full_data:
            full_data = full_data.replace(data, "")
            file.write(full_data)
            print(f"Data deleted from file. ")
        else:
            print(f"Data not found in file. ")

while True:
    print("\nMenu:")
    print("1. Create a File")
    print("2. Overwrite a File")
    print("3. Read a File")
    print("4. Add Data to a File")
    print("5. Delete Data from a File")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        filename = input("Enter the name of the file to create: ")
        create_file(filename)
    elif choice == '2':
        filename = input("Enter the name of the file to overwrite data: ")
        data = input("Enter the new data: ")
        overwrite_file(filename, data)
    elif choice == '3':
        filename = input("Enter the name of the file to read: ")
        read_data(filename)
    elif choice == '4':
        filename = input("Enter the name of the file to add data: ")
        data = input("Enter data to add into the file: ")
        add_data(filename, data)
    elif choice == '5':
        filename = input("Enter the name of the file to delete data: ")
        data = input("Enter the data to be deleted: ")
        delete_data(filename, data)
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again!")