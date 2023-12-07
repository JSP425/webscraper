import webscraper as ws


new = ws.report("C:/Users/jpark/Desktop/newsearch.xlsx")

new.createSearchTab("clist", categoryCode="mca", searchTerm="harley ", cl=["vancouver", "abbotsford", "edmonton", "calgary", "victoria", "nanaimo", "whistler"])
new.createSearchTab("mtnview", dl="https://www.mountainviewhd.com/--inventory?condition=pre-owned")
new.createSearchTab("calg", dl="https://www.calgaryharleydavidson.ca/pre-owned-harley-bikes--inventory?condition=pre-owned")

new.run(autoOpen=True)
