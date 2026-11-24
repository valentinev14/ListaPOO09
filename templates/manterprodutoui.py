import streamlit as st
import pandas as pd
import time
from service import Service

class ManterProdutoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    @staticmethod
    def __fmt_produto(p):
        return f"{p.get_id()} - {p.get_descricao()} - R$ {p.get_preco():.2f}"

    @staticmethod
    def __fmt_categoria(c):
        return f"{c.get_id()} - {c.get_descricao()}"

    @staticmethod
    def listar():
        produtos = sorted(Service.produto_listar(), key=lambda o: o.get_id())
        if len(produtos) == 0: st.write("Nenhum produto cadastrado")
        else:
            list_dic = []
            for obj in produtos:
                cat = Service.categoria_listar_id(obj.get_id_categoria())
                list_dic.append({
                    "id": obj.get_id(),
                    "descricao": obj.get_descricao(),
                    "preco": obj.get_preco(),
                    "estoque": obj.get_estoque(),
                    "categoria": cat.get_descricao() if cat is not None else "-"
                })
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        categorias = sorted(Service.categoria_listar(), key=lambda o: o.get_id())
        if len(categorias) == 0:
            st.write("Cadastre uma categoria antes de inserir produtos")
        else:
            descricao = st.text_input("Informe a descrição do produto")
            preco = st.number_input("Informe o preço", min_value=0.0, step=0.01, format="%.2f")
            estoque = st.number_input("Informe o estoque", min_value=0, step=1)
            categoria = st.selectbox("Informe a categoria", categorias,
                                     format_func=ManterProdutoUI.__fmt_categoria)
            if st.button("Inserir"):
                try:
                    Service.produto_inserir(descricao, preco, int(estoque), categoria.get_id())
                    st.success("Produto inserido com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)

    @staticmethod
    def atualizar():
        produtos = sorted(Service.produto_listar(), key=lambda o: o.get_id())
        categorias = sorted(Service.categoria_listar(), key=lambda o: o.get_id())
        if len(produtos) == 0: st.write("Nenhum produto cadastrado")
        elif len(categorias) == 0: st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Atualização de Produtos", produtos,
                              format_func=ManterProdutoUI.__fmt_produto)
            k = op.get_id()
            ids = [c.get_id() for c in categorias]
            idx = ids.index(op.get_id_categoria()) if op.get_id_categoria() in ids else 0
            descricao = st.text_input("Nova descrição", op.get_descricao(), key=f"prod_desc_{k}")
            preco = st.number_input("Novo preço", min_value=0.0, step=0.01, format="%.2f",
                                    value=float(op.get_preco()), key=f"prod_preco_{k}")
            estoque = st.number_input("Novo estoque", min_value=0, step=1,
                                      value=int(op.get_estoque()), key=f"prod_estoque_{k}")
            categoria = st.selectbox("Nova categoria", categorias, index=idx,
                                     format_func=ManterProdutoUI.__fmt_categoria,
                                     key=f"prod_cat_{k}")
            if st.button("Atualizar"):
                try:
                    Service.produto_atualizar(k, descricao, preco, int(estoque), categoria.get_id())
                    st.success("Produto atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)

    @staticmethod
    def excluir():
        produtos = sorted(Service.produto_listar(), key=lambda o: o.get_id())
        if len(produtos) == 0: st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de Produtos", produtos,
                              format_func=ManterProdutoUI.__fmt_produto)
            if st.button("Excluir"):
                Service.produto_excluir(op.get_id())
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()