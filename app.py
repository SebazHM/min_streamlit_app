import streamlit as st
import datetime
import boto3
import json 
import os 

DATA_FILE = "apl_rapporter.json"

def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def add_entry(date, week_num, txt):
    data = read_data()
    data.append({
        'week': week_num,
        'date': date,
        'txt': txt,
    })
    write_data(data)
 
AWS_REGION = "us-east-1"  # Ändra detta till din önskade region, t.ex. "eu-west-1" för Irland
# Skapa en DynamoDB-resurs med specificerad region
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table("MinBas")
today = datetime.datetime.today()
week_num = today.isocalendar()[1]
st.write ("Vecka:",week_num,"")
date = st.date_input ("Vecka")
txt = st.text_area('')
st.feedback("stars")
if st.button ("Spara"):
 add_entry(week_num,date,txt)
 
st.button ("Redigera")



