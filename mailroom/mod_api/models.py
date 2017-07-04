from ..mailroom import db
from ..common.models import Base

class Mailgroup(Base):
    name = db.Column(db.String(256), nullable=False)
    mailboxes = db.relationship('Mailbox', backref='mailgroup', lazy='dynamic')
    
    @property
    def serialize(self):
        serialized = super().serialize
        serialized['mailboxes'] = [mailbox.serialize for mailbox in self.mailboxes.all()]
        return serialized

class Mailbox(Base):
    mailgroup_id = db.Column(db.Integer, db.ForeignKey('mailgroup.id'))
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    is_visible = db.Boolean()
    
    @property
    def serialize(self):
        return self.serialize_some(['id', 'name'])
