import requests

class FigmaClient:
    def __init__(self, token, file_id):
        self.token = token
        self.file_id = file_id
        self.base_url = "https://api.figma.com/v1"

    def get_file_json(self):
        headers = {"X-Figma-Token": self.token}
        url = f"{self.base_url}/files/{self.file_id}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def extract_layout_data(self, frame_name):
        data = self.get_file_json()
        # TODO: Traverse document tree to find frame by name and extract layout info
        return []
