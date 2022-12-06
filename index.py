import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

df = pd.read_csv("airline_data_average.csv")



st.title("Airline Price Data Analysis")

select = st.selectbox(
    'Choose your first graph:', ('distance', 'round_trip', 'total_covid_cases', 'total_covid_deaths', 'total_covid_tests_per_thousand', 'total_covid_vaccinations', 'oil_price_per_barrel', 'inflation_adjusted_itin_fare', 'inflation_adjusted_fare_per_mile')
    )

select2 = st.selectbox(
    'Choose your second graph to overlay', ('distance', 'round_trip', 'total_covid_cases', 'total_covid_deaths', 'total_covid_tests_per_thousand', 'total_covid_vaccinations', 'oil_price_per_barrel', 'inflation_adjusted_itin_fare', 'inflation_adjusted_fare_per_mile')
)