#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:57:38 2019

@author: ashubunutu
"""

import cv2
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from skimage.measure import compare_ssim
from scipy import sparse




 
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

 
source=cv2.VideoCapture('test.mp4')
ret=get_frame(source)


trans=cv2.VideoCapture('source.mp4')
trans_ret=get_frame(trans)


trans_ret_single=trans_ret[54]
source_frame=ret[54]




for i in range(0,len(trans_ret_single)):
    dest_mat=np.array(trans_ret_single[i])
    source_mat=np.array(source_frame[i])
    
    
a=compare_ssim(source_mat,dest_mat,multichannel=True)
#a_sparse, b_sparse = sparse.csr_matrix(source_mat), sparse.csr_matrix(dest_mat)
#
#sim_sparse = cosine_similarity(a_sparse, b_sparse, dense_output=False)
#print(sim_sparse)
