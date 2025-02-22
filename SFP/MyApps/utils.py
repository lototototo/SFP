import json
import datetime

def import_trufflehog3_scan(report):
    with open(report, 'r') as file:
        data = json.load(file)
        for i in range(len(data)):
            title = data[i]['rule']['id'] + ' '+ 'found in' + ' ' + data[i]['path']
            line = data[i]['line']
            file_path = data[i]['path']
            mitigate_before = datetime.date.today()
            scanner = 'Trufflehog3'
            product = 'Back'
            severity = data[i]['rule']['severity']
            print(f'{title, line, file_path, mitigate_before, scanner, product, severity}')

def main():
    report = 'trufflehog3.json'
    import_trufflehog3_scan(report)

if __name__ == '__main__':
    main()