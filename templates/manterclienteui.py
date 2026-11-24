import streamlit as st
import pandas as pd
import time
from service import Service

class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    @staticmethod
    def listar():
        clientes = sorted(Service.cliente_listar(), key=lambda o: o.get_id())
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            try:
                Service.cliente_inserir(nome, email, fone)
                st.success("Cliente inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)

    @staticmethod
    def atualizar():
        clientes = sorted(Service.cliente_listar(), key=lambda o: o.get_id())
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", clientes)
            k = op.get_id()
            nome = st.text_input("Novo nome", op.get_nome(), key=f"cli_nome_{k}")
            email = st.text_input("Novo e-mail", op.get_email(), key=f"cli_email_{k}")
            fone = st.text_input("Novo fone", op.get_fone(), key=f"cli_fone_{k}")
            if st.button("Atualizar"):
                try:
                    Service.cliente_atualizar(k, nome, email, fone)
                    st.success("Cliente atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)

    @staticmethod
    def excluir():
        clientes = sorted(Service.cliente_listar(), key=lambda o: o.get_id())
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de Clientes", clientes)
            if st.button("Excluir"):
                Service.cliente_excluir(op.get_id())
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()