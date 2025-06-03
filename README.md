# Introduction to Databases and SQL #

This repository uses Python and DuckDB to introduce the basic practical skills of using SQL to interact with databases.
We do this using a technology called "Jupyter Notebooks" - a different way of running Python code (and other languages).
Jupyter notebooks are commonly used in data science as they keep the contents of memory in between executions  
(ie - your variables last a bit longer). You can identify a Jupyter notebooks by its file extension: "*.ipynb".
Notebooks have cells: we are using two different types of cells:

- Markdown cells: which provide explanation. Markdown is a markup language that allows for easy addition of formatting.
Markdown is used by Github (for pages like this README) and other simple content.
- Python cells: which have code to run

## The Notebooks ##

The exercises are split into three notebooks:

- `1_intro_to_sql.ipynb` Teaching you to use SQL to:
  - Create a table
  - Use appropriate data types for columns
  - Insert data into the table
  - Write a simple query

- `2_querying_data.ipynb`  Teaching you to use SQL to:
  - Run queries to count the number of rows in a table
  - Run queries to select only rows that meet a given condition
  - Aggregate data to calculate totals, averages and counts: including using conditions

- `3_joining_tables` Teaching you to use SQL to:
  
  - Create foreign key to primary key relationships between tables
  - Write queries that gather data from multiple tables
  - Use a variety of join types for different scenarios

## Running Tests

Install the dependencies from `requirements.txt` and execute the test suite using `pytest`:

```bash
pip install -r requirements.txt
pytest
```
