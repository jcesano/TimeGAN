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
def complete_col_NaN_values_with_last_valid_value(df_in, column_name):
  print("Completing NaN values in column: ",column_name, "\n")

  col_length = len(df_in[column_name])
  last_value = df_in.loc[0, column_name]
  affected_values = 0
  for i in range(1, col_length):
    if np.isnan(df_in.loc[i, column_name]):
      df_in.loc[i, column_name] = last_value
      affected_values += 1
    else:
      last_value = df_in.loc[i, column_name]
  
  print("Total rows affected in column ", column_name," is:", affected_values, "\n")

def complete_NaN_values_with_last_valid_value(df_in):
  print("Completing NaN values with the last valid value of the same NaN's column \n")

  complete_col_NaN_values_with_last_valid_value(df_in, "S008")

  complete_col_NaN_values_with_last_valid_value(df_in, "S035")

  complete_col_NaN_values_with_last_valid_value(df_in, "S038")

  complete_col_NaN_values_with_last_valid_value(df_in, "S048")

  complete_col_NaN_values_with_last_valid_value(df_in, "S050")

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
  
  showing_shape_of_data(v_original_data)

  showing_datatypes_of_data(v_original_data)

  showing_head_of_data(v_original_data)

  showing_missing_values(v_original_data)

  # select the float columns
  df_num = v_original_data.select_dtypes(include=[np.float64])
  
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

print("Showing some features of the sensors data \n")
show_data_features(original_df)

transforming_negative_values_in_NaN(original_df)

print("Showing some features of the sensors data after transformation of negative values \n")
show_data_features(original_df)

complete_NaN_values_with_last_valid_value(original_df)

print("Showing some features of the sensors data after transformation of NaN values \n")
show_data_features(original_df)

grouped_df = grouping_by_date(original_df)

print("showing the first rows of the grouped dataset \n")
print(grouped_df.head())

print("Detecting gaps in DateTime column... \n")
print(grouped_df.columns)

begin_date = grouped_df.index.min()
end_date =  grouped_df.index.max()
print("The begin datetime of data is:", begin_date, "\n")
print("The end datetime of data is:", end_date, "\n")


full_range = pd.date_range(start=begin_date, end=end_date, freq='H')

print("Full range begining is: \n")

print(full_range[:10], "\n")

full_range_len = len(full_range)
print("The full range has the number of ", full_range_len, " entries \n")

grouped_df_len = len(grouped_df)
print("The number of entries in grouped_df is: ", grouped_df_len, "\n")

print("So we have ", grouped_df_len - full_range_len, "entries that are missing to complete full date range \n")

print("The missing entries are the following: \n")

print(type(grouped_df))
grouped_df_datetime = pd.to_datetime(grouped_df.index)

print(full_range.difference(grouped_df_datetime))
