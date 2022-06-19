# Bruno, Jared Ivan D.
# Hilario, Cyrille Jaye N.

class Character:
    def __init__(self, characterClass, weapon, ability):
        self.characterClass = characterClass
        self.weapon = weapon
        self.ability = ability

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
                    self.characterClass = 'Knight'
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
        while True:
            if(self.characterClass == "Wizard"):
                print("\nSelect an Ability:")
                print("\t[1] Energy Ball")
                print("\t[2] Dragons Breath")
                print("\t[3] Crown of Flame")
                print("\t[4] Hail Storm\n")
                choice = int(input("Select: "))
                
                if choice in (1, 2, 3, 4):
                    if choice == 1:
                        self.ability = "Energy Ball"
                        print("You selected Energy Ball")
                    elif choice == 2:
                        self.ability = "Dragons Breath"
                        print("You selected Dragons Breath")
                    elif choice == 3:
                        self.ability = "Crown of Flame"
                        print("You selected Crown of Flame")
                    elif choice == 4:
                        self.ability = "Hail Storm"
                        print("You selected Hail Storm")
                    break
                else:
                    print("Invalid Input")
                    continue
            
            if(self.characterClass == "Knight"):
                print("\nSelect an Ability:")
                print("\t[1] Fire Slash")
                print("\t[2] Power Slash")
                print("\t[3] Gigantic Storm")
                print("\t[4] Chaotic Disaster\n")
                choice = int(input("Select: "))
                
                if choice in (1, 2, 3, 4):
                    if choice == 1:
                        self.ability = "Fire Slash"
                        print("You selected Fire Slash")
                    elif choice == 2:
                        self.ability = "Power Slash"
                        print("You selected Power Slash")
                    elif choice == 3:
                        self.ability = "Gigantic Storm"
                        print("You selected Gigantic Storm")
                    elif choice == 4:
                        self.ability = "Chaotic Disaster"
                        print("You selected Chaotic Disaster")
                    break
                else:
                    print("Invalid Input")
                    continue
            
            if(self.characterClass == "Archer"):
                print("\nSelect an Ability:")
                print("\t[1] Take Aim")
                print("\t[2] Quick Shot")
                print("\t[3] Blazing Arrow")
                print("\t[4] Frost Arrow\n")
                choice = int(input("Select: "))
                
                if choice in (1, 2, 3, 4):
                    if choice == 1:
                        self.ability = "Take Aim"
                        print("You selected Take Aim")
                    elif choice == 2:
                        self.ability = "Quick Shot"
                        print("You selected Quick Shot")
                    elif choice == 3:
                        self.ability = "Blazing Arrow"
                        print("You selected Blazing Arrow")
                    elif choice == 4:
                        self.ability = "Frost Arrow"
                        print("You selected Frost Arrow")
                    break
                else:
                    print("Invalid Input")
                    continue
            
            if(self.characterClass == "Assassin"):
                print("\nSelect an Ability:")
                print("\t[1] Cloaking")
                print("\t[2] Enchant Poison")
                print("\t[3] Sonic Acceleration")
                print("\t[4] Meteor Assault\n")
                choice = int(input("Select: "))
                
                if choice in (1, 2, 3, 4):
                    if choice == 1:
                        self.ability = "Cloaking"
                        print("You selected Cloaking")
                    elif choice == 2:
                        self.ability = "Enchant Poison"
                        print("You selected Enchant Poison")
                    elif choice == 3:
                        self.ability = "Sonic Acceleration"
                        print("You selected Sonic Acceleration")
                    elif choice == 4:
                        self.ability = "Meteor Assault"
                        print("You selected Meteor Assault")
                    break
                else:
                    print("Invalid Input")
                    continue

print("Customize your first character:")
char1 = Character("initClass", "initWeapon", "initAbility")
char1.SetClass()
char1.SetWeapon()
char1.SetAbility()
print("\nCharacter 1 Details:")
print("Class: " + char1.characterClass)
print("Weapon: " + char1.weapon)
print("Ability: " + char1.ability + "\n")

print("Customize your second character:")
char2 = Character("initClass", "initWeapon", "initAbility")
char2.SetClass()
char2.SetWeapon()
char2.SetAbility()
print("\nCharacter 2 Details:")
print("Class: " + char2.characterClass)
print("Weapon: " + char2.weapon)
print("Ability: " + char2.ability + "\n")