'''Alvaro Quintero
P1: Create a New Python Module (Company Byline)
This project is to help better my skills and abilities as a future analyst'''

import math
import statistics

def main():
    

    # Define Variables
    company_name: str = 'Rudy Was Offsides Inc.'
    company_description: str = 'Company that helps you get ahead of the game'
    company_founding_year: int = 2024
    company_city: str = 'Houston'
    company_state: str = 'The great state of Texas'
    company_number_employees: int = 1
    company_offers_benefits: bool = True
    products_offered: list = ['financial help', 'house buying tips', 'car buy tips', 'how to become the best you you can be']
    product_price: list = [100, 300, 500, 200]
    company_sourced_outside_US: bool = False
    company_public_stock: bool = True
    company_stock_price: float = 10000

# Multiline string with byline using f-string formatting
    byline: str = f"""
    Information:
    Name: {company_name}
    Description: {company_description}
    Founding Year: {company_founding_year}
    City: {company_city}
    State: {company_state}
    Number of Employees: {company_number_employees}
    Employee Benefits: {company_offers_benefits}
    employee_satisfaction: float = 9.9
    work_options: list = ['Remote', 'Hybrid', 'Onsite']
    Restroom_breaks: unlimited


    import statistics

smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)



    Products With Pricing:
    Products Offered: {products_offered}
    Product Price: {product_price}
    Max Product Price: {max(product_price)}
    Min Product Price: {min(product_price)}
    Mean Product Price: {statistics.mean(product_price)}
    Median Product Price: {statistics.median(product_price)}
    Standard Deviation of Product Price: {statistics.stdev(product_price)}
    Public Stock: {company_public_stock}
    Stock Price: ${company_stock_price}
    """

    print(byline)

# Call the main function to execute the code
if __name__ == '__main__':
    main()
