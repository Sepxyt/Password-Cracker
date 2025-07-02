

import bcrypt

def password_crack(hashed_password: bytes, wordlist_file: str):
    with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            guess = line.strip()
            if bcrypt.checkpw(guess.encode('utf-8'), hashed_password):
                print(f"Password Cracked: {guess}")
                return True
    print("Password not found in wordlist ")
    return False

def main():
    hashed = input("Enter hashed password: ").encode('utf-8')
    wordlist = input("Enter path to wordlist file: ").strip()
    password_crack(hashed, wordlist)

if __name__ == "__main__":
    main()