import customtkinter as ctk
import sqlite3
import csv
from datetime import datetime
from tkinter import messagebox
import logging

# Configuração de logs
logging.basicConfig(filename="system_errors.log", level=logging.ERROR)

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("enterprise_data.db")
        self.create_tables()

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

    def registrar_venda(self, produto, valor):
        try:
            cursor = self.conn.cursor()
            data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
            cursor.execute("INSERT INTO vendas (produto, valor, data) VALUES (?, ?, ?)", 
                           (produto, float(valor), data_atual))
            self.conn.commit()
            return True
        except Exception as e:
            logging.error(f"Erro ao registrar: {e}")
            return False

    def atualizar_venda(self, id_venda, produto, valor):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE vendas SET produto = ?, valor = ? WHERE id = ?", 
                           (produto, float(valor), id_venda))
            self.conn.commit()
            return True
        except Exception as e:
            logging.error(f"Erro ao atualizar: {e}")
            return False

    def selecionar_vendas(self, filtro=""):
        cursor = self.conn.cursor()
        if filtro:
            cursor.execute("SELECT id, produto, valor, data FROM vendas WHERE produto LIKE ? ORDER BY id DESC", (f'%{filtro}%',))
        else:
            cursor.execute("SELECT id, produto, valor, data FROM vendas ORDER BY id DESC")
        return cursor.fetchall()

    def deletar_venda(self, id_venda):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM vendas WHERE id = ?", (id_venda,))
            self.conn.commit()
            return True
        except Exception as e:
            logging.error(f"Erro ao deletar: {e}")
            return False

class VendasApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.db = Database()
        
        self.title("SVP PRO - Gestão de Vendas")
        self.geometry("1100x750")
        ctk.set_appearance_mode("dark")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.setup_sidebar()
        self.setup_main_area()
        self.atualizar_ui()

    def setup_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="SVP PRO", font=("Roboto", 28, "bold"), text_color="#2ecc71").pack(pady=(30, 10))
        
        # Painel de Resumo
        self.sumario_frame = ctk.CTkFrame(self.sidebar, fg_color="#1e1e1e", corner_radius=10)
        self.sumario_frame.pack(padx=20, pady=20, fill="x")

        self.lbl_total_vendas = ctk.CTkLabel(self.sumario_frame, text="Vendas: 0", font=("Roboto", 13))
        self.lbl_total_vendas.pack(pady=(10, 0))
        
        self.lbl_faturamento = ctk.CTkLabel(self.sumario_frame, text="R$ 0,00", font=("Roboto", 22, "bold"), text_color="#2ecc71")
        self.lbl_faturamento.pack(pady=(0, 10))

        # Filtro
        ctk.CTkLabel(self.sidebar, text="PESQUISAR", font=("Roboto", 11, "bold"), text_color="gray").pack(pady=(20, 0))
        self.entry_busca = ctk.CTkEntry(self.sidebar, placeholder_text="Nome do produto...", width=200)
        self.entry_busca.pack(pady=10, padx=20)
        self.entry_busca.bind("<KeyRelease>", lambda e: self.atualizar_ui())

        self.btn_exportar = ctk.CTkButton(self.sidebar, text="Exportar CSV", fg_color="#34495e", hover_color="#2c3e50", command=self.exportar_csv)
        self.btn_exportar.pack(side="bottom", pady=20, padx=20)

    def setup_main_area(self):
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Registro e Edição
        self.form_frame = ctk.CTkFrame(self.main_container)
        self.form_frame.pack(fill="x", pady=(0, 20))
        
        self.edit_id = None # Controla se estamos editando ou criando
        
        self.entry_prod = ctk.CTkEntry(self.form_frame, placeholder_text="Produto", width=300, height=45)
        self.entry_prod.grid(row=0, column=0, padx=15, pady=20)

        self.entry_valor = ctk.CTkEntry(self.form_frame, placeholder_text="Preço", width=120, height=45)
        self.entry_valor.grid(row=0, column=1, padx=5, pady=20)

        self.btn_salvar = ctk.CTkButton(self.form_frame, text="REGISTRAR", width=150, height=45,
                                     fg_color="#2ecc71", hover_color="#27ae60",
                                     font=("Roboto", 14, "bold"), command=self.salvar_dados)
        self.btn_salvar.grid(row=0, column=2, padx=15, pady=20)

        self.scroll_vendas = ctk.CTkScrollableFrame(self.main_container, label_text="HISTÓRICO DE MOVIMENTAÇÕES", label_font=("Roboto", 12, "bold"))
        self.scroll_vendas.pack(fill="both", expand=True)

    def preparar_edicao(self, id_v, produto, valor):
        self.edit_id = id_v
        self.entry_prod.delete(0, "end")
        self.entry_prod.insert(0, produto)
        self.entry_valor.delete(0, "end")
        self.entry_valor.insert(0, str(valor))
        self.btn_salvar.configure(text="ATUALIZAR", fg_color="#f39c12", hover_color="#e67e22")

    def salvar_dados(self):
        prod = self.entry_prod.get()
        valor = self.entry_valor.get().replace(",", ".")
        
        if not prod or not valor:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        if self.edit_id: # Modo Edição
            if self.db.atualizar_venda(self.edit_id, prod, valor):
                self.edit_id = None
                self.btn_salvar.configure(text="REGISTRAR", fg_color="#2ecc71", hover_color="#27ae60")
        else: # Modo Inserção
            self.db.registrar_venda(prod, valor)
            
        self.entry_prod.delete(0, "end")
        self.entry_valor.delete(0, "end")
        self.atualizar_ui()

    def atualizar_ui(self):
        for widget in self.scroll_vendas.winfo_children():
            widget.destroy()

        vendas = self.db.selecionar_vendas(self.entry_busca.get())
        total = 0
        
        for v in vendas:
            id_v, produto, valor, data = v
            total += valor
            
            card = ctk.CTkFrame(self.scroll_vendas, fg_color="#2b2b2b", height=50)
            card.pack(fill="x", pady=2, padx=5)
            
            # Clique no nome para editar
            lbl_nome = ctk.CTkLabel(card, text=produto, width=300, anchor="w", cursor="hand2", font=("Roboto", 13, "bold"))
            lbl_nome.pack(side="left", padx=15, pady=10)
            lbl_nome.bind("<Button-1>", lambda e, iv=id_v, p=produto, vl=valor: self.preparar_edicao(iv, p, vl))

            ctk.CTkLabel(card, text=f"R$ {valor:.2f}", text_color="#2ecc71", width=120, font=("Roboto", 13)).pack(side="left")
            ctk.CTkLabel(card, text=data, text_color="gray", font=("Roboto", 11)).pack(side="left", padx=20)
            
            ctk.CTkButton(card, text="✕", width=30, height=30, fg_color="transparent", text_color="#e74c3c",
                          hover_color="#3d2121", command=lambda i=id_v: self.confirmar_exclusao(i)).pack(side="right", padx=10)

        self.lbl_total_vendas.configure(text=f"Vendas: {len(vendas)}")
        self.lbl_faturamento.configure(text=f"R$ {total:.2f}")

    def confirmar_exclusao(self, id_v):
        if messagebox.askyesno("Excluir", "Tem certeza que deseja apagar esta venda?"):
            if self.db.deletar_venda(id_v):
                self.atualizar_ui()

    def exportar_csv(self):
        vendas = self.db.selecionar_vendas()
        if not vendas: return
        nome_arq = f"relatorio_{datetime.now().strftime('%d%m_%H%M')}.csv"
        with open(nome_arq, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['ID', 'Produto', 'Valor', 'Data'])
            writer.writerows(vendas)
        messagebox.showinfo("Sucesso", f"Exportado como {nome_arq}")

if __name__ == "__main__":
    app = VendasApp()
    app.mainloop()