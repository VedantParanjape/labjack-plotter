from ljm_wrapper import labjack_wrapper as lm
import time
ljm = lm.ljmWrapper()

counter = 0
def run_ljm():
    global counter
    if counter == 2:
        return False
    
    counter+=1
    return True

ljm.analog_read_stream_setup([3], 10)
for i in ljm.analog_read_stream(run_ljm):
    print (i)