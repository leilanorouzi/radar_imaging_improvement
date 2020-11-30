import json
import os
import sys
from tkinter import Tk
from tkinter import filedialog


def select_directory():
    '''
    This function, opens a window and asks the user to choose the folder that contains the files
    :return: the path of the input data
    :rtype: str
    '''

    # You can choose the directory of the input data
    root = Tk()
    root.geometry('200x150')
    root.withdraw()

    input_dir = filedialog.askdirectory(
                                        title='Choose the directory of the data',
                                        initialdir=os.getcwd(),
                                        mustexist=True) + '/'

    # root.mainloop()
    root.destroy()

    return input_dir

def read_data_paths():
    '''

    :return: file paths of input data files
        rfn: antenna file
        sfn: source file
        filename_iono: ionosphric profile file
        filename_mag: magnetic field file
    :rtype : tuple
    '''

    # -------------------------------------------------
    # Getting input data. There are 2 ways to import the data
    # 1- You can select the data folder
    #run the function read_initial_inputs to import initial setup information
    # input_dir = select_directory()

    # 2- or you can type it in here directly.
    # If you would like to use this method please, comment above line and uncomment following line.
    # input_dir = read_initial_inputs()['input_dir']
    initial_data = read_initial_inputs ()
    input_dir = initial_data['input_dir']
    antenna_file = initial_data['antenna_file']
    source_file = initial_data['source_file']
    ionosphere_file = initial_data['ionosphere_file']
    magnetic_file = initial_data['magnetic_file']

    #join filename and the path together
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    # file name of the antenna
    rfn = os.path.join(input_dir,antenna_file)
    # file name of the source
    sfn = os.path.join(input_dir,source_file)
    # file path of ionospheric parameter
    filename_iono = os.path.join (input_dir, ionosphere_file)
    # file path of magnetic feild parameter
    filename_mag = os.path.join (input_dir,magnetic_file)

    return rfn,sfn,filename_iono,filename_mag

def read_initial_inputs()->dict:
    '''
    :return: initial setup information
    :rtype: dict
    '''
    filepath = "initial_inputs.json"
    print (filepath)
    if os.path.exists(filepath):
        f = open(filepath)
        data = json.load(f)
    else:
        print (">>>>>>\t"+filepath + ' file does not exist')
    return data


read_initial_inputs()