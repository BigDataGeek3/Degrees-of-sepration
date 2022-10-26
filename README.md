# Degrees-of-sepration
This project demonstrates the six degrees of separation concept by finding connections between actors through the movies that they have worked in together.
Using a small practice dataset containing 1000 movies with 4 actors from each we can find a link between two people
Inputs required:
/n sPath - filepath to the location of the excel file 6DS data.xlsx
Person1 - One actor from that database
Person2 - Another actor from that database

Output:
A table showing in sequence Person1 acted in Movie A with person B who acted in Movie B.....etc with Person2
If any one of the names cannot be found in the dataset or it is not possible to find a path within 3 degrees of sepration an error message will be displayed
