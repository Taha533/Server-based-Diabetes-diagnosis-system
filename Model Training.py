import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import  joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
df = pd.read_excel("Diabetes_Classification.xlsx",sheet_name= "Diabetes_Classification")
df.drop(["Patient number","Unnamed: 16","Unnamed: 17"],axis=1,inplace=True)
gender = {"female": 0,"male":1}
target = {"No diabetes": 0,"Diabetes": 1}
df["Gender"] = df["Gender"].map(gender)
df["Diabetes"] = df["Diabetes"].map(target)
df.drop(["hip"],axis=1,inplace=True)
df.drop(["BMI"],axis=1,inplace=True)
df.drop(["Weight"],axis=1,inplace=True)
df.drop(['Height'],axis=1,inplace=True)

x = df.drop("Diabetes",axis=1)
y =df["Diabetes"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import precision_score,recall_score,f1_score
from sklearn.metrics import brier_score_loss

lr =LogisticRegression(C=1.4,solver ="liblinear",penalty='l1')#10,lbfgs,C =0.7,solver='lbfgs',random_state = 10, c=1.4
lr.fit(x_train,y_train)
lr_pred = lr.predict(x_test)
lr_prob = lr.predict_proba(x_test)
print(classification_report(y_test,lr_pred))
lr_tr_acc = lr.score(x_train,y_train)
lr_te_acc = lr.score(x_test,y_test)
print(f"Train accuracy: {lr.score(x_train,y_train)}")
print(f"Test accuracy: {lr.score(x_test,y_test)}")

joblib.dump(lr, "lr_model.sav")