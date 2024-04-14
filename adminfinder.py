import sys
import asyncio
import aiohttp
from urllib.parse import urljoin
from urllib.parse import urlparse

wordfile = open("./wordlist.txt", "r")
wordlist = wordfile.readlines()
wordfile.close()

site = "https://iosddl.net/"


class AdminFinder:
    def __init__(self):
        print("Admin Finder")
        asyncio.run(self.adminLocate())

    async def adminLocate(self):
        try:
            async with aiohttp.ClientSession() as session:
                tasks = []
                for word in wordlist:
                    word = word.strip("\n")
                    admin = "/" + word
                    url = urljoin(site, admin)
                    tasks.append(self.check_admin(session, url))
                await asyncio.gather(*tasks)

        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit()

        except Exception as e:
            print("Error: " + str(e))
            pass

    async def check_admin(self, session, url):
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    print("Admin page found: " + url)
                    f = open("admin.txt", "a")
                    f.write(url + "\n")
                    f.close()

                elif response.status == 302:
                    print("Admin page found: " + url)

                elif response.status == 404:
                    print("Admin page not found: " + url)

                elif response.status == 410:
                    print("Admin page not found: " + url)

                else:
                    print("Error: " + url)

        except Exception as e:
            print("Error: " + str(e))
            pass


if __name__ == "__main__":
    AdminFinder()
