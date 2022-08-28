import pandas as pd
import plotly.express as px
import streamlit as st 

st.set_page_config(page_title = "Fire or not fire",
                   page_icon = ':fire:',
                   layout = "wide")
df = pd.read_csv('train (2).csv')



# Side bar
st.sidebar.header("Please filter here: ")

day = st.sidebar.multiselect(
    "Select the day: ",
    options=df['day'].unique(),
    default=df['day'].unique()
)

month = st.sidebar.multiselect(
    "Select the month: ",
    options=df['month'].unique(),
    default=df['month'].unique()
)

df_selection = df.query(
    "day == @day & month == @month"
)

# Main page
st.title("Datacup Dashboard")
st.markdown("##")

total_fire_incidents = len(df_selection[(df_selection.Classes == "fire")])
total_not_fire_incidents = len(df_selection[(df_selection.Classes == "not fire")])
percentage_of_fire_incidents = round(total_fire_incidents/(total_fire_incidents+total_not_fire_incidents),2)

left_column,middle_column,right_column =  st.columns(3)
with left_column:
    st.subheader("Total fire incidents:")
    st.subheader(f'{total_fire_incidents}')
with right_column:
    st.subheader("Total incidents with no fire:")
    st.subheader(f'{total_not_fire_incidents}')
with middle_column:
    st.subheader("Percentage of fire incidents:")
    st.subheader(f'{percentage_of_fire_incidents}')

st.markdown("---")

fig1 = px.bar(df, x='Classes', y='Temperature')
fig1.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False))
)

fig2 = px.bar(df, x='Classes', y='Rain')
fig2.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig1, use_container_width=True)
right_column.plotly_chart(fig2, use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)
