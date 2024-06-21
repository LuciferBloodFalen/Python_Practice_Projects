def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            val = ord('a') if char.islower() else ord('A')
            cipher_char = chr((ord(char) - val + direction * shift) % 26 + val)
            result += cipher_char
        else:
            result += char
    return result

input_file_path = input("Enter the path of the input file: ")
output_file_path = input("Enter the path of the output file: ")
shift = int(input("Enter the shift value for encryption/decryption: "))
operation = input("Do you want to encrypt (E) or decrypt (D) the file? ")

direction = 1 if operation.lower() == 'e' else -1

with open(input_file_path, 'r') as file:
    text = file.read()
cipher_text = caesar_cipher(text, shift, direction)

with open(output_file_path, 'w') as file:
    file.write(cipher_text)

action = "encrypted" if operation.lower() == 'e' else "decrypted"
print(f"Operation {action} successfully!!")