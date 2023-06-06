import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.lib.dplyr import DataFrame
from rpy2.robjects.lib.ggplot2 import ggplot, aes_string
from rpy2.rinterface_lib.callbacks import logger as r_logger
import logging

r_logger.setLevel(logging.ERROR)  # Silence R warning messages

# Import the required R packages
gratis = importr("gratis")
r_base = importr("base")
ggplot2 = importr("ggplot2")

# Set the seed value
r_base.set_seed(1)

# Call generate_ts to create the specified time series
generated_ts = gratis.generate_ts(n=120)

# Create a dataframe and autoplot the generated time series
plot_data = DataFrame(generated_ts)
plot = ggplot(plot_data) + ggplot2.geom_line(aes_string(x="Index", y="Value"))

# Display the plot
plot.show()