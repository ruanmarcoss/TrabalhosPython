#2
# Mercado Tech ---
# Solicitar Nome do funcionário
# Solicitar idade
# Informar se o funciomnário pode adquirir produtos alcoolicos

#3
# Cadastro Produtos Mercadp Tech
# Solicitar o nome do produto
# Solicitar a categoria do produto (Alcoolicos e Não alcoolicos)
# Exibir o produto cadastrado 

print ('='*50, '\n'*3)


funcionario = input( 'funcionario : ')
idade = int(input ( 'idade : ' ) )

if (idade) <= 17:
    print ('Não pode adquirir produtos alcoolicos')
else:
    print ('Pode adquirir produtos alcoolicos')


print ('='*50, '\n'*9)

produto = input ( 'nome do produto : ' ) 
categoria = input ( 'alcoolico ou não alcoolico : ' )
print(f'produto : {produto} categoria : {categoria}')
 

print ('='*50, '\n'*3)
