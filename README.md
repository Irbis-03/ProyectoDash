# ProyectoDash
#This project is about a dashboard build with Python, Stramlit, Sqlite and Chinook sample database. This represents a digital music store. Contains artists albums, and tracks. This also allows to open in a application and show the query relational databases and allows to show it in a interactive visualization.

#Interactions for the project to work:

#1. Place all files in one folder:
#ProyectoDash.py  
#queries.py  
#chinook.db  
#requirements.txt

#2. Intstall requirements
#pip install -r requirements.txt

#3. Run in streamlit
# streamlit run ProyectoDash.py

#The dataset used is the Chinook database, a public sample database that models a digital music store. It contains multiple related tables, including:

artist: stores artist names
album: stores albums linked to artists
track: stores individual songs linked to albums
invoice: invoice_line (optional) → stores sales data

The dataset allows practicing SQL operations such as:

JOINs across tables
Aggregations (COUNT, SUM)
Filtering and ranking queries
