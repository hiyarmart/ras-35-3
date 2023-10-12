class SuperHero(object):
    people = 'people'

    def __init__(self, name, nickname, SuperPower, health_points, catchphrase):
           self.name = name
           self.nickname = nickname
           self.superpower = SuperPower
           self.health_points = health_points
           self.catchphrase = catchphrase

    def name_print(self):
        return f'Имя героя:{self.name}'
    def healtha_x2(self):
        self.health_points *= 2
        return self.health_points

    def __str__(self):
        return (f"nickname: {self.nickname} \n"
            f"SuperPower: {self.superpower} \n"
            f"Health: {self.health_points}")

    def __len__(self):
        return len(self.catchphrase)

    def Crit(self):
        self.damage **= 2
        return self.damage

class AirHero(SuperHero):
      def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.damage = damage
        self.fly = fly
      def healtha_x2(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points, self.fly

      def Fact(self):
        return "The wind ic cool"

class SpaseHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase,)
        self.damage = damage
        self.fly = fly
    def healtha_x2(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points, self.fly
    def NewPhrase(self):
        return 'True in the true_phrase'

    def Fact(self):
      return "male is fine without the sun"

class Villain(AirHero):
    SuperHero.people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, ):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)

        def gen_x(self):
            pass

invincible = SuperHero('Mark Greyson','invincible','superpower, super durability','500','Smart can"t be weak')

Omni_man = AirHero('Nollan', 'Omni_man', 'superpower, super durability, flight', '700', 'being a father is the best achievement', '300' )

allen_the_alien = SpaseHero('Allen', 'Alien', 'superpower,super speed, flight', '450', 'Universe is smaller than it seems', '200')

Mad_Genius = Villain('Angctrom Levy', 'Mad Genius','Time trevel', '200', 'Time is nothing in my eyes', '100')

def print_hero_info(hero_instance):
    print(hero_instance.name_print())
    hero_instance.health_x2(
    print(str(hero_instance)),
    print(f'длина фразы: {len(hero_instance.catchphrase)}\n'),

print_hero_info(invincible),
print_hero_info(Omni_man),
print_hero_info(allen_the_alien),
print_hero_info(Mad_Genius),

print(allen_the_alien.NewPhrase()),
print(Omni_man.Fact()),
print(allen_the_alien.Fact()),
print(Omni_man.Crit()),
print(allen_the_alien.Crit()),
print(Mad_Genius.Crit()),






