import bcrypt

def password_hash(password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def main():
    password = input("Enter Password to hash: ")
    hash_password = password_hash(password)
    print(f"Hashed Password: {hash_password.decode()}")

if __name__ == "__main__":
    main()