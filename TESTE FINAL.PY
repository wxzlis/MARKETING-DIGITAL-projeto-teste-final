import tkinter as tk

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Clientes")
root.geometry("400x300")
root.configure(bg="#20B2AA") 
 # Define a cor de fundo

# Função para exibir os dados no console
def enviar_dados():
    nome = entry_nome.get()
    email = entry_email.get()
    celular = entry_celular.get()
    interrese_no_servico = entry_interesse_no_servico.get()



    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Celular: {celular}")
    print(f"Interesse:{interrese_no_servico}")

    print("-" * 30)

# Criar e posicionar os rótulos e campos de entrada
tk.Label(root, text="Nome:", bg="pink").pack(anchor="w", padx=10, pady=2)
entry_nome = tk.Entry(root, width=40)
entry_nome.pack(padx=10, pady=2)

tk.Label(root, text="E-mail:", bg="pink").pack(anchor="w", padx=10, pady=2)
entry_email = tk.Entry(root, width=40)
entry_email.pack(padx=10, pady=2)

tk.Label(root, text="Celular:", bg="pink").pack(anchor="w", padx=10, pady=2)
entry_celular = tk.Entry(root, width=40)
entry_celular.pack(padx=10, pady=2)

tk.Label(root, text="Interesse:", bg="pink").pack(anchor="w", padx=10, pady=2)
entry_interrese_no_servico = tk.Entry(root, width=40)
entry_interrese_no_servico.pack(padx=10, pady=2)




# Criar botão de envio
btn_enviar = tk.Button(root, text="Enviar", command=enviar_dados, bg="PINK", fg="GREEN")
btn_enviar.pack(pady=10)

btn_andamento = tk.Button(root, text="EM ANDAMENTO", command=enviar_dados, bg="PINK", fg="GREEN")
btn_andamento.pack(pady=10)


btn_convertido = tk.Button(root, text="CONVERTIDO", command=enviar_dados, bg="PINK", fg="GREEN")
btn_convertido.pack(pady=10)

btn_perdido = tk.Button(root, text="PERDIDO", command=enviar_dados, bg="PINK", fg="GREEN")
btn_perdido.pack(pady=10)



# Iniciar o loop principal
root.mainloop()
