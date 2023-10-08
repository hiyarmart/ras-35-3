class SuperHero(object):
    people = 'people'
    def __init__(self,name,nickname,SuperPower,health_points,catchphrase):
           self.name = name
           self.nickname = nickname
           self.superpower = SuperPower
           self.health_points = health_points
           self.catchphrase = catchphrase
    def __str__(self):
        return f'Nickname: {self.nickname}\n' \
                          f'SuperPower: {self.superpower}\n' \
                          f'HealthPoints: {self.health_points}\n'
    def __len__(self):
            return len(self.catchphrase)
    def print_name(self):
        print(f'SuperHero Name: {self.name}')
    def print_health_points(self):
            if isinstance(self.health_points, (int,float)):
                print(f'Health point: {self.health_points * 2} (*2)')
            else:
                print('Error,Health Points can only be int,float')

Hero = SuperHero('Aang','Avatar','water,fire,air,earth',\
                 100.0, 'if you want to become a warrior,get rid of fear')
Hero.print_name()
Hero.print_health_points()
print(Hero.__str__())
print(len(Hero))