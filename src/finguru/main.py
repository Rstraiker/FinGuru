from menu import *
from operacoes import sm

engine = sm.create_engine("sqlite:///database.db")
sm.SQLModel.metadata.create_all(engine)
menu()