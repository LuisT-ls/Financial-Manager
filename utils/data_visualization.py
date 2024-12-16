import matplotlib.pyplot as plt

class DataVisualizer:
    @staticmethod
    def plot_monthly_cash_flow(monthly_flow: dict):
        """Gera gráfico de fluxo de caixa mensal"""
        plt.figure(figsize=(10, 5))
        plt.bar(monthly_flow.keys(), monthly_flow.values())
        plt.title('Fluxo de Caixa Mensal')
        plt.xlabel('Mês')
        plt.ylabel('Valor')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('monthly_cash_flow.png')
        plt.close()
    
    @staticmethod
    def plot_spending_by_category(categories: dict):
        """Gera gráfico de gastos por categoria"""
        plt.figure(figsize=(8, 8))
        plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
        plt.title('Gastos por Categoria')
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig('spending_categories.png')
        plt.close()