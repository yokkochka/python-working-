# Начало урока, небольшая теория
# dog = 'dog'
# print(id(dog))
# print(type(dog))

# class Cat:
#     'Это кошка'
#     def say():
#         print('Meow, meow')
#         
#         
# cat_say = Cat.say()
# print(Cat.__doc__)

# class Apple:
#     def __init__(self):
#         self.ap = 12
#         
#     def eat(self, num):
#         self.ap -= num
#         return self.ap
# 
# l = Apple()
# 
# apple = Apple()
# print(apple.ap)
# print(apple.eat(3))
# print(apple.ap)
# print(l.ap)


# Начало RPG
import random
import time


class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.lvl = 1
        self.exp = 0
        self.skill = None
        
    def create_hero(name, species, prof):
        hp = 0
        damage = 0
        if species == species_list[0]:
            hp += 100
            damage += 50
        elif species == species_list[1]:
            hp += 50
            damage += 100
        elif species == species_list[2]:
            hp += 70
            damage += 60
        elif species == species_list[3]:
            hp += 90
            damage += 110
        elif species == species_list[4]:
            hp += 20
            damage += 140
        else:
            print('Я не знаю кто ты...')
        
        if prof == prof_list[0]:
            hp += 100
            damage += 50
        elif prof == prof_list[1]:
            hp += 60
            damage += 100
        elif prof == prof_list[2]:
            hp += 50
            damage += 70
        elif prof == prof_list[3]:
            hp += 30
            damage += 110
        elif prof == prof_list[4]:
            hp += 80
            damage += 50
        else:
            print('Я незнаю такой профессии')
        
        return Player(name, hp, damage)
    
    def attack(self, victim):
        max_exp = self.lvl *100
        victim.hp -= self.damage
        
        if victim.hp <= 0:
            print(f'Поздравляем, {victim.name} повержен! +20 опыта')
            time.sleep(1)
            self.exp += 20
            if self.exp >= max_exp:
                self.levelup(max_exp)
                
            thing = random.randint(0,3)
            
            if thing == 1:
                wpn = self.create_weapon()
                print(f'Вам выпало новое оружие! {wpn[0]} {wpn[1]}')
                time.sleep(1)
            elif thing == 2:
                armor = self.create_armor()
                print(f'Вам выпала новая броня! {armor[0]} {armor[1]}')
                time.sleep(1)
            elif thing == 3:
                food = self.create_food()
                print(f'Вам выпала вкусняшка! {food}')
                time.sleep(1)
            else:
                print('Награды нет... Повезет в следующий раз')
                time.sleep(1)
                
            self.skill = random.choice(powers)
            print(f'Теперь вы одврены способностью: {self.skill}')
            time.sleep(1)
            
            return False
        else:
            if self.skill is not None:
                ability()
            print(f'{victim.name}, теперь имеет {victim.hp} очков здоровья')
            time.sleep(1)
            return True
    
    def levelup(self, max_exp):
        self.exp -= max_exp
        self.lvl += 1
        self.damage += self.lvl * 5
        self.hp += self.lvl*10
        print(f'{self.name}, поздравляем с повышением уровня! Уровень: {self.lvl}')
        time.sleep(1)
    
    def create_weapon(self):
        wpn_type = wearpon_type_list[random.randint(0,2)]
        wpn_rare = random.choice(list(wearpon_rare_dict.keys()))
        if wpn_type == wearpon_type_list[0]:
            self.damage += 4*wpn_rare
        elif wpn_type == wearpon_type_list[1]:
            self.damage += 5*wpn_rare
        elif wpn_type == wearpon_type_list[2]:
            self.damage += 6*wpn_rare
        return wpn_type, wearpon_rare_dict[wpn_rare]
    
    def create_armor(self):
        armor_type = armor_type_list[random.randint(0,2)]
        armor_rare = random.choice(list(armor_rare_dict.keys()))
        if armor_type == armor_type_list[0]:
            self.hp += 4*armor_rare
        elif armor_type == armor_type_list[1]:
            self.hp += 5*armor_rare
        elif armor_type == armor_type_list[2]:
            self.hp += 6*armor_rare
        return armor_type, armor_rare_dict[armor_rare]
    
    def create_food(self):
        r_heal_size = random.choice(list(heal.keys()))
        self.hp += r_heal_size
        return heal[r_heal_size]
    
         
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def create_enemy():
        rnd_name = random.choice(enemy_name)
        rnd_hp = random.randint(10, 50)
        rnd_damage = random.randint(30,70)
        return Enemy(rnd_name, rnd_hp, rnd_damage)
    
    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            print(f'Поздравляем, {victim.name} повержен!')
            time.sleep(1)
            quit()
            
        else:
            print(f'{victim.name}, оставшееся здоворье: {victim.hp}')
            time.sleep(1)
            

# Функция битвы
def fight_choice():
    answer = input(f'Готов сразиться с {enemy.name}? (ответ "да" ил "нет")').lower()
    if answer == 'да':
        rezult = hero.attack(enemy)
        if rezult:
            enemy.attack(hero)
            fight_choice()
    elif answer == 'нет':
        plan = random.randint(0,1)
        if plan == 0:
            print('Побег не удался. Монстр нападает')
            time.sleep(1)
            enemy.attack(hero)
            fight_choice()
        elif plan == 1:
            print('Вы сбежали от монстра')
            time.sleep(1)
    else:
        print('Будь внимательнее, ибо у меня нет такого варианта действий')
        time.sleep(1)
        fight_choice()

def ability():
    if hero.skill == 'Замораживание':
        print('Вы заморозили монстра! Теперь он не атакует тебя')
        time.sleep(1)
        enemy.damage = 0
    elif hero.skill == 'Отравление':
        print('Вы отравили монстра, ему -10 здоровья')
        time.sleep(1)
        enemy.hp -= 10
    elif hero.skill == 'Лечение':
        print('Твое оружие вылечило тебя +10 здоровья')
        time.sleep(1)
        hero.hp += 10
        
        
enemy_name = ['Видридж', 'Крилл', 'Сюзи', 'Примк']        
species_list = ['эльф', 'гном', 'человек', 'троль', 'пандарен']
prof_list = ['лучник', 'воин', 'маг', 'жрец', 'друид']
wearpon_type_list = ['Меч', 'Лук', 'Посох']
wearpon_rare_dict = {1: 'Обычный', 2: 'Редкий', 3: 'Эпический'}
armor_type_list = ['Шлем', 'Бфрьер' , 'Щит']
armor_rare_dict = {1: 'Обычный', 2: 'Редкий', 3: 'Эпический'}
heal = {5: 'Апельсин', 10: 'Каша Геркулес', 15: 'Творожная запеканка'}
powers = ['Замораживание', 'Отравление', 'Лечение']


my_name = input('Введите имя своего героя: ').lower()
print(f'Доступные расы: {species_list}')
my_species= input('Выберите доступную расу своего героя: ').lower()
print(f'Доступные пофессии: {prof_list}')
my_prof= input('Выберите доступную профессию своего героя: ').lower()
hero = Player.create_hero(my_name, my_species, my_prof)
print(f'Характеристики {hero.name} : Здоровье: {hero.hp}, Урон: {hero.damage}, Урон: {hero.lvl}, Опыт: {hero.exp}')

while True:
    event = random.randint(1,2)
    if event == 1:
        print('Тебе никто не встретился')
        time.sleep(1)
    elif event == 2:
        enemy = Enemy.create_enemy()
        print(f'Тебе встретился {enemy.name}!')
        print(f'Статы монстра: \nЗдоровье: {enemy.hp}, \nУрон: {enemy.damage}')
        print(f'Статы героя {hero.name}:  \nЗдоровье: {hero.hp} \nУрон: {hero.damage} \nУровень: {hero.lvl} \nОпыт: {hero.exp}')
        time.sleep(2)
        fight_choice()
   
# enemy = Enemy.create_enemy()
# print(enemy.name, enemy.hp, enemy.damage)


        
    