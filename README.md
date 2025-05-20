# CS361-Microservice A
written by Michael Cook CS361

## Introduction
This is a microservice written out with the intention to support a partners application in CS361.
The microservice itself recieves a string: "city, state" and returns a string: "longitude, latitude"

## Required Modules

- geopy

- pyzmq

## Usage
The microservice is meant to be used locally, clone and download to root directory. This microservice utilizes ZeroMQ to communicate requested data. The microservice will be bound to port 5555 Ex.:
```
socket.bind("tcp://*:5555")
```
In order to recieve requested data, a string must be written in the form: "city, state".
When all requests have been made, the microservice will take in the uppercase character 'Q' to shutdown the microservice Ex:
```
socket.send_string("Q")
```

## Example calls for ZeroMQ
Call using "San Francisco, CA"
```
socket.send_string("San Francisco, CA")
```
Recieve
```
message = socket.recv_string()
```
## UML Sequence Diagram

![alt text](UML.drawio.png)
