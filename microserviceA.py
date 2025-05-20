import time

import zmq
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

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
            message = socket.recv_string()
            print(f"Received: {message}")

            if not message:
                socket.send_string("Invalid input.")
                continue

            if message.upper() == "Q":
                socket.send_string("Shutting down.")
                break

            response = findLngLat(message)
            time.sleep(3)
            socket.send_string(response)

    except Exception as e:
        print(f"Error while processing message: {e}")

    finally:
        socket.close()
        context.term()
        print("Server shut down.")


if __name__ == "__main__":
    main()
