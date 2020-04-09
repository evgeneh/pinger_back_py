from app import db, ma
from datetime import datetime

class Host(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(64), unique=True)
    is_available = db.Column(db.Boolean, default=False)
    per_loss = db.Column(db.Integer, default=100)
    min_latency = db.Column(db.Float, default=0)
    max_latency = db.Column(db.Float, default=0)
    avg_latency = db.Column(db.Float, default=0)
    jitter = db.Column(db.Float, default=0)
    updated = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Host, self).__init__(*args, **kwargs)

    def __repr__(self):
        return  '<Host id: {}, ip: {}, loss: {}%>'.format(self.id, self.ip, self.per_loss)

class HostSchema(ma.ModelSchema):
    class Meta:
        model = Host