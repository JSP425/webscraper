import webscraper as ws
import os
import pytest
from openpyxl import load_workbook # to test formatting in Excel

exDir = "C:/Users/jpark/Desktop/"

# @pytest.mark.skip(reason="temporarily skipping")
def test_report(random_name):
    inst = ws.report(exDir + random_name + ".xlsx")

    inst.createSearchTab("testTab")
    inst.workbook.close() # <-- needed to create the workbook but will cause warning; otherwise load_workbook cannot find it
    testWB = load_workbook(exDir + random_name + ".xlsx")
    testWS = testWB["testTab"]

    inst.run()

    assert isinstance(inst, ws.report)

    assert os.path.exists(exDir + random_name + ".xlsx") == True

    assert testWS["B1"].font.bold == True  # Check if B1 is bold
    assert testWS["B1"].number_format == 'General'  # Check currency format
    assert 59.0 <= testWS.column_dimensions['D'].width <= 61.0  # Check width; due to rounding, will not return 60 exactly

    os.remove(exDir + random_name + ".xlsx")


