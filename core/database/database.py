from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Float, MetaData, ForeignKey, BigInteger
from threading import Lock
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


lock = Lock()
engine = create_engine('postgresql://username:password@postgresql:5432/titan',
                       echo=True)

metadata = MetaData()


OHLCV = Table('OHLCV', metadata,
              Column('ID', Integer, primary_key=True),
              Column('Exchange', String),
              Column('Pair', String),
              Column('Timestamp', String),
              Column('Open', Float),
              Column('High', Float),
              Column('Low', Float),
              Column('Close', Float),
              Column('Volume', Float),
              Column('Interval', String),
              Column('TimestampRaw', BigInteger),
              Column('PairID', Integer, ForeignKey('TradingPairs.ID')),
              )

TradingPairs = Table('TradingPairs', metadata,
                     Column('ID', Integer, primary_key=True),
                     Column('Exchange', String),
                     Column('BaseCurrency', String),
                     Column('QuoteCurrency', String),
                     Column('Interval', String)
                     )


TradingOrders = Table('TradingOrders', metadata,
                      Column('Timestamp', String),
                      Column('OrderID', Integer, primary_key=True),
                      Column('Exchange', String),
                      Column('Pair', String),
                      Column('Position', String),
                      Column('Amount', Float),
                      Column('Price', Float),
                      Column('Simulated', String)
                      )


def drop_tables():
    print('Dropping tables...')
    metadata.drop_all(engine)


def create_tables():
    metadata.create_all(engine)


def reset_db():
    print('Resetting database...')
    drop_tables()
    create_tables()
