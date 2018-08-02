import pandas as pd 

#years = range(2014, 2018)

#shop1 = pd.Series([2409.14, 2941.01, 3567.7, 5679.9], index=years)
#shop2 = pd.Series([2509.14, 2741.01, 3167.7, 5779.9], index=years)
#shop3 = pd.Series([2609.14, 2841.01, 3467.7, 5879.9], index=years)

#shops = pd.concat([shop1, shop2, shop3], axis=1)
#cities = ["New Delhi", "Mumbai", "Pune"]
#shops.columns = cities
#print(shops)

cities = {"name": ["London", "Berlin", "Madrid", "Rome"],
			"population": [6776565, 787899, 787675, 4576567],
			"country": ["England", "Germany", "Spain", "Italy"]}

city_frame = pd.DataFrame(cities)
#print(city_frame.columns.values)

#ordinals = ["first", "second", "third", "forth"]

#city_frame = pd.DataFrame(cities, index=ordinals)

city_frame = city_frame.sort_values(by="population", ascending=False)
print(city_frame)