from serial import Serial,SerialException
import time
import logging
import sys
import os

port=None;
ser=None;
baudrate=None;

def check_available_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]

    result = []
    for port in ports:
        try:
            s = Serial(port)
            s.close()
            result.append(port)
        except (OSError, SerialException):
            pass

    return result

def check_com_still_connected(port):
    try:
        s= Serial(port);
        s.close();
        flag=1;
    except (OSError, SerialException):
        flag=0;
        
    return flag;


def init():
    global port,ser,baudrate;
    port=input("Enter The Port Number : ");
    baudrate=input("Enter The BaudRate : ");
    file=input("Enter file name to store the log with .log extension : ");
    user=os.getlogin();
    print(user);
    directory=r"C:\Users\{}\Documents\Arduino\logs".format(user);
    location=r"C:\Users\{}\Documents\Arduino\logs\{}".format(user,file);
    print(location);

    if(os.path.exists(directory) == True):
        logging.basicConfig(filename=location,format='%(asctime)s %(message)s',level=logging.DEBUG);
    else:
        os.makedirs(directory);
        logging.basicConfig(filename=location,format='%(asctime)s %(message)s',level=logging.DEBUG);
        
    check=check_com_still_connected(port);
    if(check==1):
        ser=Serial(port,baudrate,timeout=5);
        print("Port Started at : ",ser.portstr);
        ser.close();
    elif(check==0):
        print("\nNo port connected\n");
        init();


def log():
    init();
    while True:
        ch=check_com_still_connected(port);
        if(ch==1):
            try :
                    ser=Serial(port,baudrate,timeout=5);
                    x=ser.readline();
                    x=x.decode('utf-8')
                    print(x);
                    logging.info(x)
                    ser.close();
            except SerialException :
                    logging.info("Port has been ejected");
        elif(ch==0):
            logging.info("COM Port Disconnected");
            reconnect=input("Press 1 to Reconnect The COM Port\nPress 2 to Terminate Logging");
            reconnect=int(reconnect);
            if(reconnect==1):
                ch=check_com_still_connected(port)
                while(ch != 1):
                    ch=check_com_still_connected(port);
            elif(reconnect==2):
                sys.exit();


log();

