from tkinter import *

def mostrar_serviço():
    servico_var.set("Selecione o serviço")  # Define um texto padrão para o menu

def gerar_script():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    ponto_referencia = entry_ponto_referencia.get()
    servico = servico_var.get()

    resultado = ""

    if servico == "Serviço emergencial":
        resultado = (f"NOME: {nome}\nTelefone: {telefone}\nPONTO DE REFERENCIA: {ponto_referencia}\n"
                     "CLIENTE INFORMA QUE ESTA COM FALTA DE ENERGIA INDIVIDUAL SOLICITA AGILIDADE NO ATENDIMENTO")
    elif servico == "Serviço de protocolo":
        resultado = (f"NOME: {nome}\nTelefone: {telefone}\nPONTO DE REFERENCIA: {ponto_referencia}\n"
                     "CLIENTE ENTROU EM CONTATO PARA OBTER INFORMAÇÕES REFERENTE AO SEU PROTOCOLO")
    elif servico == "Serviço canal errado":
        resultado = (f"NOME: {nome}\nTelefone: {telefone}\nPONTO DE REFERENCIA: {ponto_referencia}\n"
                     "CLIENTE INFORMADO QUE ESSE CANAL ATENDE APENAS UNIDADES DE ALTA TENSÃO E PODER PUBLICO, FOI PASSADO O NUMERO CORRETO AO MESMO")
    elif servico == "Serviço de reclamação":
        descricao = entry_descricao.get()
        remediacao = entry_remediacao.get()
        meio_de_resposta = entry_meio_de_resposta.get()
        resultado = (f"O cliente {nome} do telefone {telefone} próximo {ponto_referencia}\n"
                     f"reclamou o seguinte problema: {descricao}\n"
                     f"deseja que seja resolvido com: {remediacao}\n"
                     f"deseja receber a resposta por meio de: {meio_de_resposta}")
    else:
        resultado = "Opção inválida"

    # Exibir o resultado na área de texto
    text_resultado.delete(1.0, END)
    text_resultado.insert(INSERT, resultado)

def copiar_para_clipboard():
    # Obtém o texto da área de texto e copia para a área de transferência
    texto = text_resultado.get(1.0, END)
    Janela.clipboard_clear()
    Janela.clipboard_append(texto.strip())

def focus_next(event):
    # Move o foco para o próximo widget
    event.widget.tk_focusNext().focus()
    return "break"

# Configuração da janela principal
Janela = Tk()
Janela.title("Script para Serviços")

# Labels e entradas
Label(Janela, text="Nome do Cliente:").grid(column=0, row=0)
entry_nome = Entry(Janela)
entry_nome.grid(column=1, row=0)
entry_nome.bind("<Return>", focus_next)  # Vincula Enter ao foco no próximo widget

Label(Janela, text="Telefone do Cliente:").grid(column=0, row=1)
entry_telefone = Entry(Janela)
entry_telefone.grid(column=1, row=1)
entry_telefone.bind("<Return>", focus_next)  # Vincula Enter ao foco no próximo widget

Label(Janela, text="Ponto de Referência:").grid(column=0, row=2)
entry_ponto_referencia = Entry(Janela)
entry_ponto_referencia.grid(column=1, row=2)
entry_ponto_referencia.bind("<Return>", focus_next)  # Vincula Enter ao foco no próximo widget

Label(Janela, text="Escolha o serviço:").grid(column=0, row=3)
servico_var = StringVar()
servico_var.set("Selecione o serviço")  # Define o texto padrão

# Lista de opções para o menu suspenso
opcoes_servicos = ["Serviço emergencial", "Serviço de protocolo", "Serviço canal errado", "Serviço de reclamação"]

# Criação do menu suspenso
servico_menu = OptionMenu(Janela, servico_var, *opcoes_servicos)
servico_menu.grid(column=1, row=3)

Label(Janela, text="Descrição da Reclamação:").grid(column=0, row=4)
entry_descricao = Entry(Janela)
entry_descricao.grid(column=1, row=4)

Label(Janela, text="Solução Desejada:").grid(column=0, row=5)
entry_remediacao = Entry(Janela)
entry_remediacao.grid(column=1, row=5)

Label(Janela, text="Meio de Resposta:").grid(column=0, row=6)
entry_meio_de_resposta = Entry(Janela)
entry_meio_de_resposta.grid(column=1, row=6)

# Botão para gerar script
botao_gerar_script = Button(Janela, text="Gerar Script", command=gerar_script)
botao_gerar_script.grid(column=0, row=7, columnspan=2)

# Botão para copiar o texto para a área de transferência
botao_copiar = Button(Janela, text="Copiar para Área de Transferência", command=copiar_para_clipboard)
botao_copiar.grid(column=0, row=8, columnspan=2)

# Área de texto para exibir o resultado
text_resultado = Text(Janela, height=10, width=100)
text_resultado.grid(column=0, row=9, columnspan=2)

Janela.mainloop()
