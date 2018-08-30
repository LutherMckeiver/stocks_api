from .meta import Base
from datetime import datetime as dt
from .associations import roles_association
from sqlalchemy.orm import relationship
from sqlalchemy.exc import DBAPIError
from cryptacular import bcrypt
from sqlalchemy import(
Column,
Index,
Integer,
Text,
String,
DateTime
)


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullabe=False, unique=True)
    password = Column(Text, nullable=False)
    locations = relationship(back_populates='account',)
    roles = relationship(AccountRole, secondary=roles_association, back_populates='accounts')
    
    date_created = Column(Integer, primary_key=True)
    date_updated = Column(Integer, primary_key=True)

    def __init__(self, email=None, password=None)
    self.email = email
    self.password = manager.encode(password, 10)

    @classmethod
    def new(cls, request, email=None, password=None):
        pass
        if request.dbsession is None:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)

        # Todo Assign roles to new user
        admin_role = request.dbsession.query(AccountRole).filter(
            AccountRole.name == 'admin').one_or_none()

        user.roles.append(admin_role)
        request.dbsession.flush()

        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()
    @classmethod
    def one(cls, request, email=None):
        return request.dbsession.query(cls).filter(
            cls.email ==email).one_or_none)

    @classmethod
    def check_credentials(cls, request, email, password):
        pass
        if request.dbsession is None:
            raise DBAPIError

        try:
            account = request.dbsession.query(cls).filter(
                cls.email == email) one_or_none()
        except DBAPIError:
            return None

        if account is not None:
            # if manager.check(account.password,)

        return None
