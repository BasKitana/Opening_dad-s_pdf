import os
from pypdf import PdfReader


def find_pdf_password(pdf_path):
    # Check if the file exists
    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' was not found.")
        return

    print("Opening PDF and starting brute-force (0000-9999)...")

    try:
        reader = PdfReader(pdf_path)

        # Check if the PDF is actually encrypted
        if not reader.is_encrypted:
            print("This PDF is not password protected.")
            return

        # Loop through all possible 4-digit combinations
# Loop through all possible 4-digit combinations
        for guess in range(1000000):  # 000000 to 999999
            password = f"{guess:06d}"
            
            # Print the attempt to the screen so you can see it
            print(f"Trying: {password}")
            
            # Attempt to decrypt
            result = reader.decrypt(password)
            
            if result:
                print(f"\n[+] Success! The password is: {password}")
                return

            # Optional: Print progress every 1000 attempts so you know it's working
            if guess % 1000000 == 0 and guess > 0:
                print(f"Tested up to {password}...")

        print("\n[-] Failed to find the password. Are you sure it is 4 digits?")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Replace this with the actual path to your father's PDF file
    file_path = r""
    find_pdf_password(file_path)