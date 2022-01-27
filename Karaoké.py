#Définitions de la classe Player 
class Player:
    def __init__(self,name):
        self.__name = name
        self.__scoreChanson = 0
        self.__scoreMoyen = 0
        self.__scoreTotal = -50
        self.__bestScore = 50
        self.__worstScore = 100

    def getName (self):
        return self.__name

    def getScoreChanson(self,score):
        self.__scoreChanson = score 
        if self.__scoreChanson < 50:
            self.__scoreChanson = 50
        if self.__scoreChanson > 100:
            self.__scoreChanson = 100
        return self.__scoreChanson

    def getScoreMoyen(self,nombreChanson):
        self.__scoreMoyen = self.__scoreTotal / nombreChanson
        return self.__scoreMoyen

    def getScoreTotal(self):
        self.__scoreTotal += self.__scoreChanson
        return self.__scoreTotal

    def getMeilleurScore(self):
        if (self.__scoreChanson > self.__bestScore):
            self.__bestScore = self.__scoreChanson
        return self.__bestScore

    def getPireScore(self):
        if (self.__scoreChanson < self.__worstScore):
            self.__worstScore = self.__scoreChanson
        return self.__worstScore 


#Définition de la classe Karaoké

class Karaoke:
    def __init__(self,nombreJoueur,numeroChanson,nombreChanson,meilleurScoreChanson):
        self.__nombreJoueur = nombreJoueur
        self.__numeroChanson = numeroChanson
        self.__nombreChanson = nombreChanson
        self.__meilleurScoreChanson = meilleurScoreChanson

    def getNumeroChanson (self):
        return self.__numeroChanson

    def getNombreJoueur (self):
        return self.__nombreJoueur

    def getNombreChanson (self):
        return self.__nombreChanson

    def getMeilleurScoreChansons(self,scoreChanson):
        if scoreChanson > self.__meilleurScoreChanson:
            self.__meilleurScoreChanson = scoreChanson
        return self.__meilleurScoreChanson


#Début Programme 

jeu = Karaoke(int(input("Combien de joueurs ?")),1,5,0)
nameRequested = jeu.getNombreJoueur() #Pas possible au dessus de 2

#while (nameRequested > 0): (pas fonctionnel)
    #newPlayer = Player(str(input("Entrez un nom de joueur ?")))
    

#Définition des variables
if (nameRequested == 1):
    joueur1 = Player(str(input("Quel est le nom du joueur 1 ?")))

elif (nameRequested == 2):
    joueur1 = Player(str(input("Quel est le nom du joueur 1 ?")))
    joueur2 = Player(str(input("Quel est le nom du joueur 2 ?")))


nombreChanson = 5



chanson1 = "Bohemian Rhapsody"
bestPlayerChanson1 = ""
chanson2 = "Sunday Bloody Sunday"
bestPlayerChanson2 = ""
chanson3 = "Never Gonna Give You Up"
bestPlayerChanson3 = ""
chanson4 = "Walking on Sunshine"
bestPlayerChanson4 = ""
chanson5 = "La Danse des Canards"
bestPlayerChanson5 = ""


#Scores du Joueur 1

print("Quels furent les scores de", joueur1.getName(), " ? \n")

scoreChanson1 = int(input("Pour Bohemian Rhapsody ? \n"))

joueur1.getScoreChanson(scoreChanson1)
joueur1.getScoreTotal()
joueur1.getMeilleurScore()
joueur1.getPireScore()

scoreChanson2 = int(input("Pour Sunday Bloody Sunday ? \n"))

joueur1.getScoreChanson(scoreChanson2)
joueur1.getScoreTotal()
joueur1.getMeilleurScore()
joueur1.getPireScore()

scoreChanson3 = int(input("Pour Never Gonna Give You Up ? \n"))

joueur1.getScoreChanson(scoreChanson3)
joueur1.getScoreTotal()
joueur1.getMeilleurScore()
joueur1.getPireScore()

scoreChanson4 = int(input("Pour Walking on Sunshine ? \n"))

joueur1.getScoreChanson(scoreChanson4)
joueur1.getScoreTotal()
joueur1.getMeilleurScore()
joueur1.getPireScore()

scoreChanson5 = int(input("Pour La Danse des Canards ? \n"))

joueur1.getScoreChanson(scoreChanson5)
joueur1.getScoreTotal()
joueur1.getMeilleurScore()
joueur1.getPireScore()

print ("Le score total de ", joueur1.getName(), " est ", joueur1.getScoreTotal())
print ("Le meilleur score de ", joueur1.getName(), " est", joueur1.getMeilleurScore())
print ("Le pire score de ", joueur1.getName(), " est ",joueur1.getPireScore())
print ("Sa moyenne est de",joueur1.getScoreMoyen(5))

#Scores du joueur 2

if (nameRequested >= 2):

    print("Quels furent les scores de", joueur2.getName(), " ? \n")

    scoreChanson1 = int(input("Pour Bohemian Rhapsody ? \n"))

    joueur2.getScoreChanson(scoreChanson1)
    joueur2.getScoreTotal()
    joueur2.getMeilleurScore()
    joueur2.getPireScore()

    scoreChanson2 = int(input("Pour Sunday Bloody Sunday ? \n"))

    joueur2.getScoreChanson(scoreChanson2)
    joueur2.getScoreTotal()
    joueur2.getMeilleurScore()
    joueur2.getPireScore()

    scoreChanson3 = int(input("Pour Never Gonna Give You Up ? \n"))

    joueur2.getScoreChanson(scoreChanson3)
    joueur2.getScoreTotal()
    joueur2.getMeilleurScore()
    joueur2.getPireScore()

    scoreChanson4 = int(input("Pour Walking on Sunshine ? \n"))

    joueur2.getScoreChanson(scoreChanson4)
    joueur2.getScoreTotal()
    joueur2.getMeilleurScore()
    joueur2.getPireScore()

    scoreChanson5 = int(input("Pour La Danse des Canards ? \n"))

    joueur2.getScoreChanson(scoreChanson5)
    joueur2.getScoreTotal()
    joueur2.getMeilleurScore()
    joueur2.getPireScore()

    print ("Le score total de ", joueur2.getName(), " est ", joueur2.getScoreTotal())
    print ("Le meilleur score de ", joueur2.getName(), " est", joueur2.getMeilleurScore())
    print ("Le pire score de ", joueur2.getName(), " est ",joueur2.getPireScore())
    print ("Sa moyenne est de",joueur2.getScoreMoyen(5))



#Résultat

if (jeu.getNombreJoueur() > 1):
    if(joueur1.getScoreTotal() > joueur2.getScoreTotal()):
        print(joueur1.getName(), "a gagné avec", joueur1.getScoreTotal(), " !")

    elif():
        print(joueur2.getName(), "a gagné avec", joueur2.getScoreTotal(), " !")

    else:
        print("Les 2 joueurs sont à égalité !")

