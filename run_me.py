import webscraper as ws


new = ws.report("newsearch")

new.createSearchTab("clist", searchTerm="harley ",cl=["vancouver", "abbotsford", "edmonton", "calgary", "victoria", "nanaimo", "whistler"])
new.createSearchTab("mtnview", dl="https://www.mountainviewhd.com/--inventory?condition=pre-owned")
new.createSearchTab("calg", dl="https://www.calgaryharleydavidson.ca/pre-owned-harley-bikes--inventory?condition=pre-owned")

new.run()