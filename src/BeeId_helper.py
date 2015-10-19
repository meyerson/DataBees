from PIL import Image
import numpy as np

def img_to_matrix(filename, verbose=False):
    """
    takes a filename and turns it into a numpy array of RGB pixels
    """
    img = Image.open(filename)
    
    img = list(map(list,list(img.getdata())))
    return np.array(img)

def flatten_image(img):
    """
    takes in an (m, n) numpy array and flattens it
    into an array of shape (1, m * n)
    """
    print(img)
    s = img.shape[0] * img.shape[1]
    print(s)
    img_wide = [(x[0],x[1],x[2]) for x  in img.reshape(1, s)]~

    return img_wide[0]
