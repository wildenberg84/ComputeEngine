import socket
import protocol_library as lib
import os
import keygen

# Command -- Description
# 0       -- Reserved for extensibility
# 1       -- Read function (next 16 bytes represent function size, then read function)
protocol = {0 : 'undefined',
            1 : lib.read_function
            }

    
pub_key = ''
priv_key = ''

# Check for server public key
if os.path.isfile('./server_public.key'):
    # key exists, load from file
    with open('server_public.key', 'r', encoding='utf8') as f:
        try:
            pub_key = f.read()
            f.close()
        except Exception as e:
            print(e)
else:
    # key file does not exist, generate a key and safe to file
    pub_key = keygen.generate_key(256)
    print(pub_key) # DEBUG ONLY -- REMOVE!
    
    with open('server_public.key', 'w+', encoding='utf8') as f:
        try:
            f.write(pub_key)
            f.close()
        except Exception as e:
            print(e)
    
# Check for server private key
if os.path.isfile('./server_private.key'):
    # key exists, load from file
    with open('server_private.key', 'r', encoding='utf8') as f:
        try:
            priv_key = f.read()
            f.close()
        except Exception as e:
            print(e)
else:
    # key file does not exist, generate a key and safe to file
    priv_key = keygen.generate_key(256)
    print(priv_key) # DEBUG ONLY -- REMOVE!
    
    with open('server_private.key', 'w+', encoding='utf8') as f:
        try:
            f.write(priv_key)
            f.close()
        except Exception as e:
            print(e)



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
            
        
        
