# About
In this project, I created an ETL process to extract real estate data from an API ([RapidAPI](https://rapidapi.com/apidojo/api/realty-in-us/)) to a relational database. With the API provided by that website, it was possible to access the data using Python and load it into the MySQL database.

Finally, the entire process was transferred to the cloud and automated using AWS services.

The data extracted is about sale, rental and sold properties in New York City.

# Details
This project was made with Python and Docker. The AWS section is detailed only my [personal page](https://arthursteffens.github.io/project3_etl-pipeline-API-realty-python-aws.html).


# Usage
To properly execute this pipeline, make sure you have Python 3 and Docker installed on your machine.
Follow this steps:
- Clone this repository and navigate into it.
- In repository folder, run ```pip install -r requirements.txt``` on terminal
- Run ```docker-compose up -d``` on terminal. This will bring up a container with MySQL database.
- Run ```python main.py```

You can edit the variables on ```user_data.py``` to retrieve information about other cities and the amount of data.