import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import os


import yfinance as yf
from plotly import graph_objs as go

# - - - Title - - -
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# - - - Header Section - - -
with st.container():
    st.subheader("Stock Market Data Analysis")
    st.title("Predicting The Baltic Dry Index")


import datetime
from datetime import date




# ------ layout setting---------------------------
window_selection_c = st.sidebar.container() # create an empty container in the sidebar
window_selection_c.markdown("## Insights") # add a title to the sidebar container
sub_columns = window_selection_c.columns(2) #Split the container into two columns for start and end date

def show_delta(self):
        """
        Returning a predicted value for the BDI Index
        """

        cols = st.columns(2)
        (color, marker) = ("green", "+") if difference >= 0 else ("red", "-")

        cols[0].markdown(
            f"""<p style="font-size: 90%;margin-left:5px">{self.symbol} \t {e}</p>""",
            unsafe_allow_html=True
        )
        cols[1].markdown(
            f"""<p style="color:{color};font-size:90%;margin-right:5px">{marker} \t {difference} {marker} {change} % </p>""",
            unsafe_allow_html=True
        )




# - - - Date Selection - - -
def nearest_business_day(DATE: datetime.date):
    """
    Takes a date and transform it to the nearest business day
    """
    if DATE.weekday() == 5:
        DATE = DATE - datetime.timedelta(days=1)

    if DATE.weekday() == 6:
        DATE = DATE + datetime.timedelta(days=1)
    return DATE
# ----------Time window selection-----------------
YESTERDAY=datetime.date.today()-datetime.timedelta(days=1)
YESTERDAY = nearest_business_day(YESTERDAY) #Round to business day

DEFAULT_START=YESTERDAY - datetime.timedelta(days=10193)
DEFAULT_START = nearest_business_day(DEFAULT_START)

START = sub_columns[0].date_input("From", value=DEFAULT_START, max_value=YESTERDAY - datetime.timedelta(days=1))
END = sub_columns[1].date_input("To", value=YESTERDAY, max_value=YESTERDAY, min_value=START)

START = nearest_business_day(START)
END = nearest_business_day(END)


# - - - Creating the Chart - - -
# ---------------stock selection------------------
STOCK = np.array([ "BDI", "CIP"])
SYMB = window_selection_c.selectbox("select stock", STOCK)



if SYMB=='BDI':
    data=pd.read_csv("../raw_data/data/BDI/cleaned_weekly_BDI.csv")
elif SYMB=='CIP':
    data=pd.read_csv("../raw_data/data/CIP/weekly_cleaned_cip.csv")




# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['time'], y=data['close'], name="stock"))
    fig.layout.update(title_text='Adjust the range :point_down:', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()


@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, END)
    data.reset_index(inplace=True)
    return data






















# data_load_state = st.text('Loading...')
# data_load_state.text('Data displayed below!')

# - - - Creating the Slider - - -




# def get_slider_data():
#     el_nino=pd.read_csv("raw_data/data/Climate Data/el_nino.csv")
#     return pd.DataFrame({
#           'first column': el_nino['time'],
#           'Predicted Number': el_nino['Temperature']
#         })

# df = get_slider_data()

# from datetime import datetime
# start_time = st.slider(
#     "When do you want to start?",
#     value=datetime(1995, 1, 1),
#     format="MM/DD/YY")
# st.write("Start time:", start_time)

# filtered_df = df[df['first column'] % start_time]

# st.write(df)


# # - - - Feature Drop Down - - -
# def get_select_box_data():

#     return pd.DataFrame({
#           'first column': list(range(1, 11)),
#           'second column': np.arange(10, 101, 10)
#         })

# df = get_select_box_data()

# option = st.selectbox('Select a line to filter', df['first column'])

# filtered_df = df[df['first column'] == option]

# st.write(filtered_df)


# - - - Value Output Box - - -



# - - - Error Graph - - -
