<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span>Desafio de Código</span>
    <img align="center" width="100px" src="https://hermes.dio.me/tracks/b092559f-ec20-4401-83e5-d98b6278b7b1.png">    
</h1>

Soluções propostas para o desafio de código do  **Santander Bootcamp Cibersegurança** pela [Digital Innovation One](https://www.dio.me/) <img width="70px" background-color="black" src="https://hermes.digitalinnovation.one/assets/diome/logo.svg">.

[![Link do Curso](https://img.shields.io/badge/▶-000?style=for-the-badge&logo=movie&logoColor=E94D5F)](https://web.dio.me/track/santander-bootcamp-ciberseguranca) 
[![Link do Curso](https://img.shields.io/badge/Acesse%20o%20Curso%20na%20Plataforma-E94D5F?style=for-the-badge)](https://web.dio.me/track/santander-bootcamp-ciberseguranca) 

## Desafio 1 - Verificando URL com **JavaScript**

### Descrição

Neste desafio, desenvolva uma solução que simule uma verificação de segurança em uma URL. Dessa forma, sua tarefa é implementar uma verificação que determine se uma URL é segura ou não.

**Lembre-se**: As URLs seguras começam com "https://" enquanto URLs não seguras começam com "http://".

**Entrada**
Para esse desafio, a entrada esperada é a URL que o usuário deseja verificar. A URL pode ser inserida como uma string de texto pelo usuário.

**Saída**
A saída esperada é o resultado da verificação de segurança da URL. Dependendo do protocolo da URL (HTTP ou HTTPS), o programa deve imprimir uma mensagem indicando se a URL é segura ou não segura.

**Exemplos**
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saída |
|---------|-----------------------------|
| https://web.dio.me/	| URL segura |
| https://github.com/	| URL segura |
| http://gitluby.com/	| URL nao segura |
| www.example.com | Formato invalido |

### Código:
```
// Leitura da entrada do usuário:
const url = gets();
var resultado;

if (url.startsWith("https://")) {
  resultado = "URL segura";
} else if ( url.startsWith("http://")) {
  resultado = "URL nao segura";
} else {
  resultado = "Formato invalido";
}
// Exibe o resultado
print(resultado);
```
Saídas:
> TESTE #1
> - **Dado de entrada:**
> - www.example.com
> - **Saída esperada:**
> - Formato invalido
> - **Sua Saída:**
> - Formato invalido

<br>

> TESTE #2
> - **Dado de entrada:**
> - http://gitluby.com/
> - **Saída esperada:**
> - URL nao segura
> - **Sua Saída:**
> - URL nao segura

<br>

> TESTE #3
> - **Dado de entrada:**
> - https://github.com/
> - **Saída esperada:**
> - URL segura
> - **Sua Saída:**
> - URL segura

## Desafio 2 -  Verificando URL com **Python**

```
url = input()

if "https://" in url:
    resultado = "URL segura"
elif "http://" in url:
    resultado = "URL nao segura"
else:
    resultado = "Formato invalido"

# Exibe o resultado
print(resultado)
```

## Desafio 3 -  Verificando URL com **Kotlin**

```
fun main() {
    // Lê a entrada do usuário ou usa uma string vazia se nenhuma entrada for fornecida
    val url = readLine() ?: "" 

    val resultado: String

    if (url.startsWith("https://")) {
        resultado = "URL segura"
    } else if (url.startsWith("http://")  ) {
        resultado = "URL nao segura"
    } else {
        resultado = "Formato invalido"
    }

    //Exibe o resultado
    println(resultado)
}
```

## Desafio 4 -  Verificando URL com **Java**

```
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String url = scanner.nextLine(); // Lê a entrada do usuário

        String resultado;
        if (url.startsWith("https://")) {
            resultado = "URL segura";
        } else if (url.startsWith("http://")) {
            resultado = "URL nao segura";
        } else {
            resultado = "Formato invalido";
        }

        // Exibe o resultado
        System.out.println(resultado);
    }
}
```

## Desafio 5 -  Verificando URL com **C#**

```
using System;

class Program {
    static void Main(string[] args) {
        // Lê a entrada do usuário
        string url = Console.ReadLine(); 

        string resultado;
        if (url.StartsWith("https://")) {
            resultado = "URL segura"; 
        } else if ( url.StartsWith("http://")) {
            resultado = "URL nao segura";
        } else {
            resultado = "Formato invalido";
        }

        // Exibe o resultado
        Console.WriteLine(resultado);
    }
}
```

## Redes Socias

[![PerfilDIO](https://img.shields.io/badge/DIO-0077B5?style=for-the-badge&logo=dio&logoColor=white)](https://web.dio.me/users/marcelo_soares92)
[![GitLab](https://img.shields.io/badge/GitLab-000?style=for-the-badge&logo=gitlab&logoColor=E94D5F)](https://gitlab.com/Mdsoare/)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://github.com/Mdsoare/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marcelodsoares/) 

<table>
  <tr>
    <td>
      <img width="80px" align="center" src="https://avatars.githubusercontent.com/Mdsoare"/>
    </td>
    <td align="left">
      <a href="https://github.com/Mdsoare">
        <span><b>Marcelo Soares</b></span>
      </a>
      <br>
      <span>Analista de Sistemas</span>
    </td>
  </tr>
</table>

##
<div align="center">Disponibilizado por <a href="https://github.com/Mdsoare">🕶 Marcelo Soares ®</a>.</div>