from PIL import Image
class PillowTest(object):
    uslessVar = 0
    def __init__(self):
        uselessVar=0

    def testFunc(self,path):
        im = Image.open(path)
        im.show()
        box = (100,100,400,400)
        region = im.crop(box)
        region.show()


