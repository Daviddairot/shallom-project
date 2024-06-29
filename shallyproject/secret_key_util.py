# secret_key_util.py
import os
import random
import string

SECRET_KEY_FILE = os.path.join(os.path.dirname(__file__), 'secret_key.txt')

def generate_secret_key(length=50):
    """Generate a random SECRET_KEY."""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def get_or_create_secret_key():
    """Get or create a new SECRET_KEY and save it to the file."""
    if os.path.exists(SECRET_KEY_FILE):
        with open(SECRET_KEY_FILE, 'r') as f:
            secret_key = f.read().strip()
    else:
        secret_key = generate_secret_key()
        with open(SECRET_KEY_FILE, 'w') as f:
            f.write(secret_key)
    return secret_key

def rotate_secret_key():
    """Rotate the SECRET_KEY and update the file."""
    secret_key = generate_secret_key()
    with open(SECRET_KEY_FILE, 'w') as f:
        f.write(secret_key)
    return secret_key
