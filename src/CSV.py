import csv
import pandas as pd


class CSV:
    def __init__(self, path):
        try:
            self.__read_csv(path)
        except IOError:
            print("Can't open file")
            exit(2)

    def get_data(self):
        return self.__data

    @staticmethod
    def export(filename, data, header=None):
        df = pd.DataFrame(data)
        df.to_csv(filename, encoding="utf-8", index=False, header=header)

    def __read_csv(self, filename):
        file = open(filename, "rU", encoding="utf8")
        reader = csv.reader(file, delimiter=",")

        self.__data = []
        for row in reader:
            self.__data.append(row)

        file.close()
