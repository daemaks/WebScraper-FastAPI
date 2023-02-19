# Web Scraper using BeautifulSoup4 and FastAPI

This project is a simple web scraper built using Python's **BeautifulSoup4** and **FastAPI**.

## Installation

* Clone this repository to your local machine using
* Navigate to the project directory
    ```
    $ cd WebScraper-FastAPI
    ```
* Install the required packages using
    ```
    $ pip install -r requirements.txt
    ```
## Usage
* Run the python script *collect_events.py* and wait
    ```
    $ python3 src/collect_events.py
    ```
* Start the FastAPI server in *src* folder 
    ```
    $ uvicorn main:app --reload
    ```
* Open your web browser and go to http://127.0.0.1:8000/docs
* Select the URL you want to use
* Click on the **"Try it out!"** button to execute the request