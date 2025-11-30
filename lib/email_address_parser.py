# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
       
        filter_string = re.compile(r'[A-z]\w*\.\w+@\w+\.[a-z]+|[A-z]\w*\@\w+\.[a-z]+')
        filtered_emails = filter_string.findall(self.email_addresses)
        unique_emails = sorted(set(filtered_emails))
        return unique_emails
