# Logs Analysis
This project is a reporting tool that prints out reports (in plain text) based on the data in the database. The database called(news) has 3 tables:
* articles - Which maintains a list of all articles
* authors  - Maintains a list of all authors
* logs - Maintains a log of when an article is accessed on the website and by whom.
It is developed as a part of udacity Full Stack Developer Nano Degree.
## How To Run

### Step 1: Set UP
#### Dependencies
The project is developed in python3 and uses certain dependecies and Postgres SQL database, stored in `reqirements.txt`. To install the dependencies using pip:

`pip install -r requirements.txt`

#### Database
Postgres SQL is required to be set up. The file `newsdata.zip` contains the file `newsdata.sql` within it, which has all the data on which the reporting tool runs it's queries. After installing Postgres SQL, the database (named news) can be loaded using the command:

`psql -d news -f newsdata.sql`

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
