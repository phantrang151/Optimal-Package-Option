# -*- coding: utf-8 -*-
import pandas as pd
class Helper:
    
    '''
    Purpose: To calculate revenue based on our optimal package option
    Input  : Clients'order, product code, optimal package option, products'details
             Optimal_package_option is a dictionary, key is the package size, value is the number of 
             packages chosen for that size
    Output : Details on the number of packages of different sizes 
    '''
    def calculate_revenue(self, no_of_package,product_code,package_option, product_details):
        revenue_details = ""
        final_message = ""
        revenue = 0
        total_delivered = 0
        
        if package_option is not None:
            # calculate revenue based on number of packages offerred at different sizes  
            for key,value in package_option.items():
                
                unit_price = float(product_details[(product_details['Product_Code']== product_code) \
                             & (product_details['Pack_Size']== key)].Unit_Price)
    
                revenue += value * unit_price    
                total_delivered += key * value                   
                revenue_details += '\n'+ '\t' + str(value) + ' * '+ str(key) + str(product_code) + ' $'+ str(unit_price)
    
            final_message = str(no_of_package) + " " + product_code + " $"+ str(round(revenue,2))
            # if we cannot deliver all items clients need, inform them how many items we can deliver
            if(total_delivered < no_of_package):
                final_message += "\n Can only deliver "+ str(total_delivered) + " packages"
            final_message += revenue_details
        
        # when no package is delivered
        else:
            final_message = str(no_of_package) + " " + product_code + " $0"
            min_package_size = min(product_details[product_details['Product_Code']== product_code].Pack_Size.tolist())
            final_message += "\n Minimum pakage size is "+ str(min_package_size)
            
        return final_message
    
    
    '''
    Purpose: To check if input is valid
    Input  : Clients' order and product codes offerred
    Output : Return error message if input is valid. If input is valid, error message is empty 
    '''
    def is_input_valid(self,demand,product_code,all_product_codes):
        error_message = ""
        
        if float(demand) % 1 != 0:
            error_message += str(demand) + " " + str(product_code)
            error_message += "\n Quantity must be an integer"
            
        elif float(demand) < 1:
            error_message += str(demand) + " " + str(product_code)
            error_message += "\n Quantity must be a positive integer"   
        
        elif product_code not in all_product_codes:
            error_message += str(demand) + " " + str(product_code)
            error_message += "\n This product code does not exist"
            
        return error_message
            