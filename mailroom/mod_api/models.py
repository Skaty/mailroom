from ..mailroom import db
from ..common.models import Base

class Mailgroup(Base):
    name = db.Column(db.String(256), nullable=False)
    mailboxes = db.relationship('Mailbox', backref='mailgroup', lazy='dynamic')

    @property
    def serialize(self):
        serialized = super().serialize
        serialized['mailboxes'] = [mailbox.serialize for mailbox in self.mailboxes.all() if mailbox.is_visible]
        return serialized

class Mailbox(Base):
    mailgroup_id = db.Column(db.Integer, db.ForeignKey('mailgroup.id'))
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    template = db.Column(db.Text(), nullable=False)
    is_visible = db.Column(db.Boolean())

    @property
    def serialize(self):
        return self.serialize_some(['id', 'name'])
