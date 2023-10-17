#!/bin/bash

# ETAPAS ADICIONAIS:
# chmod +x generate_hash.sh
# apt install -y md5sum sha1sum sha256sum sha512sum

# Hash a partir de um texto:
# ./generate_hash.sh --texto

# Hash a partir de um arquivo:
# ./generate_hash.sh --arquivo


generate_hash() {
    texto="$1"
    tipo="$2"
    if [ "$tipo" == "md5" ]; then
        echo -n "$texto" | md5sum
    elif [ "$tipo" == "sha1" ]; then
        echo -n "$texto" | sha1sum
    elif [ "$tipo" == "sha256" ]; then
        echo -n "$texto" | sha256sum
    elif [ "$tipo" == "sha512" ]; then
        echo -n "$texto" | sha512sum
    else
        echo "Tipo de hash inválido"
    fi
}

main() {
    if [ "$1" == "--texto" ]; then
        read -p "Digite o texto: " texto
        read -p "Escolha o tipo de hash (md5, sha1, sha256, sha512): " tipo
        generate_hash "$texto" "$tipo"
    elif [ "$1" == "--arquivo" ]; then
        read -p "Digite o caminho para o arquivo: " arquivo
        if [ -f "$arquivo" ]; then
            read -p "Escolha o tipo de hash (md5, sha1, sha256, sha512): " tipo
            texto=$(cat "$arquivo")
            generate_hash "$texto" "$tipo"
        else
            echo "Arquivo não encontrado."
        fi
    else
        echo "Você deve especificar --texto ou --arquivo."
    fi
}

main "$@"
