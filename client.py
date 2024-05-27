import os
import socket

IP=socket.gethostbyname(socket.gethostname())
PORT=8888
ADDR=(IP,PORT)
FORMAT="utf-8"
SIZE=1024
Server=f"SERVER : {ADDR}"


def main():
    CLIENT_DATA_PATH="client_data_path"
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    details=client.recv(SIZE).decode(FORMAT)
    details=details.split("@")
    print(details[0])
    print(Server)
    print(f"MYADDR : {details[1]}")

    while True:
        data=input("\n---> ")
        data=data.split(" ")
        cmd=data[0]

        if(cmd=="HELP"):
            client.send(cmd.encode(FORMAT))
            reply=client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] : {reply}")
        
        elif(cmd=="LOGOUT"):
            client.send(cmd.encode(FORMAT))
            break

        elif(cmd=="LIST"):
            client.send(cmd.encode(FORMAT))
            reply=client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] : {reply}")

        elif(cmd=="UPLOAD"):
            filename=data[1]
            with open(f"{CLIENT_DATA_PATH}/{filename}","r") as f:
                text=f.read()
            send_data=f"{cmd}@{filename}@{text}"
            client.send(send_data.encode(FORMAT))
            reply=client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] : {reply}")

        elif(cmd=="DOWNLOAD"):
            filename=data[1]
            file =os.listdir(CLIENT_DATA_PATH)
            access="yes"
            if filename in file:
                print("[FILE MANAGER] : The file already exists." )
                inp=input("Overwrite? y/n :")
                if inp=="yes" or inp=="YES" or inp=="Yes" or inp=="y" or inp=="Y":
                    access="yes"
                elif inp=="no" or inp=="NO" or inp=="No" or inp=="n" or inp=="N":
                    access="no"

            if access=="yes":
                client.send(f"{cmd}@{filename}".encode(FORMAT))
                data=client.recv(SIZE).decode(FORMAT)
                data=data.split("@")
                present=data[0]
                text=data[1]

                if present=="0":
                    print("[SERVER] : The file not fount in the server.")

                elif present=="1":
                    filepath=os.path.join(CLIENT_DATA_PATH,filename)
                    with open(filepath,"w") as f:
                        f.write(text)
                    print("The file downloaded successfully.")

            elif access=="no":
                print("The download process cancelled.")

        elif(cmd=="CLEAR"):
            os.system("clear")
            print(details[0])
            print(Server)
            print(f"MYADDR : {details[1]}")

        elif(cmd=="DELETE"):
            filename=data[1]
            client.send(f"{cmd}@{filename}".encode(FORMAT))
            msg=client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] : {msg}")

        elif cmd=="VIEW":
            file=os.listdir(CLIENT_DATA_PATH)
            if len(file)==0:
                print("[FILE MANAGER] : The current directory is empty")
            else:
                print(f"[FILE MANAGER] : The files in the current directory ({CLIENT_DATA_PATH}) are ")
                for fin in file:
                    print(f"               *{fin}")
        
        elif cmd=="CHANGEDIR":
            path=data[1]
            CLIENT_DATA_PATH=path
            print(f"[FILE MANAGER] : Client's directory changed to {path}")

        else:
            print(f"[SERVER] : Invalid command - {cmd} . Use HELP for commands.")

    print("[SERVER] : Disconnected from the Server.")
    client.close()

if __name__=="__main__":
    main()
