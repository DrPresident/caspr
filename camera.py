#!/usr/bin/python

from picamera import PiCamera
from time import sleep
import socket
import threading

class Camera:
    def __init__(self, res=(640, 480), fps=24):
        self.cam = PiCamera()
        self.cam.resolution = res
        self.cam.framerate = fps

    def capture(self, output="capture.png"):
        cam.capture(output)

    def stream(self, port=4200):
        # Connect a client socket to my_server:8000 (change my_server to the
        # hostname of your server)
        stream_sock = socket.socket()
        conn = None
        try:
            stream_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print 'gonna bind'
            stream_sock.bind(('0.0.0.0', port))
            print 'gonna listen'
            stream_sock.listen(0)
            print "camera feed on port", port, "h264 encoding"

            # Make a file-like object out of the connection
            # sock, addr = client_socket.accept()
            rsock, addr = stream_sock.accept()
            print "Connected:", addr
            conn = rsock.makefile('wb')
            try:
                # Start a preview and let the camera warm up for 2 seconds
                self.cam.start_preview()
                sleep(2)
                self.cam.start_recording(conn, format='h264')
                while True:
                    self.cam.wait_recording(100)
            finally:
                self.cam.stop_recording(1)
        finally:
            if conn is not None:
                conn.close()
            stream_sock.close()

    def start(self):
        daemon = threading.Thread(target=self.stream)
        daemon.setDaemon(True)
        daemon.start()


if __name__ == "__main__":
    cam = Camera(fps=10)
    cam.stream()

