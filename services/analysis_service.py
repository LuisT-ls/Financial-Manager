from typing import List
from models.transaction import Transaction, TransactionType
from collections import defaultdict
from datetime import datetime, timedelta

class FinancialAnalysisService:
    @staticmethod
    def calculate_monthly_cash_flow(transactions: List[Transaction]):
        """Calcula o fluxo de caixa mensal"""
        monthly_flow = defaultdict(float)
        for transaction in transactions:
            month_key = transaction.date.strftime("%Y-%m")
            if transaction.transaction_type == TransactionType.INCOME:
                monthly_flow[month_key] += transaction.amount
            else:
                monthly_flow[month_key] -= transaction.amount
        return dict(monthly_flow)
    
    @staticmethod
    def get_spending_by_category(transactions: List[Transaction]):
        """Agrupa despesas por categoria"""
        categories = defaultdict(float)
        for transaction in transactions:
            if transaction.transaction_type == TransactionType.EXPENSE:
                categories[transaction.category] += transaction.amount
        return dict(categories)
