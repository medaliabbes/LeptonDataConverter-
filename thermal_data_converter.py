

import argparse
import os
import cv2 
import json
import glob
import numpy as np 
from  LeptonDataConverter import * 

FRAME_RATE = 8 

def main():
    parser = argparse.ArgumentParser(description='Program to list files in a directory and save to a file')
    parser.add_argument('-f', '--folder', type=str, default='data', help='the folder name to list files from')
    parser.add_argument('-out', '--output', type=str, default='output', help='the name of the output file')
    args = parser.parse_args()

    # Check if the input folder exists
    if not os.path.isdir(args.folder):
        print(f"Error: '{args.folder}' is not a valid directory")
        return
	#Check if the folder contains files 
    file_list = glob.glob(args.folder+'/*.json')
    if(len(file_list) == 0) :
        print("No Files to be converted")
        return 
		
    converter = LeptonDataConverter() 
    
    frameSize = (320, 320)
	
    encoder = cv2.VideoWriter(args.output + '.mp4',cv2.VideoWriter_fourcc(*'DIVX'),FRAME_RATE, frameSize)
	
    for file_name in file_list :

        f = open(file_name)
		
        json_data = json.load(f)
		
        raw_data  = json_data['data']
		
        converter.setRawData(np.array(raw_data))
		
        frame     = converter.getRGBImage()

        frame     = cv2.resize(frame ,((320, 320 )))

        encoder.write(frame)
		
        f.close()

   
if __name__ == '__main__':
    main()