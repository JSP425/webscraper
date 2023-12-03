# Project Explanation

This is my first webscraping project. The intention is to be able to collect targeted data from sites such as Craigslist and write it into an Excel spreadsheet for analysis. The project started out as a single script but now I am making an effort to make it more modular as I experiment. This project is still in its early exploratory stages.

The current model tests searching for bikes but is intended to work with other categories later.

The commit history of this project in Git is inconsistent as I am also practicing branching/merging and initiating these actions from the terminal.

# Status

Currently, the webscraper is able to:
- scrape price, title, location and link information from multiple Craigslist locations and HD dealers
- organize search results into an Excel spreadsheet tab; the user can choose which results go into which tab 
- automatically apply filters into the appropriate columns so the rows can be immediately sorted for analysis

Things to do:
- add kijiji functionality
- allow user to decide search categories; currently just searching motorcycles