import csv
import os

class Player:
    def __init__(self, name='Player'):
        self.name = name
        self.gold = 50
        self.reputation_elf_mainclan = 0
        self.reputation_dwarf_mainhouse = 0
        self.reputation_human_mainkingdome = 1001
        self.im_good = 0

    def create_save_player(self, save_folder='../data'):
        with open('../data/player_data.csv', mode='w') as csv_file:
            list_values = ['name,', 'gold,', 'elf_repu,', 'dwarf_repu,', 'human_repu,', 'im_good,']
            for item in list_values:
                csv_file.write('{0}'.format(item))
            csv_file.write('\n')
        with open('../data/player_data.csv', 'a') as f:
            list_values = [self.name, self.gold, self.reputation_elf_mainclan, self.reputation_dwarf_mainhouse, self.reputation_human_mainkingdome, self.im_good]
            for item in list_values:
                f.write('{0}'.format(str(item)+','))

    def save_player_stats(self, save_folder='../data', name='Player', gold='50', reputation_elf_mainclan='0', reputation_dwarf_mainhouse='0', reputation_human_mainkingdome='0', im_good='0'):
        with open('../data/player_data.csv', mode='w') as csv_file:
            list_values = ['name,', 'gold,', 'elf_repu,', 'dwarf_repu,', 'human_repu,', 'im_good,']
            for item in list_values:
                csv_file.write('{0}'.format(item))
            csv_file.write('\n')
        with open('../data/player_data.csv', 'a') as f:
            list_values = [name, gold, reputation_elf_mainclan, reputation_dwarf_mainhouse, reputation_human_mainkingdome, im_good]
            for item in list_values:
                f.write('{0}'.format(str(item)+','))

# player = Player(name='Honzik')
# player.create_save_player()
# player.save_player_stats(name='Dan',gold='100')