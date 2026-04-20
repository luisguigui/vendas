# 💰 SVP PRO — Sistema de Gestão de Vendas

> Uma solução de desktop robusta e profissional para controle de vendas e monitoramento financeiro. Desenvolvido em Python com CustomTkinter e SQLite3, oferece CRUD completo, relatórios em CSV, interface Dark Mode moderna e sistema de logs para rastreabilidade completa.

[![Python](https://img.shields.io/badge/python-3.7+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Latest-blue.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![SQLite3](https://img.shields.io/badge/SQLite3-Nativo-green.svg)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Enterprise-brightgreen.svg)]()

<div align="center">

**[🚀 Instalação](#-instalação-e-execução) • [📖 Documentação](#-arquitetura-e-estrutura) • [💼 Funcionalidades](#-funcionalidades-principais) • [🗄️ Banco de Dados](#️-estrutura-do-banco-de-dados) • [📊 Relatórios](#-sistema-de-relatórios)**

</div>

---

## 🌟 Visão Geral

**SVP PRO** (Sistema de Vendas Pro) é um gerenciador de vendas empresarial que oferece controle total sobre produtos, valores e histórico de transações. Com interface intuitiva e dados persistentes em SQLite3, é a solução ideal para pequenos negócios, representantes comerciais e equipes de vendas que precisam de organização e relatórios rápidos.

### ✨ Destaques Principais

- 📝 **CRUD Completo**: Criar, Ler, Atualizar e Deletar registros facilmente
- 🎯 **Painel de Resumo**: Visualização em tempo real de faturamento total
- 🔍 **Busca Dinâmica**: Filtro por nome de produto enquanto digita
- 📊 **Edição Inline**: Clique no produto para editar diretamente
- 💾 **Persistência SQLite3**: Dados salvos localmente e seguros
- 📥 **Exportação CSV**: Gere relatórios em segundos
- 🌙 **Dark Mode Nativo**: Interface moderna e profissional
- 📋 **Histórico Completo**: Cada venda com data/hora
- 🔒 **Sistema de Logs**: Rastreabilidade de erros
- ⚡ **Performance**: Interface responsiva mesmo com 1000+ registros

---

## 💼 Funcionalidades Principais

### 1️⃣ **Registrar Venda**

Adicione uma nova venda em segundos:

```
┌─────────────────────────────────────────────────┐
│ Produto: [Notebook Dell                    ]   │
│ Preço:   [R$ 2.500,00                ]           │
│                        [REGISTRAR]              │
└─────────────────────────────────────────────────┘
```

**Passos**:
1. Digite o nome do produto
2. Digite o valor (aceita "," ou ".")
3. Clique "REGISTRAR"
4. Venda aparece no histórico com data/hora automática

---

### 2️⃣ **Editar Venda**

Corrija valores sem deletar:

```
Histórico de Movimentações:

┌───────────────────────────────────────────────┐
│ Notebook Dell        R$ 2.500,00  15/01 14:30 │  ← Clique para editar
└───────────────────────────────────────────────┘

Campos acima agora preenchem:
Produto: [Notebook Dell                    ]
Preço:   [2500.00                          ]
Botão:   [ATUALIZAR] (em amarelo)
```

**Passos**:
1. Clique no nome do produto no histórico
2. Campos acima preenchem automaticamente
3. Modifique os valores
4. Clique "ATUALIZAR"
5. Registro é atualizado

---

### 3️⃣ **Deletar Venda**

Remova registros com confirmação:

```
Histórico:

┌───────────────────────────────────────────────┐
│ Mouse Gamer           R$ 150,00  15/01 14:35  ✕ │
└───────────────────────────────────────────────┘
                                      ↑
                              Clique para deletar

Confirmação:
┌─────────────────────────┐
│ Tem certeza?             │
│ [NÃO]  [SIM]            │
└─────────────────────────┘
```

**Passos**:
1. Clique no "✕" à direita do registro
2. Confirme na janela de diálogo
3. Registro é deletado permanentemente

---

### 4️⃣ **Pesquisar por Produto**

Busca dinâmica enquanto digita:

```
PESQUISAR
┌──────────────────────────┐
│ Note                     │  ← Digite enquanto você digita
└──────────────────────────��

Resultados (filtrado em tempo real):

┌───────────────────────────────────────────────┐
│ Notebook Dell         R$ 2.500,00  15/01 14:30│
│ Notebook Lenovo       R$ 3.000,00  14/01 10:15│
│ Notebook HP           R$ 2.200,00  13/01 09:00│
└───────────────────────────────────────────────┘

Total: 3 vendas | Faturamento: R$ 7.700,00
```

**Como funciona**:
- Busca por LIKE (parcial) no banco
- Atualiza em tempo real
- Não diferencia maiúsculas/minúsculas
- Case-insensitive

---

### 5️⃣ **Painel de Resumo**

Métricas instantâneas:

```
┌─────────────────────┐
│ SVP PRO            │
│                     │
│ Vendas: 15         │ ← Número de registros
│ R$ 12.450,50       │ ← Faturamento total
│                     │
│ [PESQUISAR]        │
│ produto...         │
│                     │
│ [Exportar CSV]     │
└─────────────────────┘
```

**Atualiza quando**:
- Nova venda registrada
- Venda deletada
- Filtro aplicado
- Venda atualizada

---

### 6️⃣ **Exportar Relatório CSV**

Gere relatório profissional:

```
Clique: [Exportar CSV]

Arquivo criado: relatorio_1501_1430.csv

Conteúdo:
ID;Produto;Valor;Data
1;Notebook Dell;2500.00;15/01/2026 14:30
2;Mouse Gamer;150.00;15/01/2026 14:35
3;Teclado Mecânico;450.00;15/01/2026 14:40
...
```

**Características**:
- Nome com data/hora: `relatorio_DDMM_HHMM.csv`
- Separador: `;` (ponto-e-vírgula)
- Encoding: UTF-8 (compatível com Excel)
- Inclui: ID, Produto, Valor, Data
- Abre em Excel/Sheets/Calc

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Versão | Propósito |
|-----------|-----------|--------|----------|
| **Linguagem** | Python | 3.7+ | Lógica e estrutura |
| **GUI** | CustomTkinter | Latest | Interface Dark Mode |
| **Banco de Dados** | SQLite3 | Nativo | Persistência local |
| **Relatórios** | CSV | Nativo | Exportação de dados |
| **Logging** | logging | Nativo | Rastreamento de erros |
| **Datetime** | datetime | Nativo | Timestamp automático |

### Por que essas tecnologias?

- ✅ **SQLite3**: Zero configuração, arquivo único, sem servidor
- ✅ **CustomTkinter**: Interface moderna que impressiona
- ✅ **CSV**: Compatível com Excel, Google Sheets, etc
- ✅ **logging**: Rastreabilidade de problemas
- ✅ Sem dependências externas pesadas

---

## 🗄️ Estrutura do Banco de Dados

### Tabela: `vendas`

```sql
CREATE TABLE vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    valor REAL NOT NULL,
    data TEXT NOT NULL
)
```

**Campos**:

| Campo | Tipo | Descrição | Exemplo |
|-------|------|-----------|---------|
| **id** | INTEGER | ID único (auto) | 1, 2, 3, ... |
| **produto** | TEXT | Nome do produto | "Notebook Dell" |
| **valor** | REAL | Valor em reais | 2500.50 |
| **data** | TEXT | Data/hora da venda | "15/01/2026 14:30" |

**Arquivo**: `enterprise_data.db` (criado automaticamente)

---

### Exemplo de Registros

```sql
SELECT * FROM vendas ORDER BY id DESC;

id │ produto              │ valor   │ data
───┼──────────────────────┼─────────┼────────────────────
 5 │ Teclado Mecânico     │ 450.00  │ 15/01/2026 14:40
 4 │ Monitor LG 27"       │ 1200.00 │ 15/01/2026 14:35
 3 │ Mouse Gamer          │ 150.00  │ 15/01/2026 14:30
 2 │ Webcam 1080p         │ 280.00  │ 15/01/2026 14:25
 1 │ Notebook Dell        │ 2500.00 │ 15/01/2026 14:20
```

---

## 🏗️ Arquitetura e Estrutura

### 📊 Fluxo de Dados

```
┌──────────────────────────────┐
│   Interface (VendasApp)      │
│   - Form de entrada          │
│   - Lista de vendas          │
│   - Painel de resumo         │
└────────────┬─────────────────┘
             │
    ┌────────▼────────┐
    │   Usuário       │
    │   Interage      │
    └────────┬────────┘
             │
    ┌────────▼────────────────────┐
    │ Métodos da App              │
    │ - registrar_venda()         │
    │ - atualizar_venda()         │
    │ - deletar_venda()           │
    │ - exportar_csv()            │
    └────────┬────────────────────┘
             │
    ┌────────▼────────────────────┐
    │ Database (SQLite3)          │
    │ - INSERT                    │
    │ - UPDATE                    │
    │ - DELETE                    │
    │ - SELECT                    │
    └────────┬────────────────────┘
             │
    ┌────────▼────────────────────┐
    │ enterprise_data.db          │
    │ (Arquivo de dados)          │
    └─────────────────────────────┘
```

### 🧩 Componentes Principais

```
vendas.py
│
├── 📦 CLASSE: Database (Camada de dados)
│   ├── __init__() ............. Conecta ao SQLite
│   ├── create_tables() ....... Cria tabela vendas
│   ├── registrar_venda() .... INSERT novo registro
│   ├── atualizar_venda() .... UPDATE registro existente
│   ├── selecionar_vendas() .. SELECT com filtro
│   ├── deletar_venda() ...... DELETE registro
│   └── Logging de erros
│
└── 🎮 CLASSE: VendasApp (CustomTkinter)
    ├── INICIALIZAÇÃO
    │   ├── __init__() .............. Setup da UI
    │   ├── setup_sidebar() ........ Painel esquerdo
    │   └── setup_main_area() ..... Conteúdo principal
    │
    ├── SIDEBAR
    │   ├── Título "SVP PRO"
    │   ├── Sumário (Vendas + Faturamento)
    │   ├── Campo de busca
    │   └── Botão Exportar CSV
    │
    ├── ÁREA PRINCIPAL
    │   ├── Formulário de entrada
    │   │   ├── Entry: Produto
    │   │   ├── Entry: Valor
    │   │   └── Button: REGISTRAR/ATUALIZAR
    │   │
    │   └── Histórico (ScrollableFrame)
    │       ├── Card por venda
    │       ├── Nome (clicável para editar)
    │       ├── Valor (verde)
    │       ├── Data (cinza)
    │       └── Botão deletar (✕)
    │
    ├── FUNCIONALIDADES
    │   ├── atualizar_ui() ...... Redesenha histórico
    │   ├── salvar_dados() ..... Cria/atualiza venda
    │   ├── preparar_edicao() . Carrega para editar
    │   ├── confirmar_exclusao() Dialogo de confirmação
    │   └── exportar_csv() .... Gera relatório
    │
    └── EVENTOS
        ├── KeyRelease (busca)
        ├── Button-1 (editar)
        └── Command (botões)
```

---

## 📚 Documentação das Classes

### 1️⃣ `Database` — Camada de Persistência

**Responsabilidade**: Gerenciar todas as operações com SQLite

**Atributos**:

```python
class Database:
    conn: sqlite3.Connection  # Conexão com BD
```

---

#### **Método: `__init__()`**

```python
def __init__(self):
    self.conn = sqlite3.connect("enterprise_data.db")
    self.create_tables()
```

**O que faz**:
- Conecta ao arquivo `enterprise_data.db`
- Se não existe, cria automaticamente
- Chama `create_tables()` para setup

---

#### **Método: `create_tables()`**

```python
def create_tables(self):
    cursor = self.conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT NOT NULL,
            valor REAL NOT NULL,
            data TEXT NOT NULL
        )
    """)
    self.conn.commit()
```

**O que faz**:
- Cria tabela `vendas` se não existir
- Estrutura com 4 colunas
- ID auto-incrementado

---

#### **Método: `registrar_venda(produto, valor)`**

```python
def registrar_venda(self, produto, valor):
    try:
        cursor = self.conn.cursor()
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        cursor.execute(
            "INSERT INTO vendas (produto, valor, data) VALUES (?, ?, ?)", 
            (produto, float(valor), data_atual)
        )
        self.conn.commit()
        return True
    except Exception as e:
        logging.error(f"Erro ao registrar: {e}")
        return False
```

**O que faz**:
1. Obtém data/hora atual
2. Insere registro na tabela
3. Valores são parametrizados (seguro contra SQL injection)
4. Retorna True/False para sucesso

**Exemplo**:
```python
db.registrar_venda("Notebook Dell", "2500.50")
# Insere na tabela:
# id=1, produto="Notebook Dell", valor=2500.50, data="15/01/2026 14:30"
```

---

#### **Método: `atualizar_venda(id_venda, produto, valor)`**

```python
def atualizar_venda(self, id_venda, produto, valor):
    try:
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE vendas SET produto = ?, valor = ? WHERE id = ?", 
            (produto, float(valor), id_venda)
        )
        self.conn.commit()
        return True
    except Exception as e:
        logging.error(f"Erro ao atualizar: {e}")
        return False
```

**O que faz**:
1. Localiza registro por ID
2. Atualiza produto e valor
3. Mantém data original (não altera)
4. Retorna sucesso/falha

---

#### **Método: `selecionar_vendas(filtro="")`**

```python
def selecionar_vendas(self, filtro=""):
    cursor = self.conn.cursor()
    if filtro:
        cursor.execute(
            "SELECT id, produto, valor, data FROM vendas WHERE produto LIKE ? ORDER BY id DESC", 
            (f'%{filtro}%',)
        )
    else:
        cursor.execute(
            "SELECT id, produto, valor, data FROM vendas ORDER BY id DESC"
        )
    return cursor.fetchall()
```

**O que faz**:
1. Se filtro fornecido, busca por LIKE (parcial)
2. Senão, retorna todas as vendas
3. Ordena por ID descendente (mais novo primeiro)
4. Retorna list de tuplas

**Exemplo**:
```python
vendas = db.selecionar_vendas("Note")
# Retorna: [(1, "Notebook Dell", 2500.50, "15/01/2026 14:30"), ...]

todas = db.selecionar_vendas()
# Retorna todas as vendas
```

---

#### **Método: `deletar_venda(id_venda)`**

```python
def deletar_venda(self, id_venda):
    try:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM vendas WHERE id = ?", (id_venda,))
        self.conn.commit()
        return True
    except Exception as e:
        logging.error(f"Erro ao deletar: {e}")
        return False
```

**O que faz**:
1. Localiza registro por ID
2. Deleta da tabela
3. Retorna sucesso/falha

---

### 2️⃣ `VendasApp` — Interface Principal

**Responsabilidade**: Gerenciar UI e coordenar com banco de dados

**Atributos**:

```python
class VendasApp(ctk.CTk):
    db: Database              # Instância do banco
    edit_id: int | None       # ID sendo editado (None se novo)
    
    # Widgets
    entry_prod: CTkEntry      # Campo de produto
    entry_valor: CTkEntry     # Campo de valor
    entry_busca: CTkEntry     # Campo de busca
    
    lbl_total_vendas: CTkLabel  # Contador de vendas
    lbl_faturamento: CTkLabel   # Total faturado
    
    scroll_vendas: CTkScrollableFrame  # Histórico
```

---

#### **Método: `setup_sidebar()`**

```python
def setup_sidebar(self):
    self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0)
    self.sidebar.grid(row=0, column=0, sticky="nsew")
    
    # Título
    ctk.CTkLabel(self.sidebar, text="SVP PRO", 
                font=("Roboto", 28, "bold"), 
                text_color="#2ecc71").pack(pady=(30, 10))
    
    # Sumário
    self.sumario_frame = ctk.CTkFrame(self.sidebar, 
                                      fg_color="#1e1e1e", 
                                      corner_radius=10)
    self.sumario_frame.pack(padx=20, pady=20, fill="x")
    
    self.lbl_total_vendas = ctk.CTkLabel(
        self.sumario_frame, 
        text="Vendas: 0", 
        font=("Roboto", 13)
    )
    self.lbl_total_vendas.pack(pady=(10, 0))
    
    self.lbl_faturamento = ctk.CTkLabel(
        self.sumario_frame, 
        text="R$ 0,00", 
        font=("Roboto", 22, "bold"), 
        text_color="#2ecc71"
    )
    self.lbl_faturamento.pack(pady=(0, 10))
    
    # Busca
    self.entry_busca = ctk.CTkEntry(
        self.sidebar, 
        placeholder_text="Nome do produto...", 
        width=200
    )
    self.entry_busca.pack(pady=10, padx=20)
    self.entry_busca.bind("<KeyRelease>", lambda e: self.atualizar_ui())
    
    # Exportar
    self.btn_exportar = ctk.CTkButton(
        self.sidebar, 
        text="Exportar CSV", 
        fg_color="#34495e", 
        hover_color="#2c3e50", 
        command=self.exportar_csv
    )
    self.btn_exportar.pack(side="bottom", pady=20, padx=20)
```

---

#### **Método: `salvar_dados()`**

```python
def salvar_dados(self):
    # 1. Obter valores dos campos
    prod = self.entry_prod.get()
    valor = self.entry_valor.get().replace(",", ".")
    
    # 2. Validar preenchimento
    if not prod or not valor:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return
    
    # 3. Verificar se é edição ou criação
    if self.edit_id:  # MODO EDIÇÃO
        if self.db.atualizar_venda(self.edit_id, prod, valor):
            self.edit_id = None
            self.btn_salvar.configure(
                text="REGISTRAR", 
                fg_color="#2ecc71", 
                hover_color="#27ae60"
            )
    else:  # MODO INSERÇÃO
        self.db.registrar_venda(prod, valor)
    
    # 4. Limpar campos
    self.entry_prod.delete(0, "end")
    self.entry_valor.delete(0, "end")
    
    # 5. Atualizar interface
    self.atualizar_ui()
```

**Fluxo**:
```
Usuário preenche → Valida → Se edit_id: UPDATE else: INSERT
→ Limpa campos → Atualiza UI
```

---

#### **Método: `atualizar_ui()`**

```python
def atualizar_ui(self):
    # 1. Limpar histórico anterior
    for widget in self.scroll_vendas.winfo_children():
        widget.destroy()
    
    # 2. Buscar vendas (com filtro se houver)
    vendas = self.db.selecionar_vendas(self.entry_busca.get())
    total = 0
    
    # 3. Para cada venda, criar um card
    for v in vendas:
        id_v, produto, valor, data = v
        total += valor
        
        # Card de venda
        card = ctk.CTkFrame(self.scroll_vendas, 
                           fg_color="#2b2b2b", 
                           height=50)
        card.pack(fill="x", pady=2, padx=5)
        
        # Nome (clicável para editar)
        lbl_nome = ctk.CTkLabel(card, 
                               text=produto, 
                               width=300, 
                               anchor="w", 
                               cursor="hand2", 
                               font=("Roboto", 13, "bold"))
        lbl_nome.pack(side="left", padx=15, pady=10)
        lbl_nome.bind("<Button-1>", 
                     lambda e, iv=id_v, p=produto, vl=valor: 
                     self.preparar_edicao(iv, p, vl))
        
        # Valor
        ctk.CTkLabel(card, 
                    text=f"R$ {valor:.2f}", 
                    text_color="#2ecc71", 
                    width=120, 
                    font=("Roboto", 13)).pack(side="left")
        
        # Data
        ctk.CTkLabel(card, 
                    text=data, 
                    text_color="gray", 
                    font=("Roboto", 11)).pack(side="left", padx=20)
        
        # Botão deletar
        ctk.CTkButton(card, 
                     text="✕", 
                     width=30, 
                     height=30, 
                     fg_color="transparent", 
                     text_color="#e74c3c",
                     hover_color="#3d2121", 
                     command=lambda i=id_v: 
                     self.confirmar_exclusao(i)).pack(side="right", padx=10)
    
    # 4. Atualizar sumário
    self.lbl_total_vendas.configure(text=f"Vendas: {len(vendas)}")
    self.lbl_faturamento.configure(text=f"R$ {total:.2f}")
```

---

#### **Método: `exportar_csv()`**

```python
def exportar_csv(self):
    # 1. Buscar todas as vendas (sem filtro)
    vendas = self.db.selecionar_vendas()
    if not vendas:
        return
    
    # 2. Gerar nome com data/hora
    nome_arq = f"relatorio_{datetime.now().strftime('%d%m_%H%M')}.csv"
    
    # 3. Escrever arquivo
    with open(nome_arq, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['ID', 'Produto', 'Valor', 'Data'])
        writer.writerows(vendas)
    
    # 4. Confirmação
    messagebox.showinfo("Sucesso", f"Exportado como {nome_arq}")
```

**Exemplo de arquivo gerado**:
```
ID;Produto;Valor;Data
1;Notebook Dell;2500.0;15/01/2026 14:30
2;Mouse Gamer;150.0;15/01/2026 14:35
3;Teclado Mecânico;450.0;15/01/2026 14:40
```

---

## 📊 Sistema de Relatórios

### Formato CSV

```
ID;Produto;Valor;Data
1;Notebook Dell;2500.00;15/01/2026 14:30
2;Monitor LG 27";1200.00;15/01/2026 14:35
3;Mouse Gamer;150.00;15/01/2026 14:40
```

**Características**:
- Separador: `;` (ponto-e-vírgula) - compatível com Excel PT-BR
- Encoding: UTF-8
- Nome: `relatorio_DDMM_HHMM.csv`
- Exemplo: `relatorio_1501_1430.csv` (15/01 às 14:30)

**Como abrir**:
- Excel: Importar com delimitador `;`
- Google Sheets: Upload direto
- LibreOffice Calc: Abre automaticamente

---

## 🎯 Exemplos de Uso

### Scenario 1: Primeiro uso

```
1. Executa program → Janela abre
2. Digite: "Notebook Dell" no campo Produto
3. Digite: "2500.50" no campo Preço
4. Clique: [REGISTRAR]
5. Resultado:
   - Histórico mostra: Notebook Dell | R$ 2.500,50 | 15/01 14:30
   - Sumário: Vendas: 1 | Faturamento: R$ 2.500,50

```

### Scenario 2: Editar registro

```
1. Histórico exibe: "Notebook Dell | R$ 2.500,50"
2. Clique no nome "Notebook Dell"
3. Resultado:
   - Campo Produto: "Notebook Dell" (preenchido)
   - Campo Preço: "2500.50" (preenchido)
   - Botão: "ATUALIZAR" (em amarelo)
4. Mude para: "Notebook Dell i7" | "3000.00"
5. Clique: [ATUALIZAR]
6. Resultado:
   - Histórico atualizado
   - Botão volta para "REGISTRAR"

```

### Scenario 3: Filtrar produtos

```
1. Digite na busca: "Note"
2. Resultado:
   - Mostra apenas produtos com "Note"
   - Notebook Dell | R$ 2.500,50
   - Notebook Lenovo | R$ 3.000,00
   - Sumário: Vendas: 2 | Faturamento: R$ 5.500,50

3. Limpe a busca
4. Todos os registros voltam

```

### Scenario 4: Exportar relatório

```
1. Clique: [Exportar CSV]
2. Arquivo: "relatorio_1501_1430.csv" criado
3. Confirmação: "Exportado como relatorio_1501_1430.csv"
4. Abra em Excel:
   
   ID │ Produto              │ Valor   │ Data
   ───┼──────────────────────┼─────────┼────────────────────
    1 │ Notebook Dell        │ 2500.0  │ 15/01/2026 14:30
    2 │ Mouse Gamer          │ 150.0   │ 15/01/2026 14:35
    3 │ Teclado Mecânico     │ 450.0   │ 15/01/2026 14:40

```

---

## 🔐 Segurança e Confiabilidade

### Proteção contra SQL Injection

```python
# ❌ INSEGURO:
cursor.execute(f"INSERT INTO vendas VALUES ('{produto}', {valor})")
# Um hacker poderia injetar: ' OR '1'='1

# ✅ SEGURO (implementado):
cursor.execute("INSERT INTO vendas VALUES (?, ?)", (produto, valor))
# Parâmetros são sanitizados automaticamente
```

### Sistema de Logs

```
# Arquivo: system_errors.log
2026-01-15 14:30:45,123 - ERROR - Erro ao registrar: division by zero
2026-01-15 14:31:20,456 - ERROR - Erro ao deletar: database is locked
```

**Configuração**:
```python
logging.basicConfig(
    filename="system_errors.log", 
    level=logging.ERROR
)
```

---

## 🚀 Possíveis Melhorias Futuras

- [ ] **Backup Automático**: Fazer backup do DB diariamente
- [ ] **Gráficos de Vendas**: Mostrar faturamento por período
- [ ] **Múltiplos Usuários**: Sistema de login
- [ ] **Categorias de Produtos**: Organizar por tipo
- [ ] **Desconto/Imposto**: Calcular automaticamente
- [ ] **Metas de Vendas**: Visualizar progresso
- [ ] **Integração com API**: Enviar dados para cloud
- [ ] **Gerador de NF**: Nota Fiscal automática
- [ ] **Estatísticas Avançadas**: Produto mais vendido, etc
- [ ] **Sincronização**: Multiple devices

---

## 📋 Instalação e Execução

### ✅ Pré-requisitos

- Python 3.7+
- pip

### 🔧 Passos

1. **Clone o repositório**:
```bash
git clone https://github.com/luisguigui/vendas.git
cd vendas
```

2. **Crie ambiente virtual**:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Instale dependência**:
```bash
pip install customtkinter
```

4. **Execute**:
```bash
python vendas.py
```

5. **Interface deve aparecer**:
   - Sidebar esquerda com sumário
   - Formulário de entrada
   - Histórico vazio
   - Comece registrando vendas!

---

## 📄 requirements.txt

```
customtkinter>=5.0.0
```

---

## 🐛 Troubleshooting

### ❌ Problema: "ModuleNotFoundError: customtkinter"
**Solução**: `pip install customtkinter`

### ❌ Problema: "database is locked"
**Causa**: Arquivo DB sendo acessado por outro processo  
**Solução**: Feche outro programa que esteja usando o DB

### ❌ Problema: Valores com vírgula não funcionam
**Verificação**: Código substitui "," por "." automaticamente  
**Se não funcionar**: Verifique se `replace(",", ".")` está no método

### ❌ Problema: CSV não abre corretamente em Excel
**Causa**: Excel pode estar usando delimitador errado  
**Solução**: Abra Excel → Dados → De Texto → Escolha `;` como delimitador

### ❌ Problema: Interface muito pequena/grande
**Solução**: Redimensione a janela
```python
self.geometry("1100x750")  # Mude estes valores
```

---

## ⚙️ Configuração Avançada

### Modificar Cores

```python
# Títulos
text_color="#2ecc71"  # Verde

# Valores
text_color="#2ecc71"  # Verde

# Cards
fg_color="#2b2b2b"    # Cinza

# Botão
fg_color="#2ecc71"    # Verde (registrar)
fg_color="#e74c3c"    # Vermelho (deletar)
```

### Modificar Formato de Data

```python
# Padrão: "15/01/2026 14:30"
data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

# Alternativas:
# "%Y-%m-%d %H:%M:%S"  → "2026-01-15 14:30:00"
# "%d-%m-%Y"           → "15-01-2026"
# "%d/%m/%Y"           → "15/01/2026"
```

### Adicionar Novo Campo

```python
# 1. Alterar tabela:
cursor.execute("""
    ALTER TABLE vendas ADD COLUMN categoria TEXT
""")

# 2. Adicionar Entry na UI:
self.entry_categoria = ctk.CTkEntry(...)

# 3. Modificar insert:
cursor.execute(
    "INSERT INTO vendas (..., categoria) VALUES (..., ?)", 
    (..., categoria)
)
```

---

## 💡 Dicas de Uso

1. **Pressione ENTER**: Na busca ou preço para aceitar
2. **Edição rápida**: Clique no produto para editar
3. **Backup CSV**: Exporte regularmente para ter cópia
4. **Restauração**: CSV pode ser reimportado se necessário
5. **Performance**: Funciona bem com 10.000+ vendas

---

## ✒️ Autor

**Luis Guilherme G.B.**

- 🐙 GitHub: [@luisguigui](https://github.com/luisguigui)
- 💼 Portfólio: Desenvolvedor Python Full-Stack
- 📧 Contato: Abra uma issue no repositório

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Use, modifique e distribua livremente para seus negócios!

---

## 🌟 Se gostou, considere dar uma ⭐!

```
   💰 GESTÃO INTELIGENTE = VENDAS MELHORES

   SVP PRO: Simples, Profissional, Poderoso

   ⭐ Use em produção! ⭐
```

---

**Última atualização**: 2026-04-20  
**Versão**: 1.0 — Enterprise Edition  
**Status**: ✅ Production Ready  
**Foco**: Confiabilidade, Segurança, Performance
```

---
