"""
beating the benchmark @CTR
__author__ : Abhijeet Bhorkar 
"""

# -*- coding: utf-8 -*-
import h5py    # HDF5 support
import numpy as np
from sklearn import metrics,preprocessing,cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm, cross_validation
import sklearn.linear_model as lm
import pandas as p


loadData = lambda f: np.genfromtxt(open(f,'r'), delimiter=' ')

def main():

  print "loading data.."
  # Open hdf5 file
  df = p.read_csv('train.shuffled', nrows = 100);
  df["date_time"] = df['hour'].apply(string_to_date);
  dfts = df.set_index("date_time");
  time_mean =dfts.groupby(lambda x: x.time()).mean();
  print "saving data to hdf5"
  print time_mean
  test = p.read_csv('test');

 # df.to_hdf('train_hdf.h5','df')
 # traindata = p.read_hdf('train_hdf.h5','df');
  
def string_to_date(date_string):
    return datetime.datetime.strptime('20'+str(date_string),"%Y%m%d%H")
if __name__=="__main__":
  main()

