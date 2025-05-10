import zmq
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

geolocator = Nominatim(user_agent="microserviceA")

def findLngLat(findLocation):
    try:
        location = geolocator.geocode(findLocation)
    except GeocoderTimedOut:
        print("Geocoding timed out. Try again.")
        return "Timeout"

    if location:
        return f"{location.latitude}, {location.longitude}"
    else:
        return "Location not found"

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    print("Microservice running on port 5555...")

    try:
        while True:
            message = socket.recv()
            decoded = message.decode()
            print(f"Received: {decoded}")

            if not decoded:
                socket.send_string("Invalid input.")
                continue

            if decoded.upper() == 'Q':
                socket.send_string("Shutting down.")
                break

            response = findLngLat(decoded)
            time.sleep(3)
            socket.send_string(response)

    finally:
        socket.close()
        context.term()
        print("Server shut down.")

if __name__ == "__main__":
    main()
