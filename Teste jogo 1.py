Nome = input("Olá! Digite seu nome: ")
import time 
while True:
    Classe = input("Qual classe você deseja entre Mago, Guerreiro e Arqueiro? ")
    if Classe == "Mago": 
       print("Você escolheu jogar como Mago.")
       break
    elif Classe == "Guerreiro":
       print("Você escolheu jogar como Guerreiro.")
       break
    elif Classe == "Arqueiro":
       print("Você escolheu jogar como Arqueiro.")
       break
    else:
        print("Você precisa escolher entre estas classes.")
if Classe == "Guerreiro":
    arma = "espada"
elif Classe == "Arqueiro":
    arma = "arco"
elif Classe == "Mago":
    arma = "cajado ou magia"
else:
    arma = "desconhecida"
print("Com bravura, a jornada épica começa: desafios aguardam, destinos se entrelaçam, heróis se erguem triunfantes...")
time.sleep(1) 
print("Voce ve essas frase no panfleto de um jogo de rpg que por algum motivo, estava em seu bolso")
time.sleep(1)
print("...")
time.sleep(1)
print("...Someone or something approachs  you, some branches break at 2 or 3 meters high")
time.sleep(1)
print("...Its a fucking Orc!!He`s shaking your bloodstained club. ")
time.sleep(1)
print("He turns his attention to the little thing lying on the floor.It seems its you.")
while True:
    ato1=input("Whats is your move? Attack, To Talk, Run. ")
    if ato1=="Attack":
         print("You choosed attack")
         print("You take your",arma,"and hit the orc with the most strong attack you can do")
         time.sleep(1)
         print("Well, he looks more angry than before")
         time.sleep(1)
         print("He goes in your direction and hits you with your club")
         time.sleep(1)
         print("Now we know why him club was stained in blood, well, at least was not your blood. ")
         time.sleep(1)
         print("YOU DIED")
         break
    elif ato1=="Dialogar":
         print("You choosed talk to him")
         break
    elif ato1=="Fugir":
        print("You choosed Run from him")
        break
    else:
        print("Man, you need to do something, do you wanna f#cking die?")
        
        
     


