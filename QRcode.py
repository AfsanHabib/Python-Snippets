
import pyqrcode
import png


link="https://www.facebook.com/afsanhabib10/"
url=pyqrcode.create(link)

# url.svg("afsan.svg",scale=8)
url.png("afsan.png",scale=8)
