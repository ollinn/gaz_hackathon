import sqlalchemy as db
from sqlalchemy.orm import declarative_base, relationship


class PreBase:
    id = db.Column(db.Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class AuditMixin:
    date_created = db.Column(db.Date)
    date_modified = db.Column(db.Date)
    created_by = db.Column(db.String(30))
    modified_by = db.Column(db.String(30))


class Department(Base, AuditMixin):
    __tablename__ = 'stg_department'
    name = db.Column(db.String(50))
    type = db.Column(db.String(50))
    ref_id = db.Column(db.Integer, db.ForeignKey('stg_department.id'))
    head_department = relationship(
        lambda: Department,
        remote_side=lambda: Department.id,
        backref='sub_departments')

    def __repr__(self):
        return f'{self.name}'


def create_db(engine):
    Base.metadata.create_all(engine)
