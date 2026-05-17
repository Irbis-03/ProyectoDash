import streamlit as st
import sqlite3
import pandas as pd
import queries
import matplotlib.pyplot as plt

DB_PATH = "chinook.db"

def run_query(query, params=()):
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(query, conn, params=params)

st.title("Chinook Music Dashboard")

# Sidebar filters
top_n = st.sidebar.slider("Top N", 5, 20, 10)
search = st.sidebar.text_input("Search track")

metric = st.sidebar.selectbox(
    "Metric",
    ["Track Count", "Total Duration"]
)

# Top artists
if metric == "Track Count":
    df = run_query(queries.QUERY_TOP_ARTISTS_COUNT, (top_n,))
else:
    df = run_query(queries.QUERY_TOP_ARTISTS_DURATION, (top_n,))

st.subheader("Top Artists")
st.bar_chart(df.set_index("artist"))

# Track explorer
df_tracks = run_query(queries.QUERY_TRACK_DETAILS)

if search:
    df_tracks = df_tracks[df_tracks["track"].str.contains(search, case=False)]

st.subheader("Track Explorer")
st.dataframe(df_tracks)

# Histogram 
df_len = run_query(queries.QUERY_TRACK_LENGTH)

st.subheader("Track Length Distribution")

fig, ax = plt.subplots()
ax.hist(df_len["minutes"], bins=20)
ax.set_xlabel("Minutes")
ax.set_ylabel("Number of Tracks")

st.pyplot(fig)

# Revenue table
if st.sidebar.checkbox("Show Revenue"):
    try:
        df_rev = run_query(queries.QUERY_TOP_TRACKS_REVENUE, (top_n,))
        st.subheader("Top Tracks by Revenue")
        st.bar_chart(df_rev.set_index("Name"))
    except:
        st.warning("Revenue table not found in database")
        
df = run_query("SELECT name FROM sqlite_master WHERE type='table';")
st.write(df)