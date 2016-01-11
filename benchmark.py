import redis
import threading
import time
import logging

FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(filename='redis-benchmark.log', level=logging.INFO, format=FORMAT)

def worker(id):
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	while True: # Infinite loop for workers
		logging.info("Running worker id: %d" % id)
		try:
			r.set('redis-benchmark-worker%d' % id, time.time())
			r.get('redis-benchmark-worker%d' % id)
			#r.delete('redis-benchmark-worker%d' % id)
			time.sleep(1)
		except:
			logging.critical("Lost redis. Trying to reconnect.")
			r = redis.StrictRedis(host='localhost', port=6379, db=0)
	return

threads = []

for i in range(0,2): # Change this for number of workers 
	t = threading.Thread(target=worker, args=(i,))
	threads.append(t)
	t.start()
