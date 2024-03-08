import streamlit as st
import pandas as pd
from functions import *

prompt="write a E-mail marketing a phone product, these are the customer details, customize your email appealing to the customer."
def main():
    st.title("File Upload")

    file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

    if file is not None:
        df = pd.read_csv(file) if file.name.endswith("csv") else pd.read_excel(file)
        st.dataframe(df)
        customer_list = load_customer_data(df,prompt)
    
        if st.button("Submit"):
            email_generation(customer_list)


if __name__ == "__main__":
    main()