import json
import os


class EurekaClientMock():
    def get_apps(self):
        app_file = os.path.join(os.path.dirname(__file__),
                                'fixtures', 'apps.json')
        return json.load(open(app_file, 'rb'))
