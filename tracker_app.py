import streamlit as st
import pandas as pd
import os
from datetime import date

# File to store data
FILE_NAME = "transactions.csv"

# Initialize CSV if not exists
if not os.path.exists(FILE_NAME):
    df_init = pd.DataFrame(columns=["Date", "Type", "Category", "Amount", "Description"])
    df_init.to_csv(FILE_NAME, index=False)

# Load existing data
df = pd.read_csv(FILE_NAME)

st.set_page_config(page_title="Income & Expense Tracker", layout="centered")

st.title("💰 Income & Expense Tracker")

# --- Add Transaction ---
st.header("➕ Add New Transaction")

col1, col2 = st.columns(2)
with col1:
    t_type = st.selectbox("Type", ["Income", "Expense"])
    category = st.text_input("Category")
with col2:
    amount = st.number_input("Amount (RM)", min_value=0.0, format="%.2f")
    t_date = st.date_input("Date", value=date.today())

description = st.text_area("Description (optional)")

if st.button("Add Transaction"):
    if category and amount > 0:
        new_data = pd.DataFrame([[t_date, t_type, category, amount, description]],
                                columns=["Date", "Type", "Category", "Amount", "Description"])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(FILE_NAME, index=False)
        st.success("Transaction added!")
        st.experimental_rerun()
    else:
        st.warning("Please fill in required fields.")

# --- View Transactions ---
st.header("📋 Transaction History")
st.dataframe(df.sort_values(by="Date", ascending=False), use_container_width=True)

# --- Summary ---
st.header("📊 Summary")

income_total = df[df["Type"] == "Income"]["Amount"].sum()
expense_total = df[df["Type"] == "Expense"]["Amount"].sum()
balance = income_total - expense_total

col3, col4, col5 = st.columns(3)
col3.metric("Total Income", f"RM {income_total:.2f}")
col4.metric("Total Expense", f"RM {expense_total:.2f}")
col5.metric("Current Balance", f"RM {balance:.2f}")

