from ..mailroom import db

class Base(db.Model):
    """Base Model class which is inherited from other Models"""
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    
    @property
    def serialize(self):
        """Serializes the Model data instance"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def serialize_some(self, columns = None):
        """Serializes only columns that are specified in the columns argument"""
        if columns is None:
            columns = [c.name for c in self.__table__.columns]
        return {c: getattr(self, c) for c in columns if c in self.__table__.columns}