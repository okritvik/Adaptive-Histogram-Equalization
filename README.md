# Adaptive-Histogram-Equalization
Part of the Second Project - ENPM 673 - Perception for Autonomous Robots

## Required Libraries:  
* OpenCV : Version 4.1
* NumPy
* Matplotlib
* OS
* Time

## Pipeline: 
<p align="center">
  <img src="https://user-images.githubusercontent.com/40200916/186265906-1c5bf523-fdc6-456c-8999-5396011ee366.png" width="100%">
</p>

## Given Dataset and Result:
Image   |  Result |
:-------------------------:|:-------------------------:
<img src= "https://user-images.githubusercontent.com/40200916/186530588-48357407-4fee-4597-9bc8-c0f7d19eb6de.png"> | <img src="https://user-images.githubusercontent.com/40200916/186530638-52a9137c-0f6c-4bad-87a0-352571140a4c.png" width="100%"> 
## Running the Code:
The working directory should have adaptive_hist_data and Adaptive_Histogram_Equalization folders along with the code.

**Format/Syntax:**  
		```python3 adaptive_histogram_equalization.py```

## Exiting From the Code:

1. Press any key after the visualization is done. Make sure that the image window is selected while giving any key as an input.

2. You can always use ctrl+c to exit from the program.

### Note:
The resultant image is not interpolated. Hence, the grid lines are visible in the equalized image.
Make sure that the directory tree is maintained.
Uncomment some of the lines in the code to vizualize each image.
adaptive_hist_data folder has the image dataset for processing
Adaptive_Histogram_Equalization folder has the resultant images after executing the pipeline.
