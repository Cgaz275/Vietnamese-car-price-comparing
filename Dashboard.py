import streamlit as st
import pandas as pd
import plotly.express as px

import os

current_directory = os.path.dirname(__file__)
csv_path = os.path.join(current_directory, 'car_detail_en.csv')
datasets = pd.read_csv(csv_path)

# sidebar
st.sidebar.title('Dashboard `Demo`')
st.sidebar.header('Vietnamese car price range')
st.sidebar.subheader('Cars filtered')


# Price by brand
selected_brand = st.sidebar.multiselect('Select a car brand', datasets['brand'].unique())

# Price by model
selected_model = st.sidebar.multiselect('Select a car model', datasets['car_model'].unique())

# Price by condition
selected_condition = st.sidebar.selectbox('Select car condition', datasets['condition'].unique())

st.markdown('<h1>Searching</h1>', unsafe_allow_html=True)

# Filter data based on selected parameters
filtered_data = datasets[
    (datasets['brand'].isin(selected_brand)) &
    (datasets['car_model'].isin(selected_model)) &
    (datasets['condition'] == selected_condition)
]

# Define columns to display
display_columns = ['brand', 'car_model', 'condition', 'car_name', 'year_of_manufacture', 'price. price']

# Display the filtered data with selected columns
st.dataframe(filtered_data[display_columns])

st.markdown('<h1>Price chart</h1>', unsafe_allow_html=True)


# Create a bar chart using Plotly Express
# Create a bar chart using Plotly Express with category_orders for brand
fig_by_brand = px.bar(
    filtered_data, x='brand', y='price', color='brand',
    title='Comparison by brand', labels={'price': 'Price'}
)

# Create a bar chart using Plotly Express with category_orders for car_model
fig_by_model = px.bar(
    filtered_data, x='car_model', y='price', color='car_model',
    title='Comparison by model', labels={'price': 'Price'}
)

# Show the chart
st.plotly_chart(fig_by_brand)
st.plotly_chart(fig_by_model)

print(datasets['price'].dtype)
print(datasets['price'].unique())