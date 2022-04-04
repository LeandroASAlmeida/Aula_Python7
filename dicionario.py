
#listar os itens do dicionario
#print(emails)

#listar todos os nomes
#print(emails['Maria'])

#listar todos os emails
#for email in emails:
#       print(emails[email])
emails = {}

emails['Juca'] = 'juca@gmail.com'
emails['Leandro'] = 'leandroslv@gmail.com'
emails['Maria'] = 'maria@hotmail.com'
emails['codigo'] = 12345
emails[5] = True
emails['lista'] = [1,2,'três',0.5,False]
print(emails)
print(emails['lista'][1])
emails['lista'] = ()
print(emails)

if 'Maria' in emails:
    print('existe')
    emails['Maria'] = 'EmailAtualizado@gmail.com'
else:
    print('não existe')
    emails['Maria'] = 'novoEmail@hotmail.com'

print(emails)

#Excluiu e atualizou email da Maria
try:
    emails.pop('Maria')
except:
    print('Ocorreu algum erro ao tentar excluir o email')