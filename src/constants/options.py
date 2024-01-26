
lists = [
  "test proxies",
  "update proxies",
  "ddos all requests",
  "ddos basic",
  "dns record",
  "spam post",
  "admin finder",
  "clone website",
  "bruteforce website",
  "ip reverse",
  "stack scanner",
  "smtp killer",
]
lists = sorted(lists)
lists.insert(0, "exit")

options = {}
key = 0;

for item in lists:
    options[key] = item
    key += 1