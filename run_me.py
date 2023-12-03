import webscraper as ws

first = ws.report("testsearch")
first.sources(cl = ["vancouver", "abbotsford", "edmonton", "calgary", "victoria", "nanaimo", "whistler"])
first.runCL("harley", openauto=True)

second = ws.report("dltest")
second.sources(dl = "https://www.trevdeeley.com/--inventory?condition=pre-owned")
second.runDL(openauto=True)
