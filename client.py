import socket
import marshal
import pickle
import sys
import os
import keygen

# Load client public/private keys
pub_key = ''
priv_key = ''
pub_key, priv_key = keygen.get_keys('./client_public.key', 'client_private.key')

# custom function to send to server
def send_function():
    import numpy
    print(numpy.empty([3,2], dtype = int)) # obviously this is useless as it prints on the server
    
    return 'Hello from beyond!'


# set up server
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

try:
    sock.connect(('localhost', 12345))
    cmd = (1).to_bytes(8, byteorder='little', signed=False) # 1 = read function
    print('Command number: ' + str(cmd))

    # send command
    sock.send(cmd)

    # dump function code to variable
    mdata = marshal.dumps(send_function.__code__)
    
    # send size of data
    print('Send function size: ' + str(sys.getsizeof(mdata)))
    sock.send(sys.getsizeof(mdata).to_bytes(16, byteorder='little', signed=False))

    # send function to server
    sock.send(mdata)

    size = sock.recv(16) # read size of return data
    size = int.from_bytes(size, byteorder='little', signed=False)

    result = sock.recv(size) # read specified size of bytes

    result = pickle.loads(result) # unmarshal the code bytes literal
    print(result) # client knows what result (type) is so what to do with it
                  # depends on the send function
    
except Exception as e:
    print(e)
finally:
    sock.close()
    
    
