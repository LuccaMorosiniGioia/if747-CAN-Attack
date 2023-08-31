import can


def capture_can():
    print('Initialing Packet Capture')
    bus = can.interface.Bus(interface='socketcan', channel='can0', bitrate=500000)
    
    count = 0
    msgs = []
    while count <= 5:
        try:
            msg = bus.recv()
        except can.CanOperationError:
            print('Except: CanOperationError')
        except:
            print('Unkown Error Receiving Can Msg')
        else:
            msgs.append(str(msg)+'\n')
            print(msg)
            count += 1

    f = open('can_dump.txt', 'a')
    f.writelines(msgs)
    f.close()

    print('Capture Done')
    