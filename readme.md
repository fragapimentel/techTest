# Technical test for Upciti

This project is an Inter-process communication prototype for a technical test.

The test is coded in python by using a TCP socket connection between the server and the clients. In this context we have one server and one or more clients. This work in a context of producer/consumer where the server produces information that is passed to the client, or the consumer. 

The producer generates a data object containing the time of the data creation and other random values. This is a simulation of a boundingbox for image object detection like we can obtain with a (SSD) Single Shot Detection algorithm. 

The project is divided in three python code files: i) the server (pub_server.py); ii) the client (sub_client.py) and; iii) the data class (data_class.py). 

The server and the client uses pyzmp for TCP connection for communication. The data is passed as a python pickle buffer of the data class object.

The data_class.py contains the data and 3 main functions: the initialization; set_data for creation of random values; and print to print all the content of all attribures. The data class is used by the client and the server.

## Usage

Run the server command followed by the TCP port. 

```bash
python3 pub_server.py 5555
```

If the port is not specified it uses by default the port 5555.

Run each client by the followed command, the TCP port and the server IP.

```bash
python3 sub_client.py 5555 localhost
```

