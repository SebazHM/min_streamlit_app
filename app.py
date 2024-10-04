AWS_REGION = "us-east-1"  # Ändra detta till din önskade region, t.ex. "eu-west-1" för Irland
# Skapa en DynamoDB-resurs med specificerad region
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
import streamlit as st
import datetime
table = dynamodb.Table("MinBas")
today = datetime.datetime.today()
week_num = today.isocalendar()[1]
st.write ("Vecka:",week_num,"")
date = st.date_input ("Vecka")
txt = st.text_area('')
st.feedback("stars")
st.button ("Spara")
st.button ("Redigera")

def add_entry(week_num,date,txt):
 table.put_item(
Item={
"week_num":week_num,
"date":date,
"txt":txt,
}
)
