import cv2
import threading,queue,time

class BufferedVideoWriter(cv2.VideoWriter):
    def __init__(self,filename,fourcc,fps,frameSize,maxBufferSize=25):
        cv2.VideoWriter.__init__(self,filename=filename,fourcc=fourcc,fps=fps,frameSize=frameSize)
        self.thread=None
        self.queue=queue.Queue()
        self.fps=fps
        self.maxBufferSize=maxBufferSize
    def start(self):
        if self.thread:
            return
        dt=1/self.fps
        def loop():
            t=time.time()
            while self.thread or self.queue.qsize():
                frame,ts=self.queue.get()
                while t<ts:
                    cv2.VideoWriter.write(self,frame)
                    t+=dt
        self.thread=threading.Thread(target=loop)
        self.thread.start()
    def stop(self):
        if not self.thread:
            return
        t=self.thread
        self.thread=None
        t.join()
        self.release()
    def write(self,image):
        if self.thread and self.queue.qsize()<self.maxBufferSize:
            return self.queue.put((image,time.time()))
        
        
   