##############################################################################
# server-python.py
# Name:
# NetId:
###############################################################################

import sys
import socket
import queue

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 1


def server(server_port):
    #print('Listening on port {}'.format(server_port))
    myQueue = queue.Queue(QUEUE_LENGTH)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', server_port))
        s.listen()
        while True:
            conn, addr = s.accept()
            myQueue.put((conn, addr))

            # Process connection queue 
            if myQueue.full():
                #print('Processing conn...')
                while not myQueue.empty():
                    conn, addr = myQueue.get()
                    #print(f'Connected by {addr}')
                    res = ""
                    while True:
                        data = conn.recv(RECV_BUFFER_SIZE)
                        if not data:
                            break
                        res += data.decode()
                    print(res)
                        
            else:
                #print('Queue size:', myQueue.qsize())
                pass
                

def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)


if __name__ == "__main__":
    main()
