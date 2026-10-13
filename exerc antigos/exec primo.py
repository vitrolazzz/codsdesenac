def localizar_primo(num):
    divisores=[]
    if num >2:
        for contador in range (2,num+1):
            x = num/contador
            if num%contador == 0:
                divisores.append(contador)
            else: 
                contador+=1
    return divisores
            
    
num1 = int(input("Insira uma número de referência:\n"))
divisores = localizar_primo(num1)
if len(divisores)==1:
    print ("Esse número é primo")
else:
    localizar_primo(num1+1)

print(f"{divisores}")