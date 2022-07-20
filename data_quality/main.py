import os
import logging
import numpy as np
import pandas as pd
import json

logging.basicConfig(filename="C://Users//tumul//PycharmProjects//python-labs//data_quality//input//test_dataquality.json",
                    format= '%(asctime)s %(message)s',
                    filemode= 'w',
                    level = logging.DEBUG)
logging.getLogger('data_quality').disable = True
logger = logging.getLogger(__name__)

def handle_duplicates(data):
    #To check whether file contains duplicate values
    dup_rows = data.duplicated()
    logging.info(f"A total of {dup_rows.shape[0]} duplicate rows are present in a file")
    print(dup_rows)













if __name__=="__main__":
    #check whether the file is present for the further process
    input_file_path = "C://Users//tumul//PycharmProjects//python-labs//data_quality/input//IN_videos.csv"
    if os.path.exists(input_file_path):
        logging.info("Input file exists for processing")
    input_data = pd.read_csv(input_file_path)
    print(input_data.shape)
    print(input_data.columns)

    #handling duplicate values
    dedup_values = handle_duplicates(input_data)