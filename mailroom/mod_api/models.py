from ..mailroom import db
from ..common.models import Base

class Mailbox(Base):
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    is_visible = db.Boolean()

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
