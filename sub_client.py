import sys
import zmq
import pickle
import data_class

port = "5555"
if len(sys.argv) > 1:
	port = sys.argv[1]
	port = int(port)

host = 'localhost'
if len(sys.argv) > 2:
	host = sys.argv[2]
	
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.PULL)

print('Collecting updates from server...')
socket.connect(f'tcp://{host}:{port}')

while True:
	p = socket.recv()
	d = pickle.loads(p)
	print(d.print())
