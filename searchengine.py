import shelve
d=shelve.open('data.shelve')

while True:
    query = raw_input("please give the query:\n")
    if query in d:
        result = d[query][:100]
        print "\n".join(result)