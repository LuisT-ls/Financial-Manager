# database/database.py
import sqlite3
import json
from typing import List
from datetime import datetime  # Adicionando esta importação
from models.transaction import Transaction, TransactionType
from models.user import User

class DatabaseManager:
    def __init__(self, db_path='financial_manager.db'):
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self):
        """Cria tabelas necessárias no banco de dados"""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                amount REAL,
                description TEXT,
                date TEXT,
                category TEXT,
                transaction_type TEXT
            )
        ''')
        self.conn.commit()
    
    def save_transaction(self, transaction: Transaction):
        """Salva uma transação no banco de dados"""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO transactions 
            (amount, description, date, category, transaction_type) 
            VALUES (?, ?, ?, ?, ?)
        ''', (
            transaction.amount, 
            transaction.description, 
            transaction.date.isoformat(), 
            transaction.category,
            transaction.transaction_type.name
        ))
        self.conn.commit()
    
    def get_transactions(self):
        """Recupera todas as transações"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM transactions')
        transactions = []
        for row in cursor.fetchall():
            transactions.append(Transaction(
                amount=row[1],
                description=row[2],
                date=datetime.fromisoformat(row[3]),
                category=row[4],
                transaction_type=TransactionType[row[5]]
            ))
        return transactions