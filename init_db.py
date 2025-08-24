import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# ------------------------------------------------------------
# EXERCISES LIST
# ------------------------------------------------------------
data = {
    "theme": ["cross_joins", "cross_joins", "group by"],
    "exercise_name": ["beverages_and_food", "sizes_and_trademarks", "group_by_ventes"],
    "tables": [
        ["beverages", "food_items"],
        ["sizes", "trademarks"],
        ["clients", "ventes"],
    ],
    "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01"],
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")


# -----------------------------------------
# CROSS JOIN EXERCISE
# -----------------------------------------
csv = """
beverage, price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")


# -----------------------------------------
# CROSS JOIN EXERCISE 2
# -----------------------------------------
csv3 = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(csv3))
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

csv4 = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""
trademarks = pd.read_csv(io.StringIO(csv4))
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")


# -----------------------------------------
# GROUP BY EXERCISE
# -----------------------------------------
csv5 = """
client
Oussama
Julie
Chris
Tom
Oussama
Julie
Chris
Tom
Oussama
Julie
Chris
Tom
"""
clients = pd.read_csv(io.StringIO(csv5))
con.execute("CREATE TABLE IF NOT EXISTS clients AS SELECT * FROM clients")

csv6 = """
vente
120
49
35
23
19
5.99
20
18.77
39
10
17
12
"""
ventes = pd.read_csv(io.StringIO(csv6))
con.execute("CREATE TABLE IF NOT EXISTS ventes AS SELECT * FROM ventes")

con.close()
