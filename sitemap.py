
import os
import sys

args = sys.argv[1:]
if len(args) == 0:
    print("Usage: python sitemap.py <web root>")
    exit(1)

#domain = args[0].split('/')[-1]
domain = args[0]
isweb = args[1] if len(args) > 1 else None

BASE_URL = f'/'  # Base URL of your website
ROOT = f'{domain}/'   # Path to your web root directory
if isweb:
    ROOT = '/var/www/'+ROOT
else:
    ROOT = './'

print(domain, BASE_URL)
def find_valid_endpoints(directory):
    """
    Recursively finds and returns a list of valid web endpoints based on presence of index.html in a directory.

    :param directory: The root directory to start the search from.
    :return: A list of valid web endpoint paths.
    """
    valid_endpoints = []
    for root, dirs, files in os.walk(directory, followlinks=True):
        # Skip any directories that start with a dot
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        # Check if 'index.html' exists in the current directory
        if 'index.html' in files:
            # Construct the valid endpoint by removing the directory path prefix, then trim it to be a valid URL path
            endpoint = os.path.relpath(root, directory)
            if endpoint == '.':
                continue
            else:
                # Prepend a '/' to non-root paths and replace os specific separators with URL separators.
                endpoint = endpoint.replace(os.path.sep, '/')
            
            valid_endpoints.append(endpoint)

    return valid_endpoints

# Replace '/path/to/webroot' with your actual web server's root directory's full path

endpoints = find_valid_endpoints(ROOT)
endpoints.sort()

# Create sitemap.txt in ROOT
with open(os.path.join(ROOT, 'sitemap.txt'), 'w') as sitemap:
    for endpoint in endpoints:
        sitemap.write(BASE_URL + endpoint + '\n')

print(f'Wrote {len(endpoints)} endpoints to {ROOT}sitemap.txt')
