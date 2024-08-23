from beautifultable import BeautifulTable

class ContactBook:
    def __init__(self):
        self.__data = {}
    
    def add_contact(self, name=None, address=None, phone_number=None, email=None):
        if name and address and phone_number and email:
            if phone_number not in self.__data:
                self.__data[phone_number] = [name, address, phone_number, email]
                print("Added successfully")
            else:
                print("Number already exists")
        else:
            print("Please enter all the values")

    def delete_contact(self, phone_number=None):
        if phone_number:
            if phone_number in self.__data:
                del self.__data[phone_number]
                print("Deleted successfully")
            else:
                print("Phone number does not exist in the database")
        else:
            print("Please enter a phone number")

    def edit_contact(self, name=None, address=None, phone_number=None, email=None):
        if phone_number and phone_number in self.__data:
            contact_info = self.__data[phone_number]
            if name:
                contact_info[0] = name
            if address:
                contact_info[1] = address
            if email:
                contact_info[3] = email
            self.__data[phone_number] = contact_info
            print("Data updated successfully")
        else:
            print("Phone number does not exist in the database")

    def search_contact(self, query=None, sort_field=None):
        if query:
            search_arr = []
            for key, val in self.__data.items():
                search_arr.append(val + [" ".join(val)])
                        
            result = set()
            for word in query.lower().split():
                for i in range(len(search_arr)):
                    if word in search_arr[i][-1].lower():
                        result.add(i)
            
            ans = []
            for i in result:
                ans.append(search_arr[i][:-1])
            
            sort_index = 0
            if sort_field == "name":
                sort_index = 0
            elif sort_field == "address":
                sort_index = 1
            elif sort_field == "phone_number":
                sort_index = 2
            elif sort_field == "email":
                sort_index = 3

            ans.sort(key=lambda x: x[sort_index])

            self.view_contact(ans)
        else:
            return []

    def view_contact(self, data):
        table = BeautifulTable()
        for contact_info in data:
            table.rows.append(contact_info)

        table.rows.header = [str(i) for i in range(1, len(data) + 1)]
        table.columns.header = ["Name", "Address", "Phone Number", "Email"]
        print(table)

    def console(self):
        while True:
            try:
                print("\n1. Add Contact\n2. Delete Contact\n3. Edit Contact\n4. Search Contact\n5. View Contacts\n6. Stop")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    name = input("Name: ")
                    address = input("Address: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    self.add_contact(name, address, phone_number, email)

                elif choice == 2:
                    phone_number = input("Phone Number: ")
                    self.delete_contact(phone_number)
                
                elif choice == 3:
                    name = input("Name: ")
                    address = input("Address: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    self.edit_contact(name, address, phone_number, email)
                
                elif choice == 4:
                    query = input("Search: ")
                    sort_by = input("Sort by (name/address/phone_number/email): ")
                    self.search_contact(query, sort_by)

                elif choice == 5:
                    self.view_contact(list(self.__data.values()))
                
                elif choice == 6:
                    break

                else:
                    print("Invalid choice. Please choose again.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == '__main__':
    contact_book = ContactBook()
    contact_book.console()
