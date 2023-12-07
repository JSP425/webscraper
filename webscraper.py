from bs4 import BeautifulSoup
import requests
import xlsxwriter
import subprocess # this is for opening the file automatically after
from craigslistscraper import cl_search
from dealerscraper import dl_search

class report():
    """
    Create an Excel workbook instance containing webscraped search results organized into
    tabs.

    An instance first requires the user to specify a file path to create the Excel workbook. 
    The user then uses the createSearchTab to determine what searches to appear in that tab.
    Finally the user will use the run method to execute the webscraping and automatically open 
    the workbook.
    
    """
    def __init__(self, filePath: str) -> None:
        self.filedestination = filePath
        self.workbook = xlsxwriter.Workbook(self.filedestination)
    
    
    def addPriceTabFormat(self, targetWorksheet):
        """
        Apply default column titles im bold

        This also applies number formatting to prices so it can be sorted later.
        This method is utilized in createSearchTab method
        
        """

        bold = self.workbook.add_format({'bold': True})
        currency_format = self.workbook.add_format({'num_format': '$#,##0.00'})
        targetWorksheet.set_column('B:B', None, currency_format)

        # Widen
        # changing column width changes formatting from currency to custom
        # worksheet.set_column('B:B', 10)

        targetWorksheet.set_column('D:D', 60)

        # Text with formatting.
        targetWorksheet.write('B1', 'Price', bold)
        targetWorksheet.write('D1', 'Name', bold)
        targetWorksheet.write('F1', 'Location', bold)
        targetWorksheet.write('I1', 'Link', bold)

    def writePriceTabFormat(self, targetDict):
        """
        Write the contents of a dictionary into a spreadsheet
        
        """


        cellRow = 2
        for value in targetDict.values():

            self.worksheet.write(f"B{cellRow}", value[0])
            self.worksheet.write(f"D{cellRow}", value[1])
            self.worksheet.write(f"F{cellRow}", value[2])
            self.worksheet.write(f"I{cellRow}", value[3])

            cellRow += 1
        
    def createSearchTab(self, tabName, categoryCode = None, searchTerm="", cl = [], dl = [], kj = []):
        """
        Creates a tab within the Excel workbook instance

        User specifies the tab name and from which webpages to scrape from in this method. 
        Multiple tabs can be created in a workbook and tab can contain multiple webscraping sources.
        The actual execution of the webscraping is intiated by this method.
        
        """

        self.worksheet = self.workbook.add_worksheet(tabName)
        self.addPriceTabFormat(self.worksheet)

        if cl:
            clDict = cl_search(cl, categoryCode, searchTerm)
            self.writePriceTabFormat(clDict)
        if dl:
            dlDict = dl_search(dl)
            self.writePriceTabFormat(dlDict)
        

        self.worksheet.autofilter('B1:I1')

        # self.workbook.close() <-- this will make it unwritable in funciton below. keep it open
    
    def run(self):
        """
        Opens the workbook for viewing

        """
        self.workbook.close()
        subprocess.Popen(['start', 'excel', self.filedestination], shell=True)


