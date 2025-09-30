import streamlit as st
import pandas as pd
import datetime


rooms = ['Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5', 'Room 6']
bins = ['Refuse Bin', 'Recycle Bin']

def get_week_number():
    today = datetime.date.today()
    return today.isocalendar()[1]  # ISO week number


def get_assignment(week_number):
    room = rooms[(week_number - 4) % len(rooms)]
    bin_type = bins[(week_number - 1) % len(bins)]
    return room, bin_type



st.set_page_config(page_title = 'Trash Timetable', page_icon = '🗑️', layout = 'centered')
st.title('Trash 🗑️ Timetable')

week_number = get_week_number()
room, bin_type = get_assignment(week_number)


weeks_ahead = 7
schedule = []

for i in range(weeks_ahead):
    future_week = week_number + i
    r, b = get_assignment(future_week)
    year = datetime.date.today().year
    start_date = datetime.date.fromisocalendar(year, future_week, 1)
    end_date = datetime.date.fromisocalendar(year, future_week, 7)
    schedule.append({
        'Dates': f"{start_date.strftime('%d %b')} - {end_date.strftime('%d %b')}",
        'Room': r,
        'Bin': b})


st.header("This Week's Duty")
if datetime.date.today() == datetime.date.fromisocalendar(datetime.date.today().year, week_number, 7):
    st.warning(f"Hey **{room}**, it's Sunday, please don't forget to take out the **{bin_type}**")
else:
    st.success(f'**{room}** is responsible for the **{bin_type}** by Sunday :)')

st.header('Upcoming Schedule')
df = pd.DataFrame(schedule[1:])
st.table(df)