import os
import hashlib
import hmac

def hash_file(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def verify_hash(file_path, expected_hash):
    expected_hash = expected_hash.strip().lower()

    if len(expected_hash) != 64 or any(character not in "0123456789abcdef" for character in expected_hash):
        return False

    return hmac.compare_digest(hash_file(file_path), expected_hash)
 