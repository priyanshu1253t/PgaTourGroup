import streamlit as st
import pandas as pd

# Load the grouped player data
df = pd.read_csv("C:/Users/Priyanshu/Downloads/Pga/grouped_players_balanced.csv")

# Set up the page
st.set_page_config(page_title="Golf Player Groups", layout="wide")
st.title("🏌️ PGA Golf Player Groups")
st.markdown("Grouped by playing style and performance metrics (max 4 per group)")

# Sort by group number
df = df.sort_values(by='Group_No')

# Get all unique groups
group_ids = sorted(df['Group_No'].unique())

# Display two groups per row
for i in range(0, len(group_ids), 2):
    cols = st.columns(2)

    for j in range(2):
        if i + j < len(group_ids):
            group_id = group_ids[i + j]
            group_df = df[df['Group_No'] == group_id]

            with cols[j]:
                st.markdown(f"### 📦 Group {group_id}")
                for _, row in group_df.iterrows():
                    st.markdown(f"- **{row['player_name']}**  | SG: {row['sg_total']:.2f} | Play Style: {row['play_style']} | Fan Score: {row.get('fan_score', 'N/A')}")
