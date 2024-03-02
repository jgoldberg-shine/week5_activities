from bs4 import BeautifulSoup
import pandas as pd

# Open the HTML file
my_file = open("index.html", "r")

# Parse the HTML file using BeautifulSoup
souped_html = BeautifulSoup(my_file, "lxml")

# Print the file contents
print(my_file)

# Find all categories in the HTML file
categories = souped_html.find_all("h3")

# Find all elements with class "gold" (first favorites)
first_fav = souped_html.find_all(class_="gold")

# Find all elements with class "silver" (second favorites)
second_fav = souped_html.find_all(class_="silver")

# Find all elements with class "bronze" (third favorites)
third_fav = souped_html.find_all(class_="bronze")


print(categories)

# Create a DataFrame using pandas, with columns for Category, First, Second, Third
df = pd.DataFrame({
    "Category": [category.text for category in categories],
    "First": [first.text for first in first_fav],
    "Second": [second.text for second in second_fav],
    "Third": [third.text for third in third_fav]
})

# Print the DataFrame
print(df)

# Write the DataFrame to an Excel file named "favourites.xlsx", without including the index
df.to_excel("favourites.xlsx", index=False)
