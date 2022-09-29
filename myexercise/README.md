# CyVerse Coding Exercise

Note: the sample data set is large and there's no requirement to use all of the data in the exercise. Feel free to use a
subset of the data or to use another data set entirely.

## Part 1: RESTful Web Service Endpoint

For this portion of the exercise, use the data in the provided CSV file and create a RESTful web service that returns
the data in JSON format. It is up to your preference, time, and any skills you'd like to demonstrate whether you use the
file directly or ingest it into a database system or similar, and whether the web service supports features such as
sorting and filtering of the data.

## Part 2: User Interface

For this portion of the exercise, use the web service you created in part 1 as the data source for a web interface that
displays that data in an HTML table, once again with any extra features of your choice.

At CyVerse we use many languages in the backend, especially Go and Clojure, and we use NextJS/React for our frontend,
but you are welcome to use any tools and frameworks you prefer.

## Start virtual environment
cd myexercise
source venv/bin/activate

## Install dependencies
pip install -r requirements/base.txt

## Load data
python3 manage.py etl <project directory>/coding-exercise/myexercise/myexercise/community/management/commands/United_States_COVID19_Community_Levels_by_County.csv County