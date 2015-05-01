from BeautifulSoup import BeautifulSoup          # For processing HTML
import urllib2                                   # URL tools
import re                                        # Regular expressions
 
def FindHits(proxyUrl):
    # URL to HTML parse
    url = 'http://mazii.net/api/mazii/%E5%AD%97/10'
 
    if len(proxyUrl) > 0:
        # Proxy set up
        proxy = urllib2.ProxyHandler( {'http': proxyUrl} )
 
        # Create an URL opener utilizing proxy
        opener = urllib2.build_opener( proxy )
        urllib2.install_opener( opener )
 
        # Aquire data from URL
        request = urllib2.Request( url )
        response = urllib2.urlopen( request )
    else:
        # Aquire data from URL
        response = urllib2.urlopen( url )
 
    # Extract data as HTML data
    html = response.read()
 
    # Parse HTML data
    soup = BeautifulSoup( html )
 
    # Search requested page for <div> section with id="footer"
    # (The result is returned in unicode)
    footer = soup.findAll( 'div', id="footer" )
 
    # Hint: on this site, it is known that only a single "footer" section
    # exists, and that the hit counter resides in that same section
 
    # Search for the frase "Hits=<some number>"
    pattern = re.compile( r'Hits=.*[0-9]' )
    items = re.findall( pattern, str(footer[0]) )
 
    # Print result
    print items[0]        # -> "Hits=<count>"
 
 
if __name__ == "__main__":
    print "Processing..."
    FindHits("58.132.25.19:3128")          # Supply proxy if required. 
                          # FindHist("http://<proxyname>:<port>")