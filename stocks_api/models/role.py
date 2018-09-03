from .associations import roles_association
from sqlalchemy.orm import relationship
from .meta import Base
from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
)


class AccountRole(Base):
    """
    This is for the account role table. to assign roles to a
    particular account.
    """
    __tablename__ = 'account_roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    accounts = relationship('Account', secondary=roles_association, back_populates='roles')
