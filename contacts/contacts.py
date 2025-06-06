import csv


def show_contacts():
    with open('contacts.csv', 'r') as contacts:
        reader = csv.reader(contacts)
        for rows in reader:
            print(rows)


def add_contacts():
    name = input('Enter name: ')
    number = input('Enter number: ')
    with open('contacts.csv', 'a', newline='') as contacts:
        writer = csv.writer(contacts)
        writer.writerow([name, number])
