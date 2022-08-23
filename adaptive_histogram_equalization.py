import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

#Directory of the images to be equalized
path = os.getcwd()+"/adaptive_hist_data"
print(path)

#Directory where we save the equalized images
saving_path = os.getcwd()+"/Adaptive_Histogram_Equalization"

def compute_cdf(bins):
    
    """
    Parameters
    ----------
    bins : Bins
        Frequency of the intensity values (256 bins).

    Returns
    -------
    cdf : list
        Cumulative distribution function for the bins.

    """
    
    cdf = []
    N = sum(bins) #Total Frequency of the intensity
    # print("N: ",N)
    for a in range(0,len(bins)):
        ci = bins[:a+1]
        cdf.append(sum(ci)/N)
    # print(cdf)
    return cdf


# try:
for image in os.listdir(path):
    frame = cv2.imread(path+"/"+image)
    # print(frame.shape)
    # cv2.imshow("Frame",frame)
    
    #BLUE CHANNEL
    b_frame = frame[:,:,0]
    # plt.imshow(b_frame,cmap='gray')
    # plt.show()
    
    # Dividing the frame into 8x8 tiles
    h_tile = int(b_frame.shape[0]/8) 
    w_tile = int(b_frame.shape[1]/8)
    for h in range(h_tile,b_frame.shape[0]+1,h_tile):
        for w in range(w_tile,b_frame.shape[1]+1,w_tile):
            # print(h,w)
            b_bins = np.zeros((256,),dtype=int).tolist() #Bins
            # print(len(b_bins))
            sub_frame = b_frame[h-h_tile:h,w-w_tile:w] #Tile
            # print("Sub frame - ",h-8,h,w-8,w)
            # print(sub_frame)
            # print(sub_frame.shape)
            for i in range(0,sub_frame.shape[0]):
                for j in range(0,sub_frame.shape[1]):
                    b_bins[sub_frame[i][j]] += 1 # Generating the Bins
            # print(b_bins)
            cdf = compute_cdf(b_bins) #Computing the CDF
            # print(cdf)
            
            #Replacing the pixel values of the grid with the computed CDF
            for i in range(h-h_tile,h):
                for j in range(w-w_tile,w):
                    cdf_mult = cdf[b_frame[i][j]]
                    b_frame[i][j] = np.uint8(cdf_mult*255)
                    # sub_frame[i-h+8][j-w+8] = np.uint8(cdf_mult*255)
            # print(sub_frame)
            # time.sleep(2)
            
    # plt.imshow(b_frame,cmap='gray')
    # plt.show()
    
    # GREEN CHANNEL - Process is same as the blue channel
    g_frame = frame[:,:,1]
    for h in range(h_tile,g_frame.shape[0]+1,h_tile):
        for w in range(w_tile,g_frame.shape[1]+1,w_tile):
            g_bins = np.zeros((256,),dtype=int).tolist()
            sub_frame = g_frame[h-h_tile:h,w-w_tile:w]
            # print(sub_frame.shape)
            for i in range(0,sub_frame.shape[0]):
                for j in range(0,sub_frame.shape[1]):
                    g_bins[sub_frame[i][j]] += 1
            # print(g_bins)
            cdf = compute_cdf(g_bins)
            for i in range(h-h_tile,h):
                for j in range(w-w_tile,w):
                    cdf_mult = cdf[g_frame[i][j]]
                    g_frame[i][j] = np.uint8(cdf_mult*255)
    
    # RED CHANNEL - Process is same as the blue channel
    r_frame = frame[:,:,2]
    for h in range(h_tile,r_frame.shape[0]+1,h_tile):
        for w in range(w_tile,r_frame.shape[1]+1,w_tile):
            r_bins = np.zeros((256,),dtype=int).tolist()
            sub_frame = r_frame[h-h_tile:h,w-w_tile:w]
            # print(sub_frame.shape)
            for i in range(0,sub_frame.shape[0]):
                for j in range(0,sub_frame.shape[1]):
                    r_bins[sub_frame[i][j]] += 1
            # print(r_bins)
            cdf = compute_cdf(r_bins)
            for i in range(h-h_tile,h):
                for j in range(w-w_tile,w):
                    cdf_mult = cdf[r_frame[i][j]]
                    r_frame[i][j] = np.uint8(cdf_mult*255)
    
    #Merging the equalized blue, green and red channels
    
    result = cv2.merge((b_frame,g_frame,r_frame))
    # cv2.imshow("Frame",frame)
    # cv2.imshow("Resultant Image",result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite(saving_path+"/"+image,result) #Saving the adaptive equalized image
    # print("Success")
