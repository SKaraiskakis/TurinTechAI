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
from rpy2.robjects import pandas2ri
import rpy2.robjects.lib.ggplot2 as ggplot2
import matplotlib.pyplot as plt
from io import BytesIO

# Activate pandas conversion for R & Python data frames
pandas2ri.activate()

# Load required R packages
base = importr('base')
gratis = importr('gratis')
forecast = importr('forecast')
feasts = importr('feasts')

# Define the R code as a string
r_code = """
library(gratis)
library(ggplot2)
library(forecast)
library(feasts)
set.seed(1)
ts_obj <- mar_model(seasonal_periods=12) %>%
  generate(length=120, nseries=2)
autoplot(ts_obj, y = "value")
"""

# Run the R code and extract the ggplot2 object
r_plot = robjects.r(r_code)

# Convert ggplot2 object to an image and display
r_png = rpy2.robjects.lib.grdevices.render_to_bytesio(r_plot, format="png")
bytes_io = BytesIO(r_png)
img = plt.imread(bytes_io)
plt.imshow(img)
plt.axis('off')
plt.show()