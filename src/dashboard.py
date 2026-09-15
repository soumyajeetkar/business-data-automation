import streamlit as st
import pandas as pd
from pathlib import Path


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Business Sales Dashboard",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("📊 Business Sales Dashboard")

st.write(
    "Interactive sales analysis generated from CSV data."
)


# ==========================================
# LOAD CSV FILES
# ==========================================

input_folder = Path("data/input")

csv_files = list(input_folder.glob("*.csv"))

if not csv_files:

    st.error("No CSV files found in data/input/")

    st.stop()


all_data = []


for file in csv_files:

    df = pd.read_csv(file)

    df["Source_File"] = file.name

    all_data.append(df)


combined_df = pd.concat(
    all_data,
    ignore_index=True
)


# ==========================================
# DATA CLEANING
# ==========================================

combined_df["Date"] = pd.to_datetime(
    combined_df["Date"],
    errors="coerce"
)

combined_df["Quantity"] = pd.to_numeric(
    combined_df["Quantity"],
    errors="coerce"
)

combined_df["Price"] = pd.to_numeric(
    combined_df["Price"],
    errors="coerce"
)

combined_df = combined_df.dropna(
    subset=[
        "Date",
        "Customer",
        "Product",
        "Category",
        "Quantity",
        "Price"
    ]
)


# ==========================================
# CALCULATE REVENUE
# ==========================================

combined_df["Total"] = (
    combined_df["Quantity"]
    * combined_df["Price"]
)


# ==========================================
# SIDEBAR FILTERS
# ==========================================

st.sidebar.header("🔎 Filters")


categories = sorted(
    combined_df["Category"].unique()
)

selected_categories = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)


products = sorted(
    combined_df["Product"].unique()
)

selected_products = st.sidebar.multiselect(
    "Select Product",
    products,
    default=products
)


# ==========================================
# FILTER DATA
# ==========================================

filtered_df = combined_df[
    combined_df["Category"].isin(
        selected_categories
    )
    &
    combined_df["Product"].isin(
        selected_products
    )
]


# ==========================================
# KEY METRICS
# ==========================================

total_revenue = filtered_df["Total"].sum()

total_quantity = filtered_df["Quantity"].sum()

total_orders = len(filtered_df)

average_order_value = (
    total_revenue / total_orders
    if total_orders > 0
    else 0
)


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "💰 Total Revenue",
    f"₹{total_revenue:,.0f}"
)

col2.metric(
    "📦 Quantity Sold",
    f"{total_quantity:,.0f}"
)

col3.metric(
    "🧾 Orders",
    f"{total_orders:,}"
)

col4.metric(
    "📈 Average Order",
    f"₹{average_order_value:,.0f}"
)


st.divider()


# ==========================================
# PRODUCT ANALYSIS
# ==========================================

st.subheader("🏆 Revenue by Product")


product_sales = (
    filtered_df
    .groupby("Product")["Total"]
    .sum()
    .sort_values(ascending=False)
)


st.bar_chart(product_sales)


# ==========================================
# CATEGORY ANALYSIS
# ==========================================

st.subheader("📊 Revenue by Category")


category_sales = (
    filtered_df
    .groupby("Category")["Total"]
    .sum()
    .sort_values(ascending=False)
)


st.bar_chart(category_sales)


# ==========================================
# MONTHLY ANALYSIS
# ==========================================

st.subheader("📅 Monthly Revenue")


filtered_df["Month"] = (
    filtered_df["Date"]
    .dt.to_period("M")
    .astype(str)
)


monthly_sales = (
    filtered_df
    .groupby("Month")["Total"]
    .sum()
)


st.line_chart(monthly_sales)


# ==========================================
# TOP PRODUCTS TABLE
# ==========================================

st.subheader("🥇 Product Performance")


product_table = (
    filtered_df
    .groupby("Product")
    .agg(
        Total_Revenue=("Total", "sum"),
        Quantity_Sold=("Quantity", "sum"),
        Orders=("Product", "count")
    )
    .sort_values(
        "Total_Revenue",
        ascending=False
    )
)


st.dataframe(
    product_table,
    use_container_width=True
)


# ==========================================
# RAW DATA
# ==========================================

with st.expander("📋 View Sales Data"):

    st.dataframe(
        filtered_df,
        use_container_width=True
    )