# read the data from data source
# save it in data/raw for further use

import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    print(df.head)