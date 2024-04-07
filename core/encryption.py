from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

plaintext = b"Hello, world!"
cipher_text = cipher.encrypt(plaintext)
decrypted_text = cipher.decrypt(cipher_text)
