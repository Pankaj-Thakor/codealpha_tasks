# ==========================================================
# Project : Stock Portfolio Tracker
# Author  : Thakor Pankajji Devendraji
# Language: Python
# ==========================================================

# ==========================
# STOCK DATABASE
# ==========================

stocks = {
    "RELIANCE": {"exchange": "NSE", "price": 1450},
    "TCS": {"exchange": "NSE", "price": 3800},
    "INFY": {"exchange": "NSE", "price": 1600},
    "HDFCBANK": {"exchange": "BSE", "price": 1750},
    "ICICIBANK": {"exchange": "BSE", "price": 1250},
    "SBIN": {"exchange": "BSE", "price": 900},
}

portfolio = []


# ==========================
# DISPLAY AVAILABLE STOCKS
# ==========================

def show_stocks():
    print("\n==============================================")
    print("        AVAILABLE STOCKS")
    print("==============================================")
    print(f"{'Stock':<15}{'Exchange':<10}{'Price'}")
    print("----------------------------------------------")

    for stock, details in stocks.items():
        print(f"{stock:<15}{details['exchange']:<10}₹{details['price']}")

    print("==============================================\n")


# ==========================
# BUY STOCK
# ==========================

def buy_stock():
    while True:
        stock_name = input("Enter Stock Name (or DONE): ").strip().upper()

        if stock_name == "DONE":
            break

        if stock_name not in stocks:
            print(" Stock Not Found.\n")
            continue

        try:
            quantity = int(input("Enter Quantity : "))

            if quantity <= 0:
                print("Quantity must be greater than zero.\n")
                continue

        except ValueError:
            print("Invalid Quantity. Please enter a whole number.\n")
            continue

        price = stocks[stock_name]["price"]
        total = quantity * price

        # If the stock is already in the portfolio, merge quantities
        # instead of creating a duplicate entry.
        existing = next((item for item in portfolio if item["stock"] == stock_name), None)

        if existing:
            existing["quantity"] += quantity
            existing["total"] = existing["quantity"] * existing["price"]
        else:
            portfolio.append({
                "stock": stock_name,
                "exchange": stocks[stock_name]["exchange"],
                "price": price,
                "quantity": quantity,
                "total": total,
            })

        print(f" {stock_name} Added Successfully.\n")


# ==========================
# VIEW PORTFOLIO
# ==========================

def view_portfolio():
    if len(portfolio) == 0:
        print("\nNo Stocks Purchased Yet.\n")
        return

    print("\n==============================================================")
    print("                     MY PORTFOLIO")
    print("==============================================================")
    print(f"{'Stock':<15}{'Exch':<10}{'Qty':<8}{'Price':<10}{'Total'}")
    print("--------------------------------------------------------------")

    grand_total = 0

    for item in portfolio:
        print(f"{item['stock']:<15}"
              f"{item['exchange']:<10}"
              f"{item['quantity']:<8}"
              f"₹{item['price']:<9}"
              f"₹{item['total']}")

        grand_total += item["total"]

    print("--------------------------------------------------------------")
    print(f"Total Investment : ₹{grand_total}")
    print("==============================================================\n")


# ==========================
# SAVE PORTFOLIO
# ==========================

def save_portfolio():
    if len(portfolio) == 0:
        print("Nothing to save — no stocks in portfolio.\n")
        return

    try:
        with open("portfolio.txt", "w", encoding="utf-8") as file:
            file.write("=========== STOCK PORTFOLIO ===========\n\n")

            total_amount = 0

            for item in portfolio:
                file.write(
                    f"{item['stock']} | "
                    f"{item['exchange']} | "
                    f"Qty : {item['quantity']} | "
                    f"Price : ₹{item['price']} | "
                    f"Total : ₹{item['total']}\n"
                )
                total_amount += item["total"]

            file.write("\n---------------------------------\n")
            file.write(f"Total Investment : ₹{total_amount}")
            file.write("\n---------------------------------\n")

        print("Portfolio saved as 'portfolio.txt'")

    except OSError as e:
        print(f" Could not save portfolio: {e}")


# ==========================
# MAIN PROGRAM
# ==========================

def main():
    print("==========================================")
    print("      STOCK PORTFOLIO TRACKER")
    print("==========================================")

    name = input("Enter Your Name : ").strip()

    print(f"\nWelcome {name or 'Investor'}!")

    show_stocks()
    buy_stock()
    view_portfolio()
    save_portfolio()

    print("\nThank you for using Stock Portfolio Tracker.")


if __name__ == "__main__":
    main()