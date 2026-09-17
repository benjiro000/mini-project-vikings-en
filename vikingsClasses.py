import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        """
        Soldier

        Modify the Soldier constructor function and add 2 methods to its
        prototype: attack(), and receiveDamage().

        constructor function
        - should receive 2 arguments (health & strength)
        - should receive the health property as its 1st argument
        - should receive the strength property as its 2nd argument

        attack() method
        - should be a function
        - should receive 0 arguments
        - should return the strength property of the Soldier

        receiveDamage() method
        - should be a function
        - should receive 1 argument (the damage)
        - should remove the received damage from the health property
        - shouldn't return anything
        """

        self.health = health
        self.strength = strength
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        """
        Viking

        A Viking is a Soldier with an additional property, their name. They
        also have a different receiveDamage() method and new method, battleCry().

        inheritance
        - Viking should inherit from Soldier

        constructor function
        - should receive 3 arguments (name, health & strength)
        - should receive the name property as its 1st argument
        - should receive the health property as its 2nd argument
        - should receive the strength property as its 3rd argument

        attack() method
        (Inherited from Soldier, no need to reimplement it.)
        - should be a function
        - should receive 0 arguments
        - should return the strength property of the Viking

        receiveDamage() method
        (Reimplemented for Viking because it needs different return values.)
        - should be a function
        - should receive 1 argument (the damage)
        - should remove the received damage from the health property
        - if the Viking is still alive, returns "NAME has received DAMAGE points of damage"
        - if the Viking dies, returns "NAME has died in act of combat"

        battleCry() method
        - should be a function
        - should receive 0 arguments
        - should return "Odin Owns You All!"
        """
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health >0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
            


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        """
        Saxon

        A Saxon is a weaker kind of Soldier. Unlike a Viking, a Saxon has no
        name. Their receiveDamage() method will also be different than the
        original Soldier version.

        inheritance
        - Saxon should inherit from Soldier

        constructor function
        - should receive 2 arguments (health & strength)
        - should receive the health property as its 1st argument
        - should receive the strength property as its 2nd argument

        attack() method
        (Inherited from Soldier, no need to reimplement it.)
        - should be a function
        - should receive 0 arguments
        - should return the strength property of the Saxon

        receiveDamage() method
        (Reimplemented for Saxon because it needs different return values.)
        - should be a function
        - should receive 1 argument (the damage)
        - should remove the received damage from the health property
        - if the Saxon is still alive, returns "A Saxon has received DAMAGE points of damage"
        - if the Saxon dies, returns "A Saxon has died in combat"
        """
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)


    def vikingAttack(self):
        # your code here
        viking_index = random.randint(0, len(self.vikingArmy) - 1)
        saxon_index = random.randint(0, len(self.saxonArmy) - 1)
        viking = self.vikingArmy[viking_index]
        saxon = self.saxonArmy[saxon_index]
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.pop(saxon_index)
        return result

    def saxonAttack(self):

        # optional: "random.choice"
        # your code here
        saxon_index = random.randint(0, len(self.saxonArmy) - 1)
        viking_index = random.randint(0, len(self.vikingArmy) - 1)
        saxon = self.saxonArmy[saxon_index]
        viking = self.vikingArmy[viking_index]
        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.pop(viking_index)
        return result


    def showStatus(self):
        # your code here
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
