def summarize_by_date():
  print("Hello Julio")
    ## Runtime directory
    code_dir = os.path.abspath(".")
    if not os.path.exists(code_dir):
        raise ValueError(f"Code directory not found at {code_dir}.")

    ## Data directory
    data_path = os.path.abspath("TimeGAN/data")
    if not os.path.exists(data_path):
        raise ValueError(f"Data file not found at {data_path}.")
    data_dir = os.path.dirname(data_path)
    data_file_name = os.path.basename(data_path)

    ## Output directories
    args.model_path = os.path.abspath(f"TimeGAN/output/{args.exp}/")
    out_dir = os.path.abspath(args.model_path)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    #########################
    # Load and preprocess data for model
    #########################

    # data_path = "TimeGAN/data/stock.csv"
    data_path = "TimeGAN/data/NO2_sequence_five_sensors.csv"

summarize_by_date()
