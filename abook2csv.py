import argparse
import codecs
import configparser
import csv
import os
import sys


def create_parser():
    parser = argparse.ArgumentParser(description='Convert .abook to .csv')

    parser.add_argument('-f', '--file', nargs='?', type=str,
                        help='.abook file to convert')
    parser.add_argument('-c', '--csv', nargs='?', type=str,
                        help='.csv out file, if not set .abook file name will be used')
    parser.add_argument('-d', '--dir', nargs='?', type=str,
                        help='convert all .abook files in directory')

    return parser


def convert(abookpath, csvpath):
    header = ('Title', 'First Name', 'Middle Name', 'Last Name', 'Nick Name', 'Display Name', 'Company', 'Department', 'Job Title', 'Office Location', 'E-mail Address', 'Notes', 'Web Page', 'Birthday', 'Other Email', 'Other Phone', 'Other Mobile', 'Mobile Phone',
              'Home Email', 'Home Phone', 'Home Fax', 'Home Street', 'Home City', 'Home State', 'Home Postal Code', 'Home Country', 'Business Email', 'Business Phone', 'Business Fax', 'Business Street', 'Business City', 'Business State', 'Business Postal Code', 'Business Country')

    csvfile = open(csvpath, 'w', newline='', encoding='utf-8')
    writer = csv.writer(csvfile)
    writer.writerow(header)

    with open(abookpath, 'r', encoding='utf-8') as abook:
        j = 0
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

                csvrow = []
                i = 0
                while i < len(header):
                    if header[i] == 'Title':
                        print('Set title: {}'.format(abookrow[0]))
                        csvrow.append(abookrow[0])
                    elif header[i] == 'First Name':
                        print('Set first name: {}'.format(abookrow[1]))
                        csvrow.append(abookrow[1])
                    elif header[i] == 'Last Name':
                        print('Set last name: {}'.format(abookrow[2]))
                        csvrow.append(abookrow[2])
                    elif header[i] == 'Display Name':
                        print('Set display name: {}'.format(
                            abookrow[1]+' ' + abookrow[2]))
                        csvrow.append(abookrow[1]+' ' + abookrow[2])
                    elif header[i] == 'E-mail Address':
                        print('Set e-mail: {}'.format(abookrow[3]))
                        csvrow.append(abookrow[3])
                    else:
                        csvrow.append('')
                    i += 1

                writer.writerow(csvrow)
                j += 1
                print('{} contact done\n'.format(j))

    csvfile.close()
    print('{0} file done, output in {1}\n'.format(abookpath, csvpath))


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.dir != None:
        directory = args.dir
        for filename in os.listdir(directory):
            if filename.endswith(".abook"):
                abookpath = directory+'/'+filename
                csvpath = abookpath.replace('.abook', '.csv')
                try:
                    convert(abookpath, csvpath)
                except:
                    print('Cannot convert {}'.format(abookpath))
    elif args.file != None:
        abookpath = args.file
        csvpath = args.csv
        if csvpath == None:
            csvpath = abookpath.replace('.abook', '.csv')

        try:
            convert(abookpath, csvpath)
        except:
            print('Cannot convert {}'.format(abookpath))
