import pandas as pd
from sklearn.preprocessing import StandardScaler
from k_means_constrained import KMeansConstrained
df=pd.read_csv("C:/Users/Priyanshu/Downloads/Pga/cleaned_pga_player_stats_with_playstyle.csv")
features = ['driving_dist','gir','scrambling','sg_putt','sg_ott','sg_app','sg_t2g','sg_total','fan_score']
X=df[features]
X=X.fillna(X.mean())
scaler=StandardScaler()
scale=scaler.fit_transform(X)
groupno=len(df)//4
leftover = len(df) % 4
kmeans = KMeansConstrained(
    n_clusters=groupno,
    size_min=1,
    size_max=4,
    random_state=42
)

df['Group_No'] = kmeans.fit_predict(scale) + 1
if leftover > 0:
    leftover_df = df.iloc[groupno * 4:].copy()
    leftover_df['Group_No'] = df['Group_No'].max() + 1
    df = pd.concat([df, leftover_df], ignore_index=True)
df.to_csv("C:/Users/Priyanshu/Downloads/Pga/grouped_players_balanced.csv", index=False)
