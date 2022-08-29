import requests
url = 'http://172.18.58.80/index.php'
r = requests.get(url)
print(r.text)

print("************")

# status code
print("Status code:")
print("\t*", r.status_code)

print("************")

h = requests.head(url)
print("Header:")

print("************")

# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])

print("************")

headers = {
    'User-Agent' : 'Iphone 8'
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

