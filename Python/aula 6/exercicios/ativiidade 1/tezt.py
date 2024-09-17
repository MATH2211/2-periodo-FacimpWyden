import os

# Nome do arquivo onde os dados serão armazenados
ARQUIVO_CONTATOS = 'contatos.txt'

def criar_arquivo():
    """Cria o arquivo de contatos se não existir."""
    if not os.path.exists(ARQUIVO_CONTATOS):
        with open(ARQUIVO_CONTATOS, 'w') as f:
            pass  # Apenas cria o arquivo vazio

def criar_contato(nome, telefone):
    """Cria um novo contato e o adiciona ao arquivo."""
    with open(ARQUIVO_CONTATOS, 'a') as f:
        f.write(f"{nome},{telefone}\n")

def ler_contatos():
    """Lê e exibe todos os contatos do arquivo."""
    if not os.path.exists(ARQUIVO_CONTATOS):
        print("Arquivo de contatos não encontrado.")
        return

    with open(ARQUIVO_CONTATOS, 'r') as f:
        contatos = f.readlines()

    if not contatos:
        print("Nenhum contato encontrado.")
        return

    print("Contatos:")
    for contato in contatos:
        nome, telefone = contato.strip().split(',')
        print(f"Nome: {nome}, Telefone: {telefone}")

def atualizar_contato(nome_antigo, novo_nome, novo_telefone):
    """Atualiza um contato existente."""
    if not os.path.exists(ARQUIVO_CONTATOS):
        print("Arquivo de contatos não encontrado.")
        return

    with open(ARQUIVO_CONTATOS, 'r') as f:
        contatos = f.readlines()

    with open(ARQUIVO_CONTATOS, 'w') as f:
        contato_atualizado = False
        for contato in contatos:
            nome, telefone = contato.strip().split(',')
            if nome == nome_antigo:
                f.write(f"{novo_nome},{novo_telefone}\n")
                contato_atualizado = True
            else:
                f.write(contato)

        if not contato_atualizado:
            print("Contato não encontrado.")

def deletar_contato(nome):
    """Deleta um contato existente."""
    if not os.path.exists(ARQUIVO_CONTATOS):
        print("Arquivo de contatos não encontrado.")
        return

    with open(ARQUIVO_CONTATOS, 'r') as f:
        contatos = f.readlines()

    with open(ARQUIVO_CONTATOS, 'w') as f:
        contato_deletado = False
        for contato in contatos:
            nome_contato, telefone = contato.strip().split(',')
            if nome_contato == nome:
                contato_deletado = True
            else:
                f.write(contato)

        if not contato_deletado:
            print("Contato não encontrado.")

# Funções principais do CRUD
def main():
    criar_arquivo()
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Criar contato")
        print("2. Ler contatos")
        print("3. Atualizar contato")
        print("4. Deletar contato")
        print("5. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            criar_contato(nome, telefone)
        elif opcao == '2':
            ler_contatos()
        elif opcao == '3':
            nome_antigo = input("Digite o nome do contato a ser atualizado: ")
            novo_nome = input("Digite o novo nome do contato: ")
            novo_telefone = input("Digite o novo telefone do contato: ")
            atualizar_contato(nome_antigo, novo_nome, novo_telefone)
        elif opcao == '4':
            nome = input("Digite o nome do contato a ser deletado: ")
            deletar_contato(nome)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
