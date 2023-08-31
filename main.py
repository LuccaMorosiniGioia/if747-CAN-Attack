from Capture.capture import capture_can

f_dict = {
    '1': capture_can
}

if __name__ == '__main__':
    print(' 1 - Captura de pacotes\n',
          '2 - DoS Attack\n',
          '3 - Falsify Attack')
    
    op = input()
    f_dict[op]()