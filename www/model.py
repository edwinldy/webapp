# 导入:
# UniqueConstraint用于unique约束条件
from sqlalchemy import Column, String, Text, Float, Boolean, UniqueConstraint, ForeignKey
from database import Base
import time, uuid
from datetime import datetime

def next_id():
    #根据时间生成一个长度为50字节的uuid
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'users'

    # 表的结构:
    id = Column(String(50), default=next_id(), primary_key=True)
    email = Column(String(50), unique=True) # unique=True，必须唯一
    passwd = Column(String(50))
    admin = Column(Boolean(), default=False)
    name = Column(String(50))
    image = Column(String(500), default='about:blank')
    created_at = Column(Float(), default=time.time)
    # 将model转成dict
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Questionnaire(Base):
    __tablename__ = 'questionnaire'

    id = Column(String(50), default=next_id(), primary_key=True)
    content = Column(String(100))
    created_by = Column(String(50))
    created_at = Column(Float(), default=time.time)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Topic(Base):
    __tablename__ = 'topics'

    id = Column(String(50), default=next_id(), primary_key=True)
    questionnaire_id = Column(String(50))
    content = Column(String(100))
    topic_type = Column(Boolean(), default=True)
    created_at = Column(Float(), default=time.time)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Menu(Base):
    __tablename__ = 'menus'

    id = Column(String(32), default=uuid.uuid4().hex, primary_key=True)
    content = Column(String(50))
    date = Column(String(10))
    created_at = Column(Float(), default=time.time)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Vote(Base):
    __tablename__ = 'votes'

    id = Column(String(50), default=next_id(), primary_key=True)
    menu_id = Column(String(32))
    user_id = Column(String(50))
    created_at = Column(Float(), default=time.time)

'''
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:r00t@localhost:3306/awesome')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
#new_user = User(email="test@example.com", passwd='123456',name='test',)
# 添加到session:
#session.add(new_user)
# 提交即保存到数据库:
#session.commit()
# 关闭session:
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).all()
# 打印类型和对象的name属性:
print('type:', type(user))
for l in user:
    print(l.name)
#print('name:', user.name)

session.close()
'''
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import scoped_session, sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    engine = create_engine('mysql+mysqlconnector://root:r00t@localhost:3306/restaurant')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    Base = declarative_base()
    # new_user = User(email="admin@example.com", passwd='123456',name='amin',)
    # session.add(new_user)
    # session.commit()
    # new_quest = Questionnaire(content="5月17日调查表", created_by="001463472966399b7664da00f414ba4871ecc55191c129d000")
    # session.add(new_quest)
    # session.commit()
    # new_topic1 = Topic(questionnaire_id="0014634734250430f78a3e3f9924c18ba66e9a64cdc2c54000", content="菜品1")
    # new_topic2 = Topic(questionnaire_id="0014634734250430f78a3e3f9924c18ba66e9a64cdc2c54000", content="菜品2")
    # new_topic3 = Topic(questionnaire_id="0014634734250430f78a3e3f9924c18ba66e9a64cdc2c54000", content="菜品3")
    # session.add(new_topic1)
    # session.add(new_topic2)
    # session.add(new_topic3)
    # session.commit()
    # Menu.metadata.create_all(bind=engine)
