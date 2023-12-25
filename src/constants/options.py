
lists = [
  "test proxies",
  "ddos all requests",
  "ddos basic",
  "dns record",
  "admin finder",
  "scraping",
  "bruteforce website",
  "ip reverse",
  "ip tracker",
  "stack scanner",
]
lists = sorted(lists)
lists.insert(0, "exit")

options = {}
key = 0;

for item in lists:
    options[key] = item
    key += 1