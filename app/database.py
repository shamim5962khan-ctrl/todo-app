from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://neondb_owner:npg_ANYK2csJWP4H@ep-summer-cloud-a8mki4dh-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()