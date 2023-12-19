import webscraper as ws
import time


saveFileTo = "C:/Users/jpark/Desktop/newsearch.xlsx"

startTime = time.time()
new = ws.report(saveFileTo)

new.createSearchTab("clist", categoryCode="mca", searchTerm="harley", cl=["vancouver", "abbotsford", "edmonton", "calgary", "victoria", "nanaimo", "whistler"])
new.createSearchTab("mtnview", dl="https://www.mountainviewhd.com/--inventory?condition=pre-owned")
new.createSearchTab("calg", dl="https://www.calgaryharleydavidson.ca/pre-owned-harley-bikes--inventory?condition=pre-owned")
new.createSearchTab("kijiji", kj="https://www.kijiji.ca/b-motorcycles/british-columbia/harley/k0c30l9007")

new.run(autoOpen=True)

endTime = time.time()

elapsedTime = endTime - startTime
print(f"Execution took {elapsedTime} seconds")