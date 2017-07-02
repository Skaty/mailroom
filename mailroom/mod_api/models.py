from ..mailroom import db
from ..common.models import Base

class Mailbox(Base):
    email = db.Column(db.String(256), nullable=False, unique=True)
