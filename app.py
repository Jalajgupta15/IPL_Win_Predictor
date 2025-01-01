import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load match data from the provided CSV file
matches = pd.read_csv('matches.csv')

# Team statistics
teams_stats = {
    "Rising Pune Supergiant": {"home_wins": 5, "away_wins": 5, "home_matches": 8, "away_matches": 8},
    "Mumbai Indians": {"home_wins": 58, "away_wins": 51, "home_matches": 101, "away_matches": 86},
    "Chennai Super Kings": {"home_wins": 51, "away_wins": 49, "home_matches": 89, "away_matches": 75},
    "Delhi Capitals": {"home_wins": 3, "away_wins": 7, "home_matches": 6, "away_matches": 10},
    "Sunrisers Hyderabad": {"home_wins": 30, "away_wins": 28, "home_matches": 63, "away_matches": 45},
    "Rajasthan Royals": {"home_wins": 29, "away_wins": 46, "home_matches": 67, "away_matches": 80},
    "Deccan Chargers": {"home_wins": 18, "away_wins": 11, "home_matches": 43, "away_matches": 32},
    "Kings XI Punjab": {"home_wins": 38, "away_wins": 44, "home_matches": 91, "away_matches": 85},
    "Royal Challengers Bangalore": {"home_wins": 35, "away_wins": 49, "home_matches": 85, "away_matches": 95},
    "Kolkata Knight Riders": {"home_wins": 34, "away_wins": 58, "home_matches": 83, "away_matches": 95},
    "Delhi Daredevils": {"home_wins": 25, "away_wins": 42, "home_matches": 72, "away_matches": 89},
    "Pune Warriors": {"home_wins": 6, "away_wins": 6, "home_matches": 20, "away_matches": 26},
    "Kochi Tuskers Kerala": {"home_wins": 2, "away_wins": 4, "home_matches": 7, "away_matches": 7},
    "Gujarat Lions": {"home_wins": 1, "away_wins": 12, "home_matches": 14, "away_matches": 16}
}

# Set up the IPL-themed style
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #1E1E1E;
        color: white;
    }
    .stButton>button {
        background-color: #FF9800;
        color: white;
        border-radius:10px;
        border:none;
        padding:10px;
        font-size:16px;
        font-weight:bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("IPL Win Predictor")

# Select teams for prediction
team1 = st.selectbox("Select Team A", list(teams_stats.keys()))
team2 = st.selectbox("Select Team B", list(teams_stats.keys()))

# Inputs for match conditions
target_runs = st.number_input("Target Runs", min_value=0)
runs_scored = st.number_input("Runs Scored", min_value=0)
overs_completed = st.number_input("Overs Completed", min_value=0.0)
wickets_lost = st.number_input("Wickets Lost", min_value=0)
venue = st.selectbox("Venue", matches['venue'].unique())

# Function to calculate win probability based on statistics and match conditions
def calculate_win_probability(team1_name, team2_name):
    team1_stats = teams_stats[team1_name]
    team2_stats = teams_stats[team2_name]

    # Example calculation based on home win percentage adjusted for current match conditions
    team1_win_percentage = (team1_stats["home_wins"] / team1_stats["home_matches"]) * (runs_scored / target_runs) * (1 - (wickets_lost / overs_completed))
    team2_win_percentage = (team2_stats["away_wins"] / team2_stats["away_matches"]) * ((target_runs - runs_scored) / target_runs) * (1 - (wickets_lost / overs_completed))

    return max(0.0, min(100.0, team1_win_percentage * 100)), max(0.0, min(100.0, team2_win_percentage * 100))

# Calculate win probabilities
if target_runs > runs_scored:
    team1_prob, team2_prob = calculate_win_probability(team1, team2)

    # Display results with graphics
    st.subheader("Win Probabilities")
    
    fig, ax = plt.subplots()
    teams = [team1 + ' (A)', team2 + ' (B)']
    probabilities = [team1_prob if target_runs > runs_scored else None,
                    team2_prob if target_runs > runs_scored else None]
    
    ax.bar(teams, probabilities,
           color=['#FF5733', '#33FF57'], edgecolor='black')
    
    ax.set_ylim(0,100)
    ax.set_ylabel("Win Probability (%)")
    ax.set_title("Win Probability Comparison")
    
    # Add gridlines for better readability
    ax.yaxis.grid(True)
    
    st.pyplot(fig)

if st.button("Predict Winner"):
    if target_runs > runs_scored:
        if team1_prob > team2_prob:
            st.success(f"{team1} is predicted to win!")
        elif team2_prob > team1_prob:
            st.success(f"{team2} is predicted to win!")
        else:
            st.warning("It's a tie!")
