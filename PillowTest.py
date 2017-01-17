from PIL import Image
class PillowTest:
    uslessVar = 0
    thresh1 = 0 
    def __init__(self):
        uselessVar=0

    def testFunc(self,path):
        im = Image.open(path)
        im.show()
        box = (100,100,400,400)
        region = im.crop(box)
        region.show()

    """ Rios, Vickii"""
    def obomify(self,path):
	im= Image.open(path)
	im.show()
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



