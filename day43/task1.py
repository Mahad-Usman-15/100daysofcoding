from pwdlib import PasswordHash

password_hash=PasswordHash.recommended()


def hashpassword(password):
    return password_hash.hash(password)

def verify_hash(hashedpassword,original):
    return password_hash.verify(original,hashedpassword)
password="impossible"
hashed_password=hashpassword(password)

print(verify_hash(password,hashed_password))