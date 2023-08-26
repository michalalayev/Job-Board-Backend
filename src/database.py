from sqlmodel import SQLModel, create_engine
import models.job_models  # need the models to create the tables

mysql_url = "mysql+pymysql://root:root@localhost:3306/project"

engine = create_engine(mysql_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
