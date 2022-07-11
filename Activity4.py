# Bruno, Jared Ivan D.
# Hilario, Cyrille Jaye N.

import csv

class Character:
    def __init__(self, characterClass, weapon, ability1, ability2):
        self.characterClass = characterClass
        self.weapon = weapon
        self.ability1 = ability1
        self.ability2 = ability2

    def SetClass(self):
        while True:
            print("Select a Class:")
            print("\t[1] Wizard")
            print("\t[2] Knight")
            print("\t[3] Archer")
            print("\t[4] Assassin\n")
            choice = int(input("Select: "))
            
            if choice in (1, 2, 3, 4):
                if choice == 1:
                    self.characterClass = "Wizard"
                    print("You selected Wizard")
                elif choice == 2:
                    self.characterClass = "Knight"
                    print("You selected Knight")
                elif choice == 3:
                    self.characterClass = "Archer"
                    print("You selected Archer")
                elif choice == 4:
                    self.characterClass = "Assassin"
                    print("You selected Assassin")
                break
            else:
                print("Invalid Input")
                continue
    
    def SetWeapon(self):
        while True:
            print("\nSelect a Weapon:")
            print("\t[1] Wizard Staff")
            print("\t[2] Sword")
            print("\t[3] Bow & Arrow")
            print("\t[4] Katar\n")
            choice = int(input("Select: "))
            
            if choice in (1, 2, 3, 4):
                if choice == 1:
                    self.weapon = "Wizard Staff"
                    print("You selected Wizard Staff")
                elif choice == 2:
                    self.weapon = "Sword"
                    print("You selected Sword")
                elif choice == 3:
                    self.weapon = "Bow & Arrow"
                    print("You selected Bow & Arrow")
                elif choice == 4:
                    self.weapon = "Katar"
                    print("You selected Katar")
                break
            else:
                print("Invalid Input")
                continue
    
    def SetAbility(self):
        i = 0
        while i < 2:
            if(self.characterClass == "Wizard"):
                if i == 0:
                    print("\nSelect Ability 1:")
                if i == 1:
                    print("\nSelect Ability 2:")
                print("\t[1] Energy Ball")
                print("\t[2] Dragons Breath")
                print("\t[3] Crown of Flame")
                print("\t[4] Hail Storm\n")
                choice = int(input("Select: "))
                
                if choice in (1, 2, 3, 4):
                    if choice == 1:
                        if i == 0:
                            self.ability1 = "Energy Ball"
                        if i == 1:
                            self.ability2 = "Energy Ball"
                        print("You selected Energy Ball")
                    elif choice == 2:
                        if i == 0:
                            self.ability1 = "Dragons Breath"
                        if i == 1:
                            self.ability2 = "Dragons Breath"
                        print("You selected Dragons Breath")
                    elif choice == 3:
                        if i == 0:
                            self.ability1 = "Crown of Flame"
                        if i == 1:
                            self.ability2 = "Crown of Flame"
                        print("You selected Crown of Flame")
                    elif choice == 4:
                        if i == 0:
                            self.ability1 = "Hail Storm"
                        if i == 1:
                            self.ability2 = "Hail Storm"
                        print("You selected Hail Storm")

                    if self.ability1 == self.ability2:
                        print("Ability already chosen")
                        continue

                    i += 1
                else:
                    print("Invalid Input")
                    continue
            
            if(self.characterClass == "Knight"):
                if i == 0:
                    print("\nSelect Ability 1:")
                if i == 1:
                    print("\nSelect Ability 2:")
                print("\t[1] Fire Slash")
                print("\t[2] Power Slash")
                print("\t[3] Gigantic Storm")
                print("\t[4] Chaotic Disaster\n")
                choice = int(input("Select: "))
                
                if choice in (1, 2, 3, 4):
                    if choice == 1:
                        if i == 0:
                            self.ability1 = "Fire Slash"
                        if i == 1:
                            self.ability2 = "Fire Slash"
                        print("You selected Fire Slash")
                    elif choice == 2:
                        if i == 0:
                            self.ability1 = "Power Slash"
                        if i == 1:
                            self.ability2 = "Power Slash"
                        print("You selected Power Slash")
                    elif choice == 3:
                        if i == 0:
                            self.ability1 = "Gigantic Storm"
                        if i == 1:
                            self.ability2 = "Gigantic Storm"
                        print("You selected Gigantic Storm")
                    elif choice == 4:
                        if i == 0:
                            self.ability1 = "Chaotic Disaster"
                        if i == 1:
                            self.ability2 = "Chaotic Disaster"
                        print("You selected Chaotic Disaster")

                    if self.ability1 == self.ability2:
                        print("Ability already chosen")
                        continue

                    i += 1
                else:
                    print("Invalid Input")
                    continue
            
            if(self.characterClass == "Archer"):
                if i == 0:
                    print("\nSelect Ability 1:")
                if i == 1:
                    print("\nSelect Ability 2:")
                print("\t[1] Take Aim")
                print("\t[2] Quick Shot")
                print("\t[3] Blazing Arrow")
                print("\t[4] Frost Arrow\n")
                choice = int(input("Select: "))
                
                if choice in (1, 2, 3, 4):
                    if choice == 1:
                        if i == 0:
                            self.ability1 = "Take Aim"
                        if i == 1:
                            self.ability2 = "Take Aim"
                        print("You selected Take Aim")
                    elif choice == 2:
                        if i == 0:
                            self.ability1 = "Quick Shot"
                        if i == 1:
                            self.ability2 = "Quick Shot"
                        print("You selected Quick Shot")
                    elif choice == 3:
                        if i == 0:
                            self.ability1 = "Blazing Arrow"
                        if i == 1:
                            self.ability2 = "Blazing Arrow"
                        print("You selected Blazing Arrow")
                    elif choice == 4:
                        if i == 0:
                            self.ability1 = "Frost Arrow"
                        if i == 1:
                            self.ability2 = "Frost Arrow"
                        print("You selected Frost Arrow")

                    if self.ability1 == self.ability2:
                        print("Ability already chosen")
                        continue

                    i += 1
                else:
                    print("Invalid Input")
                    continue
            
            if(self.characterClass == "Assassin"):
                if i == 0:
                    print("\nSelect Ability 1:")
                if i == 1:
                    print("\nSelect Ability 2:")
                print("\t[1] Cloaking")
                print("\t[2] Enchant Poison")
                print("\t[3] Sonic Acceleration")
                print("\t[4] Meteor Assault\n")
                choice = int(input("Select: "))
                
                if choice in (1, 2, 3, 4):
                    if choice == 1:
                        if i == 0:
                            self.ability1 = "Cloaking"
                        if i == 1:
                            self.ability2 = "Cloaking"
                        print("You selected Cloaking")
                    elif choice == 2:
                        if i == 0:
                            self.ability1 = "Enchant Poison"
                        if i == 1:
                            self.ability2 = "Enchant Poison"
                        print("You selected Enchant Poison")
                    elif choice == 3:
                        if i == 0:
                            self.ability1 = "Sonic Acceleration"
                        if i == 1:
                            self.ability2 = "Sonic Acceleration"
                        print("You selected Sonic Acceleration")
                    elif choice == 4:
                        if i == 0:
                            self.ability1 = "Meteor Assault"
                        if i == 1:
                            self.ability2 = "Meteor Assault"
                        print("You selected Meteor Assault")

                    if self.ability1 == self.ability2:
                        print("Ability already chosen")
                        continue

                    i += 1
                else:
                    print("Invalid Input")
                    continue

print("Customize your character:")
char = Character("initClass", "initWeapon", "initAbility1", "initAbility2")
char.SetClass()
char.SetWeapon()
char.SetAbility()
print("\nCharacter Details:")
print("Class: " + char.characterClass)
print("Weapon: " + char.weapon)
print("Ability: " + char.ability1 + " & " + char.ability2 + "\n")

with open('characterdb.csv', 'a', newline="") as f:
    fieldnames = ['class', 'weapon', 'ability1', 'ability2']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    if f.tell() == 0:
        csv_writer.writeheader()

    csv_writer.writerow({'class' : char.characterClass, 'weapon' : char.weapon, 'ability1' : char.ability1, 'ability2' : char.ability2})

print("Character successfully saved in database (characterdb.csv)")