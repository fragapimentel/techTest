import zmq
import sys
import time
import pickle
import data_class
	
port = '5555'
if len(sys.argv) > 1:
	port =  sys.argv[1]
	int(port)

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:%s" % port)

d = data_class.data()

while True:
	d.set_data()
	print(d.print())
	p = pickle.dumps(d, -1)
	socket.send(p, flags=0)
	time.sleep(1)