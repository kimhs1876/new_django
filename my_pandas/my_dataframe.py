class MyDataFrame(object):
    def __init__(self, columns, index):
        self.columns = columns
        self.index = index

    @staticmethod
    def main():
        df = MyDataFrame(10,3)