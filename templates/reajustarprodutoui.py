import streamlit as st
import time
from service import Service

class ReajustarProdutoUI:
    @staticmethod
    def main():
        st.header("Reajuste de Preços")
        ReajustarProdutoUI.reajustar()

    @staticmethod
    def reajustar():
        produtos = sorted(Service.produto_listar(), key=lambda o: o.get_id())
        if len(produtos) == 0: st.write("Nenhum produto cadastrado")
        else:
            percentual = st.number_input("Informe o percentual de reajuste (%)",
                                         min_value=-100.0, value=0.0, step=1.0, format="%.2f",
                                         help="Positivo = reajuste, negativo = promoção")
            if st.button("Reajustar"):
                try:
                    Service.produto_reajustar(percentual)
                    st.success("Preços reajustados com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)