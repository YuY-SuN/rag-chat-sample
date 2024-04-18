from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# ベースクラスの定義
Base = declarative_base()

# user テーブルのクラス定義
class User(Base):
    __tablename__ = 'user'
    id = Column(String, primary_key=True)

    # history テーブルとのリレーション（1対多）
    histories = relationship("History", back_populates="user")

