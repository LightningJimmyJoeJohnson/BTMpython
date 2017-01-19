from PIL import Image
from PIL import ImageFilter
from sys import platform
import os
import getpass
class PillowTest:
    uslessVar = 182
    thresh1 = 0
    def __init__(self):
        uselessVar=0

    def pathMaker(self,fileName): #Gets the user name of the current user and uses that to create a file path to the given image name. Only works if the image is in the proper directory
        user = getpass.getuser()

        if platform == "linux" or platform == "linux2": #uses the patform import from the cyc class
            return "/home/" +os.getuid() + "/Documents/PythonProjects/BTMpython-master/" + fileName
        # TODO: add case for osx
        elif platform == "win32":
            return "C:/Users/" + user + "/Desktop/BTMpython-master/" + fileName

    def crop(self,fileName):
        path = self.pathMaker(fileName)
        im = Image.open(path)
        im.show()
        box = (100,100,400,400)
        region = im.crop(box)
        region.show()

    """Vickii Rios"""
    def obomify(self,fileName):
        path = self.pathMaker(fileName)
        im= Image.open(path)
        pixels= list(im.getdata())

        darkBlue = (0, 51, 76)
        red = (217, 26, 33)
        lightBlue = (112, 150, 158)
        yellow = (252, 227, 166)

        list_2= []

        num = 0

        for trip in pixels:
            b=sum(trip)
            #print (b)

            if b < self.thresh1:
                list_2.append(darkBlue)
            elif b > 182 and b < 364:
                list_2.append(red)
            elif b > 364 and b < 546:
                list_2.append(lightBlue)
            else:
                list_2.append(yellow)


        newpic = Image.new("RGB" , (im.size))
        newpic.putdata(list_2)

        newpic.show()

    def blurImage(self,fileName):
        path = self.pathMaker(fileName)
        im = Image.open(path)
        imout = im.filter(ImageFilter.BLUR)
        imout.show()

    def contourImage(self,fileName):
        path = self.pathMaker(fileName)
        im = Image.open(path)
        imout = im.filter(ImageFilter.CONTOUR)
        imout.show()
