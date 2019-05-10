# coding=utf-8
import numpy as np
import pandas as pd
import time
from sklearn.metrics import accuracy_score,recall_score,precision_score,confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron as sk_perceptron


class MyPerceptron():

    def __init__(self):
        self.w=[]
        self.b=0
        self.learning_rate=0.01
        self.max_iter_num=30000

    def sign(self,sign_res):
        return np.where(sign_res>0,1,-1)

    def fit(self,X,y):
        print("perceptron is running")
        self.w = np.zeros(len(X[0]),dtype=float)
        iter = 0
        while( iter<= self.max_iter_num):
            wrongNum = 0
            for i in range(X.shape[0]):
                x = X[i]
                label = y[i]
                if ((np.dot(x,self.w)+self.b) * label) <= 0:
                    wrongNum += 1
                    self.w = self.w + self.learning_rate * np.dot(label,x)
                    self.b = self.b + self.learning_rate * label
            # print("now is running iter in:",iter)
            iter += 1
            if wrongNum == 0:
                break
        print("MyPerceptron count_iter:",iter)
        return self

    def predict(self,X):
        return self.sign(np.dot(X,self.w)+self.b)

def read_data():
    data_clos = ['label','sell_price','age','sell_speed','mileage','avg_mileage']
    train_data = pd.read_excel('../data/Perceptron_data.xlsx', header=None, sheet_name='TRAIN_DATA',names=data_clos)
    test_data = pd.read_excel('../data/Perceptron_data.xlsx', header=None, sheet_name='TEST_DATA',names=data_clos)
    stdscaler = StandardScaler()
    train_x = stdscaler.fit_transform(train_data.drop(['label'],axis=1))
    train_y = train_data['label']*2-1
    test_x = stdscaler.transform(test_data.drop(['label'],axis=1))
    test_y = test_data['label']*2-1
    return train_x, test_x, train_y, test_y

if __name__ == '__main__':
    train_x, test_x, train_y, test_y = read_data()
    print("train shape:",train_x.shape,"test.shape",test_x.shape)
    perceptron = MyPerceptron()
    perceptron.fit(train_x, train_y)
    print ("MyPerceptron w:",perceptron.w)
    print ("MyPerceptron b:",perceptron.b)
    train_pred = perceptron.predict(train_x)
    test_pred = perceptron.predict(test_x)
    print(confusion_matrix(test_y,test_pred))
    print("MyPerceptron test precision:", precision_score(test_y, test_pred))
    print("MyPerceptron test recall:", recall_score(test_y, test_pred))
    print("MyPerceptron test aucc:", accuracy_score(test_y, test_pred))
    print("MyPerceptron train aucc:",accuracy_score(train_y,train_pred))

    # use sk_learn Perceptron compute aucc
    clf = sk_perceptron()
    start = time.time()
    clf.fit(train_x,train_y)
    print("fit cost time:",(time.time() - start)/60)
    train_pred = clf.predict(train_x)
    test_pred = clf.predict(test_x)
    print("sk_perceptron train accu:",accuracy_score(train_y,train_pred))
    print("sk_perceptron test accu:",accuracy_score(test_y,test_pred))
    print(confusion_matrix(test_y, test_pred))
