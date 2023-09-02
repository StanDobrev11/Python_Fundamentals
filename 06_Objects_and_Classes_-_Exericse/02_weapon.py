class Weapon:
    __bullets = 0

    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):  # shooting  till no bullets left
        if self.bullets > Weapon.__bullets:
            Weapon.__bullets += 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self):  # returns remaining bullets
        return f"Remaining bullets: {self.bullets - Weapon.__bullets}"

#
# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
