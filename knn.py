import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

movie = pd.read_excel('../data/movies.xlsx',sheet_name=1)
