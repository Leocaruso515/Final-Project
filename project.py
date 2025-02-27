def calculate_profit_margin(cost_price, selling_price):
    """Calculates the profit margin percentage."""
    if cost_price <= 0 or selling_price <= 0:
        raise ValueError("Prices must be greater than zero.")
    profit = selling_price - cost_price
    return (profit / selling_price) * 100


def calculate_break_even_point(fixed_costs, selling_price, variable_costs):
    """Determines the number of units needed to break even."""
    if selling_price <= variable_costs:
        raise ValueError("Selling price must be greater than variable costs.")
    return fixed_costs / (selling_price - variable_costs)


def apply_discount(selling_price, discount_percentage):
    """Applies a discount to the selling price."""
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount must be between 0 and 100.")
    return selling_price * (1 - discount_percentage / 100)


def calculate_tax(price, tax_rate):
    """Calculates the total price including tax."""
    if tax_rate < 0:
        raise ValueError("Tax rate must be non-negative.")
    return price * (1 + tax_rate / 100)


def suggest_retail_price(cost_price, desired_margin):
    """Suggests an ideal retail price based on the desired profit margin."""
    if desired_margin < 0:
        raise ValueError("Desired margin must be non-negative.")
    return cost_price * (1 + desired_margin / 100)


def project_annual_revenue(monthly_revenue):
    """Estimates annual revenue based on monthly revenue."""
    return monthly_revenue * 12


def analyze_sales_trends(sales_data):
    """Analyzes sales trends and returns the highest and lowest sales months."""
    if not sales_data:
        raise ValueError("Sales data cannot be empty.")
    highest_month = max(sales_data)
    lowest_month = min(sales_data)
    return highest_month, lowest_month


def main():
    """Main function to ask for user input and perform calculations."""
    try:
        print("This information is private. Please enter your credentials.")
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        cost_price = float(input("Enter cost price: "))
        selling_price = float(input("Enter selling price: "))
        fixed_costs = float(input("Enter fixed costs: "))
        variable_costs = float(input("Enter variable costs per unit: "))
        discount_percentage = float(input("Enter discount percentage: "))
        tax_rate = float(input("Enter tax rate: "))
        desired_margin = float(input("Enter desired profit margin: "))
        monthly_revenue = float(input("Enter monthly revenue: "))
        sales_data = list(map(float, input("Enter sales data for each month separated by spaces: ").split()))
        
        print("\nResults:")
        print("Profit Margin:", calculate_profit_margin(cost_price, selling_price))
        print("Break-even Point:", calculate_break_even_point(fixed_costs, selling_price, variable_costs))
        print("Price after Discount:", apply_discount(selling_price, discount_percentage))
        print("Price after Tax:", calculate_tax(selling_price, tax_rate))
        print("Suggested Retail Price:", suggest_retail_price(cost_price, desired_margin))
        print("Projected Annual Revenue:", project_annual_revenue(monthly_revenue))
        print("Sales Trends (Highest & Lowest):", analyze_sales_trends(sales_data))
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
