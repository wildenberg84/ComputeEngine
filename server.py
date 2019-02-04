import socket
import protocol_library as lib
import keygen

# Command -- Description
# 0       -- Reserved for extensibility
# 1       -- Read function (next 16 bytes represent function size, then read function)
protocol = {0 : 'undefined',
            1 : lib.read_function
            }

# Load server public/private keys
pub_key = ''
priv_key = ''
pub_key, priv_key = keygen.get_keys('./server_public.key', 'server_private.key')

# start up server     
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.bind(('', 12345))

while(True):
    try:
        sock.listen(10)
        client, addr = sock.accept()
        print('Connected to ', client)
        
        data = client.recv(8) 
        cmd = int.from_bytes(data, byteorder='little', signed=False)

        protocol[cmd](client)
            
    except Exception as e:
        print(e)
    finally:
        client.close()
            
        
        
