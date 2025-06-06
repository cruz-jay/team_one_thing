import csv


def show_contacts():
    contact_list = []
    with open('./contacts/contacts.csv', 'r') as contacts:
        reader = csv.reader(contacts)
        for idx, item in enumerate(reader):
            contact_list.append([item[0], item[1]])
    return contact_list


def add_contacts():
    name = input('Enter name: ')
    number = input('Enter number (Please include tac -): ')
    with open('contacts.csv', 'a', newline='') as contacts:
        writer = csv.writer(contacts)
        writer.writerow([name, number])
