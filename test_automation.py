# test_automation.py
import can
import time

def run_can_message_test(bus):
    for _ in range(5):  # Run the test 5 times for demonstration purposes
        received_message = bus.recv(timeout=5.0)

        if received_message:
            if len(received_message.data) == 4:
                print("Test Passed: Received a CAN message with valid format.")
            else:
                print("Test Failed: Received a CAN message with invalid format.")
        else:
            print("Test Failed: No message received within the timeout.")

if __name__ == "__main__":
    with can.interface.Bus(channel='vcan0', bustype='socketcan') as bus:
        # Run the test automation
        run_can_message_test(bus)
