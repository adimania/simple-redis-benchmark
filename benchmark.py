import redis
import threading
import time

def worker(id):
	while True: # Infinite loop for workers
		print "Running worker id: %d" % id	
		r = redis.StrictRedis(host='localhost', port=6379, db=0)
		r.set('redis-benchmark-worker%d' % id, time.time())
		r.get('redis-benchmark-worker%d' % id)
		#r.delete('redis-benchmark-worker%d' % id)
		time.sleep(1)
	return

threads = []

for i in range(0,2): # Change this for number of workers 
	t = threading.Thread(target=worker, args=(i,))
	threads.append(t)
	t.start()
