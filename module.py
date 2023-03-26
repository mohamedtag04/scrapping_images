from serpapi import GoogleSearch
import requests

def get_google_search_results(query,num_of_page):
    '''
    This function returns the results of a google search for a given query and page number
    '''
    params = {
        "q": query,
        "tbm": "isch",
        "ijn": f"{num_of_page}",
        "api_key": "your serpapi key"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results

def get_image_urls(results):
    '''
    This function returns the image urls from the results of a google search
    '''
    image_urls = []
    for result in results["images_results"]:
        image_urls.append(result["original"])
    return image_urls

def images_6_pages(query:str)->list:
    '''
    This function returns the image urls from the results of a google search for 6 pages of results
    '''
    image_urls = []
    for i in range(0, 6):
        results = get_google_search_results(query, i)
        image_urls.extend(get_image_urls(results))
    return image_urls

def download_image(image_url, query, i):
    '''
    This function downloads the image to the local folder
    '''
    image = requests.get(image_url)
    if image.status_code == 200:
        file_name = f"{query}_{i}.jpg"
        with open(file_name, 'wb') as f:
            f.write(image.content)
        print(f"Downloaded {i}'th image to local folder")
    else:
        print(f"Error in image url for the {i}'th image")

def download_images(query:str):
    '''
    This function downloads the images to the local folder
    '''
    image_urls = images_6_pages(query)
    for i in range(0, len(image_urls)):
        download_image(image_urls[i], query, i)