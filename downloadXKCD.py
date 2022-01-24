#! python3
# downloadXKCD.py - Downloads every XKCD comic

import requests, os, bs4

url = r'http://xkcd.com/1525'  # starting url
os.makedirs(r'D:\xkcd', exist_ok=True)       #create folder to store comics in

while not url.endswith('#'):

    # Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    # Find the URL of the image
    comicImg = soup.select('#middleContainer > a:nth-child(8)')
    if comicImg == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicImg[0].get('href')
        # Download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to the folder created earlier
        imageFile = open(os.path.join(r'D:\xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the 'prev' button URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
