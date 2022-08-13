from ipaddress import ip_address, IPv4Address, IPv6Address


def check():
    global split
    IP = input('Enter the ip address: ')
    try:
        if type(ip_address(IP)) is IPv4Address:
            print('IPv4')
            m = str(IP)
            for i in range(len(IP)):
                if IP[i] == '.':
                    split = int(m[:i])
                    print(split)
                    break
            if split in range(0, 127):
                print('class A')
            elif split in range(128, 191):
                print('class B')
            elif split in range(192, 223):
                print('class C')
            elif split in range(224, 239):
                print('class D')
        elif type(ip_address(IP)) is IPv6Address:
            print('IPv6')
    except ValueError:
        print('Invalid IP')


def windowsize():
    rwnd = int(input('Enter the size of rwnd: '))
    cwnd = int(input('Enter the size of cwnd: '))
    size = min(rwnd, cwnd)
    print('The window size is', size)


def mainloop(i):
    switcher = {
        0: check(),
        1: windowsize()
    }


if __name__ == '__main__':
    i = int(input('Enter your choose'))
    mainloop(i)
