import sqlmodel as sm
from typing import Optional

class operacao(sm.SQLModel, table=True):
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    categoria: str
    valor: float
    tipo: str  # 'debito' ou 'credito'


def debitar(categoria: str, valor: float):
    # fazer todo o processo
    print("operação realizada com sucesso")
    
def creditar(categoria: str, valor: float):
    print("operação realizada com sucesso")