#!/bin/bash

# ETAPAS ADICIONAIS:
# chmod +x generate_hash.sh
# apt install -y coreutils

generate_hash_texto() {
    local texto="$1"
    local tipo="$2"
    
    case "$tipo" in
        md5)    echo -n "$texto" | md5sum ;;
        sha1)   echo -n "$texto" | sha1sum ;;
        sha256) echo -n "$texto" | sha256sum ;;
        sha512) echo -n "$texto" | sha512sum ;;
        *)      echo "Tipo de hash inválido" ;;
    esac
}

generate_hash_arquivo() {
    local arquivo="$1"
    local tipo="$2"

    case "$tipo" in
        md5)    md5sum "$arquivo" ;;
        sha1)   sha1sum "$arquivo" ;;
        sha256) sha256sum "$arquivo" ;;
        sha512) sha512sum "$arquivo" ;;
        *)      echo "Tipo de hash inválido" ;;
    esac
}

main() {
    if [[ "$1" == "--texto" ]]; then
        read -r -p "Digite o texto: " texto
        read -r -p "Escolha o tipo de hash (md5, sha1, sha256, sha512): " tipo
        generate_hash_texto "$texto" "$tipo"
    elif [[ "$1" == "--arquivo" ]]; then
        read -r -p "Digite o caminho para o arquivo: " arquivo
        if [[ -f "$arquivo" ]]; then
            read -r -p "Escolha o tipo de hash (md5, sha1, sha256, sha512): " tipo
            generate_hash_arquivo "$arquivo" "$tipo"
        else
            echo "Arquivo não encontrado."
        fi
    else
        echo "Você deve especificar --texto ou --arquivo."
    fi
}

main "$@"