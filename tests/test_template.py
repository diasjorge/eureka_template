import unittest
import json
import os
from eureka_template.template import Template
from eureka_client_mock import EurekaClientMock


class TestTemplateApplications(unittest.TestCase):

    def setUp(self):
        eureka_client = EurekaClientMock()
        template_file = os.path.join(os.path.dirname(__file__),
                                     'fixtures', 'template.j2')
        template = Template(eureka_client, template_file)
        self.conf = json.loads(template.render())

    def test_render_applications(self):
        self.assertEqual(2, len(self.conf))

    def test_render_instances(self):
        for app in self.conf:
            self.assertGreaterEqual(len(app['instances']), 1)


class TestTemplateApplication(unittest.TestCase):

    def setUp(self):
        eureka_client = EurekaClientMock()
        template_file = os.path.join(os.path.dirname(__file__),
                                     'fixtures', 'template-app.j2')
        template = Template(eureka_client, template_file)
        self.conf = json.loads(template.render())

    def test_render_application(self):
        self.assertEqual(1, len(self.conf))
        self.assertEqual("MYAPPLICATION", self.conf[0]["name"])


if __name__ == '__main__':
    unittest.main()
