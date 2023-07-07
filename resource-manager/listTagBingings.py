from google.cloud import resourcemanager_v3
from google.api_core.client_options import ClientOptions
 
def list_cluster_tags():
    regional_endpoint = "us-central1-c-cloudresourcemanager.googleapis.com"
    client_options = ClientOptions(api_endpoint=regional_endpoint)
    client = resourcemanager_v3.TagBindingsClient(client_options=client_options)
    parent = "//container.googleapis.com/projects/vidyadhar-case-testing/locations/us-central1-c/clusters/cluster-1"
 
    request = resourcemanager_v3.ListTagBindingsRequest(parent=parent,)
    page_result = client.list_tag_bindings(request=request)
 
    for response in page_result:
        print(response)
 
list_cluster_tags()
