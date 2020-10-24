import socket               # Import socket module
import threading
import os
from tqdm import tqdm

def see():   #Deamon Thread to Keep listening
   while True:
    ro1=(s.recv(5000).decode())
    print(ro1)
    if ro1=="stop":
     break 
     s.close
    if ro1=="file1":
     f1='heart2'
     newf=open(f1,'wb+')
     while True:
       
       s1=s.recv(buff)
       try:
        r=s1.decode()
        if r=="Done":
         newf.close()
         print("File transfer Over")
         break
       except:
          newf.write(s1)
    


     
def encrypt(a): #A function to encode the data using custom made encrytion
   a1=a.encode('unicode_escape')
   a2=len(a1)
    
  
        
   
s = socket.socket(socket.AF_INET)         # Create a socket object
host = '80.78.219.189'  # Get local machine name
port = 12345               # Reserve a port for your recieving.

buff=4096
kk=0

s.connect((host, port))
print(s.recv(5000))
print(host)
print("Enter what you want the other person want to know bakayaro!, \nType stop to stop. Enjoy\n")
see1=threading.Thread(target=see)
see1.daemon=True
see1.start()
while True:
     in1=input()
     if in1=="stop":
         s.close
         break


      
     if in1=="file":

        s.send(bytes(in1,'utf-8'))
        f1=input("Please type the file you want to send with its extension\n")
        f1=open(f1,'rb+',buff)    
         
        
        while True:      
         
            s1=f1.read(buff)
            
            if s1:
              s.sendall(s1)
                
              
            if not s1:
              print("Transfer successful!!")
              s.send(bytes("Done",'UTF-8'))
              f1.close
              break

     try:
      in1=bytes(in1,'UTF-8')
      s.send(in1)
     except:
       pass




     
s.close()

                    # Close the socket when done
