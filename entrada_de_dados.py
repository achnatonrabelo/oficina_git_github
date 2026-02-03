# Entrada de dados: programa solicita dados do usuário
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

# Processamento de dados: Formatação da mensagem que será exibida
saida_01 = f"Seu nome é {nome} e você tem {idade} anos de idade"
saida_02 = "Seu nome é " + nome + " e você tem " + idade + " anos de idade"

# Saída de dados
print(saida_01)
print(saida_02)