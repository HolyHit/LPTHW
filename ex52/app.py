#Problems I noticed, but couldn't work better with due to false organising of my time:
#1.) No special features like Login/Passwords
#2.) No Saving
#3.) Way too many global variables. Working with variables from my own imported game didn't work the way I expected it to.
#4.) My Old game was way too unmodular to be used easily. Had to change a few codes (Mainly delete the raw_inputs), but a good learning progress I guess.
#5.) Not sure about the readability of the code. I think it is readable and relatively easily understandable, but I wrote it so not sure. Especially with the amounts of If, Try/Except and Global Variables
#6.) No Fancy Graphics TT I had not enough experience with HTML or especially CSS to really make good use of it in the time I set myself. No Sound either.

#Overall, this is pretty much what I imagine a working, but not perfectly executed port of a game would look like way simplified. But it works, I used and learned quite a bit about the Flash Plugin on my own as well as
# got a lot of experience with modularity of code, writing it correctly and what NOT to do to make code modular and easily understandable afterwards.



from flask import Flask, render_template, request, session
from flask import redirect, url_for
import Ex45

app = Flask(__name__)


#@app.route('/<user>')
#def index(user):
#    return render_template('form.html', name = user)






@app.route('/', methods=['POST'])

def GiveName():
 #UserName(UN) is being used often enouhg to warrant making it a global variable
    #First asking for the name
    if request.form["Playername"]:
        global UN
        UN = request.form.get('username')
        if UN is None or UN == "":
            UN = 'Nobody'
        global player1
        player1 = Ex45.Player(100, 100, 5, 20, 30, 0, False, UN)
        print('Player 1 set!')

        return redirect(url_for('start'))



@app.route('/', methods=['GET'])

def FirstVisit():
    return render_template('FirstVisit.html')


@app.route('/start', methods=['GET'])
def start():
    try :
        UN
        return render_template('Start.html', username = UN)
    except:
        return redirect(url_for('FirstVisit'))


@app.route('/start', methods=['POST'])
def startPost():
    if request.form["A"] == "Do you want to fight?":
        return redirect(url_for('fightstart'))

    else:
        return redirect(url_for('FirstVisit'))
# CHECK FOR VARIABLE CHECK PLS

@app.route('/fightstart', methods=['GET'])
def fightstart():
    try:
        global UN, player1, enemy1, BerserkDuration
        BerserkDuration = -6 #Some number < 0 so BerserkDuration is set and works
        player1.CurrentHealth = player1.MaxHealth
        enemy1 = Ex45.EnemyBasic(100, 100, 5, 20, 30, 50, False, 'Grunt')
        PlayerDescription = "Your current stats: Health: %d/%d | Armor: %d | %d - %d Attack |  CurrentXP: %d/100"%(player1.CurrentHealth,player1.MaxHealth,player1.armor,player1.attackLow,player1.attackHigh, player1.xp)
        EnemyDescription  = "Your opponents stats: Health: %d/%d | Armor: ?? | ?? - ?? Attack"%(enemy1.CurrentHealth, enemy1.MaxHealth)

        return render_template('fight.html', PD = PlayerDescription, ED = EnemyDescription)

    except:
        return redirect(url_for('FirstVisit'))

@app.route('/fight', methods=['POST'])
def fightdescision():
    global Message, BerserkDuration
    if request.form["A"] == "Basic Attack":
        player1.basic_attack(enemy1)
        enemy1.basic_attack(player1)
        Message = "You attacked your opponent! He attacks back!"
        return redirect(url_for('fight'))

    elif request.form["A"] == "Health Potion":

        player1.CurrentHealth = player1.CurrentHealth + 25
        if player1.CurrentHealth > player1.MaxHealth:
            player1.CurrentHealth = player1.MaxHealth
        enemy1.basic_attack(player1)
        Message = "You used a Health Potion! Your opponent still attacks you!"
        return redirect(url_for('fight'))

    elif request.form["A"] == "Flee":
        Message = "You don't flee in a combat simulator!"
        print(Message)
        enemy1.basic_attack(player1)
        return redirect(url_for('fight'))

    elif request.form["Item_1"] == "Berserk":
        if BerserkDuration <= 0:

            print "Berserk mode activated"
            Message = "Berserk mode activated! Double the Damage, but no Armor for 4 rounds. Your opponent attacks you!"
            global oldArmor, oldattackLow, oldattackHigh
            oldArmor = player1.armor
            oldattackLow = player1.attackLow
            oldattackHigh = player1.attackHigh
            BerserkDuration = 4
            Ex45.berserk(player1)
        else:
            print "Already did that."
            Message = "You're already Berserking around. Round wasted!"
        enemy1.basic_attack(player1)
        print ("YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO") #Testing to see why the next move doesn't work (EDIT: It now works)
        return redirect(url_for('fight'))

    elif request.form["Item_1"] == "Throw":
        print "Threw that opponent"
        Ex45.throw(player1, enemy1)
        if enemy1.stun == True:
            Message = "You try to throw your opponent! It worked!"
        elif enemy1.stun == False:
            Message = "You try to throw your opponent! It failed!"
        enemy1.basic_attack(player1)
        return redirect(url_for('fight'))

    else:
        enemy1.basic_attack(player1)
        return redirect(url_for('fight'))


@app.route('/fight', methods=['GET'])
def fight():
    global player1, enemy1, Message, BerserkDuration, oldArmor, oldattackLow, oldattackHigh
    try:
        try:
            BerserkDuration = BerserkDuration - 1
            print BerserkDuration
            if BerserkDuration <= 0:
                player1.armor = oldArmor
                player1.attackLow = oldattackLow
                player1.attackHigh = oldattackHigh
                PlayerDescription = "Your current stats: Health: %d/%d | Armor: %d | %d - %d Attack | CurrentXP: %d/100"%(player1.CurrentHealth,player1.MaxHealth,player1.armor,player1.attackLow,player1.attackHigh,player1.xp)
                EnemyDescription  = "Your opponents stats: Health: %d/%d | Armor: ?? | ?? - ?? Attack"%(enemy1.CurrentHealth, enemy1.MaxHealth)
                if player1.CurrentHealth > 0 and enemy1.CurrentHealth > 0:
                    return render_template('fight.html', PD = PlayerDescription, ED = EnemyDescription, ME = Message)

                elif player1.CurrentHealth > 0 and enemy1.CurrentHealth <= 0:
                    Ex45.FightWon(player1, enemy1)
                    return render_template('Win.html')

                elif player1.CurrentHealth <= 0 and enemy1.CurrentHealth > 0:
                    return render_template('Loss.html')

                elif player1.CurrentHealth <= 0 and enemy1.CurrentHealth <= 0:
                    return render_template('Draw.html')

                else:
                    return redirect(url_for('FirstVisit'))

            else:
                PlayerDescription = "Your current stats: Health: %d/%d | Armor: %d | %d - %d Attack | CurrentXP: %d/100"%(player1.CurrentHealth,player1.MaxHealth,player1.armor,player1.attackLow,player1.attackHigh,player1.xp)
                EnemyDescription  = "Your opponents stats: Health: %d/%d | Armor: ?? | ?? - ?? Attack"%(enemy1.CurrentHealth, enemy1.MaxHealth)
                if player1.CurrentHealth > 0 and enemy1.CurrentHealth > 0:
                    return render_template('fight.html', PD = PlayerDescription, ED = EnemyDescription, ME = Message)
                elif player1.CurrentHealth > 0 and enemy1.CurrentHealth <= 0:
                    Ex45.FightWon(player1, enemy1)
                    return render_template('Win.html')

                elif player1.CurrentHealth <= 0 and enemy1.CurrentHealth > 0:
                    return render_template('Loss.html')

                elif player1.CurrentHealth <= 0 and enemy1.CurrentHealth <= 0:
                    return render_template('Draw.html')
                else:
                    return redirect(url_for('FirstVisit'))


        except:
            PlayerDescription = "Your current stats: Health: %d/%d | Armor: %d | %d - %d Attack | CurrentXP: %d/100"%(player1.CurrentHealth,player1.MaxHealth,player1.armor,player1.attackLow,player1.attackHigh,player1.xp)
            EnemyDescription  = "Your opponents stats: Health: %d/%d | Armor: ?? | ?? - ?? Attack"%(enemy1.CurrentHealth, enemy1.MaxHealth)
            if player1.CurrentHealth > 0 and enemy1.CurrentHealth > 0:
                return render_template('fight.html', PD = PlayerDescription, ED = EnemyDescription, ME = Message)

            elif player1.CurrentHealth > 0 and enemy1.CurrentHealth <= 0:
                Ex45.FightWon(player1, enemy1)
                return render_template('Win.html')

            elif player1.CurrentHealth <= 0 and enemy1.CurrentHealth > 0:
                return render_template('Loss.html')

            elif player1.CurrentHealth <= 0 and enemy1.CurrentHealth <= 0:
                return render_template('Draw.html')
            else:
                return redirect(url_for('FirstVisit'))
    except:
        return redirect(url_for('FirstVisit'))





if __name__ == "__main__":
    app.run()
