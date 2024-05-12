#Anoushka Saha
#Python Packages
#May 12th, 2024
#Day 16 Practice

#Importing class from package
from prettytable import PrettyTable

#Creating an object and saving it to variable
table = PrettyTable()

#Adding data to table using methods
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

#Changing alignment attribute
table.align["Pokemon Name"] = "l"
table.align["Type"] = 'l'

print(table)
