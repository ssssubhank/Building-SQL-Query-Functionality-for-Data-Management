import csv
from csv import DictReader

class Query:
    def __init__(self, file):
        self.query = ""
        self.filename = ""
        self.order_by_column = ""
        self.order_ascending = True

        try:
            with open(file, 'r') as Q:
                self.query = Q.read().strip()
        except Exception as e:
            print('Please provide a valid query file:', e)
            return

    def validation(self):
        query = self.query
        sample = query.lower().split()

        if len(sample) < 4:
            print("Query format is incorrect. Ensure it follows the 'SELECT column FROM file' format.")
            return

        if sample[0] != 'select':
            print("Query should start with the keyword: select")
            return

        if sample[2] != 'from':
            print("You should mention 'from'")
            return

        self.filename = sample[3]

        # Check for ORDER BY clause
        if 'orderby' in sample:
            order_by_index = sample.index('orderby')
            self.order_by_column = sample[order_by_index + 1]
            if len(sample) > order_by_index + 2 and sample[order_by_index + 2] in ['asc', 'desc']:
                self.order_ascending = sample[order_by_index + 2] == 'asc'

        if sample[1] == '*':
            self.readingall()
        else:
            self.readingcols(sample[1])

    def readingcols(self, column):
        try:
            with open(self.filename, "r") as datafile:
                dict_reader = DictReader(datafile)
                list_of_dict = list(dict_reader)

                if not list_of_dict:
                    print(f"The file '{self.filename}' is empty.")
                    return

                colList = list(list_of_dict[0].keys() if list_of_dict else [])
                if column in colList:
                    if self.order_by_column:
                        list_of_dict.sort(key=lambda x: x[self.order_by_column], reverse=not self.order_ascending)
                    self.printTable(list_of_dict, [column])
                else:
                    print(f"Column '{column}' not found in the file.")
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")

    def readingall(self):
        try:
            with open(self.filename, "r") as datafile:
                dict_reader = DictReader(datafile)
                list_of_dict = list(dict_reader)

                if not list_of_dict:
                    print(f"The file '{self.filename}' is empty.")
                    return

                if self.order_by_column:
                    list_of_dict.sort(key=lambda x: x[self.order_by_column], reverse=not self.order_ascending)
                self.printTable(list_of_dict)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")

    def printTable(self, myDict, colList=None):
        if not colList:
            colList = list(myDict[0].keys() if myDict else [])
        myList = [colList] # 1st row = header
        for item in myDict:
            myList.append([str(item[col] if item[col] is not None else '') for col in colList])
        colSize = [max(map(len, col)) for col in zip(*myList)]
        formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
        myList.insert(1, ['-' * i for i in colSize]) # Separating line
        for item in myList:
            print(formatStr.format(*item))

# Example usage
if __name__ == "__main__":
    a = Query('query.txt')
    a.validation()
