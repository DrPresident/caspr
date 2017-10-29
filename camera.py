#!/usr/bin/python

from picamera import PiCamera
from time import sleep
import socket

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
        stream_sock.bind(('0.0.0.0', port))
        stream_sock.listen(0)
        print "Listening on port", port

        # Make a file-like object out of the connection
        # sock, addr = client_socket.accept()
        rsock, addr = stream_sock.accept()
        print "Connected:", addr
        conn = rsock.makefile('wb')
        try:
            # Start a preview and let the camera warm up for 2 seconds
            self.cam.start_preview()
            sleep(2)
            # Start recording, sending the output to the connection for 60
            # seconds, then stop
            self.cam.start_recording(conn, format='h264')
            while True:
                pass
        finally:
            self.cam.stop_recording()
            conn.close()
            stream_sock.close()

    def start(self):
        self.daemon = threading.Thread(target=self.stream)
        self.daemon.setDaemon(True)
        self.daemon.start()


if __name__ == "__main__":
    cam = Camera()
    cam.stream()

