"""
beating the benchmark @CTR
__author__ : Abhijeet Bhorkar 
"""

# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/bhorkar/data_science/KaggleAux/kaggleaux')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.nonparametric.kde import KDEUnivariate
from statsmodels.nonparametric import smoothers_lowess
from pandas import Series, DataFrame
from patsy import dmatrices
from sklearn import datasets, svm, metrics,preprocessing
#from kaggleAux import predict as ka


loadData = lambda f: np.genfromtxt(open(f,'r'), delimiter=' ')

def main():

  print "loading data.."
  # Open hdf5 file
  df = pd.read_csv('train.shuffled', nrows = 100);
  df = df.dropna();
  # specifies the parameters of our graphs
  fig = plt.figure(figsize=(18,6)); 
  alpha=alpha_scatterplot = 0.2 
  alpha_bar_chart = 0.55
   # lets us plot many diffrent shaped graphs together 
  ax1 = plt.subplot2grid((2,3),(0,0))
# plots a bar graph of those who surived vs those who did not.               
  df.click.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
  ax1.set_xlim(-1, 2)
# puts a title on our graph
  plt.title("Distribution of click, (1 = clicked)")    

  plt.subplot2grid((2,3),(0,1))
  plt.scatter(df.click, df.banner_pos, alpha=alpha_scatterplot)
# sets the y axis lable
  plt.ylabel("banner pos")
# formats the grid line style of our graphs                          
  plt.grid(b=True, which='major', axis='y')  
  plt.title("Survial by banner pos,  (1 = clicked)")

  df["date_time"] = df['hour'].apply(string_to_date);
  dfts = df.set_index("date_time");
  time_mean =dfts.groupby(lambda x: x.time()).mean();
  print "saving data to hdf5"
  print time_mean
  test = pd.read_csv('test');

 # df.to_hdf('train_hdf.h5','df')
 # traindata = p.read_hdf('train_hdf.h5','df');
  
def string_to_date(date_string):
    return datetime.datetime.strptime('20'+str(date_string),"%Y%m%d%H")
if __name__=="__main__":
  main()

