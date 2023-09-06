from Capture.capture import capture_can
from DoS.dos import dos_attack
import os

f_dict = {"1": capture_can, "2": dos_attack}

if __name__ == "__main__":
    print(" 1 - vcan0\n", "2 - can0\n")
    can_type = input()

    if can_type == "1":
        os.system("sudo modprobe vcan")
        os.system("sudo ip link add dev vcan0 type vcan")
        os.system("sudo ip link set up vcan0")
    else:
        os.system("sudo ip link set can0 up type can bitrate 500000")

    print(" 1 - Captura de pacotes\n", "2 - DoS Attack\n", "3 - Falsify Attack")

    op = input()
    f_dict[op](can_type)
