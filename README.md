# Sistema de Controle Financeiro Pessoal

## 📌 Descrição do Projeto

Um sistema abrangente de gerenciamento financeiro pessoal desenvolvido em Python, projetado para ajudar usuários a controlar, analisar e otimizar suas finanças de maneira simples e intuitiva.

## ✨ Funcionalidades

### Principais Recursos

- Registro de receitas e despesas
- Categorização de transações
- Visualização de fluxo de caixa
- Análise de gastos por categoria
- Geração de relatórios financeiros
- Interface gráfica amigável

### Recursos Detalhados

- Suporte a diferentes tipos de transações (Receita, Despesa, Investimento)
- Gráficos interativos de desempenho financeiro
- Recomendações automáticas de economia
- Armazenamento local de dados

## 🛠 Tecnologias Utilizadas

### Principais Bibliotecas

- **Interface Gráfica**: Tkinter
- **Visualização de Dados**: Matplotlib
- **Banco de Dados**: SQLite
- **Linguagem**: Python 3.8+

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- pip
- venv (recomendado)

### Passos de Instalação

1. Clone o repositório

```bash
git clone https://github.com/LuisT-ls/Financial-Manager.git
cd Financial-Manager
```

2. Crie um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# ou
venv\Scripts\activate  # No Windows
```

3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 🖥 Como Usar

### Executando o Projeto

```bash
python main.py
```

### Funcionalidades Principais

1. **Adicionar Transação**

   - Insira valor, descrição, categoria e tipo de transação
   - Tipos: Receita, Despesa, Investimento

2. **Visualizar Transações**

   - Tabela completa de todas as transações registradas

3. **Relatórios**
   - Gráfico de Fluxo de Caixa Mensal
   - Distribuição de Gastos por Categoria
   - Recomendações de Economia

## 📊 Estrutura do Projeto

```
financial_manager/
│
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
│
├── models/                 # Modelos de dados
│   ├── transaction.py
│   └── user.py
│
├── database/               # Gerenciamento de banco de dados
│   └── database.py
│
├── services/               # Serviços de análise
│   ├── analysis_service.py
│   └── recommendation_service.py
│
├── ui/                     # Interface de usuário
│   └── gui_interface.py
│
└── utils/                  # Utilitários
    └── data_visualization.py
```

## 🔜 Roadmap de Desenvolvimento

### Próximas Implementações

- [ ] Sistema de autenticação de usuários
- [ ] Suporte a múltiplas moedas
- [ ] Exportação de relatórios em PDF
- [ ] Integração com APIs bancárias
- [ ] Modo escuro/claro
- [ ] Backup e restauração de dados

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor, siga estas etapas:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona NovaFeature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📧 Contato

Luís Antonio Souza Teixeira

E-mail - luishg213@outlook.com

Link do Projeto: [https://github.com/LuisT-ls/Financial-Manager](https://github.com/LuisT-ls/financial-manager)

---

**Desenvolvido com ❤️ por Luís Teixeira**
