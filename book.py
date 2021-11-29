import tablib

book = tablib.Databook()
headers = ('first_name', 'last_name')

data = tablib.Dataset(headers=headers)
data.append(('keyword','prdCnt'))
book.add_sheet(data)


with open('test.xlsx', 'wb') as f:
    f.write(book.export('xlsx'))