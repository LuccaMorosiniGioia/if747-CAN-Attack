import can
import time


def capture_can(can_type):
    print("Initialing Packet Capture")

    if can_type == "1":
        bus = can.interface.Bus(interface="socketcan", channel="vcan0", bitrate=500000)
    else:
        bus = can.interface.Bus(interface="socketcan", channel="can0", bitrate=500000)

    count = 0
    msgs = []
    init_time = time.time()

    while time.time() - init_time <= 600:
        try:
            msg = bus.recv(timeout=10)
        except can.CanOperationError:
            print("Except: CanOperationError")
        except:
            print("Unkown Error Receiving Can Msg")
        else:
            msgs.append(str(msg) + "\n")
            print(msg)

    f = open("can_dump.txt", "a")
    f.writelines(msgs)
    f.close()

    print("Capture Done")
    bus.shutdown()
