import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/mnt/combined_common_players.csv')

# Set the plot style
sns.set_style('whitegrid')

# Visualization 1: Boxplot of salary by position
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='POS', y='salary')
plt.title('Salary Distribution by Position')
plt.xlabel('Position')
plt.xticks(rotation=45)
plt.ylabel('Salary')
plt.savefig('salary_by_position.png')
plt.show()

# Visualization 2: Scatter plot of career points vs salary, colored by position
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='career_PTS', y='salary', hue='POS')
plt.title('Career Points vs Salary Colored by Position')
plt.xlabel('Career Points')
plt.ylabel('Salary')
plt.legend(title='Position')
plt.savefig('points_salary.png')
plt.show()

# Visualization 3: Career trajectory of James Harden
selected_player = 'James Harden'
player_data = df[df['NAME'] == selected_player].sort_values(by='season')

plt.figure(figsize=(10, 6))
plt.plot(player_data['season'], player_data['salary'], marker='o', label='Salary')
plt.plot(player_data['season'], player_data['career_PTS'], marker='s', label='Career Points')
plt.plot(player_data['season'], player_data['career_TRB'], marker='^', label='Career Rebounds')
plt.title(f'Career Trajectory of {selected_player}')
plt.xlabel('Season')
plt.xticks(rotation=45)
plt.ylabel('Value')
plt.legend()
plt.savefig('harden_trajectory.png')
plt.show()

# Visualization 4: Violin plot of career PER by position
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='POS', y='career_PER')
plt.title('Career Player Efficiency Rating (PER) by Position')
plt.xlabel('Position')
plt.xticks(rotation=45)
plt.ylabel('Career PER')
plt.savefig('per_by_position.png')
plt.show()
