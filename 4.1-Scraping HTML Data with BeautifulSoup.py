##### Important ######
#In Python 3.10, the provided bs4.zip file will not work at this time.

#Instead of using the provided folder, students will need to install BeautifulSoup at the command line.

#Please follow these steps:

#    open Powershell and navigate to your user directory

#    at the prompt type - pip install beautifulsoup4 and then enter

#    once the installation completes, you should be able to complete the assignments

#    make sure that you have deleted the bs4 folder if you downloaded it.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
spans = soup('span')
numbers = []
for span in spans:
    numbers.append(int(span.string))
print (sum(numbers))