from random import randint



# CHARACTERS
class Pawn(object):
    def __init__(self, MaxHealth, CurrentHealth, armor, attackLow, attackHigh, xp, stun, name):
        self.MaxHealth = MaxHealth
        self.CurrentHealth = CurrentHealth
        self.armor = armor
        self.attackLow = attackLow
        self.attackHigh = attackHigh
        self.stun = False
        self.name = name.upper()
        self.xp = xp

    def basic_attack(self, other):
        if self.stun == True:
            chance = randint(1,10)
            if chance >= 7:
                self.stun = False
                print "%r MANAGES TO STAND UP!"%self.name
            print "%r IS TOO BUSY LYING ON THE GROUND TO ATTACK!" %self.name
        elif self.CurrentHealth <= 0:
            return

        else:
            attack = randint(self.attackLow, self.attackHigh) - other.armor
            other.CurrentHealth -= attack
            print "%s HITS %s FOR %r DAMAGE" %(self.name, other.name, attack)



class Player(Pawn):
    pass







class EnemyBasic(Pawn):
    pass




#THE FIGHT

class Fight(object):
    def __init__(self, Player, Enemy):
        self.Player = Player
        self.Enemy = Enemy
        self.name = name

    def FightStart(self, Player, Enemy):
        global BerserkDuration
        if Enemy.CurrentHealth <= 0:
            Fight.FightWon(self, Player, Enemy)
        else:
            if BerserkDuration >= 0:
                BerserkDuration = BerserkDuration + 1
            if BerserkDuration == 3:
                Player.armor = oldarmor
                Player.attackLow = oldattackLow
                Player.attackHigh = oldattackHigh
                BerserkDuration = -4
                print "YOU CALM YOURSELF AND LEAVE BERSERK MODE"
                raw_input("Press Enter")
            Fight.Fightscreen(self, Player, Enemy)
            Fight.FightPlayerChoice(self, Player, Enemy)
            Enemy.basic_attack(Player)
            Fight.FightStart(self, Player, Enemy)

    def Fightscreen(Fight, Player, Enemy):
        if isinstance(Enemy, EnemyBasic):
            printborder()
            monsterpic = open("Ex45BasicMonster.txt")
            print monsterpic.read()

            printborder()
            print """

                %s's Stats: Health: %d/%d | Armor: %d | %d - %d Attack
                Enemies Stats: Health: %d/%d | Armor: ?? | ?? - ?? Attack

                """ %(name, Player.CurrentHealth,Player.MaxHealth,Player.armor,Player.attackLow,Player.attackHigh, Enemy.CurrentHealth, Enemy.MaxHealth)
            print """

                    1. Attack | 2.Special Move | 3. Item | 4. Run
                """
            printborder()

    def FightPlayerChoice(self, Player, Enemy):
        answer = raw_input("What is your plan?\n>")
        answer.lower()
        if  "1" in answer or "attack" in answer:
            Player.basic_attack(Enemy)
            return

        if "2" in answer or "special" in answer or "move" in answer or "specialmove" in answer:
            Fight.special_move_menu(self, Player, Enemy)
            return

        if "3" in answer or "item"in answer:
            print "This thing would have made more sense if you could actually pick up items. \n Let's just say you used a health potion or something."
            Player.CurrentHealth = Player.CurrentHealth + 20
            if Player.CurrentHealth > Player.MaxHealth:
                Player.CurrentHealth = Player.MaxHealth1

            return



        if "4" in answer or "run" in answer:
            chance = randint(1,10)
            if chance <= 3:
                print "You have failed to run away!"
                raw_input("Press Enter")
                return

            elif chance > 3:
                print "You have managed to run away! But since this is only a simulation, this doesn't really get you much, so let's just stay in the fight."
                raw_input("Press Enter")
                # Normaly I would just call the map Class again, but for this this is just fine
                return
            else:
                print "You have managed to run away! But since this is only a simulation, this doesn't really get you much, so let's just stay in the fight."
                raw_input("Press Enter")
                return
        else:
            Fight.FightPlayerChoice(self, Player, Enemy)


    def special_move_menu(Fight, Player, Enemy):
        printborder()
        print("\n1. Berserk Mode\n2. Throw\n3. Help\n4. Back")
        printborder()
        answer = raw_input("Which move do you want to do?\n>")
        answer.lower()
        if  "1" in answer or "berserk" in answer:
            berserk(Player, Enemy)

        if "2" in answer or "throw" in answer:
            throw(Player, Enemy)

        if "3" in answer or "help"in answer:
            answer = raw_input("What move do you want to know more about?\n>")
            if  "1" in answer or "berserk" in answer:
                print "Berserk Mode: Doubles your attack but removes all of your armor!"
                raw_input("Press Enter")
                Fight.special_move_menu(Player, Enemy)

            if "2" in answer or "throw" in answer:
                print "Throw: 50% chance of stunning your opponent!"
                raw_input("Press Enter")
                Fight.special_move_menu(Player, Enemy)

            if "4" in answer or "back" in answer:
                print "Back: Goes back to the main fight screen!"
                raw_input("Press Enter")
                Fight.special_move_menu(Player, Enemy)
            else:
                Fight.special_move_menu(Player, Enemy)

        if "4" in answer or "back" in answer:
            Fight.FightStart(Player, Enemy)
        else:
            Fight.FightStart(Player, Enemy)

def FightWon(Player, Enemy):
    printborder()
    Player.xp = Player.xp + Enemy.xp
    xpLeft = 100 - Player.xp
    print("You have slain your opponent! You gain %d Experience! %d left for your next level up!")%(Enemy.xp , xpLeft )
    printborder()
    if xpLeft <= 0:
        LevelUp( Player)



def LevelUp(Player):
    print "You have gained a level! Your Health rises from %d to %d! Your attack rises from %d-%d to %d-%d"%(Player.MaxHealth, Player.MaxHealth+10, Player.attackLow, Player.attackHigh, Player.attackLow+10, Player.attackHigh+10)
    Player.MaxHealth = Player.MaxHealth + 10
    Player.attackLow = Player.attackLow + 10
    Player.attackHigh = Player.attackHigh + 10
    Player.CurrentHealth = Player.MaxHealth
    printborder()
    Player.xp = 0





# SPECIAL MOVES, WOULD MAKE MORE SENSE IN THE PLAYER CLASS, BUT I ALREADY GOT THEM HERE AND DONT HAVE THE TIME TO MOVE THEM TO THE PLAYER CLASS
# ALSO IT WORKS, SO YEAH
def berserk(Player):
    global oldarmor, oldattackLow, oldattackHigh, BerserkDuration
    BerserkDuration = 0
    Player.armor = 0
    Player.attackLow = Player.attackLow * 2
    Player.attackHigh = Player.attackHigh * 2
    print "YOU HAVE ENTERED BERSERK MODE"
    return

def throw(Player, Enemy):
    chance = randint(0,10)
    if chance >= 5:
        Enemy.stun = True
        print "You have managed to throw your opponent of their feet!"
        ThrowWorked = True
        return
    else:
        print "Your throw has failed!"
        ThrowWorked = False
        return ThrowWorked









def printborder():
    print "\n########################################################################################################\n"
 # I know I could use #*30 or something similiar, this makes it way more obvious what this function does though and I need those \n


def start():
    printborder()
    print "Welcome to 'Unimaginative Dungeon Crawler 2'! Please enter your name!"
    printborder()
    global name
    name = raw_input("> ")

    print """
Hello %s! Welcome to my little Combat Simulation. Originally, I wanted to create a
full functioning dungeon crawler. However, I only managed to create a working combat system.
The Key features here are the easy to change variables for Pawns (Player or Enemy), the implementation
of a rudementary Level Up system and just generally my first experimenting with object oriented programming :)
    """%name
    raw_input("Press Enter")





#if __name__ == "__main__":
def StartTheGame():
    start()
    player1 = Player(100, 100, 5, 20, 30, 0, False, name) #Player gets an instance so variables get saved
    BerserkDuration = -4 #A value below 0 so the Berserk Mode timer works
    oldarmor = player1.armor #Saved value for Berserk Mode
    oldattackLow = player1.attackLow
    oldattackHigh = player1.attackHigh

# I call this through the engine or something else, but since it was originally planned to have a complete game centered around this, this way works for testing just fine
    basicfight = Fight(player1, EnemyBasic(100, 100, 5, 10, 20, 20, False, "Grunt")) # Can be called again and again for random encounters, since EnemyBasic here isn't a specific instance

    basicfight.FightStart(player1, EnemyBasic(100, 100, 5, 10, 20, 20, False, "Grunt"))




#MOVEMENT SYSTEM







#----------------Testing the Fighting System----------------------
#Player1 = Player(100,100,5,10,20)
#Enemy1 = EnemyBasic(100,100,20,5,5)

#print "%d/%d Health | %d Armor | %d-%d Attack"%(Player1.CurrentHealth,Player1.MaxHealth,Player1.armor,Player1.attackLow,Player1.attackHigh)

#while Enemy1.CurrentHealth > 0:
#    raw_input ("Hit the enemy?")
#    Player1.basic_attack(Enemy1, Player1.attackLow, Player1.attackHigh)
#    print Enemy1.CurrentHealth
