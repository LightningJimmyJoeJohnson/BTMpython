from PIL import Image
from PIL import ImageFilter
from sys import platform
import os
import getpass
class BTMPillowLib:
    uslessVar = 182

    #thresh holds
    thresh1 = 0
    thresh2 = 0
    thresh1 = 0
    thresh1 = 0
    #colors
    color1 = (0,0,0)
    color2 = (0,0,0)
    color3 = (0,0,0)
    color4 = (0,0,0)

    def __init__(self):
        uselessVar=0

    def pathMaker(self,fileName): #Gets the user name of the current user and uses that to create a file path to the given image name. Only works if the image is in the proper directory
        user = getpass.getuser()

        if platform == "linux" or platform == "linux2": #uses the patform import from the cyc class
            return "/home/" +os.getuid() + "/Documents/PythonProjects/BTMpython/" + fileName
        # TODO: add case for osx
        elif platform == "win32":
            return "C:/Users/" + user + "/Desktop/BTMpython-master/" + fileName

    def showImage(self,fileName):
        path = self.pathMaker(fileName)
        im = Image.open(path)
        im.show()

    def cropImage(self,fileName, left, top, right, lower ):
        path = self.pathMaker(fileName)
        im = Image.open(path)
        box = (left,top,right,lower)
        region = im.crop(box)
        region.show()

    """Vickii Rios"""
    def obomify(self,fileName):
        path = self.pathMaker(fileName)
        im= Image.open(path)
        pixels= list(im.getdata())

        self.color1 = (0, 51, 76)
        self.color2 = (217, 26, 33)
        self.color3 = (112, 150, 158)
        self.color4 = (252, 227, 166)

        self.thresh1 = 182
        self.thresh2 = 364
        self.thresh3 = 546

        list_2= []

        num = 0

        for trip in pixels:
            b=sum(trip)
            #print (b)

            if b < self.thresh1:
                list_2.append(self.colo1)
            elif b > self.thresh1 and b < self.thresh2:
                list_2.append(self.color2)
            elif b > self.thresh2 and b < self.thresh3:
                list_2.append(self.color3)
            else:
                list_2.append(self.color4)


        newpic = Image.new("RGB" , (im.size))
        newpic.putdata(list_2)

        newpic.show()

    def trumpify(self, fileName, xTop, yTop, xBot, yBot):

        if xBot >= 819:
            xBot = 818

        if yBot >= 671:
            yBot = 670
        path = self.pathMaker(fileName)
        path2 = self.pathMaker("TrumpHair.png")
        im= Image.open(path)
        im2 = Image.open(path2)
        box = (xTop, yTop)
        im.paste(im2,box, im2)
        im.show()



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

    def customFilter(self,fileName): #Color Values and threshholds need to be set before use
        path = self.pathMaker(fileName)
        im= Image.open(path)
        pixels= list(im.getdata())

        list_2= []

        num = 0

        for trip in pixels:
            b=sum(trip)
            #print (b)

            if b < self.thresh1:
                list_2.append(self.colo1)
            elif b > self.thresh1 and b < self.thresh2:
                list_2.append(self.color2)
            elif b > self.thresh2 and b < self.thresh3:
                list_2.append(self.color3)
            else:
                list_2.append(self.color4)


        newpic = Image.new("RGB" , (im.size))
        newpic.putdata(list_2)

        newpic.show()
