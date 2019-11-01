from PIL import Image
__author__ = 'Student'

def flip_horizontal(img):
    """Flip the specified image left to right and return the modified image"""
    #reading image
    im = Image.open("filename")

    #flipping image horizontally
    newimg = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    
    return img

def make_linear_ramp(white):
    # putpalette expects [r,g,b,r,g,b,...]
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((r*i/255, g*i/255, b*i/255))
    return ramp


def sepia_tone(img):
    """Apply the sepia tone transformation to the specified image, and return the modified image"""
    #reading image
    im = Image.open("filename")
    
    #defining sepia
    sepia = make_linear_ramp((255,240,192))
    
    #converting to grayscale
    if im.mode != "L":
        im = im.convert("L")
        
    #converting to sepia
    im.putpalette(sepia)



    return img

def convert_to_gray_scale(img):
    """Apply the gray scale transformation to the specified image, and return the modified image"""
    #reading image
    im = Image.open("filename")

    if im.mode != "L":
        im = im.convert("L")

    return img

def flip_vertical(img):
    """Flip the specified image upside down and return the modified image"""
    #reading image
    im = Image.open("filename")

    #flipping image vertically
    newimg = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    return img

def rotate_right_90(img):
    """Rotate the specified image 90 degrees to the right and return the modified image"""
    #reading image
    im = Image.open("filename")
    
    #flipping image 90 degrees
    newimg = im.transpose(PIL.Image.ROTATE_90)
    
    return img

#construct a new image that
#is a copy of img in which
#each pixel retains all the red
#and loses the green and blue components.
#the function returns the modified image
def red_filter(img):
    """Apply the red filter transformation to the specified image, and return the modified image"""
    #with Image.open(filename) as img:
    w = img.width
    h = img.height

    newimg = Image.new('RGB', (w,h))
    for y in range(h):
        for x in range(w):
            r, g, b = img.getpixel((x,y))
            
            newimg.putpixel((x, y), (r, 0, 0))
        
    return newimg

#construct a new image that
#is a copy of img in which
#each pixel's red, green, and blue
#components are replaced with their complement with respect to 255
#the function returns the modified image
def negative(img):
    """Apply the negative transformation to the specified image, and return the modified image"""
    
    w = img.width
    h = img.height

    newimg = Image.new('RGB', (w,h))
    
    for y in range(h):
        for x in range(w):
            p = img.getpixel((x,y))  # in mode RGBA, p is a 4-tuple, in mode RGB a 3-tuple
            
            newpixel = (255 - p[0], 255 - p[1], 255 - p[2])
            newimg.putpixel((x,y), newpixel)


    return newimg

##DO NOT MODIFY THE FUNCTIONS BELOW
##THEY ARE USED FOR TESTING YOUR FUNCTIONS
##AND DISPLAYING IMAGES
    
#don't modify this function    
def test_one(transform, filename):
    transformName = str(transform).split()[1]
    
    try:
        #create an image corresponding to the specified file
        with Image.open(filename) as img:
            print(filename, img.format, "%dx%d" % img.size, img.mode)
            print("Starting "+ transformName)
        
            #apply the specified transformation to the image (mode RGB)
            img = transform(img.convert("RGB"))
        
            #show the transformed image
            img.show(title="{}({})".format(transformName, filename))
    except IOError:
        print("\t"+transformName + ":Error")
        import sys, traceback
        traceback.print_exc()

#don't modify this function
#I will use it to test all your functions
def test_all():
    transforms = [flip_horizontal, sepia_tone, convert_to_gray_scale, flip_vertical, rotate_right_90]
    for t in transforms:
        test_one(t, "penguins.gif")
        
if __name__ == '__main__':
    print(__author__)
    test_one(red_filter, "penguins.gif")    
    test_one(negative, "penguins.gif")
    #test_all()
