import pandas as pd
import scipy.io
from scipy.signal import find_peaks
from pathlib import Path
import matplotlib.pyplot as plt
import os
from processing import list_indexes, list_subsections, get_average, get_variable

if __name__=='__main__':

    # Define the list of variables to extract
    var_list = ['ne0','te0','taue','betap']
    # Run through the variables first
    for var in var_list:
        print(f"Running variable: {var}")
        # Reinitiate an empty rows list to serve as CSV output for new variable
        rows = []
        # Directory for .mat files
        dir_path  = "./mats/nbi_only" # Set this up!
        # Loop though all the .mat files in directory
        for file in os.listdir(dir_path):
            print(f"Running processing for {file}")
            full_dataset = scipy.io.loadmat(f"{os.path.join(dir_path,file)}")

            # list_subsections(full_dataset) # Uncomment to list subsections for matrix
            # list_indexes(full_dataset) # Uncomment to list indexes for matrix
            # Assign
            y = get_variable(var, full_dataset)
            # Below is code to automate the find the peak plateau
            # Not necessary for this since the 50->100 range will suffice for all
            # x= [float(i) for i in list(range(1,len(y)+1))]
            # peaks, plateaus = find_peaks(y, plateau_size=1)
            # print(plateaus['left_edges'][1])
            # print(plateaus['right_edges'][-2])
            # Get average and standard deviation insert into row with file name
            avg, std = get_average(50, 100, var, full_dataset)
            row = [file, avg, std]
            rows.append(row)
            # plt.plot(y) # Uncomment to get plots
            # plt.show() # Uncomment to get plots
        # Output CSVs
        df = pd.DataFrame(rows)
        output_filepath = f"./outputs/{var}_values.csv" # Set this up!
        df.to_csv(output_filepath, header=False, index=False)
