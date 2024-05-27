import os
import socket
import threading

IP=socket.gethostbyname(socket.gethostname())
PORT=8888
ADDR=(IP,PORT)
FORMAT="utf-8"
SIZE=1024
SERVER_DATA_PATH="/home/sriram/bhp/server_data"

def handle_client(con,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    con.send(f"Welcome to the File Server.@{addr}".encode(FORMAT))

    while True:
        data=con.recv(SIZE).decode(FORMAT)
        data=data.split("@")
        cmd=data[0]

        if cmd=="LIST":
            file=os.listdir(SERVER_DATA_PATH)
            send_data=""

            if len(file)==0:
                send_data+="The server directory is empty"
            else:
                send_data+="The files in the server directory are\n           *"
                send_data+="\n           *".join(f for f in file)
            con.send(send_data.encode(FORMAT))
            print(f"{addr} : Listing files in the server's directory.")

        elif cmd=="HELP":
            data="The basic commands are \n"
            data+="LIST                ---> List all the files from the server.\n"
            data+="UPLOAD <filename>   ---> Upload a file to the server.\n"
            data+="DOWNLOAD <filename> ---> Download a file from the server.\n"
            data+="DELETE <filename>   ---> Delete a file from the server.\n"
            data+="CHANGEDIR <path>    ---> Change the client's directory.\n"
            data+="LOGOUT              ---> Disconnect from the server.\n"
            data+="HELP                ---> List all the commands.\n"
            data+="CLEAR               ---> Clear the screen.\n"
            data+="VIEW                ---> View files in the client's directory."
            
            con.send(data.encode(FORMAT))
            print(f"{addr} : Seeking HELP...")

        elif cmd=="LOGOUT":
            break

        elif cmd=="UPLOAD":
            filename=data[1]
            text=data[2]
            filepath=os.path.join(SERVER_DATA_PATH,filename)
            with open(filepath,"w") as f:
                f.write(text)

            send_data="File uploaded successfully."
            con.send(send_data.encode(FORMAT))
            print(f"{addr} : Upload {filename} in the server.")

        elif cmd=="DOWNLOAD":
            filename=data[1]
            files=os.listdir(SERVER_DATA_PATH)
            present="0"
            text=""
            if filename in files:
                present="1"
                with open(f"{SERVER_DATA_PATH}/{filename}","r") as f:
                    text=f.read()
                print(f"{addr} : Download {filename} from the server.")
            con.send(f"{present}@{text}".encode(FORMAT))
            
                


        elif cmd=="DELETE":
            file=os.listdir(SERVER_DATA_PATH)
            filename=data[1]
            send_data=""
            if len(file)==0:
                send_data+="The server directory is empty."
            else:
                if filename in file:
                    os.system(f"rm {SERVER_DATA_PATH}/{filename}")
                    send_data+="The file is deleted successfully."
                    print(f"{addr} : Delete {filename} from the server.")
                else:
                    send_data+="The file not found."
            con.send(send_data.encode(FORMAT))

    print (f"[DISCONNECTED] {addr} disconnected")
    print(f"[ACTIVE CONNECTION] {threading.active_count()-2}")
    con.close()

def main():
    print("[STARTING] Server is starting...")
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening...")

    while True:
        con,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(con,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count()-1}")

if __name__=="__main__":
    main()
