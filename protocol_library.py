import socket
import sys
import marshal
import pickle
import run_function as run

def read_function(client):
    print('Reading function size and data')
    # get function size
    data = client.recv(16)

    if data:
        size = int.from_bytes(data, byteorder='little', signed=False)
        print('size of function is: ' + str(size))
        
        func = client.recv(size) # to make sure you don't over-read

        func = marshal.loads(func) # unmarshal the code bytes literal
        print('Running function...')
        result = run.start(func) # run the function

        result = pickle.dumps(result) # pickle the results

        print('Returning result')
        # send the client the size of the result
        client.send(sys.getsizeof(result).to_bytes(16, byteorder='little', signed=False))

        # send the result(s)
        client.send(result)
        
    else:
        print('No size was sent.')
