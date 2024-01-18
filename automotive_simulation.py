import can
import time
import random

def send_vehicle_data(bus):
    while True:
        speed = random.randint(0, 120)  # Simulating speed in km/h
        rpm = random.randint(800, 5000)  # Simulating RPM

        message = can.Message(arbitration_id=0x100, data=[speed // 256, speed % 256, rpm // 256, rpm % 256],
                              is_extended_id=False)

        bus.send(message)
        print(f"Sent: Speed={speed} km/h, RPM={rpm}")
        time.sleep(1)

if __name__ == "__main__":
    with can.interface.Bus(channel='vcan0', bustype='socketcan') as bus:
        send_vehicle_data(bus)
