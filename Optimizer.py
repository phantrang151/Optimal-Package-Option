# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:45:24 2019

@author: Trang
"""
import pandas as pd
import numpy as np
import math
from collections import defaultdict

class Optimizer:
    
    def __init__(self, no_of_package, package_choice_list):

        # number of packages demanded by clients
        self.demand = int(no_of_package)
        # list of package sizes for a particular product
        self.choices = sorted(package_choice_list)
        # this list is to store minimum number of packages required
        # min number of packages required for 1 items, 2 items,..., N items
        self.min_package = [0] * (self.demand + 1)
        # list of package size chosen
        self.chosen_package = [0] * (self.demand + 1)
        # max number of packages for a particular order
        self.MAX = math.inf
        
        
    '''
    Purpose: Based on the number of items required by clients and package options, 
             find the minimum of packages required. Start with finding the minimum
             packages for 1 item, 2 items,... then N items
    '''      
    def compute_optimal_package(self):
        
        # the number of packages required is 0 when number of items = 0
        self.min_package[0] = 0
        
        # find the min packages required when items = 1, 2, then N 
        for  cur_num_items in range(1, self.demand+1):
            
            # by default, we set the number of packages required to be MAX
            self.min_package[cur_num_items] = self.MAX
            
            # search the min number of packages, considering all options for size
            for  cur_choice in self.choices:
                if (cur_choice <= cur_num_items) :
                    remain_num_items = cur_num_items - cur_choice
                    
                    # if choosing a package size results in a smaller number of packages 
                    # update the chosen_package list, update the min_packge list
                    if (1 + self.min_package[remain_num_items] < self.min_package[cur_num_items]) :                       
                        self.min_package[cur_num_items] = 1 + self.min_package[remain_num_items]
                        self.chosen_package[cur_num_items] = cur_choice       
           
            
    '''
    Purpose: Given the total number of items, list the number of packages at
             different sizes. To support function get_final_package_combination()
    Input  : Number of items demanded
    Output : Optimal package combination, in the form of a dictionary
    '''    
    def get_optimal_choice_list(self, num_items_delivered):
        
        optimal_list = defaultdict(int)
      
        cur_num_items = num_items_delivered
        # traverse through the chosen_package list, retrieve the chosen package
        while (cur_num_items > 0) :
            optimal_list[self.chosen_package[cur_num_items]] += 1
            cur_num_items = cur_num_items - self.chosen_package[cur_num_items]
        
        return optimal_list


    '''
    Purpose: If we cannot deliver the number of items required, find the nearest number
             of items that we can deliver
    Output : Optimal package combination
    '''
    def get_final_package_combination(self):
        
        final_package_combination = None
        
        # firstly, check if we can deliver the number of items required
        # if not, the min number of pacakges calculated is MAX or INFINITIVE
        # after that, find the nearest number of items that we can deliver
        num_items = self.demand
        while (self.min_package[num_items] == self.MAX and num_items > 0):
            num_items -= 1
            
        if num_items > 0 and self.min_package[num_items] < self.MAX:
            final_package_combination = self.get_optimal_choice_list(num_items)
        
        return final_package_combination

            