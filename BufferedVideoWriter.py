import cv2
import threading,queue,time

class BufferedVideoWriter:
	def __init__(self,filename,fourcc,fps,frameSize,maxBufferSize=25):
		self.fourcc=fourcc
		self.thread=None
		self.queue=queue.Queue()
		self.fps=fps
		self.maxBufferSize=maxBufferSize
		self.frameSize=frameSize
		self.filename=filename
	def start(self):
		if self.thread:
			return
		dt=1./self.fps
		def loop():
			writer=cv2.VideoWriter(filename=self.filename,fourcc=self.fourcc,fps=self.fps,frameSize=self.frameSize)
			t=time.time()
			self.queue.put((cv2.rectangle(self.frameSize, (0, 0), self.frameSize, (0, 0, 0), -1),t))
			while self.thread or self.queue.qsize():
				frame,ts=self.queue.get()
				if frame is None:
					break
				while t<ts:
					writer.write(frame)
					t+=dt
			writer.release()
		self.thread=threading.Thread(target=loop)
		self.thread.start()
	def stop(self):
		if not self.thread:
			return
		self.write(None)
		t=self.thread
		self.thread=None
		t.join()
		
	def write(self,image):
		if self.thread and self.queue.qsize()<self.maxBufferSize:
			return self.queue.put((image,time.time()))
		
		
   
