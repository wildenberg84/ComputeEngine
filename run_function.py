import types
import sys

def start(func):
    # NOTE: the merger of dicts (**) requires Python 3.5 or higher
    assert sys.version_info >= (3, 5), 'You need Python 3.5 or higher to run this!'
    
    # NOTE: merging dicts copies their values, the new dict is not a backed dict!
    sandbox = {**globals()} # create a sandbox dict, add the global namespace

    client_func = types.FunctionType(func, sandbox) # declare it as a function, and give it access to the global namespace

    try: # prevent the server from crashing when client sends illegal function
        return_value = []
        return_value = client_func() # result of any return of the function

        return return_value
    except:
        print('Illegal function')
