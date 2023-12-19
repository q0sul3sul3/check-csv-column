import csv


def check_csv_column(filename):
    with open(filename, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

        for row in csv_reader:
            if len(row) != len(header):
                print(
                    f'Error: row {csv_reader.line_num} has {len(row)} columns instead of {len(header)}'
                )


if __name__ == '__main__':
    check_csv_column('data.csv')
