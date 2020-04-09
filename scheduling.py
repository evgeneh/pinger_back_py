import schedule
import time
from datetime import datetime

from app import db
from models import Host

from threading import Lock, Thread
from tcp_client import run_client
import json

ilock = Lock()

def base_update(ping_res):
    print(ping_res)
    for val in ping_res.data:
        host = db.session.query(Host).filter(Host.ip == val.ip).first()
        print(host.id)
        if host is not None:
            host.is_available = (int(val.per_loss) < 100 ) 
            host.per_loss =  int(val.per_loss)
            print(host.per_loss)
            if host.is_available:
                host.update(max_latency=float(val.max), min_latency=float(val.min), avg_latency=float(val.avg), jitter=float(val.jitter)) 
                host.updated = datetime.now()
            db.session.commit()

def ping_job():

    host = Host.query.all()
    print(host[0].ip)
    host_array_data = []
    for x in host:
        #fill request object by host list
        host_array_data.append({'ip': x.ip})
    length =  len(host_array_data)

    if length > 0:
        with ilock:
            ping_res = run_client( json.dumps( { 'length': length, 'data': host_array_data} ) )
            
            if int(ping_res.length) > 0:
                base_update(ping_res)
            
        

def start_monitor(): 
    print("----")   
    schedule.every(50).seconds.do(ping_job)
    #schedule.every(5).minutes.do(ping_job)

    while True:
        schedule.run_pending()
        time.sleep(1)


th = Thread(target=start_monitor)