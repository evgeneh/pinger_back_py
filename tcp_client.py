import socket
import threading
import json


TCP_IP = '127.0.0.1'
TCP_PORT = 8001

from types import SimpleNamespace as Namespace

def run_client(ip_str):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    #convert object of adreses to jsonify string
    s = bytes(ip_str, 'utf-8')
    sock.send(s)
    #wait for result data
    result = sock.recv(1024)
    res_str = result.decode('utf-8')
    res = json.loads(res_str, object_hook=lambda d: Namespace(**d))
    
    print(res.data[0].ip)
    sock.close()
    return res