import sys
import http.client as httplib
import socket
from urllib.parse import urljoin
from urllib.parse import urlparse
import http

wordfile = open("./wordlist.txt", "r")
wordlist = wordfile.readlines()
wordfile.close()

site = "https://iosddl.net/"


class AdminFinder:
    def __init__(self):
        print("Admin Finder")
        self.adminLocate()

    def adminLocate(self):
        try:
            for word in wordlist:
                word = word.strip("\n")
                admin = "/" + word
                url = urljoin(site, admin)
                parsed = urlparse(url)

                if parsed.scheme:
                    connection = http.client.HTTPSConnection(parsed.netloc, timeout=5)
                else:
                    connection = http.client.HTTPConnection(parsed.netloc, timeout=5)

                connection.request("GET", parsed.path)
                response = connection.getresponse()

                if response.status == 200:
                    print("Admin page found: " + url)

                elif response.status == 302:
                    print("Admin page found: " + url)

                elif response.status == 404:
                    print("Admin page not found: " + url)

                elif response.status == 410:
                    print("Admin page not found: " + url)

                else:
                    print("Error: " + url)

        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit()

        except Exception as e:
            print("Error: " + str(e))
            pass


if __name__ == "__main__":
    AdminFinder()
