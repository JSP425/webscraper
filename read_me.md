# Project Explanation

This is my first webscraping project. The intention is to be able to collect targeted data from sites such as Craigslist and write it into an Excel spreadsheet for sorting and analysis. This project is still in its early exploratory stages.

The current model tests searching for bikes but is intended to work with more categories later.

# Design
webscraper.py is the module that:
- creates the Excel workbook
- creates the tab within the workbook
- initiates the webscraping
- writes the scraping results into the workbook

The execution of the webscraping is done in separate modules that return a dictionary of its results.

The user begins by creating an instance of the report() class, which is an Excel workbook. From there, the user can use the createSearchTab() method to create a tab, name it and determine which webscraping results to populate it. The user can then open the workbook with the open() function.

Quick Example
```python
import webscraper as ws


new = ws.report("C:/Users/jpark/Desktop/newsearch.xlsx")

new.createSearchTab("clist", categoryCode="mca", searchTerm="harley ", cl=["vancouver", "abbotsford", "edmonton", "calgary", "victoria", "nanaimo", "whistler"])
new.createSearchTab("mtnview", dl="https://www.mountainviewhd.com/--inventory?condition=pre-owned")
new.createSearchTab("calg", dl="https://www.calgaryharleydavidson.ca/pre-owned-harley-bikes--inventory?condition=pre-owned")

new.run()

```



# Status

Currently, the webscraper is able to:
- scrape price, title, location and link information from multiple Craigslist locations and HD dealers
- organize search results into an Excel spreadsheet tab; the user can choose which results go into which tab 
- automatically apply filters into the appropriate columns so the rows can be immediately sorted for analysis

Things to do:
- add kijiji functionality
- allow user to run automatically?
- create UI?
