import requests
import xml.etree.ElementTree as ET

# Make a request to the OAI-PMH endpoint
base_url = 'https://archive.hshsl.umaryland.edu/oai/request'
params = {'verb': 'ListRecords', 'metadataPrefix': 'oai_dc'}
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML response
    root = ET.fromstring(response.content)
    for child in root:
        print(child.tag, child.attrib)

    # Define the namespace if necessary
    # ns = {'dc': 'http://purl.org/dc/elements/1.1/'}

    # Find the specific metadata element
    # metadata_element = root.find('.//dc:subject')
    # If the metadata element has a namespace, use the namespace in the XPath expression:
    # metadata_element = root.find('.//dc:subject', ns)

    # if metadata_element is not None:
    #     # Extract metadata value
    #     metadata_value = metadata_element.text
    #     print("Metadata Value:", metadata_value)
    # else:
    #     print("Metadata element not found.")
else:
    print("Failed to retrieve data. HTTP status code:", response.status_code)