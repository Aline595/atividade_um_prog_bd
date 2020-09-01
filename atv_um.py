######AULA DIA 24/08 ###############

from collections import Counter
from collections import defaultdict

#Definir lista: coleção de itens mutaveis
users = [
  # Dicionario(pares de chave e valor)
  {"id": 0, "name": "Hero"},
  {"id": 1, "name": "Dunn"},
  {"id": 2, "name": "Sue"},
  {"id": 3, "name": "Chi"},
  {"id": 4, "name": "Thor"},
  {"id": 5, "name": "Clive"},
  {"id": 6, "name": "Hick"},
  {"id": 7, "name": "Devin"},
  {"id": 8, "name": "Kate"},
  {"id": 9, "name": "Klein"},
]

friendships = [
  #Tupla: Coleção de itens imutavel
  (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5),
  (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

for user in users:
  user["friends"] = []


#for t in friendships:
  #print(t) -> Mostra tudo
  #Desenpacotar o pacote/ vai mostar o 0 e depois o 1
  #print(t[0])
  #print(t[1])

#Desenpacotar automatico
for i, j in friendships:
  #print(i)
  #print(j)
  users[i]["friends"].append(users[j])
  users[j]["friends"].append(users[i])

#print(users)
def number_of_friends (user):
  return len(user["friends"])

#print (number_of_friends(users[0]))

######### ATIVIDADE UM #################
"""
1-Adicione os atributos sexo e idade aos usuários da rede.
"""
def adicionar_sexo_e_idade(user, sexo, idade):
  user["sexo"] = sexo
  user["idade"] = idade
  return user

#print(adicionar_sexo_e_idade(users[3], "masculino", 20))

for user in users:
  if user["id"] < 5:
    user["sexo"] = "feminino"
    user["idade"] = 20
  else:
    user["sexo"] = "masculino"   
    user["idade"] = 40

#print(users)
"""
2- Monte um dicionário que tem como chave o id do usuário e 
como valor uma tupla. O primeiro elemento da tupla deve ter a 
quantidade de amigos do sexo masculino e o segundo elemento 
da tupla deve ter a quantidade de amigos do sexo feminino. 
Escreva funções conforme achar apropriado
"""
def contar_amigos_feminino(user):
  num = 0
  for user["friends"] in user:
    if(user["sexo"] == "feminino"):
      num += 1
  return num
  """
  return len(user["friends": "feminino"])
  """

#print(contar_amigos_feminino(users[0]))

def contar_amigos_masculino(user):
  num = 0
  for user["friends"] in user:
    if(user["sexo"] == "masculino"):
      num += 1
  return num

print(contar_amigos_masculino(users[0]))

for user in users:
  user["sexo_amigos"] = {}

def adicionar_tupla_amigos(user):
  return user["sexo_amigos"] = { "masculino": contar_amigos_masculino(user)  "feminino":contar_amigos_feminino(user) }
  
print(adicionar_tupla_amigos(users[0]))
