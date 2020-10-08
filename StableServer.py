import socket               # Import socket module
import threading
import os
from tqdm import tqdm
def see():                      #An infinite loop thread to listen to messages
    while True:
     ro1=(c.recv(5000).decode())
     print(ro1)
     if ro1=="stop":
         s.close()
     if ro1=="file":
         newf=open('yourfile2','wb+')
         while True:

           s1=c.recv(buff)
           try:
                r=s1.decode()
                if r=="Done":
                 print("File transfer Over")
                 newf.close()                 
                 break
           except:
                    newf.write(s1)
                    pass
           
           





kk=0        
dd="You shall start recieving info now_:)"                                #Starting Message
dd1=bytes(dd,'UTF-8')                                                             #Starting Message encoded in bytes
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = '0.0.0.0'             # Get local machine name
port = 12345               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                      # Now wait for client connection.
buff=409600000
c, addr = s.accept()# Establish connection with client.
print ('Got connection from', addr)
print('This is the host address',socket.gethostbyaddr)
print("Enter what you want the other person want to know bakayaro!, \nType stop to stop. Enjoy\n")
c.send(dd1)
see1=threading.Thread(target=see)
see1.daemon=True
see1.start()
while True:   #An infinite loop to keep texting        
      in1=input()
      if in1=="stop":
         break
  


      if in1=="file1":

        c.send(bytes(in1,'utf-8'))
        f1=input("Please type the file you want to send with its extension\n")
        f1=open(f1,'rb+',buff)
        while True:      
         
            s1=f1.read(buff)
            
            if s1:
              c.sendall(s1)
              kk+1  
              
            if not s1:
              print("Transfer successful!!")
              c.send(bytes("Done",'UTF-8'))
              f1.close
              break

      try:
       in1=bytes(in1,'UTF-8')
       c.send(in1)      
      except:
       pass
s.close()


                # Close the connection
