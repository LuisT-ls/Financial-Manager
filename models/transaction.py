from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto

class TransactionType(Enum):
    INCOME = auto()
    EXPENSE = auto()
    INVESTMENT = auto()

@dataclass
class Transaction:
    amount: float
    description: str
    date: datetime = field(default_factory=datetime.now)
    category: str = ''
    transaction_type: TransactionType = TransactionType.EXPENSE
    
    def validate(self):
        """Validações básicas para uma transação"""
        if self.amount <= 0:
            raise ValueError("Valor da transação deve ser positivo")
        if not self.description:
            raise ValueError("Descrição não pode estar vazia")