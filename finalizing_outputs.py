import pandas as pd
import numpy as np
import os

class finalizing_outputs(object):

    def __init__(self,location,amplitude,phase,volt):

        # take the location of antennas

        # take the received amplitude of signals at antennas

        # take the received phase of signals at antennas


        self.loaction = pd.DataFrame(location,columns=[
                                                    "x_antenna",
                                                    "y_antenna",
                                                    "z_antenna"])
        self.amplitude = pd.DataFrame(amplitude,columns =["amplitude_x",
                                                          "amplitude_y","amplitude_z"
                                                          ])
        self.phase = pd.DataFrame(phase
                                  ,columns = ["phase(deg)"]
                                  )
        self.voltage = pd.DataFrame(volt
                                    ,columns = ["volatge_x",
                                                "volatge_y",
                                                "volatge_z"]
                                    )
        #
        # print (self.loaction,np.shape(self.loaction),type(self.loaction))
        # print (self.amplitude,np.shape (self.amplitude),type(self.amplitude))
        # print (self.phase,np.shape (self.phase),type(self.phase))
        # print (self.voltage,np.shape (self.voltage),type(self.voltage))
        #
        # # generate a data frame
        self.data = pd.concat((self.loaction,self.amplitude,self.phase,self.voltage),axis=1)
        self.data = self.data.reset_index()\
                .rename(columns={"index":"antenna_id"})
        print(self.data)


    def write_data(self):
        '''
        print out the results as a csv file in a directory allocated for outputs
        :return:
        '''

        # The name of the output directory
        directory_name = "output"

        # check if the directory exist,
        # if not make a directory
        # if there is export the outputs into a file in that folder
        if not os.path.isdir(directory_name) :
            try:
                os.mkdir(directory_name)
            except OSError as error:
                print(error)
        else:
            self.data.to_csv(os.path.join(directory_name,"antenna.csv"),encoding="UTF8")
        # print('VOAAALAAA')
        return



