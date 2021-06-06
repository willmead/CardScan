from google.cloud import vision
import os


class Scanner:

    def __init__(self):
        # self.client = language.LanguageServiceClient.from_service_account_json("/path/to/file.json")
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'googlecredentials.json')
        self.client = vision.ImageAnnotatorClient.from_service_account_json(file_path)

    def scan(self, image_received):
        image = self.load_image(image_received)
        return self.read_text(image)

    def load_image(self, image):
        # with open(filename, 'rb') as image_file:
        return vision.Image(content=image.read())

    def read_text(self, image):
        return self.client.text_detection(image=image).text_annotations
