

import numpy as np 
from palette import *
from rainbow import * 

class LeptonDataConverter:
    dataIsSet = False
    def __init__(self , RawDataMatrix) :
        self.rawdata = RawDataMatrix 
        self.dataIsSet = True
        self.conversion_palette =  fusion_palette_map 

    def __init__(self) :
        self.conversion_palette =  fusion_palette_map 
        

    def setRawData(self , RawDataMatrix) :
        self.dataIsSet = True
        self.rawdata = RawDataMatrix

    def __adjustRawData(self) :

        self.adjustedData = self.rawdata.copy()
        #Calculate min and max values  
        minval = self.adjustedData.min() 
        maxval = self.adjustedData.max() 
        #scalling 
        for i in range(0 , self.adjustedData.shape[0]) :
            for j in range(0 , self.adjustedData.shape[1]) :
                self.adjustedData[i][j] = self.adjustedData[i][j] - minval 
        return self.adjustedData


    #this function return a gray image
    def __scaleData(self ):
        self.scaledData =  np.ones(self.rawdata.shape ,dtype = np.uint8)
       
        diff        =  self.adjustedData.max() - self.adjustedData.min()
       
        scaleFactor =  255 / diff 

        for i in range(0 ,self.scaledData.shape[0] ) :
            for j in range(0 ,self.scaledData.shape[1] ) :
                self.scaledData[i][j] = (self.adjustedData[i][j]) * scaleFactor 
                

        return self.scaledData


    #this function return rgb image 
    def __grayToRGB(self) :
        rgb_image = np.ones( (self.scaledData.shape[0] ,self.scaledData.shape[1] , 3 ) ,dtype=np.uint8)
	
        for i in range(0 ,self.scaledData.shape[0]):
            for j in range(0 ,self.scaledData.shape[1]) :
                rgb_image[i][j] = self.conversion_palette[self.scaledData[i][j]]
                #rgb_image[i][j] =  rainbow_palette_map[self.scaledData[i][j]]
        return rgb_image 

    
#public function        

    def getRGBImage(self):
        if self.dataIsSet == False :
            print("Please set the data to be convert using setRawData() method")
            return None
        else :
            self.__adjustRawData()
            self.__scaleData()
            return self.__grayToRGB()

    def getGrayImage(self):
        if self.dataIsSet == False :
            print("Please set the data to be convert using setRawData() method")
            return None
        else :
            self.__adjustRawData()
            return self.__scaleData()

    def getJsonKelvin(self) :

        if self.dataIsSet == False :
            print("Please set the data to be convert using setRawData() method")
            return None
        else :
            self.kelvin = self.rawdata / 100

            self.kelvin = self.kelvin.tolist()

            myjson = {
                "thermal_image" : self.kelvin
            }

            return myjson

