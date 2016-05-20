from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+mysqlconnector://root:r00t@localhost:3306/restaurant')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# 创建对象的基类:
Base = declarative_base()
Base.query = db_session.query_property()
'''
if __name__ == "__main__":
    import model
    model.User.metadata.drop_all(bind=engine)
    model.User.metadata.create_all(bind=engine)
'''