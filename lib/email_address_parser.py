import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split the string into individual email addresses
        addresses = re.split(r'[,\s]+', self.email_addresses)

        # Filter out empty strings
        addresses = [address for address in addresses if address]

        # Use a set to remove duplicates and convert back to a list
        unique_addresses = list(set(addresses))

        # Sort the list alphabetically
        unique_addresses.sort()

        return unique_addresses

