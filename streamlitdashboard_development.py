import time  # time module used to simulate a real time data

import folium
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # to create web map within the app
import streamlit_folium as st_folium # to enable folium map displays

## These packages were downloaded (streamlit, plotly, streamlit-folium, specifically) in command prompt (pip install) within the project folder directory before running script


### Read in data just like in the python api reading files

appname = "Worcester Air Quality Dashboard"
subtitle = "Access Live Air Quality Data"


########################################################

## Displaying Map Function
def folium_map(): # As folium_map is defined in this dictionary - it will visualize the map of worcester
    # Many of these functions came from the streamlit_folium package
    
    ### !!!!!!!!! NEED to read in json data in as a CSV-- this will allow us to viaualize the data when hovered over
    #df = df [(df[TotalPopulation]==TotalPopulation)] # this is the variable that will be displayed when clicked

    map = folium.Map(location= [38, -96.5]) # this sets "map" as the folium map and sets the center at the coordinates
    
    # loading census tracts geojson
    folium.GeoJson(data="AQDashboard_Data/ACS2021_JSON/ACS2021Data_Worcester_Aliases.json").add_to(map)


    #########
    #st_map = st_folium(map, width = 700, height = 450)


    #st.write(df.shape) # st functions are from streamlit library
    #st.write(df.head())
    #st.write(df.columns)
    
#########################################################

## Outlining Dashboard Function
def main(): 
    st.set_page_config(appname) # Configures set up of page
    st.title(appname) #Displays text on page
    st.caption(subtitle) # Adding some description

    ## Load in Worcester demographic GeoJson data
    df = pd.read_csv("/AQDashboard_Data/ACS_2021_Data_Massachusetts/ACS_2021_ALLDATA.csv")
    #df = pd.read_csv()
        
        # Load MAP DATA
    folium_map #### Need to call this function before it will display

    ## Develop map

    ## Build side bars
    
if __name__ == "__main__":
    main()


#####################################################
