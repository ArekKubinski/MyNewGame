import configparser, mapobject, pygame, io
from PIL import Image

class Level:

    def __init__(self, file, size, gsize):
        pygame.init()
        self.gsize = gsize
        self.screen = pygame.display.set_mode(size)
        self.file = file
        self.cp = configparser.ConfigParser()
        self.cp.read(file)

    def crop(self, infile):
        im = Image.open(infile)
        imgwidth, imgheight = im.size
        width, height = self.gsize
        lis = []
        flis = []
        for i in range(imgheight//height):
            templis = []
            for j in range(imgwidth//width):
                box = (j*width, i*height, (j+1)*width, (i+1)*height)
                templis.append(im.crop(box))
            lis.append(templis)
        for temp in lis:
            templis = []
            for i in temp:
                img = Image.new('RGB', (height,width), 255)
                img.paste(i)
                imgb = io.BytesIO()
                img.save(imgb, 'PNG')
                imgb.seek(0)
                img = pygame.image.load(imgb).convert()
                templis.append(img)
            flis.append(templis)
        return flis


    def get_screen(self):
        return self.screen

    def get_gsize(self):
        return self.gsize

    def show(self, tag):
        return self.cp[tag]

    def maping(self):
        mapkey = set()
        m = []
        xlist = []
        lines = self.cp['level']['map'].split('\n')
        for line in lines:
            for ch in line:
                xlist.append(ch)
                mapkey.add(ch)
            m.append(xlist)
            xlist = []
        return m, mapkey

    def mapparse(self):
        mapp, keys = self.maping()
        lis = []
        for key in keys:
            confkey = []
            confkey.append(key)
            for conf in self.cp[key]:
                confkey.append(self.cp[key][conf])
            lis.append(confkey)
        xlist = []
        for x in mapp:
            ylist = []
            for y in x:
                for l in lis:
                    if l[0] == y:
                        ylist.append(l[1:])
            xlist.append(ylist)
        return xlist

    def mapobj(self):
        sprite = self.crop(self.cp['level']['tileset'])
        lis = self.mapparse()
        obj = []
        y, x = 0, 0
        for l in lis:
            for w in l:
                temptuple = tuple(map(int, w[0].split(', ')))
                obj.append(mapobject.MapObject(sprite[temptuple[0]][temptuple[1]], (x, y), int(w[1] == 'true'), int(w[2] == 'true')))
                x += 1
            y += 1
            x = 0
        return obj