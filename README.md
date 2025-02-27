# Store Profit Calculator

The **Clothing Store Profit Calculator** is a Python-based application designed to help store owners analyze their business profitability. This tool calculates key financial metrics such as profit margins, break-even points, tax adjustments, retail pricing, and sales trends. By inputting basic business parameters, users can quickly determine how different factors affect their store’s profitability and revenue.

This project was designed to be both user-friendly and functional, incorporating several financial functions that provide meaningful insights for business decision-making. Additionally, the program is interactive, requiring users to input various numerical values for calculations.

## Project Files

### `project.py`
This is the main file of the project and contains all the core functions, along with an interactive command-line interface that prompts users for input and calculates the necessary financial metrics. Below are the primary functions included in this file:

1. **`calculate_profit_margin(cost_price, selling_price)`**: Computes the profit margin percentage based on the cost and selling prices.
2. **`calculate_break_even_point(fixed_costs, selling_price, variable_costs)`**: Determines the number of units required to break even.
3. **`apply_discount(selling_price, discount_percentage)`**: Adjusts the selling price based on a given discount percentage.
4. **`calculate_tax(price, tax_rate)`**: Computes the final price after tax is applied.
5. **`suggest_retail_price(cost_price, desired_margin)`**: Suggests an ideal retail price based on the desired profit margin.
6. **`project_annual_revenue(monthly_revenue)`**: Estimates the store’s annual revenue based on monthly income.
7. **`analyze_sales_trends(sales_data)`**: Determines the highest and lowest months of sales from a given dataset.
8. **`main()`**: Prompts the user for input and executes all necessary calculations, displaying the results.

Additionally, security measures were added by requiring users to enter a **username and password** before proceeding, reinforcing the importance of privacy when handling business data.

### `test_project.py`
This file contains unit tests for verifying the correctness of key functions within `project.py`. The tests are written using **pytest**, ensuring that calculations return accurate results and handle edge cases appropriately. Below are the functions that have corresponding test cases:

- `test_calculate_profit_margin()`
- `test_calculate_break_even_point()`
- `test_apply_discount()`
- `test_calculate_tax()`
- `test_suggest_retail_price()`
- `test_project_annual_revenue()`
- `test_analyze_sales_trends()`

These tests check various input conditions, including normal values, edge cases, and invalid inputs, ensuring that the program handles errors correctly and remains robust in real-world use cases.

### `requirements.txt`
This file lists any dependencies needed to run the project. Although the current implementation is based on standard Python libraries, if any additional libraries were required (e.g., for data visualization or advanced analytics), they would be listed here to simplify installation.

## Design Decisions

### Why a Command-Line Interface?
Given the project's scope, a command-line interface (CLI) was chosen for simplicity and efficiency. This approach allows users to enter their business parameters quickly without needing a graphical user interface (GUI), making it a lightweight yet powerful tool.

### Why Include Authentication?
Although not a full security system, a basic username-password authentication was implemented to reinforce the idea that business financial data is private. This simple step increases the professionalism of the application and encourages best practices for handling sensitive information.

### Why Use Pytest for Testing?
`pytest` was chosen because it provides an efficient and structured approach to unit testing. It allows for automated test execution, ensuring that core functionalities remain intact as the project evolves. Additionally, it is easy to integrate and widely used in professional Python development environments.



The **Store Profit Calculator** is a practical financial analysis tool tailored for small business owners and entrepreneurs. By allowing users to input key financial metrics, the program calculates profit margins, tax adjustments, revenue projections, and more. With a strong foundation in **modular functions and automated testing**, this project is both reliable and extensible for future improvements.

This project demonstrates an effective application of Python programming principles while maintaining a clear and structured codebase. Future expansions, such as database support and visualization, would further enhance its value for business users.

