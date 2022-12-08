import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns



def make_graph(df, selection, selection2, year_start, year_end):
    
    if year_start == "":
        year_start = df.at[df.index[0], "year"]
    else:
        year_start = int(year_start)

    if year_end == "":
        year_end = df.at[df.index[-1], "year"]
    else:
        year_end = int(year_end)

    df = df.loc[(df["year"] >= year_start) & (df["year"] <= year_end)]

    if selection == '' and selection2 == '':
        pass

    elif selection2 == '':
        fig, ax = plt.subplots(figsize=(20, 8))
        # plt.title("Inflation Adjusted Fare Per Mile In Relation To Price Of Oil, From 1993 to 2022", fontsize = 30)
        ax = sns.lineplot(data=df, y=f"{selection}", x =range(len(df)), color = "blue")
        ax.tick_params(axis='y')
        ax.set_xlabel("Year", fontsize = 18)
        ax.set_ylabel(f"{selection}", fontsize = 18, color = "b")
        length = len(df)
        plt.xticks(np.arange(0, length, 4))

        years = [str(i) for i in range(year_start, year_end+1)]

        ax.set_xticklabels(years)
        plt.tight_layout()

        return fig

    else:
        fig, ax = plt.subplots(figsize=(20, 8))
        # plt.title("Inflation Adjusted Fare Per Mile In Relation To Price Of Oil, From 1993 to 2022", fontsize = 30)
        ax = sns.lineplot(data=df, y=f"{selection}", x =range(len(df)), color = "blue")
        ax.tick_params(axis='y')
        ax.set_xlabel("Year", fontsize = 18)
        ax.set_ylabel(f"{selection}", fontsize = 18, color = "b")
        ax2 = ax.twinx()
        ax2 = sns.lineplot(data=df, y=f"{selection2}", x =range(len(df)), color = "red")
        ax2.tick_params(axis='y')
        ax2.set_ylabel(f"{selection2}", fontsize = 18, color = "r")
        length = len(df)+1
        plt.xticks(np.arange(0, length, 4))

        years = [str(i) for i in range(year_start, year_end+1)]

        ax.set_xticklabels(years)
        plt.tight_layout()

        return fig



def main():    
    df = pd.read_csv("airline_data_average.csv")

    st.title("Airline Price Data Analysis")

    years = ['']
    years.extend(list(range(1993, 2023)))
    year_start = st.selectbox('Choose a starting year:', years)
    year_end = st.selectbox('Choose an ending year:', years)

    select = st.selectbox(
        'Choose your first graph:', ('', 'inflation_adjusted_fare_per_mile','inflation_adjusted_itin_fare', 'oil_price_per_barrel', 'total_covid_cases', 'total_covid_deaths', 'total_covid_tests_per_thousand', 'total_covid_vaccinations', 'distance', 'round_trip')
        )

    select2 = st.selectbox(
        'Choose your second graph to overlay:', ('', 'inflation_adjusted_fare_per_mile','inflation_adjusted_itin_fare', 'oil_price_per_barrel', 'total_covid_cases', 'total_covid_deaths', 'total_covid_tests_per_thousand', 'total_covid_vaccinations', 'distance', 'round_trip')
    )

    if select == '' and select2 == '':
        pass
    else:
        st.write(make_graph(df, select, select2, year_start, year_end))

if __name__ == "__main__":
    main()