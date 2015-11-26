import unittest
import json
import os
from eureka_template.template import Template


class TestTemplate(unittest.TestCase):

    class EurekaClientMock():
        def get_apps(self):
            app_file = os.path.join(os.path.dirname(__file__),
                                    'fixtures', 'apps.json')
            return json.load(open(app_file, 'rb'))

    def setUp(self):
        eureka_client = TestTemplate.EurekaClientMock()
        template_file = os.path.join(os.path.dirname(__file__),
                                     'fixtures', 'template.j2')
        template = Template(eureka_client, template_file)
        self.conf = json.loads(template.render())

    def test_render_applications(self):
        self.assertEqual(2, len(self.conf))

    def test_render_instances(self):
        for app in self.conf:
            self.assertGreaterEqual(len(app['instances']), 1)

if __name__ == '__main__':
    unittest.main()
