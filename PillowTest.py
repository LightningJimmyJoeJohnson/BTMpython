from PIL import Image
class PillowTest(object):
    
    def __init__(self):
        

    def testFunc(self,path):
        im = Image.open(path)
        im.show()
        box = (100,100,400,400)
        region = im.crop(box)
        region.show()

