This project uses unsupervised learning (clustering) to group 88 PGA Tour golfers into balanced and engaging groups. It takes into account:

Player performance metrics (e.g., strokes gained, scrambling, etc.)

Fan interest scores (proxy for popularity)

The goal is to create groups that are fair, competitive, and attractive for broadcasters — where fan favorites and top performers get balanced visibility.

⚙️ How It Works
📊 Data preprocessing: Cleans and standardizes player stats.

🧠 Clustering model: KMeans groups players by combined performance and popularity.

🎯 Group balancing logic: Ensures no group is overloaded with top/fan-favorite players.

💡 Fallbacks: If a player has no fan score, a neutral low value is assigned.

🛠 Tech Stack
Python

Pandas, Scikit-learn

Streamlit (optional UI)

