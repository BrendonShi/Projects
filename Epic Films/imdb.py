import urllib.request
from bs4 import BeautifulSoup
import os


def imdb_rate(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    rating = soup.find('span', class_='sc-d541859f-1 imUuxf')
    if rating:
        print(f"Rating of the movie: {rating.text}")
        return rating.text
    else:
        print("Rating not found. Check the class name or the HTML structure of the page.")


def imdb_image(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    media_viewer_link = soup.find('a', class_='ipc-lockup-overlay ipc-focusable')

    if media_viewer_link and 'href' in media_viewer_link.attrs:
        media_viewer_url = "https://www.imdb.com" + media_viewer_link['href']
        print(f"Media Viewer URL: {media_viewer_url}")

        req = urllib.request.Request(
            media_viewer_url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')

        soup = BeautifulSoup(html, 'html.parser')

        high_res_image = soup.find('img', attrs={'src': lambda src: src and 'https://m.media-amazon.com/images/' in src})
        if high_res_image and 'src' in high_res_image.attrs:
            high_res_image_url = high_res_image['src']
            print(f"High-Resolution Image URL: {high_res_image_url}")

            image_data = urllib.request.urlopen(high_res_image_url).read()

            file_name = os.path.basename(high_res_image_url.split('?')[0])  # Extract a clean file name
            with open(file_name, 'wb') as f:
                f.write(image_data)
            print(f"High-resolution image successfully downloaded: {file_name}")
            return str(file_name)
        else:
            print("High-resolution image not found on media viewer page.")
    else:
        print("Media viewer link not found on the IMDb page.")


def imdb_name(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    movie_name = soup.find('span', class_='hero__primary-text')

    if movie_name:
        print(f"Name of the movie: {movie_name.text.strip()}")
        return movie_name.text
    else:
        print("Movie name not found. Check the class name or the HTML structure of the page.")








# write the program that would show the difference between the two webpages, texts or other shit