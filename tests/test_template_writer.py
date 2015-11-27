import unittest
import os
import time
from eureka_template.template_writer import TemplateWriter
from eureka_client_mock import EurekaClientMock


class TestTemplateWriter(unittest.TestCase):

    def setUp(self):
        self.template_file = os.path.join(os.path.dirname(__file__),
                                          'fixtures', 'template.j2')
        self.output_file = '/tmp/' + str(time.time())

    def test_writes_file(self):
        writer = TemplateWriter(EurekaClientMock(),
                                self.template_file,
                                self.output_file)

        rendered = writer.render()

        self.assertTrue(writer.write())

        self.assertEqual(rendered, open(self.output_file).read())

    def test_writes_file_when_changed(self):
        writer = TemplateWriter(EurekaClientMock(),
                                self.template_file,
                                self.output_file)

        writer.write()

        self.assertFalse(writer.write())

        writer.rendered = "We fake the content of the previous render"

        self.assertTrue(writer.write())


if __name__ == '__main__':
    unittest.main()
