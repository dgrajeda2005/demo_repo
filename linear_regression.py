import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
#warnings.filterwarnings("ignore")
# Loading the Dataset

df = sns.load_dataset("mpg")

print("{}".format(df.head()))