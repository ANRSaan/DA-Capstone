import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns

df = pd.read_csv("airline_data_average.csv")



st.title("Airline Price Data Analysis")

year_start = st.selectbox(
    'Choose a starting year:', ('',1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022)
)

year_end = st.selectbox(
    'Choose an ending year:', ('',1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022)
)

select = st.selectbox(
    'Choose your first graph:', ('', 'distance', 'round_trip', 'total_covid_cases', 'total_covid_deaths', 'total_covid_tests_per_thousand', 'total_covid_vaccinations', 'oil_price_per_barrel', 'inflation_adjusted_itin_fare', 'inflation_adjusted_fare_per_mile')
    )

select2 = st.selectbox(
    'Choose your second graph to overlay:', ('', 'distance', 'round_trip', 'total_covid_cases', 'total_covid_deaths', 'total_covid_tests_per_thousand', 'total_covid_vaccinations', 'oil_price_per_barrel', 'inflation_adjusted_itin_fare', 'inflation_adjusted_fare_per_mile')
)


def make_graph(selection, selection2):
    if selection == '' or selection2 == '':
        pass
    else:
        fig, ax = plt.subplots(figsize=(20, 8))
        # plt.title("Inflation Adjusted Fare Per Mile In Relation To Price Of Oil, From 1993 to 2022", fontsize = 30)
        ax = sns.lineplot(data=df, y=f"{selection}", x =range(len(df)), color = "blue");
        ax.tick_params(axis='y')
        ax.set_xlabel("Year", fontsize = 18)
        ax.set_ylabel(f"{selection}", fontsize = 18, color = "b")
        ax2 = ax.twinx()
        ax2 = sns.lineplot(data=df, y=f"{selection2}", x =range(len(df)), color = "red")
        ax2.tick_params(axis='y')
        ax2.set_ylabel(f"{selection2}", fontsize = 18, color = "r")
        plt.xticks(np.arange(0, len(df)+1, 4))

        ax.set_xticklabels(["1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]);
        plt.tight_layout()

        return fig
if select == '' or select2 == '':
    pass
else:
    st.write(make_graph(select, select2))