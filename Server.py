import socket
import joblib
import pickle
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=7634

s.connect((host,port))
i=1
while i==1:
    features = []
    print("wating for response")

    features = s.recv(1024)
    features = features.decode('utf-8')
    #features.append(s_messg)
    features=eval(features)
    features = [features]

    model = joblib.load("lr_model.sav")
    y_pred = model.predict(features)
    if y_pred[0] == 0:
        messg = "Diabetes Negative"
    elif y_pred[0] == 1:
        messg = "Diabetes Positive"

    s.send(messg.encode())

    c_messg=s.recv(1024)
    if c_messg.decode() == 'yes':
        i =1
    else:
        i=2
    #i=2
    #break

    # c_messg = s.recv(1024)
    # if c_messg.decode() == 'yes':
    #     i = 1
    # else:
    #     i = 2