import hashlib

def calculate_file_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    try:
        with open(file_path, 'rb') as f:
            sha256 = hashlib.sha256()
            while chunk := f.read(4096):
                sha256.update(chunk)
            return sha256.hexdigest()
    except Exception as e:
        print(f"[!] Error hashing file {file_path}: {e}")
        return None
