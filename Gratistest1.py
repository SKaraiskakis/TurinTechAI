import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

try:
    gratis = importr('gratis')
except:
    install_package = robjects.r('utils::install.packages')
    install_package('gratis')
    gratis = importr('gratis')

# Using gratis functions

# Example: using 'simulate.mar' function from gratis
# Be sure to pass the parameters according to the function signature in R, as seen here -
# https://cran.r-project.org/web/packages/gratis/gratis.pdf

generate_ts = robjects.r['generate_ts']
simulate_mar = robjects.r['simulate.mar']   # Function for simulating the MAR model

# Call generate_ts and simulate_mar with desired values
# First, create the specified time series using generate_ts
generated_ts = generate_ts(n=100)

# Next, simulate the MAR model
result = simulate_mar(generated_ts)

print(result)


import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

utils = importr('utils')
utils.install_packages('lazyeval')