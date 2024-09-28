import streamlit as st


st.set_page_config(
    page_title="About Me",
    page_icon="atom_symbol", 
    layout="wide",
    #initial_sidebar_state="expanded",
)

def main():
    st.title('welcome')
    st.header('this is my page')
    with st.sidebar.expander("Select"):
        g = st.selectbox("Tool type", ('Search','Add cif','Linking with VESTA'))


if __name__ == '__main__':
    main()
