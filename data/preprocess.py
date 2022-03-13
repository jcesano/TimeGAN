# 3rd party modules
import pandas as pd
import numpy as np

def grouping_by_date(original_df):

  return original_df.groupby('DATETIME').agg(
          Mean_S008=('S008', "mean"),    # Mean of sensor 008
          Mean_S035=('S035', "mean"),    # Mean of sensor 035
          Mean_S038=('S038', "mean"),    # Mean of sensor 038
          Mean_S048=('S048', "mean"),    # Mean of sensor 048
          Mean_S050=('S050', "mean"),    # Mean of sensor 050
          RecCount =('DATETIME', "count")   # get the count of networks            
        
        )

def complete_NaN_values_with_previous_valid_value(df_in):

def transform_column_negative_in_NaN(df_in, column_name):
  # Detecting negative numbers and turning them into NaN values
  print("Transforming column: ", column_name)
  cnt=0
  affected_values = 0
  for row in df_in[column_name]:        
    value = df_in.loc[cnt, column_name]
    if(value <= 0):      
      df_in.loc[cnt, column_name]=np.nan
      affected_values += 1 
    cnt+=1

  print("Values affected in column ", column_name, " :", affected_values, "\n")



def transforming_negative_values_in_NaN(df_in):
  # Detecting negative numbers and turning them into NaN values
  print("Transforming in each column, each negative value into a NaN value \n")

  transform_column_negative_in_NaN(df_in, 'S008')

  transform_column_negative_in_NaN(df_in, 'S035')

  transform_column_negative_in_NaN(df_in, 'S038')

  transform_column_negative_in_NaN(df_in, 'S048')

  transform_column_negative_in_NaN(df_in, 'S050')


def showing_negative_values(df_num):
  print('Negatives Found: \n')
  print(df_num.where(df_num < 0).count())

def showing_zeros_values(df_num):
  print('Zeros Found: \n')
  print(df_num.where(df_num == 0).count())

def showing_missing_values(v_original_data):
  print("Detecting missing values...\n")
  print("Checking if there is any missing value in our dataset \n")
  print(v_original_data.isnull().any())
  print("\n Total missing values for each feature: \n")
  print(v_original_data.isnull().sum())
  print("\n Checking if we have any negative values in the dataset \n")
  
def showing_shape_of_data(v_original_data):
  data_shape = v_original_data.shape
  print(f"Original shape of Sensors data_frame: {data_shape} \n")


def showing_head_of_data(v_original_data):
  print("Showing first rows of table: \n")
  print(v_original_data.head())

def showing_datatypes_of_data(v_original_data):
  print("Showing types of each column of dataframe: \n")
  print(v_original_data.dtypes)

def show_data_features(v_original_data):
  print("Showing some features of the original sensors data \n")

  showing_shape_of_data(v_original_data)

  showing_datatypes_of_data(v_original_data)

  showing_head_of_data(v_original_data)

  showing_missing_values(v_original_data)

  # select the float columns
  df_num = v_original_data.select_dtypes(include=[np.float64])
  print(df_num.head())

  showing_negative_values(df_num)
  showing_zeros_values(df_num)

  
  

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

show_data_features(original_df)

transforming_negative_values_in_NaN(original_df)

show_data_features(original_df)

complete_NaN_values_with_previous_valid_value(original_df)

# grouped_df = grouping_by_date(original_df)

# print(grouped_df.head())


# print(type(original_df))


