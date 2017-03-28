import RPi.GPIO as io

io.setmode(io.BCM)

io.setup(21,io.OUT)
io.setup(20,io.OUT)
io.setup(19,io.OUT)
io.setup(26,io.OUT)

def rotate_left():
    io.output(21,True)
    io.output(20,False)
    io.output(19,False)
    io.output(26,True)
def rotate_right():
    io.output(21,False)
    io.output(20,True)
    io.output(19,True)
    io.output(26,False)

def back():
	io.output(21,True)
	io.output(20,False)
	io.output(19,True)
	io.output(26,False)

def forward():
	io.output(21,False)
	io.output(20,True)
	io.output(19,False)
	io.output(26,True)

def stop():
	io.output(21,False)
	io.output(20,False)
	io.output(19,False)
	io.output(26,False)

