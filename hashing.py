import argon2

argon2Hasher = argon2.PasswordHasher(
    time_cost=3, # number of iterations
    memory_cost=64 * 1024, # 64mb
    parallelism=1, # how many parallel threads to use
    hash_len=32, # the size of the derived key
    salt_len=16 # the size of the random generated salt in bytes
)


password = "somePassword"
 
hash = argon2Hasher.hash(password)
 
print("Hash + salt of password", hash)
 
verifyValid = argon2Hasher.verify(hash, password)
print("Password verification success:", verifyValid)