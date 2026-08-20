#sistema de login
usuario_correto = "Murilloadm"
senha_correta = "2510"

#numeros de tentativas de login
tentativas = 3

while tentativas >= 0:
  usuario = input ("digite o usuario")
  senha = input ("digite a senha")
#verificação de usuario
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

    produtos = [ "camisa", "short", "tenis", "chinelo"]
    precos = [ 30, 20, 50, 15]
    
    carrinho = []
    while True:
     
    #selecionar produtos
      opcao = input("Escolha uma opção: ")
    
      if opcao == "1":
        for indice, produto in enumerate(produtos):
          print(f"{indice +1} - {produto} - R${precos[indice]}")
    
      elif opcao == "2":
       
        comprar = int(input("Escolha o numero do produto: "))

        if comprar <=0 or comprar >len(produtos):
          print("Opção invalida")
        
        else:
          indice2 = comprar -1
          produtos[indice2]
          produto_escolhido = produtos[indice2]
          preco_escolhido = precos[indice2]
          print(f"Você escolheu: {produto_escolhido} - R${preco_escolhido}")
        
          carrinho.append([produto_escolhido, preco_escolhido])
          print(f"{produto_escolhido} adicionado ao carrinho")

      elif opcao == "3":
       
        if len(carrinho) == 0:
          print("O carrinho está vazio.")
        else:  
          total = 0
          for indice, produto in enumerate(carrinho):

            print(f"{indice +1} - {produto[0]} - R${produto[1]}")
            
            total = total + produto[1]

          print(f"Preço total do carrinho: R${total}")
                  
      elif opcao == "4":
        if len(carrinho) == 0 :
          print("Não à produtos para remover")
      
        else:
          remover = int(input("Escolha uma opçao para remover:"))

          if remover < 1 or remover > len(carrinho) :
            print("Esse produto não existe / opção não existe")

          else:
            indice_remover = remover - 1
        
            produto_removido = carrinho[indice_remover]
            del carrinho[indice_remover]

            print(f"{produto_removido[0]} removido com sucesso!")
            
      elif opcao == "5":
        if len(carrinho) == 0:
          print("carrinho vazio")
        
        else:
          confirmar = input("deseja finalizar a compra (s/n)?")

          if confirmar =="s":
            print("Compra realizada com sucesso!")
            carrinho.clear()

          else:
            print("Compra cancelada")
      
      
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