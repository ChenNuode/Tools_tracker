from hashlib import sha256

def hash(password):
	return sha256(password.encode("utf-8")).hexdigest()