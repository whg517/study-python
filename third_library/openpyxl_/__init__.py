# encoding: utf-8

raw_data = {
    'user': [
        {'id': 1, 'name': 'xxx', 'age': 10},
        {'id': 2, 'name': 'yyy', 'age': 11},
        {'id': 1, 'name': 'zzz', 'age': 12},
    ],
    'score': [
        {'name': 'xxx', 'english': 20, 'math': 80, 'chinese': 95},
        {'name': 'yyy', 'english': 50, 'math': 70, 'chinese': 77},
        {'name': 'zzz', 'english': 20, 'math': 80, 'chinese': 90}
    ]
}

if __name__ == '__main__':
    from openpyxl import Workbook

    book = Workbook(write_only=True)
    for table in raw_data:
        sheet = book.create_sheet(table)
        data = raw_data.get(table)
        if data:
            title = data[0].keys()
            body = [list(i.values()) for i in data]
            data = [list(title)] + body
            for i in range(len(data)):
                sheet.append(data[i])
        sheet.column_dimensions['A'].width = 30
    book.save('xx.xlsx')
