import time  # time module used to simulate a real time data

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # data web app development
## These packages were downloaded (streamlit and plotly specifically) in command prompt (pip install) within the project folder directory before running script


### Read in data just like in the python api reading files

appname = "Worcester Air Quality Dashboard"
subtitle = "Access Live Air Quality Data"

## Creating function for outline of dashboard app
def main(): 
    st.set_page_config(appname) # Configures set up of page
    st.title(subtitle) #Displays text on page

    ## Load in data

    ## Develop map

    ## Build side bars
    
if __name__ == "__main__":
    main()