# NewModeInterview_NYL
NewMode Interview Test by Yulin Nong

# Data Analysis of Represent Civic Information
Short data analysis of Represent Civic Information.

Please run `pip install -r requirements.txt` to install required packages.

## 1 Data files contained in './dataFile':
All data files are collected from https://represent.opennorth.ca/data/.
Plesae refer to https://represent.opennorth.ca/api/ for further application of ` Represent Civic Information API`.
* Candidates : 
	+ House of Commons : Candidates-house-of-commons.csv  (1)
* Representatives : 
	+ All elected officials : Representatives.csv  (2)
	+ House of Commons : Representatives-house-of-commons.csv  (3)
* Provincial legislatures:
	+ Assemblée nationale du Québec : quebec-assemblee-nationale.csv  (4)
* Quebec councils
	+ Conseil municipal de Montréal : conseil-municipal-de-montreal.csv  (5)


## 2 Columns selected from each *.csv file
* Candidates-house-of-commons.csv  (1)
	+ [ 'District name', 'Primary role', 'Name', 'First name', 'Last name', 'Party name' ]
	+ shape : 1432*5
* Representatives.csv  (2)
	+ [ 'Organization', 'District name', 'Primary role', 'Name', 'First name', 'Last name','Gender', 'Party name', 'Office type' ] 
	+ shape : 1636*8
* Representatives-house-of-commons.csv  (3)
	+ [ 'District name', 'Primary role', 'Name', 'First name', 'Last name', 'Party name', 'Office type'] 
	+ shape : 333*6
* quebec-assemblee-nationale.csv  (4)
	+ [ 'District name', 'Primary role', 'Name', 'First name', 'Last name', 'Party name', 'Office type']
	+ shape 124*7
* conseil-municipal-de-montreal.csv  (5)
	+ [ 'District name', 'Primary role', 'Name', 'First name', 'Last name', 'Gender', 'Party name', 'Office type'] 
	+ shape : 64*8

## 3 All output plots are stored in './outputFile'

## 4 Short notes
* For easy read, check 'Canadian_members_of_parliment.html'
* To run jupyter notebook, use 'Canadian_members_of_parliment.ipynb'
* To run as project, start from main.py

