import argparse
import sys, time
from socket import *

timeout = .5


def scan_ports(host, start_port, end_port, protocol):

    print("Scanning: " + host + " From port: " + str(start_port) + " To Port: " + str(end_port))

    try:
        if protocol.lower() == "tcp":
            sock = socket(AF_INET, SOCK_STREAM)
            print(f"Protocol: {protocol}")
        elif protocol.lower() == "udp":
            sock = socket(AF_INET, SOCK_DGRAM)
            print(f"Protocol: {protocol}")
        else:
            print("Use UDP or TCP. Restart the program and try again.")
            exit()

        sock.settimeout(timeout)
    except:
        print("Couldn't create the socket.")


    remote_ip = host
    print(f"Scanning: {host}")

    for port in range(start_port, end_port+1):
        # Create a socket object
        #s = socket(AF_INET, sock)
        sock.settimeout(timeout)

        try:
            if protocol.lower() == "tcp":
                connection_ = create_connection((host, port))
                connection_.sendall('call me 1-800-SCANNED'
                                    .encode('utf-8'))
                connection_.close

                print(f"Port {port} is open.")
            if protocol.lower() == "udp":
                sock.sendto(b"empty", (host,port))
                data, addr = sock.recvfrom(1024)
                print(f"Port {port} is open.")
        except:
            # Print a message if the port is closed or filtered
            print(f"Port {port} is closed or filtered.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remote Port Scanner')
    # setting the IP address to scan
    parser.add_argument('--host', action="store", dest="host", default='127.0.0.1')
    # setting the starting port no.
    parser.add_argument('--start-port', action="store", dest="start_port", default=1020, type=int)
    # setting the ending port no.
    parser.add_argument('--end-port', action="store", dest="end_port", default=1028, type=int)
    # setting the default protocol to scan for
    parser.add_argument('--protocol', action="store", dest="protocol", default="tcp")
    # parse args
    given_args = parser.parse_args()
    host, start_port, end_port, protocol = given_args.host, given_args.start_port, given_args.end_port, given_args.protocol
    scan_ports(host, start_port, end_port, protocol)
