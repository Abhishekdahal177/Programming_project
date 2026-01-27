# hasher.py
import hashlib

def generate_file_hash(filepath):
    """
    Reads a file and returns its SHA-256 hash as a hexadecimal string.
    """
    sha256_hash = hashlib.sha256()
    
    try:
        with open(filepath, "rb") as f:
            # Read the file in chunks to handle large files efficiently
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
