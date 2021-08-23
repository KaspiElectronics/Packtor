# Packtor
**Packtor** is a simple and modern encryptation based on a hand written algorithm.

## Example
```py
import packtor
text = "Hello World"

# create a random algorithm
# algorithm data writes to "algorithm.json" and "algorithm_decrypt.json"
packtor.init()

# encrypt the text
encrypted = packtor.encrypt(text)
print(encrypted)

# decrypt encryped text
decrypted = packtor.decrypte(encrypted)
print(decrypted)
```
