from app import app
from flask import jsonify, request
from models import Host, HostSchema

from scheduling import th

@app.route('/api/1.0/test')
def index():   
    
    return 'ok'


@app.route('/api/1.0/host', methods=['POST'])  
def create_host():
    if request.methods == 'POST':
        ip = (request.json['ip'])
    
        try:
            host = Host.query.filter(Host.ip == ip).first()
            if host is not None:
                return jsonify({'success': False, "error": "this host already exists with id " + host.id})
            host = Host(ip=ip)
            db.session.add(host)
            db.session.commit()
            return jsonify({'success': True, "error": null})
        except:
            error ='ip upload error'
            return jsonify({'success': False, "error": error})



@app.route('/api/1.0/host/<hostid>', methods=['GET', 'DELETE'])  
def return_host(hostid):     
    if request.method == 'GET':
        try:  
            id = int(hostid)    
            host = Host.query.filter(Host.id == id).first()
            host_schema = HostSchema()
            host_data = host_schema.dump(host)
            return jsonify({'success': True, "error": 'null', 'data': host_data})
        except:
            error ='finding host error'
            return jsonify({'success': False, "error": error})
    elif request.method == 'DELETE':
        try:
            db.session.query(Host).filter(Host.id == hosid).delete()
            db.session.commit()
            return jsonify({'success': True, "error": 'null', 'data': host_data})
        except:
            return jsonify({'success': False, "error": 'Delete host error'})


@app.route('/api/1.0/hosts', methods=['GET'])  
def return_hosts_list(): 
    try:

        hosts = Host.query.all()     
        host_schema = HostSchema(many=True)    
        hosts_list = host_schema.dump(hosts)
        print(hosts_list)

        return jsonify({'success': True, "error": 'null', 'data': hosts_list})
    except:
        return jsonify({'success': False, "error": 'Get ip list error'})


    