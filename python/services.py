#哈希加密的方法

import hashlib
def hash_encrypt(input) :
    hash_code=hashlib.sha256(input.encode).hexdigest()
    return hash_code