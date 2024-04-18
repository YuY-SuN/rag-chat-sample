from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# ベースクラスの定義
Base = declarative_base()

# history テーブルのクラス定義
class History(Base):
    __tablename__ = 'history'
    userid = Column(String, ForeignKey('user.id'), primary_key=True)
    talkid = Column(String, primary_key=True)
    talknum = Column(Integer)
    text = Column(String)

    # user テーブルとのリレーション（多対1）
    user = relationship("User", back_populates="histories")

