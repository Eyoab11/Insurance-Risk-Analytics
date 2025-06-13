# scripts/convert_to_csv.py

import pandas as pd
import os

# --- CONFIGURATION ---
# 1. FIND your raw data file in the 'data' folder.
# 2. REPLACE the placeholder below with the real filename.
RAW_DATA_FILENAME = "MachineLearningRating_v3.txt" # <-- CHANGE THIS if your filename is different!
# ---------------------

# Construct the full paths based on the project structure
# This assumes you run the script from the project's root folder.
input_txt_path = os.path.join('data', RAW_DATA_FILENAME)
output_csv_path = os.path.join('data', 'insurance_data.csv') # We will name the output file this

def convert_txt_to_csv(txt_path, csv_path):
    """
    Reads a pipe-delimited TXT file and converts it to a CSV file.
    
    Args:
        txt_path (str): The path to the input TXT file.
        csv_path (str): The path to the output CSV file.
    """
    try:
        print(f"Attempting to read data from: {txt_path}")
        
        # Check if the file actually exists before trying to read it
        if not os.path.exists(txt_path):
            print(f"--- ERROR ---")
            print(f"The file '{RAW_DATA_FILENAME}' was not found in the 'data' directory.")
            print("Please check the following:")
            print("1. Is the file located inside the 'data' folder?")
            print("2. Is the 'RAW_DATA_FILENAME' variable in the script set to the correct name?")
            print(f"-----------------")
            return

        # Read the file using pandas. The key is the 'sep' parameter.
        # Change '|' to your actual delimiter if it's different (e.g., ';', '\t')
        df = pd.read_csv(txt_path, sep='|', low_memory=False)
        
        print("Data read successfully. Converting to CSV...")
        
        # Save the DataFrame to a CSV file.
        # index=False prevents pandas from writing row indices into the file.
        df.to_csv(csv_path, index=False)
        
        print(f"Successfully converted file and saved to: {csv_path}")
        print(f"New CSV file has {df.shape[0]} rows and {df.shape[1]} columns.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    convert_txt_to_csv(input_txt_path, output_csv_path)