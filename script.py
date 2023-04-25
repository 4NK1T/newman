import argparse
import re
from bs4 import BeautifulSoup

# List of parameters to replace
parameters = ["username", "password", "id", "email", "url", "address", "number", "dob"]

# Parse command line arguments
parser = argparse.ArgumentParser(description='Redact sensitive information in an HTML report')
parser.add_argument('-i', '--input', required=True, help='input file name')
parser.add_argument('-o', '--output', required=True, help='output file name')
args = parser.parse_args()

# Read input file
with open(args.input, 'r', encoding='utf-8') as f:
    html = f.read()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <tr> tags
for tr in soup.find_all('tr'):
    # Find the first <td> tag with class "text-nowrap"
    td_nowrap = tr.find('td', class_='text-nowrap')
    if td_nowrap is not None and td_nowrap.string == 'Authorization':
        # Find the next <td> tag with class "text-wrap"
        td_wrap = td_nowrap.find_next_sibling('td', class_='text-wrap')
        if td_wrap is not None:
            # Redact the content of the <td> tag with class "text-wrap"
            td_wrap.string = '*' * len(td_wrap.string)

# Loop over code blocks and replace parameter values
for parameter in parameters:
    for code in soup.find_all('code', class_='prettyPrint'):
        code.string = re.sub(fr'("{parameter}":\s*")[^"]+', fr'\1********', str(code.string))

# Write modified HTML to output file
with open(args.output, 'w', encoding='utf-8') as f:
    f.write(str(soup))
