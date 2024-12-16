# services/recommendation_service.py
from typing import List
from models.transaction import Transaction, TransactionType
from services.analysis_service import FinancialAnalysisService

class RecommendationService:
    @staticmethod
    def generate_savings_suggestions(transactions: List[Transaction]):
        """Gera sugestões de economia baseadas nos dados"""
        spending_by_category = FinancialAnalysisService.get_spending_by_category(transactions)
        suggestions = []
        
        for category, total_spent in spending_by_category.items():
            if total_spent > 500:  # Exemplo de threshold para sugestões
                suggestions.append(f"Considere reduzir gastos em {category}")
        
        return suggestions