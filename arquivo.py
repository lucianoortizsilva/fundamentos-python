import csv


##############################################
### https://docs.python.org/3/library/csv.html
##############################################
class Arquivo:

    @classmethod
    def read(cls, path):
        with open(path, mode="r", newline="", encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    @classmethod
    def create(cls, file, row):
        with open(file, mode="a", newline="", encoding="utf8") as f:
            writer = csv.writer(f)
            writer.writerow(row)
