import pandas as pd

#columns = ['age', 'week', 'opp', 'ACscr', 'OPPscr', 'location']
df = pd.read_csv('cities.csv')

df.to_html()