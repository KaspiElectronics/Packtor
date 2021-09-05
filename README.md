# Packtor
**Packtor** is a simple and modern encryption Libray\CLI based on a hand written algorithm.

## Install Packtor
```
pip install git+https://github.com/KaspiElectronics/Packtor.git
```

## Example
```py
from packtor import packtor
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
or :
```bash
$ python -m packtor.packtor.py init
$ echo Hello World > h.txt
$ python packtor.packtor.py encryptf h.txt
  ...
$ python packtor.packtor.py decryptf cache/output_encrypt.txt
  ...
```

## License
**MIT**
