#sistema de login
usuario_correto = "Murilloadm"
senha_correta = "2510"

#numeros de tentativas de login
tentativas = 3

while tentativas >= 0:
  usuario = input ("digite o usuario")
  senha = input ("digite a senha")

  if usuario == usuario_correto and senha == senha_correta:
    print(f"Seja bem vindo {usuario_correto}!")

    print("Seja bem-vindo(a) a loja virtual!!!")

    print("""
==============================
        LOJA VIRTUAL
==============================

1 - Ver produtos
2 - Comprar produto
3 - Ver carrinho
4 - Remover produto

0 - Sair
""")

    while True:
     
    #selecionar produtos
      opcao = input("Escolha uma opção: ")
    
      if opcao == "1":
        print("Camisa-40$, short-30$, tenis-60$, chinelo-15$")
    
      elif opcao == "2":
        print("""
      
        !!Compra bem sucedida!!""")

      elif opcao == "3":
        print("Parece que o carrinho ainda esta vazio :(...")

      elif opcao == "4":
       print("Produto removido!")

      elif opcao == "0":
        print("Volte sempre!")
        break
    break 
  else: 
      tentativas -= 1
      print(f"usuario ou senha incorretos. Tentativas restantes {tentativas}")

  if tentativas == 0:
        print("limite atingido! tente novamente mais tarde.")
        break
