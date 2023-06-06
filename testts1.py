import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri, r
import rpy2.robjects.lib.ggplot2 as ggplot2
from rpy2.robjects.lib import grdevices
import matplotlib.pyplot as plt
from io import BytesIO
import tempfile
import os

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

ts_df <- data.frame(time = time(ts_obj), value = as.vector(ts_obj))
ggplot(ts_df, aes(x = time, y = value)) + geom_line() + theme_minimal()
"""

# Run the R code and extract the ggplot2 object
r_plot = robjects.r(r_code)

# Save ggplot2 object as a temporary file
with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
    grdevices.png(file=tmp_file.name, width=800, height=600)
    r.plot(r_plot)
    grdevices.dev_off()

# Read the saved temporary plot into an image and display
with open(tmp_file.name, 'rb') as img_f:
    img = plt.imread(img_f)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

# Remove the temporary file
os.unlink(tmp_file.name)