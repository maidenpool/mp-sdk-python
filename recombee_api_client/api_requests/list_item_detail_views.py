from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class ListItemDetailViews(Request):
    """
    List all the detail views of a given item ever made by different users.
    """

    def __init__(self, item_id):
        """
        Required parameters:
        @param item_id: ID of the item of which the detail views are to be listed.
        
        
        """
        self.item_id = item_id
        self.timeout = 100000
        self.ensure_https = False
        self.method = 'get'
        self.path = "/items/%s/detailviews/" % (self.item_id)

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
