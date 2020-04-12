import csv
import os
import random
from typing import TextIO


class Champ():
    def create_champ(self):
        nations_list = ['elf']
        sex_list = ['male', 'female']
        champions_class = ['warrior']
        nations = random.choice(nations_list)
        sex = random.choice(sex_list)
        champ_class = random.choice(champions_class)
        names = []
        list_with_value = []
        if nations == 'elf':
            with open('../data/name.csv') as f:
                csv__reader = csv.reader(f, delimiter=',')
                for row in csv__reader:
                    names.append(row)
                len_names = len(names[0])
                name = names[0][random.randrange(1, len_names)]
        elif nations == 'human':
            pass
        elif nations == 'dwarf':
            pass
        if champ_class == 'warrior':
            champ_level = random.randrange(1, 5)
            hp = 100 + (100 * champ_level / 10)
            mana = 10 + (10 * champ_level / 10)
            strenght = 10 + (10 * champ_level / 10)
            intelect = 5 + (5 * champ_level / 10)
            armor = 0
            magic_dmg = 0 + intelect + (mana * 00.1) + (0 * champ_level / 10)
            g = name, champ_class, champ_level, hp, mana, strenght, intelect, armor, magic_dmg, nations, sex
            list_with_value.append(g)
        else:
            pass

        return list_with_value

    def save_value_champ(self, list_value, save_folder='../data'):
        if os.path.exists(save_folder):
            self.save_folder = save_folder
        else:
            os.mkdir(save_folder)
        if os.path.exists('../data/champ_data.csv'):
            pass
        else:
            with open('../data/champ_data.csv', mode='w') as csv_file:
                list_values = ['id,', 'name,', 'class,', 'level,', 'hp,', 'mana,', 'strenght,', 'intelect,', 'armor,',
                                'magic_dmg,', 'nation,', 'sex \n']
                for item in list_values:
                    csv_file.write('{0}'.format(item))
            with open('../data/champ_data.csv', 'a') as f:
                i = 0
                f.write('1,')
                while i < len(list_value[0]):
                    f.write(str(list_value[0][i])+',')
                    i += 1

champ = Champ()
champ.save_value_champ(champ.create_champ())
