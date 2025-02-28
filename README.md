# Store Profit Calculator
## Video Demo: https://youtu.be/YUeJrB_B8kg
The **Clothing Store Profit Calculator** is a Python application that aims to assist store owners in analyzing the profitability of their business. It computes important financial figures like profit margins, break-even points, tax adjustments, retail prices, and sales trends. With the input of fundamental business parameters, users can immediately see how various factors influence their store's profitability and revenue.

This project was made to be interactive along with being functional, with various financial functions that give insightful data for business decision-making. Also, the program is interactive and asks for various numerical values to be inputted to be calculated.

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
Due to the nature of the project, a command-line interface (CLI) was selected for efficiency and simplicity. This will enable users to input their business parameters rapidly without the requirement of a graphical user interface (GUI), thus being a light but effective tool.

### Why Include Authentication?
While not a complete security system, a simple username-password authentication was added to help drive home the point that business financial information is not public. This simple measure enhances the professionalism of the application and promotes good habits for working with sensitive information.

### Why Use Pytest for Testing?
`pytest` was chosen because it provides an efficient and structured approach to unit testing. It allows for automated test execution, ensuring that core functionalities remain intact as the project evolves. Additionally, it is easy to integrate and widely used in professional Python development environments.



The **Store Profit Calculator** is a useful financial analysis application designed for entrepreneurs and small business owners. By accepting input of important financial figures, the software computes profit margins, tax adjustments, revenue projections, and others. With a solid underpinning of **modular functions and automated testing**, the project is both trustworthy and maintainable for future enhancements.

This is a good application of Python programming concepts with clean and well-organized code. More features, like database integration and visualization, would further enhance its utility for business users.

