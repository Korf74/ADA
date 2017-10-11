import pandas as pd


DATA_FOLDER = 'Data'
titanic = pd.read_excel(DATA_FOLDER+'/titanic.xls')

def main():
    titanic.pclass.hist()


if __name__ == "__main__":
    main()