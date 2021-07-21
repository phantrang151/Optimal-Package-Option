# -*- coding: utf-8 -*-
import pandas as pd
from Optimizer import Optimizer
from Helper import Helper

'''
-----------------To change the number for different test cases ----------------
'''
Test_case = 'Test Case\Test Case 6'

'''
-----------------Read product details and clients'requirements ----------------
'''
product_details = pd.read_csv(Test_case + '\product_details.csv')
#print(product_details)
customer_order = pd.read_csv(Test_case +'\order.csv')
#print(customer_order)
number_of_products = customer_order.shape[0]
all_product_codes = set(product_details['Product_Code'].tolist())

'''
-----------------Process clients'orders ---------------------------------------
'''
for i in range (0, number_of_products):
    # obtain code, demand quantity and diff package sizes for each product
    no_of_package = customer_order.loc[i,'Quantity_Demand']
    product_code = customer_order.loc[i,'Product_Code']
    
    # check if input is valid, then proceed with the calculation
    helper = Helper()
    is_valid_message = helper.is_input_valid(no_of_package,product_code,all_product_codes)
    
    if is_valid_message == "":
        package_choice_list = product_details[product_details['Product_Code']== product_code].Pack_Size.tolist()
        
        # send clients' order to the Optimiser, in order to find the optimal package combination
        optimizer = Optimizer(no_of_package, package_choice_list)
        optimizer.compute_optimal_package()
        package_option = optimizer.get_final_package_combination()
        
        # calculate revenue based on the given optimal solution, display output
        message = helper.calculate_revenue(no_of_package,product_code,package_option, product_details)
        print(message)
    
    else:
        # display error message
        print(is_valid_message)

