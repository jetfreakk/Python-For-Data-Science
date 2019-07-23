import numpy as np 
import scipy as sp 
import pandas as pd 
import matplotlib as mpl 
import seaborn as sns
df = pd.read_csv("F:/Github/Python for Data Science/KB.csv")
df.head(10)
df.tail(10)
df['ImageId'].dtype
df['NameOfPokemon'].dtype
df.dtypes