import socket

# put the stuff there needed for this to work
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)  # Set a connection timeout

def get_open_ports(target, port_range, verbose = False):
# the open ports retuns the whole thing 
    open_ports = []
# if the verbose is set to true then it returns a string , im thinkking a if and elif situation here,
# then more for the invalid scenarios. Also strings. so we are going to have several "open_ports"

    return(open_ports)