# 3rd party modules
import pandas as pd

def open_input_file(file_name):  
  print("Hello Julio")
  
  # Load csv
  print("Loading data...\n")
  ori_data = pd.read_csv(file_name)
  
  return ori_data


  


#########################
# Load and preprocess data for model
#########################

file_name = "TimeGAN/data/NO2_sequence_five_sensors.csv"
original_df = open_input_file(file_name)

print(type(original_df))


