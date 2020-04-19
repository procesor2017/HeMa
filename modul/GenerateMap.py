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
                coin = random.randrange(0, 3)
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
                self.PowerofAllDwarf.append(RealCityCoor)
            else:
                pass
            e += 1
        Image.fromarray((color_world).astype(np.uint8)).save('../data/map1.png')

    def create_history1(self):

        DistanceCity = 50
        LenghtPower = len(self.PowerofAllDwarf)
        i = 0
        while i < LenghtPower:
            y1 = int(self.PowerofAllDwarf[i][1])
            x1 = int(self.PowerofAllDwarf[i][2])
            fk = 1
            while fk < LenghtPower:
                y = int(self.PowerofAllDwarf[fk][1])
                x = int(self.PowerofAllDwarf[fk][2])
                w = 0
                u = 0
                if (x1 - DistanceCity) < int(x) < (x1 + DistanceCity) and (y1 - DistanceCity) < int(y) < (
                        y1 + DistanceCity):
                    if (y1 - DistanceCity) < int(y) < (y1 + DistanceCity):
                        # (početobyvatel * 0,7) * síla_jednoho bojovníka * (sílacivilizace /100 )
                        Nation1 = (int(self.PowerofAllDwarf[i][3]) * 0.75) * int(self.PowerofAllDwarf[i][4]) * (int(self.PowerofAllDwarf[i][5]) / 100)
                        Nation2 = (int(self.PowerofAllDwarf[fk][3]) * 0.75) * int(self.PowerofAllDwarf[fk][4]) * (int(self.PowerofAllDwarf[fk][5]) / 100)
                        Nation1List = self.PowerofAllDwarf[i]
                        Nation2List = self.PowerofAllDwarf[fk]
                        with open('../data/HistoryOfDwarf.csv', 'a') as history:
                            if Nation1 < Nation2:
                                print(y, x, y1, x1)
                                for x in self.PowerofAllDwarf:
                                    if x == Nation1List:
                                        self.PowerofAllDwarf.remove(x)
                                        history.write(
                                            'Dwarf clan {WeakClan} was destroyed by {Strongclan} in {age} \n'.format(
                                                WeakClan=Nation1List[0], Strongclan=Nation2List[0],
                                                age=random.randrange(0, 1000)))
                                        w = 1
                                        u = 1
                            elif Nation1 == Nation2:
                                pass
                            else:
                                for x in self.PowerofAllDwarf:
                                    if x == Nation2List:
                                        self.PowerofAllDwarf.remove(x)
                                        history.write(
                                            'Dwarf clan {WeakClan} was destroyed by {Strongclan} in {age} \n'.format(
                                                WeakClan=Nation1List[0], Strongclan=Nation2List[0],
                                                age=random.randrange(0, 1000)))
                                        w = 1
                                        u = 1
                if w == 1:
                    pass
                else:
                    fk += 1
                LenghtPower = len(self.PowerofAllDwarf)
            if u == 1:
                pass
            else:
                i += 1
            LenghtPower = len(self.PowerofAllDwarf)
        DwarfCity = self.PowerofAllDwarf
        print(DwarfCity)
        print('start open oldmap')
        OldMap = Image.open('../data/map.png')
        e = 0
        print(len(DwarfCity))
        while e < len(DwarfCity):
            print('start print')
            draw = ImageDraw.Draw(OldMap)
            y1 = int(DwarfCity[e][1])
            x1 = int(DwarfCity[e][2])
            shape = [(x1, y1), (x1+10, y1+10)]
            draw.rectangle(shape, fill="pink")
            OldMap.save('../data/map2.png', 'PNG')
            e += 1
        print('end?')


create_world = CreateWorld()
create_world.create_history1()