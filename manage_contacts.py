import re
from typing import Optional

class ContactManager:
    '''A class to manage contacts with basic operations like create, update, delete, and read contacts.'''
    
    def __init__(self, name: str, phone_number: Optional[str | int]):
        self.name: str = name
        self.phone_number: str = ''.join(re.findall(r"\d", str(phone_number)))  # ensure phone number is stored as a string of digits
        # initialize contact as an empty dictionary
        # consider using a list of dictionaries for multiple contacts or nested dictionaries
        self.contact: dict[str, str] = {}
    
    # consider making return for function bool to confirm successful operation

    def CreateContact(self) -> None:
        # index: int = 0;
        # consider a nested dictionary 
        #self.contact.update({self.name : self.phone_number})
        self.contact[self.name] = self.phone_number
        print(f"Contact created: {self.name} - {self.phone_number}")
        
    def UpdateContact(self, name: Optional[str] = None, phone_number: Optional[str | int] = None) -> None:   
            # TODO: why is null coalescing not working??
            phone_number = ''.join(re.findall(r"\d", str(phone_number)))
            # user pass optional argument
            # if update name null find by phone number
            # if update name phone_number null find by name
            n: str = str([key for key in self.contact.values() if key == phone_number] if name is None else [key for key in self.contact.keys() if key == name][0])
            #n: str = name or self.contact[self.phone_number]
            #p: str = phone_number
            self.contact.update({n : phone_number})
            print('Contact updated successfully.')
            print("Current contacts:", self.contact)
            
    def DeleteContact(self, name: str) -> None:
        # check if contact exists
        if name not in self.contact:
            print(f"Contact '{name}' not found.")
            return
        # consider using popitem() to remove last item
        self.contact.pop(name)
        print("Contact deleted successfully.")
        print("Current contacts:", self.contact)
        
    def ReadContact(self, name: str = None, phone_number: str = None) -> None:
        # search by key or value
        # the or operator should perform action of null coalescing
        if name is None and phone_number is not None:
            name = [key for key, value in self.contact.items() if value == phone_number][0]
        elif phone_number is None and name is not None:
            phone_number = self.contact.get(name)
        elif name is None and phone_number is None:
            print("No contact found.")
            return
        #print(self.contact.fromkeys(name) or self.contact[self.contact.values().index(phone_number)])
        #self.contact.items()
        if name in self.contact:
            print(f"Contact found: {name} - {self.contact[name]}")
        else:
            print(f"Contact '{name}' not found.")
            
        

# contactManager = ContactManager("John Doe", "123-456-7890")
# contactManager.CreateContact()
# contactManager.UpdateContact("John Doe", "193-456-7890")
# contactManager.ReadContact("John Doe")
# contactManager.DeleteContact("John Doe")    
        