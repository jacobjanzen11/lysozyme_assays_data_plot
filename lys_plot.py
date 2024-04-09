##############################################################
#
# Program: Plot the absorbance of purified lysoyme samples
#          from assays of different concentrations.
# Course: Biochemistry Lab
# Author: Jacob Janzen
# Last Updated: 4/9/24
#
##############################################################

import os
import pandas as pd
import matplotlib.pyplot as plt


# Directory containing CSV files
directory = 'JJJL_assays'

# Get list of CSV files in the directory
csv_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.csv')]

for csv_file in csv_files:
    try:
        # Load CSV data into pandas dataframe
        data = pd.read_csv(csv_file)
        
        # Plot the data
        plt.plot(data['Latest: Time (s)'], data['Latest: Absorbance at 450.2 nm'], label=os.path.basename(csv_file))
    except Exception as e:
        print(f"Error loading data from {csv_file}: {e}")

# Add labels, legend, grid, and customize plot appearance
plt.xlabel('Time (s)')
plt.ylabel('Absorbance at 450.2 nm')
plt.title('Lysozyme Purification Assays')
plt.legend() # generates and displays legend based on .csv file names
plt.grid(True) # shows gridlines
plt.tight_layout() # prevents overlap of numbers and labels

# Show the plot
plt.show()
