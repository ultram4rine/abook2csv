import argparse
import codecs
import configparser
import csv


def create_parser():
    parser = argparse.ArgumentParser(description='Convert .abook to .csv')

    parser.add_argument('file', type=str, help='.abook file to convert')
    parser.add_argument('-c', '--csv', nargs='?', type=str,
                        help='.csv out file, if not set .abook file name will be used')

    return parser


def parse_config(path):
    config = configparser.ConfigParser()
    config.read_file(codecs.open(path, 'r', 'utf8'))
    return config


def convert(columns, abookpath, csvpath):
    csvfile = open(csvpath, 'w', newline='', encoding='utf-8')
    writer = csv.writer(csvfile)
    writer.writerow(columns)

    with open(abookpath, 'r', encoding='utf-8') as abook:
        for line in abook:
            params = line.split("|")
            if line == '':
                continue
            if len(params) != len(columns):
                raise Exception(
                    'Number of columns in columns.ini and in .abook file must be equal')
            else:
                i = 0
                while i < len(params):
                    params[i] = params[i].replace('\n', '').replace('\r', '')
                    i += 1

                writer = csv.writer(csvfile)
                writer.writerow(params)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    confpath = 'columns.ini'
    config = parse_config(confpath)
    columns_pairs = config.items('Columns')
    columns = []
    for num, name in columns_pairs:
        columns.append(name)

    csvpath = args.csv
    if csvpath == None:
        csvpath = args.file.replace('.abook', '')+'.csv'

    # try:
    convert(columns, args.file, csvpath)
    # except:
    #print("Преобразование прошло неудачно")
