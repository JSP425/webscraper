import webscraper as ws

tester = ws.report("testsearch")
tester.sources(cl = ["vancouver", "abbotsford", "edmonton"])
tester.run("harley")