import requests
from urllib.parse import urlparse


def google_shopping_search(query, api_key):
    """
    Perform a Google Shopping search with the given query.

    Parameters:
        query (str): The search query.
        api_key (str): The SerpAPI key.

    Returns:
        dict: The JSON response from SerpAPI.
    """
    params = {
        'engine': 'google_shopping',
        'api_key': api_key,
        'q': query,
        'num': 200
    }

    try:
        response = requests.get('https://serpapi.com/search', params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")


def extract_shop_name_from_url(url):
    """
    Extract the shop name from the URL by removing 'www.' and '.com' parts.

    Parameters:
        url (str): The URL of the product.

    Returns:
        str: The shop name extracted from the URL.
    """
    domain = urlparse(url).netloc.lower()
    # Remove 'www.' prefix and '.com' suffix
    domain = domain.replace('www.', '').replace('.com', '')
    return domain.capitalize()


def google_shopping_shop_search(api_key, query, specific_store=None):
    """
    Perform a search on Google Shopping for specific e-commerce shops.

    Parameters:
        api_key (str): The SerpAPI key.
        query (str): The search query.
        specific_store (str): The store to filter results by (e.g., 'Amazon').

    Returns:
        list: A list of product details, including shop names.
    """
    results = google_shopping_search(query, api_key)
    products = []

    if results:
        for result in results.get('shopping_results', []):
            link = result.get('link', '')
            shop_name = extract_shop_name_from_url(link)

            # Filter results by specific store if provided
            if specific_store and shop_name.lower() != specific_store.lower():
                continue

            title = result.get('title', 'No title available')
            price = result.get('price', 'No price available')
            images = result.get('thumbnail', 'No image available')
            description = result.get('description', 'No description available')

            products.append({
                'title': title,
                'link': link,
                'price': price,
                'images': [images] if isinstance(images, str) else images,
                'description': description,
                'shop_name': shop_name
            })

    return products
