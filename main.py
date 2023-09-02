from Capture.capture import capture_can
from DoS.dos import dos_attack

f_dict = {
    '1': capture_can,
    '2': dos_attack
}

if __name__ == '__main__':
    print(' 1 - Captura de pacotes\n',
          '2 - DoS Attack\n',
          '3 - Falsify Attack')
    
    op = input()
    f_dict[op]()