"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import *
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql import func

# TODO: Complete your models
class Problem(Base):
    __tablename__ = "problems"

    # Columns
    title = Column("title", TEXT, primary_key=True)
    content = Column("content", TEXT, nullable=False)
    answer = Column("answer", TEXT, nullable=False)
    subject = Column("subject", TEXT)
    solved_by = relationship("User", secondary= "solves", back_populates="problems_solved")

    def __init__(self, title, content, answer, subject):
        self.title = title
        self.content = content
        self.answer = answer
        self.subject = subject
    
    def __repr__(self):
        return self.title + "\n" + self.content

class User(Base):
    __tablename__ = "users"

    # Columns
    username = Column("username", TEXT, primary_key=True)
    password = Column("password", TEXT, nullable=False)
    problems_solved = relationship("Problem", secondary="solves", back_populates="solved_by")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return self.username

class Solve(Base):
    __tablename__ = "solves"

    id = Column("id", INTEGER, primary_key=True, autoincrement=True)
    problem_id = Column("problem_id", ForeignKey("problems.title"))
    user_id = Column("user_id", ForeignKey("users.username"))

    # credit to stack overflow user Jeff Widman
    # https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
    time_solved = Column(DateTime(timezone=True), server_default=func.now())


    def __init__(self, problem_id, user_id):
        self.problem_id = problem_id
        self.user_id = user_id