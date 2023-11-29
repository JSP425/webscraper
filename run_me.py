import webscraper as ws

tester = ws.report("testsearch")
tester.sources(cl = ["vancouver", "abbotsford", "edmonton", "calgary", "victoria", "nanaimo"])
tester.run("harley", openauto=True)