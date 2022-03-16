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

#########################
# Load and preprocess data for model
#########################
def preprocess_formatting_for_model():
  group_df = preprocess_data_cleaning()

  print(" 1- Checking the type and content of group_df['DATETIME'] \n")
  datetime_s = group_df['DATETIME']
  print("type of date_v:", type(datetime_s), '\n')
  print("types of columns",datetime_s.dtypes, "\n")
  # It is a series of datetime values 

  print("2- Extracting the day, month and year from datetime_v using dt series's method. \n")
  datetime_day_s = datetime_s.dt.day
  print("type of datetime_day_s:", type(datetime_day_s), '\n')
  print("type of content of datetime_day_s", datetime_day_s.dtypes)
  # Result is a Series of days (values of type integer).

  datetime_month_s = datetime_s.dt.month
  print("type of datetime_month_s:", type(datetime_month_s), '\n')
  print("type of content of datetime_month_s", datetime_month_s.dtypes)
  # Result is a Series of months (values of type integer).

  datetime_year_s = datetime_s.dt.year
  print("type of datetime_year_s:", type(datetime_year_s), '\n')
  print("type of content of datetime_year_s", datetime_year_s.dtypes)
  # Result is a Series of years (values of type integer).

  print("3- Converting the structures into a Dataframe to use methods astype() and apply() with lambda expressions \n")
  #import pandas as pd

  datetime_day_f = datetime_day_s.to_frame()
  print("type of datetime_day_f:", type(datetime_day_f), '\n')
  print("type of content of datetime_day_f", datetime_day_f.dtypes)
  # Result is a Dataframe containing a vector of integer values.

  datetime_month_f = datetime_month_s.to_frame()
  print("type of datetime_month_f:", type(datetime_month_f), '\n')
  print("type of content of datetime_month_f", datetime_month_f.dtypes)
  # Result is a Dataframe containing a vector of integer values.

  datetime_year_f = datetime_year_s.to_frame()
  print("type of datetime_year_f:", type(datetime_year_f), '\n')
  print("type of content of datetime_month_f", datetime_year_f.dtypes)
  # Result is a Dataframe containing a vector of integer values.

  print("4- Converting content of Dataframes from int to string \n")
  datetime_day_f_str = datetime_day_f.astype({"DATETIME":"str"})
  print("type of datetime_day_f_str:", type(datetime_day_f_str), '\n')
  print("type of content of datetime_day_f_str", datetime_day_f_str.dtypes)
  # Result is a Dataframe containing string values

  datetime_month_f_str = datetime_month_f.astype({"DATETIME":"str"})
  print("type of datetime_month_f_str:", type(datetime_month_f_str), '\n')
  print("type of content of datetime_month_f_str", datetime_month_f_str.dtypes)
  # Result is a Dataframe containing string values

  datetime_year_f_str = datetime_year_f.astype({"DATETIME":"str"})
  print("type of datetime_year_f_str:", type(datetime_year_f_str), '\n')
  print("type of content of datetime_year_f_str", datetime_year_f_str.dtypes)
  # Result is a Dataframe containing integers as string values

  print("5- Converting string numbers of length 1 into length 2 (for days and months only) putting a 0 in front \n")
  datetime_day_f_str["DATETIME"] = datetime_day_f_str["DATETIME"].apply(lambda x: x.zfill(2))
  print("type of datetime_day_f_str:", type(datetime_day_f_str), '\n')
  print("type of content of datetime_day_f_str", datetime_day_f_str.dtypes)
  print("Showing head of dataset datetime_day_f_str \n")
  print(datetime_day_f_str.head())
  # Result is a Dataframe containing numbers as string values with a "0" in front one digit numbers

  datetime_month_f_str["DATETIME"] = datetime_month_f_str["DATETIME"].apply(lambda x: x.zfill(2))
  print("type of datetime_month_f_str:", type(datetime_month_f_str), '\n')
  print("type of content of datetime_month_f_str", datetime_month_f_str.dtypes)
  print("Showing head of dataset datetime_month_f_str \n")
  print(datetime_month_f_str.head())
  # Result is a Dataframe containing numbers as string values with a "0" in front one digit numbers

  print("6- Combining the three dataframes (day, month and year) into a dataframe with one column that contains the concatenation of year+month+day. \n")

  datetime_str = datetime_year_f_str["DATETIME"] + datetime_month_f_str["DATETIME"] + datetime_day_f_str["DATETIME"]
  print(datetime_str.head())

  print("7- Adding dataframe's column containing date of format yyyymmdd as string as a new column of original dataframe \n")
  group_df["Idx"] = datetime_str
  print(group_df.head())

  print("8- Create a csv file containing columns Idx, Mean_S008, Mean_S035, Mean_S038, Mean_S048 and Mean_S050")
  group_df.to_csv('/content/TimeGAN/data/Sensors_data_formatted.csv',columns=['Idx', 'Mean_S008', 'Mean_S035', 'Mean_S038', 'Mean_S048', 'Mean_S050'])





