# used for handling numbers
import numpy as np
# used for handling the dataset
import pandas as pd
# used for handling missing data
from sklearn.impute import SimpleImputer
# used for encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# used for splitting training and testing data
from sklearn.model_selection import train_test_split
# used for feature scaling
from sklearn.preprocessing import StandardScaler


# Dataset Preprocessing
dataset = pd.read_csv("./data/UNSW-NB15_LIST_EVENTS.csv")
