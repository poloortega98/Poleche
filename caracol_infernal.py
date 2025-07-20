print("Bienvenido al programa de seguridad de WCs")
from warnings import simplefilter
es_caracol=input("¿Eres un caracol infernal?")
while es_caracol=="si":
  print("¡Fuera de aqui caracol infernal!")
  es_caracol=input("¿Eres un caracol infernal?")
print("Genial! Es una pregunta extraña pero tenemos que asegurarnos que no entre un caracol infernal a este WC")


prohibited_act_list = ["destruir un WC", "escuchar rock","comer vegetales"]

act = input("¿Qué actividad vas a realizar? ")
while act in prohibited_act_list:
    print("¡Fuera de aquí, caracol infernal!")
    act = input("¿Qué actividad vas a realizar? ")

print("Pase usted :) ¡Espero todo salga bien!")