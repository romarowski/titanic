from utils import (read_data, preprocess)


def main():
    df = read_data()
    df = preprocess(df)
    pass

if __name__ == '__main__':
    main()
