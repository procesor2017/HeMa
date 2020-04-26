import noise
import numpy as np
from PIL import Image, ImageDraw
import random



class CreateWorld:
    def __init__(self):
        reso_x = 1280
        reso_y = 1024

        shape = (reso_x, reso_y)
        octaves = 8
        persistence = 0.7
        lacunarity = 2

        blue = [65, 105, 225]
        green = [34, 139, 34]
        beach = [238, 214, 175]
        snow = [255, 250, 250]
        mountain = [139, 137, 137]

        color_City_human = [220, 20, 60]            # red
        color_City_dwarf = [199, 21, 133]           # pink :-D
        color_City_elf = [204, 204, 0]              # yellow

        base_random = random.randrange(0, 200)
        scale_random = random.randrange(500, 800)

        CoorCityListX = []
        CoorCityListY = []

        #List with coordinates cities
        self.PowerofAllHuman = []
        self.PowerofAllDwarf = []
        self.PowerofAllElfs = []

        SumCity = random.randrange(200, 500)
        Sc = 0
        while Sc < SumCity:
            x = random.randrange(10, reso_x - 10)
            CoorCityListX.append(x)
            y = random.randrange(10, reso_y - 10)
            CoorCityListY.append(y)
            Sc += 1

        world = np.zeros(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                world[i][j] = noise.pnoise2(i / scale_random,
                                            j / scale_random,
                                            octaves=octaves,
                                            persistence=persistence,
                                            lacunarity=lacunarity,
                                            repeatx=reso_x,
                                            repeaty=reso_y,
                                            base=base_random)
        # create color world
        color_world = np.zeros(world.shape + (3,))
        e = 0
        for i in range(shape[0]):
            for j in range(shape[1]):
                if world[i][j] < -0.05:
                    color_world[i][j] = blue
                elif world[i][j] < -0:
                    color_world[i][j] = beach
                elif world[i][j] < 0.15:
                    color_world[i][j] = green
                elif world[i][j] < 0.22:
                    color_world[i][j] = mountain
                elif world[i][j] < 1.0:
                    color_world[i][j] = snow
        SumCityList = len(CoorCityListX)
        Image.fromarray((color_world).astype(np.uint8)).save('../data/map.png')

        while e < SumCityList:
            if world[CoorCityListX[e], CoorCityListY[e]] < -0.05:
                pass
            elif world[CoorCityListX[e], CoorCityListY[e]] < 0.15:
                coin = random.randrange(0, 5)
                if coin == 1:
                    color_world[CoorCityListX[e], CoorCityListY[e]] = color_City_elf
                    RealCityCoor = []
                    RealCityCoor.append('NameOfClan')
                    RealCityCoor.append(CoorCityListX[e])
                    RealCityCoor.append(CoorCityListY[e])
                    RealCityCoor.append(random.randrange(1000, 5000))   # nuimber people
                    RealCityCoor.append(10)                             # power of one people
                    RealCityCoor.append(random.randrange(50, 100))                   # Power of civi
                    RealCityCoor.append(random.randrange(1, 10))
                    RealCityCoor.append('elf')
                    self.PowerofAllElfs.append(RealCityCoor)
                else:
                    color_world[CoorCityListX[e], CoorCityListY[e]] = color_City_human
                    RealCityCoor = []
                    RealCityCoor.append('NameOfClan')
                    RealCityCoor.append(CoorCityListX[e])
                    RealCityCoor.append(CoorCityListY[e])
                    RealCityCoor.append(random.randrange(5000, 20000))   # nuimber people
                    RealCityCoor.append(1)                             # power of one people
                    RealCityCoor.append(random.randrange(0, 50))                   # Power of civi
                    RealCityCoor.append(random.randrange(3, 7))
                    RealCityCoor.append('human')
                    self.PowerofAllHuman.append(RealCityCoor)

            elif world[CoorCityListX[e], CoorCityListY[e]] < 0.22:
                color_world[CoorCityListX[e], CoorCityListY[e]] = color_City_dwarf
                RealCityCoor = []
                RealCityCoor.append('NameOfClan')
                RealCityCoor.append(CoorCityListX[e])
                RealCityCoor.append(CoorCityListY[e])
                RealCityCoor.append(random.randrange(5000, 15000))  # nuimber people
                RealCityCoor.append(5)  # power of one people
                RealCityCoor.append(random.randrange(25, 75))  # Power of civi
                RealCityCoor.append(random.randrange(3, 7))
                RealCityCoor.append('dwarf')
                self.PowerofAllDwarf.append(RealCityCoor)
            else:
                pass
            e += 1
        Image.fromarray((color_world).astype(np.uint8)).save('../data/map1.png')

    def create_history1(self):

        DistanceCity = 50 # random.randrange(250, 500)
        LenghtPowerDwarf = len(self.PowerofAllDwarf)
        LenghtPowerElf = len(self.PowerofAllElfs)
        LenghtPowerHuman = len(self.PowerofAllHuman)
        i = 0
        while i < LenghtPowerDwarf:
            y1 = int(self.PowerofAllDwarf[i][1])
            x1 = int(self.PowerofAllDwarf[i][2])
            fk = 1
            u = 0
            while fk < LenghtPowerDwarf:
                y = int(self.PowerofAllDwarf[fk][1])
                x = int(self.PowerofAllDwarf[fk][2])
                w = 0
                if (x1 - DistanceCity) < int(x) < (x1 + DistanceCity) and (y1 - DistanceCity) < int(y) < (
                        y1 + DistanceCity):
                    # (početobyvatel * 0,7) * síla_jednoho bojovníka * (sílacivilizace /100 )
                    Nation1 = (int(self.PowerofAllDwarf[i][3]) * 0.75) * int(self.PowerofAllDwarf[i][4]) * (int(self.PowerofAllDwarf[i][5]) / 100)
                    Nation2 = (int(self.PowerofAllDwarf[fk][3]) * 0.75) * int(self.PowerofAllDwarf[fk][4]) * (int(self.PowerofAllDwarf[fk][5]) / 100)
                    Nation1List = self.PowerofAllDwarf[i]
                    Nation2List = self.PowerofAllDwarf[fk]
                    with open('../data/HistoryOfDwarf.csv', 'a') as history:
                        if Nation1 < Nation2:
                            for x in self.PowerofAllDwarf:
                                if x == Nation1List:
                                    self.PowerofAllDwarf.remove(x)
                                    history.write(
                                        'Dwarf clan {WeakClan} was destroyed by {Strongclan} in {age} \n'.format(
                                            WeakClan=Nation1List[0], Strongclan=Nation2List[0],
                                            age=random.randrange(0, 5000)))
                                    u = 1
                        elif Nation1 == Nation2:
                            pass
                        else:
                            for x in self.PowerofAllDwarf:
                                if x == Nation2List:
                                    self.PowerofAllDwarf.remove(x)
                                    history.write(
                                        'Dwarf clan {WeakClan} was destroyed by {Strongclan} in {age} \n'.format(
                                            WeakClan=Nation2List[0], Strongclan=Nation1List[0],
                                            age=random.randrange(0, 5000)))
                                    w = 1
                else:
                    self.PowerofAllDwarf[i][3] = self.PowerofAllDwarf[i][3] * 1.5
                    self.PowerofAllDwarf[i][5] = self.PowerofAllDwarf[i][5] * 1.2
                if w == 1:
                    pass
                else:
                    fk += 1
                LenghtPowerDwarf = len(self.PowerofAllDwarf)
            if u == 1:
                pass
            else:
                i += 1
            LenghtPowerDwarf = len(self.PowerofAllDwarf)

        i = 0
        while i < LenghtPowerElf:
            y1 = int(self.PowerofAllElfs[i][1])
            x1 = int(self.PowerofAllElfs[i][2])
            fk = 1
            u = 0
            while fk < LenghtPowerElf:
                y = int(self.PowerofAllElfs[fk][1])
                x = int(self.PowerofAllElfs[fk][2])
                w = 0
                if (x1 - DistanceCity) < int(x) < (x1 + DistanceCity) and (y1 - DistanceCity) < int(y) < (
                        y1 + DistanceCity):
                    # (početobyvatel * 0,7) * síla_jednoho bojovníka * (sílacivilizace /100 )
                    Nation1 = (int(self.PowerofAllElfs[i][3]) * 0.75) * int(self.PowerofAllElfs[i][4]) * (int(self.PowerofAllElfs[i][5]) / 100)
                    Nation2 = (int(self.PowerofAllElfs[fk][3]) * 0.75) * int(self.PowerofAllElfs[fk][4]) * (int(self.PowerofAllElfs[fk][5]) / 100)
                    Nation1List = self.PowerofAllElfs[i]
                    Nation2List = self.PowerofAllElfs[fk]
                    with open('../data/HistoryOfElf.csv', 'a') as history:
                        if Nation1 < Nation2:
                            for x in self.PowerofAllElfs:
                                if x == Nation1List:
                                    self.PowerofAllElfs.remove(x)
                                    history.write(
                                        'Elf house {WeakClan} was destroyed by {Strongclan} in {age} \n'.format(
                                            WeakClan=Nation1List[0], Strongclan=Nation2List[0],
                                            age=random.randrange(0, 5000)))
                                    u = 1
                        elif Nation1 == Nation2:
                            pass
                        else:
                            for x in self.PowerofAllElfs:
                                if x == Nation2List:
                                    self.PowerofAllElfs.remove(x)
                                    history.write(
                                        'Elf house {WeakClan} was destroyed by {Strongclan} in {age} \n'.format(
                                            WeakClan=Nation2List[0], Strongclan=Nation1List[0],
                                            age=random.randrange(0, 5000)))
                                    w = 1
                else:
                    self.PowerofAllElfs[i][3] = self.PowerofAllElfs[i][3] * 1.5
                    self.PowerofAllElfs[i][5] = self.PowerofAllElfs[i][5] * 1.2

                if w == 1:
                    pass
                else:
                    fk += 1
                LenghtPowerElf = len(self.PowerofAllElfs)
            if u == 1:
                pass
            else:
                i += 1
            LenghtPowerElf = len(self.PowerofAllElfs)

        i = 0
        while i < LenghtPowerHuman:
            y1 = int(self.PowerofAllHuman[i][1])
            x1 = int(self.PowerofAllHuman[i][2])
            fk = 1
            u = 0
            while fk < LenghtPowerHuman:
                y = int(self.PowerofAllHuman[fk][1])
                x = int(self.PowerofAllHuman[fk][2])
                w = 0
                if (x1 - DistanceCity) < int(x) < (x1 + DistanceCity) and (y1 - DistanceCity) < int(y) < (
                        y1 + DistanceCity):
                    # (početobyvatel * 0,7) * síla_jednoho bojovníka * (sílacivilizace /100 )
                    Nation1 = (int(self.PowerofAllHuman[i][3]) * 0.75) * int(self.PowerofAllHuman[i][4]) * (
                                int(self.PowerofAllHuman[i][5]) / 100)
                    Nation2 = (int(self.PowerofAllHuman[fk][3]) * 0.75) * int(self.PowerofAllHuman[fk][4]) * (
                                int(self.PowerofAllHuman[fk][5]) / 100)
                    Nation1List = self.PowerofAllHuman[i]
                    Nation2List = self.PowerofAllHuman[fk]
                    with open('../data/HistoryOfDwarf.csv', 'a') as history:
                        if Nation1 < Nation2:
                            for x in self.PowerofAllHuman:
                                if x == Nation1List:
                                    self.PowerofAllHuman.remove(x)
                                    history.write(
                                        'Dwarf clan {WeakClan} was destroyed by {Strongclan} in {age} \n'.format(
                                            WeakClan=Nation1List[0], Strongclan=Nation2List[0],
                                            age=random.randrange(0, 5000)))
                                    u = 1
                        elif Nation1 == Nation2:
                            pass
                        else:
                            for x in self.PowerofAllHuman:
                                if x == Nation2List:
                                    self.PowerofAllHuman.remove(x)
                                    history.write(
                                        'Dwarf clan {WeakClan} was destroyed by {Strongclan} in {age} \n'.format(
                                            WeakClan=Nation2List[0], Strongclan=Nation1List[0],
                                            age=random.randrange(0, 5000)))
                                    w = 1
                else:
                    self.PowerofAllHuman[i][3] = self.PowerofAllHuman[i][3] * 1.5
                    self.PowerofAllHuman[i][5] = self.PowerofAllHuman[i][5] * 1.2
                if w == 1:
                    pass
                else:
                    fk += 1
                LenghtPowerHuman = len(self.PowerofAllHuman)
            if u == 1:
                pass
            else:
                i += 1
            LenghtPowerHuman = len(self.PowerofAllHuman)

        DwarfCity = self.PowerofAllDwarf
        ElfCity = self.PowerofAllElfs
        HumanCity = self.PowerofAllHuman

        print('Počet elfu:'+ str(len(ElfCity)))
        print('Počet dwarfu:' + str(len(DwarfCity)))
        print('Počet humanu:' + str(len(HumanCity)))

        OldMap = Image.open('../data/map.png')
        e = 0

        while e < len(ElfCity):
            draw = ImageDraw.Draw(OldMap)
            y1 = int(ElfCity[e][1])
            x1 = int(ElfCity[e][2])
            shape = [(x1, y1), (x1+10, y1+10)]
            draw.rectangle(shape, fill="purple")
            OldMap.save('../data/map2.png', 'PNG')
            e += 1

        OldMap = Image.open('../data/map2.png')
        e = 0
        while e < len(DwarfCity):
            draw = ImageDraw.Draw(OldMap)
            y1 = int(DwarfCity[e][1])
            x1 = int(DwarfCity[e][2])
            shape = [(x1, y1), (x1+10, y1+10)]
            draw.rectangle(shape, fill="black")
            OldMap.save('../data/map2.png', 'PNG')
            e += 1

        OldMap = Image.open('../data/map2.png')
        e = 0
        while e < len(HumanCity):
            draw = ImageDraw.Draw(OldMap)
            y1 = int(HumanCity[e][1])
            x1 = int(HumanCity[e][2])
            shape = [(x1, y1), (x1+10, y1+10)]
            draw.rectangle(shape, fill="red")
            OldMap.save('../data/map2.png', 'PNG')
            e += 1
        # Druhý věk (Národy se řežou mezi sebou)
        ListAllRaces = []
        for x in DwarfCity:
            ListAllRaces.append(x)
        for x in ElfCity:
            ListAllRaces.append(x)
        for x in HumanCity:
            ListAllRaces.append(x)

        LenListAllRaces = len(ListAllRaces)
        DistanceCity2 = 120
        i = 0
        while i < LenListAllRaces:
            y1 = int(ListAllRaces[i][1])
            x1 = int(ListAllRaces[i][2])
            fk = 1
            u = 0
            while fk < LenListAllRaces:
                y = int(ListAllRaces[fk][1])
                x = int(ListAllRaces[fk][2])
                w = 0
                if (x1 - DistanceCity2) < int(x) < (x1 + DistanceCity2) and (y1 - DistanceCity2) < int(y) < (
                        y1 + DistanceCity2):
                    # (početobyvatel * 0,7) * síla_jednoho bojovníka * (sílacivilizace /100 )
                    Nation1 = (int(ListAllRaces[i][3]) * 0.75) * int(ListAllRaces[i][4]) * (
                                int(ListAllRaces[i][5]) / 100)
                    Nation2 = (int(ListAllRaces[fk][3]) * 0.75) * int(ListAllRaces[fk][4]) * (
                                int(ListAllRaces[fk][5]) / 100)
                    Nation1List = ListAllRaces[i]
                    Nation2List = ListAllRaces[fk]
                    with open('../data/HistoryOfAll.csv', 'a') as history:
                        if Nation1 < Nation2:
                            for x in ListAllRaces:
                                if x == Nation1List:
                                    ListAllRaces.remove(x)
                                    history.write(
                                        ' {WeakClan} was destroyed by {Strongclan} in {age} \n'.format(
                                            WeakClan=Nation1List[0], Strongclan=Nation2List[0],
                                            age=random.randrange(0, 5000)))
                                    u = 1
                        elif Nation1 == Nation2:
                            pass
                        else:
                            for x in ListAllRaces:
                                if x == Nation2List:
                                    ListAllRaces.remove(x)
                                    history.write(
                                        '{WeakClan} was destroyed by {Strongclan} in {age} \n'.format(
                                            WeakClan=Nation2List[0], Strongclan=Nation1List[0],
                                            age=random.randrange(0, 5000)))
                                    w = 1
                else:
                    ListAllRaces[i][3] = ListAllRaces[i][3] * 1.5
                    ListAllRaces[i][5] = ListAllRaces[i][5] * 1.2

                if w == 1:
                    pass
                else:
                    fk += 1
                LenListAllRaces = len(ListAllRaces)
            if u == 1:
                pass
            else:
                i += 1
            LenListAllRaces = len(ListAllRaces)
        # list nation after second age
        Elfa2a =[]
        Dwarf2a = []
        Human2a = []

        for x in ListAllRaces:
            if x[7] == 'elf':
                Elfa2a.append(x)
            elif x[7] == 'dwarf':
                Dwarf2a.append(x)
            elif x[7] == 'human':
                Human2a.append(x)

        print('Počet elfu:'+ str(len(Elfa2a)))
        print('Počet dwarfu:' + str(len(Dwarf2a)))
        print('Počet humanu:' + str(len(Human2a)))

        OldMap = Image.open('../data/map1.png')
        e = 0
        while e < len(Elfa2a):
            draw = ImageDraw.Draw(OldMap)
            y1 = int(Elfa2a[e][1])
            x1 = int(Elfa2a[e][2])
            shape = [(x1, y1), (x1+10, y1+10)]
            draw.rectangle(shape, fill="purple")
            OldMap.save('../data/map3.png', 'PNG')
            e += 1

        OldMap = Image.open('../data/map3.png')
        e = 0
        while e < len(Dwarf2a):
            draw = ImageDraw.Draw(OldMap)
            y1 = int(Dwarf2a[e][1])
            x1 = int(Dwarf2a[e][2])
            shape = [(x1, y1), (x1+10, y1+10)]
            draw.rectangle(shape, fill="black")
            OldMap.save('../data/map3.png', 'PNG')
            e += 1

        OldMap = Image.open('../data/map3.png')
        e = 0
        while e < len(Human2a):
            draw = ImageDraw.Draw(OldMap)
            y1 = int(Human2a[e][1])
            x1 = int(Human2a[e][2])
            shape = [(x1, y1), (x1+10, y1+10)]
            draw.rectangle(shape, fill="red")
            OldMap.save('../data/map3.png', 'PNG')
            e += 1






create_world = CreateWorld()
create_world.create_history1()
