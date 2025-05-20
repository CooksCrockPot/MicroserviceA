import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print("Sending first location request...")
socket.send_string("San Francisco, CA")
message = socket.recv_string()
print(f"Server replied: {message}")

print("Sending shutdown signal...")
socket.send_string("Q")
message = socket.recv_string()
print(f"Server replied: {message}")

socket.close()
context.term()
