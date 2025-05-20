import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

locations = ["San Francisco, CA", "Los Angeles, CA", "Portland, OR",
             "Eugene, OR", "Seattle, WA", "Vancouver, WA", "Boise, Idaho"]

for location in locations:
    print("Sending location request...")
    socket.send_string(location)
    message = socket.recv_string()
    print(f"Server replied: {message}")
    time.sleep(3)

print("Sending shutdown signal...")
socket.send_string("Q")
message = socket.recv_string()
print(f"Server replied: {message}")

socket.close()
context.term()
