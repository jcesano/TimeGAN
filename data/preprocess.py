# 3rd party modules
import pandas as pd
import numpy as np

def open_input_file(file_name):  
  print("Hello Julio")
  
  # Load csv
  print("Loading data...\n")
  ori_data = pd.read_csv(file_name)
  
  return ori_data


def showing_missing_values(v_original_data):
  print("Detecting missing values...\n")
  print("Checking if there is any missing value in our dataset \n")
  print(v_original_data.isnull().any())
  print("\n Total missing values for each feature: \n")
  print(v_original_data.isnull().sum())
  print("\n Checking if we have any negative values in the dataset \n")
  # select the float columns
  df_num = v_original_data.select_dtypes(include=[np.float64])
  print(df_num.head())

  print('Negatives Found: \n')
  print(df_num.where(df_num < 0).count())

  print('Zeros Found: \n')  
  print(df_num.where(df_num == 0).count())

  # select non-numeric columns
  #df_num = v_original_data.select_dtypes(exclude=[np.number])
  
  #print((v_original_data < 1).count())
  #print('Negatives Found:')
  #print(v_original_data.where(v_original_data < 0).count())
  #print('Zeros Found:')
  #print(v_original_data.where(v_original_data == 0).count())



def showing_shape_of_data(v_original_data):
  data_shape = v_original_data.shape
  print(f"Original shape of Sensors data_frame: {data_shape} \n")


def showing_head_of_data(v_original_data):
  print("Showing first rows of table: \n")
  print(v_original_data.head())

def showing_datatypes_of_data(v_original_data):
  print("Showing types of each column of dataframe: \n")
  print(v_original_data.dtypes)

def show_original_data_features(v_original_data):
  print("Showing some features of the original sensors data \n")

  showing_shape_of_data(v_original_data)

  showing_datatypes_of_data(v_original_data)

  showing_head_of_data(v_original_data)

  showing_missing_values(v_original_data)
  


#########################
# Load and preprocess data for model
#########################

file_name = "TimeGAN/data/NO2_sequence_five_sensors.csv"
original_df = open_input_file(file_name)

show_original_data_features(original_df)

print(type(original_df))


