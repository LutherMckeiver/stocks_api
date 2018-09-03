from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)


from .meta import Base


class Stock(Base):
    """
    Will populate the stock table in the database.
    """
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    company_name = Column(Text)
    exchange = Column(Integer)
    industry = Column(Text)
    website = Column(Text)
    description = Column(Text)
    ceo = Column(Text)
    issue_type = Column(Text)
    sector = Column(Text)

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    @classmethod
    def new(cls, request, **kwargs):
        """
        Creation of a new record in the table.
        """
        if request.dbsession is None:
            raise DBAPIError
        stocks = cls(**kwargs)
        request.dbsession.add(stocks)

        return request.dbsession.query(cls).filter(
            cls.stock == kwargs['symbol']).one_or_none()

    @classmethod
    def one(cls, request=None, pk=None):
        """
        This will find the one stock that the user is looking for.
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)

    @classmethod
    def destroy(cls, request=None, pk=None):
        """
        This will destroy the record.
        """
        if request.dbsession is None:
            raise DBAPIError

        # return request.dbsession.query(cls).get(pk).delete()
        return request.dbsession.query(cls).filter(
            cls.accounts.email == request.authenticated_userid).filter(
                cls.id == pk).delete()
