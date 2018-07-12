# Logs Analysis
Full Stack Developer Nano Degree Project 

## How To Run

### Step 1: Set UP
The project is developed in python3 and uses certain dependecies, stored in `reqirements.txt`. To install the dependencies using pip:

`pip install -r requirements.txt`

It is assumed that the `postgres sql` environment is set up and the database `news` with it's data exists.

### Step 2: Generating the report

To generate the report, and print it's output in the command line, use:

`python3 logs-analysis.py`

To generate the report and save it in a text file, use:

`python3 logs-analysis.py > filename.txt` 

where `filename` should be replaced with the desired output file name.

For instance, 

`python3 logs-analysis.py > output.txt` 

was used to generate the *output.txt* file in the repository which contains the generated report output.

## Structure of the Code

The code consists of 3 primary functions which interact with the database:

* **top_3_articles()** : It fetches the top 3 articles from the database sorted in descending order according to views.
* **popular_authors()**: It fetches the list of authors and the number of times their articles have been viewed in descending order of views.
* **error_significant** : It fetches all those dates from logs on which the percentage of requests resulting in error is greater than 1.
* **generate_report** : It is a helper function, which formats the report text and calls the other 3 functions.

All the functions achieve their result using a *JOINS* in a single SQL query.
