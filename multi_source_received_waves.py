import warnings

warnings.filterwarnings("default", category=DeprecationWarning)

import wave_propagation as wp
from visualization import *
from initial_setup import *
from finalizing_outputs import *


def main():

    '''
    The main code to run other modules and plot the graphics.

    :return: None
    '''

    #Read input files
    files= read_data_paths()

    # -------------------------------------------------
    # makeing an instance of the class
    # w_p = wp.WavePropagation(input_dir=input_dir, source_fn=sfn, radar_fn=rfn, dipole= True)
    w_p = wp.WavePropagation(files,dipole= True)

    #-------------------------------------------------
    # Visualization
    # Plotting the antennas and source/s location

    # Calling the visualization calss
    vis = visualization(a=w_p.antenna_location, s=w_p.source_location)
    # To obtain the location of the antenna and source and plot them
    print("\x1b[1;31m Please check the plot window.\x1b[0m\n")
    vis.source_antenna_location()

    # -------------------------------------------------
    # Calculations

    # To obtain waves at the antenna
    # run antenna_wave_received function to calculate the wave results as a data frame for all sources and antennas
    w = w_p.antennna_wave_received()
    # To obtain the total result for each antenna, call the vector_superposition function.
    # It calculate received waves from all sources for each antenna in the original reference frame
    # and add their components up.
    waves = w_p.vector_superposition(w)
    # print('\x1b[1;31mReceived waves from each source at the antenna locations:\x1b[0m \n', waves)

    # To obtain the phase difference at the antenna call phase_diff function.
    phase_difference = w_p.phase_diff()
    print('\nPhase difference in degree:\n', np.degrees(phase_difference).round(3))
    print("\x1b[1;31m===============================================================================\n\n\x1b[0m")

    # To obtain the voltage call voltage function
    voltage = w_p.voltage(waves)



    fo = finalizing_outputs(location=w_p.antenna_location,
                            amplitude=waves,
                            phase=phase_difference,
                            volt=voltage)
    fo.write_data()




    print('FINISHED')

    pass

if __name__ == '__main__':
    main()
