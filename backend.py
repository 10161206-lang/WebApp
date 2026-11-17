import streamlit as st

import pandas as pd

def create_df(file):
    df = pd.read_csv(file)
    return df

def show_data():
    return [1,"Damages cars, it can cause many "
            "accident, tire cost, rims and it will take "
            "time to fix all of it. This directly impacts "
            "residents, affecting their daily commute "
            "to work, road safety in their "
            "neighborhoods, road conditions and "
            "parking availability. Just because they "
            "are fixing potholes they are closing "
            "roads Philadelphia residents have to "
            "follow the detour and it will take time."]