import can

with can.interface.Bus(channel='vcan0', bustype='socketcan') as bus:
    message = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=False)

    bus.send(message)
    print("Message sent successfully.")

    received_message = bus.recv(timeout=10.0)

    print(received_message)
    
    
