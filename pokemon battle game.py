# Create a simple text-based pokemon battle game between two players. 
# Each player has health points (HP), and on each turn, they can attack, defend, or heal.

def pokemon(poke1, poke2):
    lst1 = [".", ".", ".", ".", "."]
    lst2 = [".", ".", ".", ".", "."]

    print(poke1 + " and " + poke2 + " have entered the battle arena!\n")
    
    while len(lst1) > 0 and len(lst2) > 0:  

        # Charmander vs Squirtle

        if poke1 == "charmender" and poke2 == "squirtle":        
            attack1 = input("Player 1 (" + poke1 + "), choose your attack: ")
            if attack1 in ["fire spin", "ember", "flame thrower", "scratch"]:
                lst2.pop()
                print("Player 1 hit! " + poke2 + "'s life: " + str(lst2))
                
            attack2 = input("Player 2 (" + poke2 + "), choose your attack: ")
            if attack2 in ["water gun", "bubble beam", "hydro pump"]:
                print("It's super effective!")
                if len(lst1) == 1:
                    lst1.pop()
                else:
                    del lst1[-2:]
                print(poke1 + "'s life: " + str(lst1))
            elif attack2 == "headbutt":
                lst1.pop()
                print(poke1 + "'s life: " + str(lst1))
            
            if len(lst1) == 0:
                print("Game over! " + poke1 + " has fainted. Player 2 wins!")
                break
            elif len(lst2) == 0:
                print("Game over! " + poke2 + " has fainted. Player 1 wins!")
                break

        # Squirtle vs Charmander

        elif poke1 == "squirtle" and poke2 == "charmender":
            attack1 = input("Player 1 (" + poke1 + "), choose your attack: ")
            if attack1 in ["water gun", "bubble beam", "hydro pump"]:
                print("It's super effective!")
                if len(lst2) == 1:
                    lst2.pop()
                else:
                    del lst2[-2:]
                print(poke2 + "'s life: " + str(lst2))
            elif attack1 == "headbutt":
                lst2.pop()
                print(poke2 + "'s life: " + str(lst2))                
            attack2 = input("Player 2 (" + poke2 + "), choose your attack: ")
            if attack2 in ["fire spin", "ember", "flame thrower", "scratch"]:
                lst1.pop()
                print(poke1 + "'s life: " + str(lst1))

            if len(lst1) == 0:
                print("Game over! " + poke1 + " has fainted. Player 2 wins!")
                break
            elif len(lst2) == 0:
                print("Game over! " + poke2 + " has fainted. Player 1 wins!")
                break

        # Charmander vs Bulbasaur

        elif poke1 == "charmender" and poke2 == "bulbasaur":
            attack1 = input("Player 1 (" + poke1 + "), choose your attack: ")
            if attack1 in ["fire spin", "ember", "flame thrower"]:
                print("It's super effective!")
                if len(lst2) == 1:
                    lst2.pop()
                else:
                    del lst2[-2:]
                print(poke2 + "'s life: " + str(lst2))
            elif attack1 == "scratch":
                lst2.pop()
                print(poke2 + "'s life: " + str(lst2))                
            attack2 = input("Player 2 (" + poke2 + "), choose your attack: ")
            if attack2 in ["energy ball", "razor leaf", "bullet seed"]:
                lst1.pop()
                print(poke1 + "'s life: " + str(lst1))
            elif attack2 == "heal":
                if len(lst2) < 5:               # Only heal if Bulbasaur's life is not full
                    lst2.append(".")
                    print(poke2 + " healed! Life: " + str(lst2))
                else:
                    print(poke2 + "'s life is full, heal failed.")
                
            if len(lst1) == 0:
                print("Game over! " + poke1 + " has fainted. Player 2 wins!")
                break
            elif len(lst2) == 0:
                print("Game over! " + poke2 + " has fainted. Player 1 wins!")
                break
            
        # Bulbasaur vs Charmander

        elif poke1 == "bulbasaur" and poke2 == "charmender":
            attack1 = input("Player 1 (" + poke1 + "), choose your attack: ")
            if attack1 in ["energy ball", "razor leaf", "bullet seed"]:
                lst2.pop()
                print(poke2 + "'s life: " + str(lst2))
            elif attack1 == "heal":
                if len(lst1) < 5:
                    lst1.append(".")
                    print(poke1 + " healed! Life: " + str(lst1))
                else:
                    print(poke1 + "'s life is full, heal failed.")                
            attack2 = input("Player 2 (" + poke2 + "), choose your attack: ")
            if attack2 in ["fire spin", "ember", "flame thrower", "scratch"]:
                print("It's super effective!")
                if len(lst1) == 1:
                    lst1.pop()
                else:
                    del lst1[-2:]
                print(poke1 + "'s life: " + str(lst1))
            elif attack2 == "scratch":
                lst1.pop()
                print(poke1 + "'s life: " + str(lst1))
            
            if len(lst1) == 0:
                print("Game over! " + poke1 + " has fainted. Player 2 wins!")
                break
            elif len(lst2) == 0:
                print("Game over! " + poke2 + " has fainted. Player 1 wins!")
                break

        # Squirtle vs Bulbasaur

        elif poke1 == "squirtle" and poke2 == "bulbasaur":
            attack1 = input("Player 1 (" + poke1 + "), choose your attack: ")
            if attack1 in ["water gun", "bubble beam", "hydro pump", "headbutt"]:
                lst2.pop()
                print(poke2 + "'s life: " + str(lst2))                
            attack2 = input("Player 2 (" + poke2 + "), choose your attack: ")
            if attack2 in ["razor leaf", "bullet seed"]:
                lst1.pop()
                print(poke1 + "'s life: " + str(lst1))
            elif attack2 == "heal":
                if len(lst2) < 5:
                    lst2.append(".")
                    print(poke2 + " healed! Life: " + str(lst2))
                else:
                    print(poke2 + "'s life is full, heal failed.".format(poke2))
            elif attack2 == "energy ball":
                print("It's super effective!")
                if len(lst1) == 1:
                    lst1.pop()
                else:
                    del lst1[-2:]
                print(poke1 + "'s life: " + str(lst1))

            if len(lst1) == 0:
                print("Game over! " + poke1 + " has fainted. Player 2 wins!")
                break
            elif len(lst2) == 0:
                print("Game over! " + poke2 + " has fainted. Player 1 wins!")
                break
        
        # Bulbasaur vs Squirtle

        elif poke1 == "bulbasaur" and poke2 == "squirtle":
            attack1 = input("Player 1 (" + poke1 + "), choose your attack: ")
            if attack1 in ["razor leaf", "bullet seed"]:
                lst2.pop()
                print(poke2 + "'s life: " + str(lst2))
            elif attack1 == "heal":
                if len(lst1) < 5:
                    lst1.append(".")
                    print(poke1 + " healed! Life: " + str(lst1))
                else:
                    print(poke1 + "'s life is full, heal failed.".format(poke1))
            elif attack1 == "energy ball":
                print("It's super effective!")
                if len(lst2) == 1:
                    lst2.pop()
                else:
                    del lst2[-2:]
                print(poke2 + "'s life: " + str(lst2))                
            attack2 = input("Player 2 (" + poke2 + "), choose your attack: ")
            if attack2 in ["water gun", "bubble beam", "hydro pump", "headbutt"]:
                lst1.pop()
                print(poke1 + "'s life: " + str(lst1))

            if len(lst1) == 0:
                print("Game over! " + poke1 + " has fainted. Player 2 wins!")
                break
            elif len(lst2) == 0:
                print("Game over! " + poke2 + " has fainted. Player 1 wins!")
                break
                
        # Game over check

        

pokemons = ["charmender", "bulbasaur", "squirtle"]
print("Available pokemons are " + str(pokemons))

print('charmender_attacks=\nfire spin\nscratch\nember\nflame thrower\n')
print('squirtle_attacks=\nwater gun\nbubble beam\nhydro pump\nheadbutt\n')
print('bulbasaur_attacks=\nenergy ball\nrazor leaf\nheal\nbullet seed\n')

poke1 = input("Player 1, choose your pokemon: ").lower()
poke2 = input("Player 2, choose your pokemon: ").lower()

pokemon(poke1, poke2)



