# ui/gui_interface.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from models.transaction import Transaction, TransactionType
from models.user import User
from database.database import DatabaseManager
from services.analysis_service import FinancialAnalysisService
from services.recommendation_service import RecommendationService

class FinancialManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Controle Financeiro Pessoal")
        self.master.geometry("800x600")

        # Inicialização de componentes
        self.user = User("Usuário Padrão", "usuario@email.com")
        self.db_manager = DatabaseManager()

        # Estilos
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12))

        # Layout principal
        self.create_main_layout()

    def create_main_layout(self):
        # Frame principal
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Seção de Adicionar Transação
        add_transaction_frame = ttk.LabelFrame(main_frame, text="Adicionar Transação", padding="10")
        add_transaction_frame.pack(fill=tk.X, pady=10)

        # Campos de entrada
        ttk.Label(add_transaction_frame, text="Valor:").grid(row=0, column=0, sticky="w")
        self.valor_entry = ttk.Entry(add_transaction_frame, width=20)
        self.valor_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_transaction_frame, text="Descrição:").grid(row=1, column=0, sticky="w")
        self.descricao_entry = ttk.Entry(add_transaction_frame, width=20)
        self.descricao_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_transaction_frame, text="Categoria:").grid(row=2, column=0, sticky="w")
        self.categoria_entry = ttk.Entry(add_transaction_frame, width=20)
        self.categoria_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(add_transaction_frame, text="Tipo:").grid(row=3, column=0, sticky="w")
        self.tipo_var = tk.StringVar()
        tipos = ["Receita", "Despesa", "Investimento"]
        self.tipo_combo = ttk.Combobox(add_transaction_frame, textvariable=self.tipo_var, values=tipos, state="readonly")
        self.tipo_combo.grid(row=3, column=1, padx=5, pady=5)
        self.tipo_combo.set("Despesa")

        # Botão de adicionar transação
        add_btn = ttk.Button(add_transaction_frame, text="Adicionar Transação", command=self.adicionar_transacao)
        add_btn.grid(row=4, column=0, columnspan=2, pady=10)

        # Seção de Relatórios
        relatorios_frame = ttk.LabelFrame(main_frame, text="Relatórios", padding="10")
        relatorios_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Botões de relatórios
        btn_frame = ttk.Frame(relatorios_frame)
        btn_frame.pack(fill=tk.X)

        ttk.Button(btn_frame, text="Fluxo de Caixa", command=self.mostrar_fluxo_caixa).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Gastos por Categoria", command=self.mostrar_gastos_categoria).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Recomendações", command=self.mostrar_recomendacoes).pack(side=tk.LEFT, padx=5)

        # Lista de transações
        self.transaction_tree = ttk.Treeview(relatorios_frame, columns=('Data', 'Descrição', 'Valor', 'Categoria', 'Tipo'), show='headings')
        self.transaction_tree.pack(fill=tk.BOTH, expand=True, pady=10)

        # Definindo cabeçalhos
        for col in ('Data', 'Descrição', 'Valor', 'Categoria', 'Tipo'):
            self.transaction_tree.heading(col, text=col)
            self.transaction_tree.column(col, width=100)

        # Atualizar lista de transações
        self.atualizar_lista_transacoes()

    def adicionar_transacao(self):
        try:
            valor = float(self.valor_entry.get())
            descricao = self.descricao_entry.get()
            categoria = self.categoria_entry.get()
            tipo_str = self.tipo_var.get()

            # Mapear tipo de transação
            tipo_mapeamento = {
                "Receita": TransactionType.INCOME,
                "Despesa": TransactionType.EXPENSE,
                "Investimento": TransactionType.INVESTMENT
            }
            transaction_type = tipo_mapeamento.get(tipo_str, TransactionType.EXPENSE)

            # Criar e salvar transação
            transaction = Transaction(
                amount=valor,
                description=descricao,
                category=categoria,
                transaction_type=transaction_type
            )

            self.user.add_transaction(transaction)
            self.db_manager.save_transaction(transaction)

            # Limpar campos
            self.valor_entry.delete(0, tk.END)
            self.descricao_entry.delete(0, tk.END)
            self.categoria_entry.delete(0, tk.END)

            # Atualizar lista de transações
            self.atualizar_lista_transacoes()

            messagebox.showinfo("Sucesso", "Transação adicionada com sucesso!")

        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def atualizar_lista_transacoes(self):
        # Limpar a lista atual
        for i in self.transaction_tree.get_children():
            self.transaction_tree.delete(i)

        # Recuperar e popular lista de transações
        transactions = self.db_manager.get_transactions()
        for transaction in transactions:
            self.transaction_tree.insert('', 'end', values=(
                transaction.date.strftime("%Y-%m-%d"),
                transaction.description,
                f"R$ {transaction.amount:.2f}",
                transaction.category,
                transaction.transaction_type.name
            ))

    def mostrar_fluxo_caixa(self):
        transactions = self.db_manager.get_transactions()
        monthly_flow = FinancialAnalysisService.calculate_monthly_cash_flow(transactions)

        # Criar figura do matplotlib
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(monthly_flow.keys(), monthly_flow.values())
        ax.set_title('Fluxo de Caixa Mensal')
        ax.set_xlabel('Mês')
        ax.set_ylabel('Valor')
        plt.xticks(rotation=45)

        # Criar janela popup para o gráfico
        popup = tk.Toplevel(self.master)
        popup.title("Fluxo de Caixa Mensal")
        
        # Incorporar gráfico do matplotlib no Tkinter
        canvas = FigureCanvasTkAgg(fig, master=popup)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)

        canvas.draw()

    def mostrar_gastos_categoria(self):
        transactions = self.db_manager.get_transactions()
        spending_categories = FinancialAnalysisService.get_spending_by_category(transactions)

        # Criar figura do matplotlib
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.pie(spending_categories.values(), labels=spending_categories.keys(), autopct='%1.1f%%')
        ax.set_title('Gastos por Categoria')

        # Criar janela popup para o gráfico
        popup = tk.Toplevel(self.master)
        popup.title("Gastos por Categoria")
        
        # Incorporar gráfico do matplotlib no Tkinter
        canvas = FigureCanvasTkAgg(fig, master=popup)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)

        canvas.draw()

    def mostrar_recomendacoes(self):
        transactions = self.db_manager.get_transactions()
        recommendations = RecommendationService.generate_savings_suggestions(transactions)

        # Criar janela popup para recomendações
        popup = tk.Toplevel(self.master)
        popup.title("Recomendações de Economia")
        popup.geometry("400x300")

        # Adicionar recomendações em uma lista
        listbox = tk.Listbox(popup, font=("Arial", 12))
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Popular lista de recomendações
        for recommendation in recommendations:
            listbox.insert(tk.END, recommendation)
