# for example this is you script file
import numpy as np
import my_packages  # route to your created packages

import my_packages.utils  #--2-- route to your created packages with utils module where the functionality is located
# if we want to put utils in my_packages which is the __init__ file
import my_packages # --1--
data = {'a': 1, 'b': 2, 'c': 3}

arr = np.array(data)

print(arr)

help(my_packages)  # you can view the help if you wnat to see the packages

# -- to use the personal packages that we created 
my_packages.utils.sample_function(break_up=True)  #--2-- we specify the packages, next access the utils file then declare the function
my_packages.sample_function(break_up=True)  # --1-- we specify the packages, next access the utils file then declare the function
# Output
# This is the break up part