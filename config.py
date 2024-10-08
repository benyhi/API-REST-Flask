from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./base_de_datos.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#CREAR DE NUEVO LA BD SIN UTILIZAR BASE DE SESSION YA QUE SQLALCHEMY
# SE ENCARGA AUTOMATICAMENTE DE ESTO.