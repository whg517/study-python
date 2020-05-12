import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker(bind=engine)


class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True, autoincrement=True)


Base = declarative_base(cls=Base)


class User(Base):
    name = Column(String)

    addresses = relationship(
        'Address',
        backref='user',
        cascade='all, delete-orphan',
        passive_deletes=True
    )


class Address(Base):
    location = Column(String)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))


def init_db():
    s = Session()
    u1 = User(name='xxx')
    u2 = User(name='xxx')
    a1 = Address(location='aaa', user=u1)
    a2 = Address(location='aaa', user=u1)
    s.add_all([
        u1, u2,
        a1, a2
    ])
    s.commit()
    s.close()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    init_db()
    session = Session()
    user = session.query(User).first()
    # res = session.query(Address).filter(Address.user_id == user.id).all()
    res = session.query(User).join(Address)
    print(res)
