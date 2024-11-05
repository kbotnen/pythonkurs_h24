#!/usr/bin/env python
# coding: utf-8

# ## Oppgave
# 
# 0: Opprett et nytt kodeprosjekt / fil.
# 
# 1: Finn et egnet bilde og se om du greier å detektere andre features, f.eks munn / øyner.
# 
# NB! Dere finner flere trente haarcascade set her [https://github.com/opencv/opencv/tree/master/data/haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)

# ## Løsningsforslag

# In[ ]:


import cv2
from matplotlib import pyplot as plt

# Create the haar cascade
catcascPath = "../data/image_video/haarcascade_frontalcatface_extended.xml" # Just an xml file that contains data about a catface.
catfaceCascade = cv2.CascadeClassifier(catcascPath) # Load the cascade into memory.


# In[ ]:


# Due to jupyters architecture we can not use cv2.imshow() so we create a helper method to utilize pyplot.
def show_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.show()


# In[ ]:


cat_face_image = cv2.imread("../data/image_video/cat3.jpg") # cv2 read in BGR format.
cat_gray_image_face = cv2.cvtColor(cat_face_image, cv2.COLOR_BGR2GRAY)

catfaces = catfaceCascade.detectMultiScale(
    cat_gray_image_face,
    scaleFactor=1.1,
    minNeighbors=5,
    flags = cv2.CASCADE_SCALE_IMAGE
)

# Iterate the list of faces and draw a rectangle around the faces.
for (x, y, w, h) in catfaces:
    cv2.rectangle(cat_face_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
show_image(cv2.cvtColor(cat_face_image, cv2.COLOR_BGR2RGB), "Number of catfaces found = %s" % len(catfaces))


# In[ ]:




