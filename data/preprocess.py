# 3rd party modules
import pandas as pd

def open_input_file(file_name):  
  print("Hello Julio")
  
  # Load csv
  print("Loading data...\n")
  ori_data = pd.read_csv(file_name)
  
  return ori_data


def showing_missing_values(v_original_data):
  print("Detecting missing values...\n")


def showing_shape_of_data(v_original_data):
  data_shape = v_original_data.shape
  print(f"Original shape of Sensors data_frame: {data_shape} /n")


def showing_head_of_data(v_original_data):
  print("Showing first rows of table: \n")
  print(v_original_data.head())

def show_original_data_features(v_original_data):
  print("Showing some features of the original sensors data \n")

  showing_shape_of_data(v_original_data)

  showing_head_of_data(v_original_data)

  showing_missing_values(v_original_data)
  


#########################
# Load and preprocess data for model
#########################

file_name = "TimeGAN/data/NO2_sequence_five_sensors.csv"
original_df = open_input_file(file_name)

show_original_data_features(original_df)

print(type(original_df))


