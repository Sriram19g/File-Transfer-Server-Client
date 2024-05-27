# File-Transfer-Server-Client

This project is a TCP-based file transfer system that allows a client to interact with a server to perform various file operations such as listing files, uploading, downloading, deleting, and changing directories. The project consists of a server (`server.py`) and a client (`client.py`) implemented in Python.

## Features

- **List Files**: View the list of files available on the server.
- **Upload Files**: Upload a file from the client to the server.
- **Download Files**: Download a file from the server to the client.
- **Delete Files**: Delete a file from the server.
- **Change Directory**: Change the client's working directory.
- **Help**: Get a list of available commands.
- **Logout**: Disconnect from the server.

## Requirements

- Python 3.x
- Network connection between the server and the client machines.

## Project Structure

```
File-transfer-server-client/
│
├── server.py
├── client.py
└── README.txt
```

## Installation and Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/File-transfer-server-client.git
   cd File-transfer-server-client
   ```

2. **Set Server and Client Data Paths**

   Make sure to update the `SERVER_DATA_PATH` in `server.py` and the `CLIENT_DATA_PATH` in `client.py` to valid directories on your machine.

3. **Run the Server**

   On the server machine, run:

   ```bash
   python3 server.py
   ```

   The server will start and listen for incoming connections on the specified IP and port.

4. **Run the Client**

   On the client machine, run:

   ```bash
   python3 client.py
   ```

   The client will connect to the server and you can start issuing commands.

## Usage

### Commands

- **LIST**: List all the files from the server.
  
  ```bash
  LIST
  ```

- **UPLOAD <filename>**: Upload a file to the server.
  
  ```bash
  UPLOAD example.txt
  ```

- **DOWNLOAD <filename>**: Download a file from the server.
  
  ```bash
  DOWNLOAD example.txt
  ```

- **DELETE <filename>**: Delete a file from the server.
  
  ```bash
  DELETE example.txt
  ```

- **CHANGEDIR <path>**: Change the client's working directory.
  
  ```bash
  CHANGEDIR /path/to/new/directory
  ```

- **LOGOUT**: Disconnect from the server.
  
  ```bash
  LOGOUT
  ```

- **HELP**: Get a list of available commands.
  
  ```bash
  HELP
  ```

- **CLEAR**: Clear the screen.
  
  ```bash
  CLEAR
  ```

- **VIEW**: View files in the client's current directory.
  
  ```bash
  VIEW
  ```

## Example Session

```plaintext
Welcome to the File Server.
SERVER : ('192.168.1.10', 8888)
MYADDR : ('192.168.1.15', 12345)

---> LIST
[SERVER] : The files in the server directory are
           *example.txt
           *data.csv

---> UPLOAD newfile.txt
[SERVER] : File uploaded successfully.

---> DOWNLOAD example.txt
The file downloaded successfully.

---> DELETE data.csv
[SERVER] : The file is deleted successfully.

---> LOGOUT
[SERVER] : Disconnected from the Server.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Acknowledgements

- Python documentation: https://docs.python.org/3/
- Socket programming resources and examples.

## Contact

For any questions or feedback, please contact gsriram200@gmail.com.

---

Feel free to customize this `README.txt` file further according to your needs. This template provides a comprehensive overview of the project and its usage, which should be helpful for anyone looking to understand and use your File-Transfer-Server-Client system.
