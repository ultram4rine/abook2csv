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


def convert(abookpath, csvpath):
    header = ('Title', 'First Name', 'Middle Name', 'Last Name', 'Nick Name', 'Display Name', 'Company', 'Department', 'Job Title', 'Office Location', 'E-mail Address', 'Notes', 'Web Page', 'Birthday', 'Other Email', 'Other Phone', 'Other Mobile', 'Mobile Phone',
              'Home Email', 'Home Phone', 'Home Fax', 'Home Street', 'Home City', 'Home State', 'Home Postal Code', 'Home Country', 'Business Email', 'Business Phone', 'Business Fax', 'Business Street', 'Business City', 'Business State', 'Business Postal Code', 'Business Country')

    csvfile = open(csvpath, 'w', newline='', encoding='utf-8')
    writer = csv.writer(csvfile)
    writer.writerow(header)

    with open(abookpath, 'r', encoding='utf-8') as abook:
        for line in abook:
            abookrow = line.split("|")
            if line == '':
                continue
            else:
                i = 0
                while i < len(abookrow):
                    abookrow[i] = abookrow[i].replace(
                        '\n', '').replace('\r', '')
                    i += 1

                print(len(header))
                csvrow = []
                i = 0
                while i < len(header):
                    print(header[i])
                    if header[i] == 'First Name':
                        print('fname')
                        csvrow.append(abookrow[1])
                    elif header[i] == 'Last Name':
                        print('lname')
                        csvrow.append(abookrow[2])
                    elif header[i] == 'Display Name':
                        print('dname')
                        csvrow.append(abookrow[1]+' ' + abookrow[2])
                        print('email')
                    elif header[i] == 'E-mail Address' or header[i] == 'Home Email':
                        csvrow.append(abookrow[3])
                    else:
                        print('empty')
                        csvrow.append('')
                    i += 1

                writer.writerow(csvrow)

    csvfile.close()


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    abookpath = args.file
    csvpath = args.csv
    if csvpath == None:
        csvpath = args.file.replace('.abook', '')+'.csv'

    try:
        convert(abookpath, csvpath)
    except:
        print("Cannot convert")
