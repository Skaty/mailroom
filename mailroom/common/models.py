from ..mailroom import db

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

    def as_dict(self, keys = None):
        if keys is None:
            keys = [c.name for c in self.__table__.columns]
        return {c: getattr(self, c) for c in keys if c in self.__table__.columns}
