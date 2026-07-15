# PGA Tour Player Grouping — Unsupervised ML for Sports Analytics

An unsupervised machine learning system that groups 88 PGA Tour golfers into balanced, broadcast-ready 4-player groups — replicating (and improving on) how tournament organizers manually build pairings.

## Problem

Tournament groupings aren't random — organizers manually balance player ability, play style/pace, and fan interest to create fair, competitive, broadcast-worthy matchups. This process is done by hand today. Could it be modeled and automated at scale?

## Approach

- **Data preprocessing:** Cleans and standardizes player statistics using `StandardScaler`
- **Clustering model:** Size-constrained **KMeans**, capped at a maximum of 4 players per cluster (`size_max=4`), to keep groups tightly balanced
- **Group balancing logic:** Post-clustering checks ensure no group is overloaded with multiple top performers or fan favorites
- **Fallback handling:** Players missing a fan-interest score are assigned a neutral low value rather than breaking the pipeline

## Features Used

- Strokes Gained: Off-the-Tee, Approach, Putting, Total
- Driving Distance, Greens in Regulation (GIR), Scrambling
- Simulated Fan Interest Score
- Play Style Tag (Aggressive, Balanced, Fast)

## Outcome

- 4-player, statistically balanced groups — no stacked stats or pacing mismatches
- Broadcast-worthy matchups that distribute fan-favorite visibility evenly across groups
- Interactive Streamlit dashboard to visualize and explore generated groupings

## Tech Stack

Python · Pandas · Scikit-learn (KMeans, StandardScaler) · Streamlit

## Why It Matters

This shows ML can replicate a process golf organizers currently do manually — but at scale and with more consistency. The same approach could support broadcasters, fantasy sports platforms, or sports analytics tools that need fair, engaging groupings.

---
*Also shared on [LinkedIn](https://www.linkedin.com/posts/priyanshutiw1253_sportsanalytics-datascience-machinelearning-ugcPost-7349453914506739714-VMhI/).*
