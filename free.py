from bs4 import BeautifulSoup

html_doc="""
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p><b>The Dormouse's story</b></p>
<p>Elsie</p>
<p>Lacie</p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.p)
