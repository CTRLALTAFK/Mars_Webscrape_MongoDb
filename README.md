# Mars_Webscrape_MongoDb

Scraping-Mars-Data
Purpose
This app scrapes data about Mars from various websites using beautiful soup. It then uses this information to render a simple website with information and images relating to mars.
app.py is a flask app has routes that take the data from the web scraping function and save it in a MongoDB database using pymongo. app.py also contains a route that renders the html page using the data from the noSQL database. scrape_mars.py is the function that uses beatiful soup, lxml, and pandas to perform the actual web scraping.
Requirements
In order to run app.py python to be installed. Python 3.6.2 was used during development. All required libraries can be found in requirements.txt and installed with the following command:

pip install requirements.txt -r

Running the Code
To run the flask app type the following into the command line:

python app.py

Copy the local address listed into your browser to render the html page.

