#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:57:38 2019

@author: ashubunutu
"""

import cv2
import numpy as np

from skimage import data, img_as_float
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
#from skimage.metrics import structural_similarity as ssim  for skimage version .0.16



 
def get_frame(cap):
    dict={} 
    index=0;
 
        # Check if camera opened successfully
    if (cap.isOpened()== False): 
       print("Error opening video stream or file")
 
# Read until video is completed
    while(cap.isOpened()):
    
  # Capture frame-by-frame
      ret, frame = cap.read()
      if ret == True:
         
#          grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
           
          dict[index]=frame
          index+=1
 
  # Break the loop
      else: 
          cap.release()
          return dict

 
    
def get_similarity_index(source,transmitted):
    loss_dic={}
    print(len(transmitted),len(source))
    if len(transmitted)<len(source):
        
        for key,value in transmitted.items():
            transmitted_frame=transmitted[key]
            if key in source:
               # print('Key exits')
                similarity=ssim(source[key],transmitted_frame,multichannel=True)
                frame_loss=1-similarity
                loss_dic[key]=np.floor(frame_loss*100)
    return loss_dic
                

    
    
source_cap=cv2.VideoCapture('test.mp4')
source=get_frame(source_cap)


trans_cap=cv2.VideoCapture('1_11.mp4')
received=get_frame(trans_cap)


similar=get_similarity_index(source,received)

x,y=zip(*(similar.items()))
plt.bar(x,y)
plt.xlabel('Frame No')
plt.ylabel('Percentaeg')

overall_loss=((len(source)-len(received))/len(source)*100)

print('Overall Loss at a recv level '+str(overall_loss))



#a_sparse, b_sparse = sparse.csr_matrix(source_mat), sparse.csr_matrix(dest_mat)
#
#sim_sparse = cosine_similarity(a_sparse, b_sparse, dense_output=False)
#print(sim_sparse)
