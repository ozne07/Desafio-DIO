# 🛡️ Desafio DIO 

Este repositório contém a documentação do projeto prático do Bootcamp de Cibersegurança da DIO. O objetivo foi configurar um ambiente controlado para simular ataques de força bruta (Brute Force) e documentar as medidas de mitigação.

## 🎯 Objetivos do Desafio

- Configurar ambiente de virtualização com **Kali Linux** e **Metasploitable 2**.
- Realizar ataques de força bruta em serviços FTP e SMB utilizando a ferramenta **Medusa**.
- Compreender o funcionamento de ataques de dicionário e *password spraying*.
- Propor recomendações de segurança para prevenir estes ataques.

## 🛠️ Ferramentas Utilizadas

- **VirtualBox:** Para virtualização das máquinas.
- **Kali Linux:** Sistema operacional ofensivo (Atacante).
- **Metasploitable 2:** Máquina virtual vulnerável (Alvo).
- **Medusa:** Ferramenta de força bruta rápida e modular.
- **Nmap/Netdiscover:** Para reconhecimento de rede.

---

## 💻 Passo a Passo da Execução

### 1. Configuração do Ambiente
As máquinas virtuais foram configuradas em modo **Host-Only (Rede Interna)** para garantir que o tráfego ficasse isolado e seguro.

- **IP Atacante (Kali):** `192.168.15.90` 
- **IP Alvo (Metasploitable):** `192.168.15.91` 

### 2. Execução dos Ataques

#### Cenário 1: Força Bruta no FTP (Porta 21)
O objetivo foi descobrir a senha do usuário `msfadmin` no serviço FTP.

**Comando utilizado:**
\`\`\`bash
medusa -h 192.168.56.91 -u msfadmin -P wordlist_senhas.txt -M ftp
\`\`\`

#### Cenário 2: Enumeração e Ataque no SSH/SMB
Utilizando uma lista de usuários e senhas para testar múltiplas combinações.

**Comando utilizado:**
\`\`\`bash
medusa -h 192.168.56.91 -U wordlist_users.txt -P wordlist_senhas.txt -M ssh
\`\`\`

---

## 🛡️ Medidas de Mitigação

Para se proteger dos ataques demonstrados acima, as seguintes medidas são recomendadas:

1.  **Políticas de Senhas Fortes:** Exigir senhas longas, complexas e com rotação periódica para inviabilizar ataques de dicionário simples.
2.  **Limitação de Tentativas (Rate Limiting):** Implementar ferramentas como **Fail2Ban**, que bloqueiam o IP de origem após um número x de tentativas falhas de login.
3.  **Desabilitar Serviços Desnecessários:** Se o FTP não é essencial, ele deve ser desativado ou substituído por SFTP (SSH File Transfer Protocol).
4.  **Autenticação Multifator (MFA):** Adicionar uma camada extra de segurança além da senha.
5.  **Monitoramento de Logs:** Utilizar SIEM ou análise de logs para detectar picos de tentativas de autenticação falhas.

## 📚 Conclusão

Este laboratório permitiu compreender na prática como ferramentas automatizadas exploram credenciais fracas. A facilidade com que as senhas foram quebradas reforça a necessidade crítica de configurações de segurança robustas e monitoramento ativo.

---
*Projeto desenvolvido para o Bootcamp de Cibersegurança da DIO.*
