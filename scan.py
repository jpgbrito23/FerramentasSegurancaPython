#Scan de portas em python

import socket



ip = input("Digite o IP/URL: ").strip().lower()

lista_padrão = [21,22,23,80,145,443,]
escolha = input("Deseja utilizar uma lista padrão ou personalizada: ").strip().lower()
if escolha == 'padrão':
    for i in lista_padrão:   
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Abrindo uma coneão IPV4 do tipo TCp
        connection.settimeout(2) # limete de tempo para estabelcer uma coneãro
        resultado = connection.connect_ex((ip,i)) # realizar a conexão na porta e no ip digitados
    
        if resultado == 0:
            print(f"DOOR {i} OPEN")
        
    connection.close()
    
elif escolha == 'personalizada':

    inicio =int(input("Informe a porta inicial que deseja verficar: "))
    final = int(input("Informe a porta final: "))
    
    for i in range(inicio,final+1):
        
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Abrindo uma coneão IPV4 do tipo TCp
        connection.settimeout(2) # limete de tempo para estabelcer uma coneãro
        resultado = connection.connect_ex((ip,i)) # realizar a conexão na porta e no ip digitados
        
        
        if resultado == 0:
            print(f"DOOR {i} OPEN")
    connection.close()
    

else:
    print("ERROR. Escolha uma das opções acima")