def decrypt_otp(encrypted_file, key_file, output_file):
    try:
        with open(encrypted_file, 'rb') as encrypted_file, open(key_file, 'rb') as key_file, open(output_file, 'wb') as output_file:
            encrypted_data = encrypted_file.read()
            key_data = key_file.read()

            if len(encrypted_data) != len(key_data):
                print("Error: The encrypted data and key must have the same length.")
                return

            decrypted_data = bytes([a ^ b for a, b in zip(encrypted_data, key_data)])
            output_file.write(decrypted_data)
            print("Decryption successful. The result has been saved to", output_file.name)
    except FileNotFoundError as e:
        print("Error:", str(e))

if __name__ == "__main__":
    encrypted_file = input("Enter the path to the encrypted file: ")
    key_file = input("Enter the path to the key file: ")
    output_file = input("Enter the path for the output file: ")

    decrypt_otp(encrypted_file, key_file, output_file)
