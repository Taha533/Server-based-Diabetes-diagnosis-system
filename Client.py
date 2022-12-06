import socket
import pickle
import joblib
#import iris
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=7634

s.bind((host,port))
s.listen(1)


# Cholesterol = float(input("Enter Cholesterol Level:"))
# Glucose = float(input("Enter Glucose Level:"))
# HDL Chol = float(input("Enter HDL Cholesterol Level:"))
# Chol/HDL ratio = float(input("Enter Chol/HDL ratio:"))
# Age = float(input("Enter Age:"))
# Gender = float(input("Enter Gender:"))
# Systolic BP = float(input("Enter Systolic BP Level:"))
# Diastolic BP = float(input("Enter Diastolic BP Level:"))
# waist = float(input("Enter waist size:"))
# Waist/hip ratio = float(input("Enter Waist/hip ratio:"))

con,addr=s.accept()
print("connected with",addr)
i=1
while i==1:
    print("Enter necessary values:")
    # sepal_length = float(input("Enter sepal_length :"))
    # sepal_width = float(input("Enter sepal_width :"))
    # petal_length = float(input("Enter petal_length:"))
    # petal_width = float(input("Enter petal_width:"))

    Cholesterol = float(input("Enter Cholesterol Level:"))
    Glucose = float(input("Enter Glucose Level:"))
    HDLChol = float(input("Enter HDL Cholesterol Level:"))
    Chol_HDLratio = float(input("Enter Chol/HDL ratio:"))
    Age = float(input("Enter Age:"))
    Gender = float(input("Enter Gender:"))
    SystolicBP = float(input("Enter Systolic BP Level:"))
    DiastolicBP = float(input("Enter Diastolic BP Level:"))
    waist = float(input("Enter waist size:"))
    Waist_hipratio = float(input("Enter Waist/hip ratio:"))

    #features = [sepal_length, sepal_width, petal_length, petal_width]
    features = [Cholesterol, Glucose, HDLChol, Chol_HDLratio,Age,Gender,SystolicBP,DiastolicBP,waist,Waist_hipratio]
    features = str(features)
    features = features.encode()
    con.send(features)
    #i=2
    #break

    #messg = "Diabetes Negative"
    #messg=input("send message to client: ")
    #con.send(messg.encode())
    print("waiting for response")
    c_messg=con.recv(1024)
    print('You are: ',c_messg.decode())

    #print("message from client: ",c_messg.decode())
    contnu = input("Do you want to continue: ")
    con.send(contnu.encode()) #s.send
    if contnu == 'yes':
        i = 1
    else:
        i = 2
