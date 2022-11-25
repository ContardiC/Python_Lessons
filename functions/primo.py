def primo(num):
    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

while True:
    num=int(input("Inserisci un numero positivo intero "))
    if num > 0:
        break
if primo(num) == 1:
    print("il numero inserito è primo")
else:
    print("Il numero inserito non è primo")
