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
    
    def sources(self, cl = [], dl = [], kj = []):
        self.cl = cl
        self.dl = dl
        # print(cl,hd,kj)
    

    def createExcel(self, searchTerm):
        self.workbook = xlsxwriter.Workbook(self.filedestination)
        self.worksheet = self.workbook.add_worksheet(searchTerm)

        bold = self.workbook.add_format({'bold': True})
        currency_format = self.workbook.add_format({'num_format': '$#,##0.00'})
        self.worksheet.set_column('B:B', None, currency_format)

        # Widen
        # changing column width changes formatting from currency to custom
        # worksheet.set_column('B:B', 10)

        self.worksheet.set_column('D:D', 60)

        # Text with formatting.
        self.worksheet.write('B1', 'Price', bold)
        self.worksheet.write('D1', 'Name', bold)
        self.worksheet.write('F1', 'Location', bold)
        self.worksheet.write('I1', 'Link', bold)

        # self.workbook.close() <-- this will make it unwritable in funciton below. keep it open

    def runCL(self, searchTerm, openauto=False):
        self.createExcel(searchTerm)


        clResults=cl_search(self.cl, searchTerm)
        # print(clResults)

        cellRow = 2
        for value in clResults.values():

            self.worksheet.write(f"B{cellRow}", value[0])
            self.worksheet.write(f"D{cellRow}", value[1])
            self.worksheet.write(f"F{cellRow}", value[2])
            self.worksheet.write(f"I{cellRow}", value[3])

            
            cellRow += 1
            # print(value)

        self.worksheet.autofilter('B1:I1')
        self.workbook.close()

        if openauto == True: 
            subprocess.Popen(['start', 'excel', self.filedestination], shell=True)

    def runDL(self, openauto=False):
        self.createExcel("dealer")


        dlResults = dl_search(self.dl)
        # print(dlResults)

        cellRow = 2
        for value in dlResults.values():

            self.worksheet.write(f"B{cellRow}", value[0])
            self.worksheet.write(f"D{cellRow}", value[1])
            self.worksheet.write(f"F{cellRow}", value[2])
            self.worksheet.write(f"I{cellRow}", value[3])

            
            cellRow += 1
            # print(value)

        self.worksheet.autofilter('B1:I1')
        self.workbook.close()

        if openauto == True: 
            subprocess.Popen(['start', 'excel', self.filedestination], shell=True)

