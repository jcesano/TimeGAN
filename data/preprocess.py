# 3rd party modules
import pandas as pd
import numpy as np

def reset_index_in_df(df_in):
  
  df_in = df_in.reset_index().rename(columns={'index': 'DATETIME'})  
  return df_in

def set_index_in_df(df_in):
  df_in = df_in.set_index("DATETIME")
  df_in.index = pd.to_datetime(df_in.index)
  return df_in

def showing_missing_values_in_grouped_data(grouped_df):
  print("Showing missing values (NaN values) in grouped data.\n")  
  showing_missing_values(grouped_df)

def transforming_gaps_into_NaN_values(grouped_df, full_range):
  print("Transforming gaps into NaN values\n")
  grouped_df = grouped_df.reindex(full_range) 

  print("Showing new length of group_df:", len(grouped_df),"\n")
  
  return grouped_df

def detecting_gaps_in_grouped_data(grouped_df):
  print("Detecting gaps in DateTime column... \n")
  
  begin_date = grouped_df.index.min()
  end_date =  grouped_df.index.max()
  print("The begin date is:", begin_date, "\n")
  print("The end date is:", end_date, "\n")


  full_range = pd.date_range(start=begin_date, end=end_date, freq='H')

  print("Full range begining is:\n")

  print(full_range[:10], "\n")

  full_range_len = len(full_range)
  print("The full range has", full_range_len, "entries \n")

  grouped_df_len = len(grouped_df)
  print("The number of entries in grouped_df is:", grouped_df_len, "\n")

  print("So we have", full_range_len - grouped_df_len, "entries that are missing to complete full date range \n")

  print("The missing entries are the following: \n")

  grouped_df_datetime = grouped_df.index

  print(full_range.difference(grouped_df_datetime))
  print("\n")

  return full_range

def grouping_by_date(original_df):

  print("Grouping the dataset by DATETIME in order to have a unique datetime as key of the dataframe \n")
  
  group_df = original_df.groupby('DATETIME').agg(    
          Mean_S008=('S008', "mean"),    # Mean of sensor 008
          Mean_S035=('S035', "mean"),    # Mean of sensor 035
          Mean_S038=('S038', "mean"),    # Mean of sensor 038
          Mean_S048=('S048', "mean"),    # Mean of sensor 048
          Mean_S050=('S050', "mean"),    # Mean of sensor 050
          RecCount =('DATETIME', "count")   # get the count of networks                    
        )
  
  # This line is needed to allow reindexing to a new range in the future
  group_df.index = pd.to_datetime(group_df.index)

  return group_df
        
def group_data_by_date(original_df):
  
  grouped_df = grouping_by_date(original_df)

  print("New columns of grouped data are: \n")
  print(grouped_df.columns)

  print("\nShowing the first rows of the grouped dataset \n")
  print(grouped_df.head())
  
  return grouped_df 

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
  return df_in

def complete_NaN_values_with_last_valid_value2(df_in):
  print("Completing NaN values with the last valid value of the same NaN's column \n")

  df_in = reset_index_in_df(df_in)

  complete_col_NaN_values_with_last_valid_value(df_in, "Mean_S008")

  complete_col_NaN_values_with_last_valid_value(df_in, "Mean_S035")

  complete_col_NaN_values_with_last_valid_value(df_in, "Mean_S038")

  complete_col_NaN_values_with_last_valid_value(df_in, "Mean_S048")

  complete_col_NaN_values_with_last_valid_value(df_in, "Mean_S050")

  complete_col_NaN_values_with_last_valid_value(df_in, "RecCount")
 
  df_in = set_index_in_df(df_in)
  
  return df_in

def complete_NaN_values_with_last_valid_value(df_in):
  print("Completing NaN values with the last valid value of the same NaN's column \n")

  complete_col_NaN_values_with_last_valid_value(df_in, "S008")

  complete_col_NaN_values_with_last_valid_value(df_in, "S035")

  complete_col_NaN_values_with_last_valid_value(df_in, "S038")

  complete_col_NaN_values_with_last_valid_value(df_in, "S048")

  complete_col_NaN_values_with_last_valid_value(df_in, "S050")

def transform_column_negative_into_NaN(df_in, column_name):
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



def transforming_negative_values_into_NaN(df_in):
  # Detecting negative numbers and turning them into NaN values
  print("Transforming in each column, each negative value into a NaN value \n")

  transform_column_negative_into_NaN(df_in, 'S008')

  transform_column_negative_into_NaN(df_in, 'S035')

  transform_column_negative_into_NaN(df_in, 'S038')

  transform_column_negative_into_NaN(df_in, 'S048')

  transform_column_negative_into_NaN(df_in, 'S050')


def showing_negative_values(df_num):
  print('Negatives Found: \n')
  print(df_num.where(df_num < 0).count())
  print("\n")

def showing_zeros_values(df_num):
  print('Zeros Found: \n')
  print(df_num.where(df_num == 0).count())
  print("\n")

def showing_negative_zero_values(v_original_data):
  print("Checking if we have any negative or zero values in the dataset.\n")
  # select the float columns
  df_num = v_original_data.select_dtypes(include=[np.float64])
  
  showing_negative_values(df_num)
  showing_zeros_values(df_num)

def showing_missing_values(v_current_data):
  print("Detecting missing values...\n")
  print("Checking if there is any missing value in our dataset.\n")
  print(v_current_data.isnull().any())
  print("\nTotal missing values for each feature: \n")
  print(v_current_data.isnull().sum())
  print("\n")
  
def showing_shape_of_data(v_original_data):
  data_shape = v_original_data.shape
  print(f"Shape of Sensors data_frame: {data_shape}. \n")


def showing_head_of_data(v_original_data):
  print("Showing first rows of dataframe: \n")
  print(v_original_data.head())
  print("\n")

def showing_datatypes_of_data(v_original_data):
  print("Showing types of each column of dataframe: \n")
  print(v_original_data.dtypes)
  print("\n")

def show_data_features(v_original_data):
  
  showing_shape_of_data(v_original_data)

  showing_datatypes_of_data(v_original_data)

  showing_head_of_data(v_original_data)

  showing_missing_values(v_original_data)

  showing_negative_zero_values(v_original_data)
  
  

def open_input_file(file_name):  
  # Load csv
  print("Loading data...\n")
  ori_data = pd.read_csv(file_name)
  
  return ori_data


def preprocess_data_cleaning():

  file_name = "TimeGAN/data/NO2_sequence_five_sensors.csv"
  original_df = open_input_file(file_name)

  print("Showing some characteristics of the sensors data. \n")
  show_data_features(original_df)

  transforming_negative_values_into_NaN(original_df)

  print("Showing the same characteristics after transformation of negative values into NaN values\n")
  show_data_features(original_df)

  complete_NaN_values_with_last_valid_value(original_df)

  print("Showing the same characteristics of the sensors data after transformation of NaN values \n")
  show_data_features(original_df)

  grouped_df = group_data_by_date(original_df)

  full_range = detecting_gaps_in_grouped_data(grouped_df)

  grouped_df = transforming_gaps_into_NaN_values(grouped_df, full_range)

  showing_missing_values_in_grouped_data(grouped_df)

  grouped_df = complete_NaN_values_with_last_valid_value2(grouped_df)
  
  grouped_df = reset_index_in_df(grouped_df)

  showing_missing_values_in_grouped_data(grouped_df)
    
  return grouped_df

def preprocess_formatting_for_model():
  group_df = preprocess_data_cleaning()

  datetime_v = group_df['DATETIME']

  date_v = pd.to_datetime(datetime_v)

  print("type of date_v:", type(date_v), '\n')



  date_year_v = date_v.dt.year
  print("type of date_year_v:", type(date_year_v), '\n')

  
  date_month_v = date_v.dt.month
  print("type of date_month_v:", type(date_month_v), '\n')

  date_day_v = date_v.dt.day
  print("type of date_day_v:", type(date_day_v), '\n')


  date_year_f = date_year_v.to_frame()
  print("type of date_year_f:", type(date_year_f), '\n')

  date_month_f = date_month_v.to_frame()
  print("type of date_month_f:", type(date_month_f), '\n')

  date_day_f = date_day_v.to_frame()
  print("type of date_day_f:", type(date_day_f), '\n')
  

  date_year_str = date_year_f['DATETIME'].astype(str)
  print("type of date_year_str:", type(date_year_str), '\n')

  date_month_str = date_month_f['DATETIME'].astype(str)
  print("type of date_month_str:", type(date_month_str), '\n')

  date_month_str = date_month_str.to_frame()
  print("type of date_month_str.to_frame():", type(date_month_str), '\n')

  date_month_str = date_month_str.astype({"DATETIME": str})
  print("Muestro dtypes luego aplicar astype({}) \n")
  print(date_month_str.dtypes)
  print("\n")

  date_month_str["DATETIME"] = date_month_str["DATETIME"].apply(lambda x: x.zfill(2))
  # df['ID'] = df['ID'].apply(lambda x: x.zfill(15))
  #date_month_str = date_month_str.apply(lambda x: x.zfill(2))

  print(type(date_month_str))

  print(date_month_str.head())


  

#########################
# Load and preprocess data for model
#########################


preprocess_formatting_for_model()
