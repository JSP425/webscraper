from bs4 import BeautifulSoup
import requests
import xlsxwriter
import subprocess # this is for opening the file automatically after
from craigslistscraper import cl_search
from dealerscraper import dl_search

class report():
    def __init__(self, filename) -> None:
        self.filename = filename
        self.filedestination = f"C:/Users/jpark/Desktop/{filename}.xlsx"
        self.workbook = xlsxwriter.Workbook(self.filedestination)
    
    
    def addPriceTabFormat(self, targetWorksheet):
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
        cellRow = 2
        for value in targetDict.values():

            self.worksheet.write(f"B{cellRow}", value[0])
            self.worksheet.write(f"D{cellRow}", value[1])
            self.worksheet.write(f"F{cellRow}", value[2])
            self.worksheet.write(f"I{cellRow}", value[3])

            cellRow += 1
        
    def createSearchTab(self, tabName, searchTerm="", cl = [], dl = [], kj = []):
        # self.workbook = xlsxwriter.Workbook(self.filedestination)

        self.worksheet = self.workbook.add_worksheet(tabName)
        self.addPriceTabFormat(self.worksheet)

        if cl:
            clDict = cl_search(cl, searchTerm)
            self.writePriceTabFormat(clDict)
        if dl:
            dlDict = dl_search(dl)
            self.writePriceTabFormat(dlDict)
        

        self.worksheet.autofilter('B1:I1')

        # self.workbook.close() <-- this will make it unwritable in funciton below. keep it open
    
    def run(self):
        self.workbook.close()
        subprocess.Popen(['start', 'excel', self.filedestination], shell=True)


