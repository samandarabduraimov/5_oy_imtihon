keys = ["name", "description", "title", "keywords", "content", "charset"]
values = ["document", "The best document", "My document", "doc, word, excel", "None"]

newdict = {key: value for key, value in zip(keys, values + [None])}
print(newdict)
