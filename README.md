Create a env # python = 3.8
``` anaconda prompt

create requirement file and add packages
# dvc
# dvc[gdrive]
# sklearn
# Pandas
```bash


Install the packages in req file  

# pip install -r requirement.txt
```bash

Create a template creating py file to create template of the project

template.py

create a folder or original data
add data inside the folder this will act as remote data storage

Now Initialize git

git init

dvc init

dvc add dataset/winequality.csv # this will add csv file to dvc

git add . # things in working directory will be added to stageing area

git commit -m "first commit" # The git commit command captures a snapshot of the project's currently staged changes. Committed snapshots can be thought of as “safe” versions of a project—Git will never change them unless you explicitly ask it to.

again adding and commiting

git add . && git commit - m "update readme.md"

git remote add origin https://github.com/AkshayAnvekar0707/mlops2-simple_dvc.git
# Above cmd is used add origin that is ur git repo, is where all ur code will be

git branch - m main
# this is used as the before branch was master now to change it to main

git push origin main
# Using this we will push our code to git repo

In params.yaml we will store all the data and model related info. Such as data training and models.

# In get_data.py
 First we will add read function to read all configs from yaml file
 Then in get data function we will mention from which key we have to read the data that is basically directory
 
# We will use argpharse to get the data!

# Now we have to load the data, we will load original data and we will save it in raw data folder for further processing.  We will save data with minimal modeification needed and we will use this data in any further process.

# Now we have to split the data for training and testing















