import streamlit as st
from templates.mantercategoriaui import ManterCategoriaUI
from templates.manterclienteui import ManterClienteUI
from templates.manterprodutoui import ManterProdutoUI
from templates.reajustarprodutoui import ReajustarProdutoUI

class IndexUI:
    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox("Menu", [
            "Cadastro de Clientes",
            "Cadastro de Categorias",
            "Cadastro de Produtos",
            "Reajuste de Preços"
        ])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Reajuste de Preços": ReajustarProdutoUI.main()

    @staticmethod
    def main():
        IndexUI.menu_admin()

IndexUI.main()