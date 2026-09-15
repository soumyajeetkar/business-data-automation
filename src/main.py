from pathlib import Path

from data_loader import (
    load_sales_data,
    clean_sales_data
)

from analyzer import (
    calculate_metrics,
    analyze_products,
    analyze_categories,
    analyze_monthly_sales
)

from report_generator import generate_report


INPUT_FOLDER = Path("data/input")

OUTPUT_FOLDER = Path("data/output")

OUTPUT_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT_FILE = (
    OUTPUT_FOLDER /
    "sales_report.xlsx"
)


# Load data

df = load_sales_data(
    INPUT_FOLDER
)


# Clean data

df = clean_sales_data(df)


# Analyze data

metrics = calculate_metrics(df)

product_sales = analyze_products(df)

category_sales = analyze_categories(df)

monthly_sales = analyze_monthly_sales(df)


# Generate report

generate_report(
    df,
    metrics,
    product_sales,
    category_sales,
    monthly_sales,
    OUTPUT_FILE
)


# Final output

print("\n" + "=" * 50)

print("BUSINESS SALES REPORT GENERATED")

print("=" * 50)

print(
    f"\nTotal Revenue: "
    f"₹{metrics['total_sales']:,.2f}"
)

print(
    f"Total Quantity: "
    f"{metrics['total_quantity']}"
)

print(
    f"Total Orders: "
    f"{metrics['total_orders']}"
)

print(
    f"Average Order Value: "
    f"₹{metrics['average_order_value']:,.2f}"
)

print(
    f"\nBest Product: "
    f"{product_sales.index[0]}"
)

print(
    f"Best Category: "
    f"{category_sales.index[0]}"
)

print(
    f"\nReport saved to: "
    f"{OUTPUT_FILE}"
)

print("\n" + "=" * 50)