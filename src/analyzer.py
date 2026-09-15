def calculate_metrics(df):

    total_sales = df["Total"].sum()

    total_quantity = df["Quantity"].sum()

    total_orders = len(df)

    average_order_value = (
        total_sales / total_orders
        if total_orders > 0
        else 0
    )

    return {
        "total_sales": total_sales,
        "total_quantity": total_quantity,
        "total_orders": total_orders,
        "average_order_value": average_order_value
    }


def analyze_products(df):

    return (
        df
        .groupby("Product")["Total"]
        .sum()
        .sort_values(ascending=False)
    )


def analyze_categories(df):

    return (
        df
        .groupby("Category")["Total"]
        .sum()
        .sort_values(ascending=False)
    )


def analyze_monthly_sales(df):

    data = df.copy()

    data["Month"] = (
        data["Date"]
        .dt.to_period("M")
        .astype(str)
    )

    return (
        data
        .groupby("Month")["Total"]
        .sum()
        .reset_index()
    )