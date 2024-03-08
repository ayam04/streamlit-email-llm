# -*- coding: utf-8 -*-
"""Untitled33.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16wtY37F2ZUeNPtd-nnGyNUr8ZhaEcquW
"""

import os
from langchain_community.llms import HuggingFaceHub
import pandas as pd
import streamlit as st

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2", model_kwargs={"temperature": 0.5, "max_new_tokens": 30000}
)

def model(question):
    response = llm(question)
    return response.strip()


def load_customer_data(df, prompt=""):
    try:
        df = df[df.apply(lambda row: len(row) == 6, axis=1)]

        customer_data = [
            f"{prompt} Customer Name: {row.iloc[0]} Customer Age: {row.iloc[1]} "
            f"Customer Email: {row.iloc[2]} Customer Company: {row.iloc[3]} "
            f"Customer Hobbies: {row.iloc[4]} Customer Company URL: {row.iloc[5]}"
            for _, row in df.iterrows()
        ]
        # print(customer_data)  
        return customer_data

    except Exception as e:
        return [f"Error loading customer data: {e}"]

def email_generation(customer_list):
  output=[]
  for i in customer_list:
    email=model(i)
    output.append(email)
    st.write(email)
    st.write('---------------------')
  # return output

def create_test_csv(input_file, output_file='test.csv', lines=5):
    df = pd.read_csv(input_file, nrows=lines)
    df.to_csv(output_file, index=False)

# create_test_csv('Customer_Dataset_Synthetic.csv')
load_customer_data("test.csv","a")