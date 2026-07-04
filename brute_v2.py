import os
from pypdf import PdfReader

def find_pdf_password(pdf_path):
    # 1. Check if the file exists
    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' was not found.")
        return

    print(f"--- Attempting to open: {pdf_path} ---")

    try:
        # 2. Open the PDF
        reader = PdfReader(pdf_path)

        # 3. Check if it is encrypted
        if not reader.is_encrypted:
            print("[-] This PDF is not password protected. It opened without a password.")
            return

        print("[+] PDF is encrypted. Starting brute-force (0000-9999)...")

        # 4. Loop through 0000 to 9999
        for guess in range(10000):
            password = f"{guess:04d}"
            
            # reader.decrypt returns:
            # 0: Failure
            # 1: Success (User Password)
            # 2: Success (Owner Password)
            result = reader.decrypt(password)

            if result > 0:
                print(f"\n[!!!] SUCCESS! The password is: {password}")
                return
            
            # Debugging: Print progress every 1000 to show it's working
            if guess % 1000 == 0 and guess > 0:
                print(f"Still working... checked up to {password}")

        print("\n[-] Finished all 10,000 combinations. No match found.")

    except Exception as e:
        print(f"\n[!] An error occurred: {e}")
        print("Tip: If the error is about 'AES' or 'cryptography', run: pip install cryptography")

if __name__ == "__main__":
    # Ensure this path uses a raw string (r"...") or forward slashes (/)
    # Replace the path below with your specific file path
    file_path = r""
    
    find_pdf_password(file_path)