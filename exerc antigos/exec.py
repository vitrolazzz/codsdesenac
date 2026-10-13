secreto=7
for i in range(1,4):
    chute = int(input("Chute:"))
    if chute == secreto:
        print("Você acertou")
        break 
    elif chute < secreto:
        print("Tente um numero maior")
    else:
        print("Tente um numero menor")
if chute != secreto:
    print("Fim de jogo, burro!")