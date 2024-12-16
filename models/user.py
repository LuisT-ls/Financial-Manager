from dataclasses import dataclass, field
from typing import List
from models.transaction import Transaction

@dataclass
class User:
    name: str
    email: str
    transactions: List[Transaction] = field(default_factory=list)
    
    def add_transaction(self, transaction: Transaction):
        """Adiciona uma nova transação"""
        transaction.validate()
        self.transactions.append(transaction)
    
    def get_balance(self):
        """Calcula o saldo total"""
        return sum(
            t.amount if t.transaction_type in [TransactionType.INCOME, TransactionType.INVESTMENT] 
            else -t.amount 
            for t in self.transactions
        )