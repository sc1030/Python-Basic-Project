'''email = input("Enter Email: ")
username, domain = email.split("@")
print(f"Username: {username}\nDomain: {domain}")
'''


import re
from typing import Tuple, Optional

class EmailParser:
    def __init__(self):
        # Regular expression for basic email validation
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    def validate_email(self, email: str) -> bool:
        """Check if the email format is valid"""
        if not email:
            return False
        return bool(re.match(self.email_pattern, email))
    
    def parse_email(self, email: str) -> Optional[Tuple[str, str]]:
        """
        Parse email into username and domain if valid
        Returns tuple (username, domain) or None if invalid
        """
        try:
            # Remove leading/trailing whitespace
            email = email.strip()
            
            # Validate email format
            if not self.validate_email(email):
                print("Error: Invalid email format")
                return None
                
            # Split email into username and domain
            username, domain = email.split("@", 1)  # Split only on first @ occurrence
            
            # Additional validation
            if not username or not domain:
                print("Error: Username or domain cannot be empty")
                return None
                
            if "." not in domain:
                print("Error: Domain must contain a top-level domain (e.g., .com)")
                return None
                
            return (username, domain)
            
        except ValueError:
            print("Error: Email must contain exactly one '@' symbol")
            return None
    
    def analyze_domain(self, domain: str) -> dict:
        """Analyze domain characteristics"""
        parts = domain.split(".")
        return {
            "domain_name": parts[0],
            "tld": parts[-1],  # Top-level domain
            "subdomains": parts[:-1] if len(parts) > 2 else []
        }

def main():
    parser = EmailParser()
    
    while True:
        email = input("Enter email (or 'quit' to exit): ")
        
        if email.lower() == 'quit':
            print("Goodbye!")
            break
            
        result = parser.parse_email(email)
        
        if result:
            username, domain = result
            print(f"Username: {username}")
            print(f"Domain: {domain}")
            
            # Additional domain analysis
            domain_info = parser.analyze_domain(domain)
            print("Domain Analysis:")
            print(f"  Domain Name: {domain_info['domain_name']}")
            print(f"  Top-Level Domain: {domain_info['tld']}")
            if domain_info['subdomains']:
                print(f"  Subdomains: {', '.join(domain_info['subdomains'])}")
            
            print()  # Empty line for readability
        
        # Prompt for another try
        print("Try another email or type 'quit' to exit")

if __name__ == "__main__":
    main()