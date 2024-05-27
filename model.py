from sqlalchemy import create_engine, MetaData, Table, select, Column, Integer, String, Date, and_
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///BaseNews.db')

metadata = MetaData()
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base = declarative_base()


class News(Base):
    __tablename__ = 'news'

    NewsID = Column(Integer, primary_key=True)
    Theme = Column(String)
    Title = Column(String)
    Text = Column(String)
    MediaPath = Column(String)
    Date = Column(String)


Base.metadata.create_all(engine)
