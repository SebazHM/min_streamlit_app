import streamlit as st
import datetime
import json
import os
from collections import defaultdict

DATA_FILE = "apl_rapporter.json"

def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_entry(week_num, date, txt):
    data = read_data()
    if str(week_num) not in data:
        data[str(week_num)] = []
    data[str(week_num)].append({
        'date': str(date),
        'txt': txt,
    })
    write_data(data)

# Main Streamlit app
today = datetime.datetime.today()
current_week_num = today.isocalendar()[1]

st.title("APL Rapporter")

st.write("Nuvarande vecka:", current_week_num)
date = st.date_input("Datum")
selected_week = date.isocalendar()[1]
txt = st.text_area('Text')

if st.button("Spara"):
    add_entry(selected_week, date, txt)
    st.success(f"Rapport sparad för vecka {selected_week}!")

if st.button("Redigera"):
    st.warning("Redigeringsfunktionen är inte implementerad ännu.")

# Display saved reports
st.subheader("Sparade rapporter")
data = read_data()
sorted_weeks = sorted(data.keys(), key=int, reverse=True)

for week in sorted_weeks:
    st.write(f"## Vecka {week}")
    for entry in data[week]:
        st.write(f"Datum: {entry['date']}")
        st.write(entry['txt'])
        st.write("---")

# Export function
if st.button("Exportera till JSON"):
    st.download_button(
        label="Ladda ner JSON",
        data=json.dumps(data, indent=2),
        file_name="apl_rapporter_export.json",
        mime="application/json"
    )



