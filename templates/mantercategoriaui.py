import streamlit as st
import pandas as pd
import time
from service import Service

class ManterCategoriaUI:
    @staticmethod
    def main():
        st.header("Cadastro de Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.inserir()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()

    @staticmethod
    def listar():
        categorias = sorted(Service.categoria_listar(), key=lambda o: o.get_id())
        if len(categorias) == 0: st.write("Nenhuma categoria cadastrada")
        else:
            list_dic = []
            for obj in categorias: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        descricao = st.text_input("Informe a descrição da categoria")
        if st.button("Inserir"):
            try:
                Service.categoria_inserir(descricao)
                st.success("Categoria inserida com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)

    @staticmethod
    def atualizar():
        categorias = sorted(Service.categoria_listar(), key=lambda o: o.get_id())
        if len(categorias) == 0: st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Atualização de Categorias", categorias,
                              format_func=lambda c: f"{c.get_id()} - {c.get_descricao()}")
            k = op.get_id()
            descricao = st.text_input("Nova descrição", op.get_descricao(), key=f"cat_desc_{k}")
            if st.button("Atualizar"):
                try:
                    Service.categoria_atualizar(k, descricao)
                    st.success("Categoria atualizada com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)

    @staticmethod
    def excluir():
        categorias = sorted(Service.categoria_listar(), key=lambda o: o.get_id())
        if len(categorias) == 0: st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Exclusão de Categorias", categorias,
                              format_func=lambda c: f"{c.get_id()} - {c.get_descricao()}")
            if st.button("Excluir"):
                Service.categoria_excluir(op.get_id())
                st.success("Categoria excluída com sucesso")
                time.sleep(2)
                st.rerun()