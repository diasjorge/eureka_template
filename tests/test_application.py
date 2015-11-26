import unittest
import json
from eureka_template.application import Application, Instance
import os


class TestApplication(unittest.TestCase):

    def setUp(self):
        app_file = os.path.join(os.path.dirname(__file__),
                                'fixtures', 'app.json')
        self.info = json.load(open(app_file, 'rb'))

    def test_from_info_set_name(self):
        application = Application.from_info(self.info)
        self.assertEqual("MYAPPLICATION", application.name)

    def test_from_info_set_instances(self):
        application = Application.from_info(self.info)
        for instance in application.instances:
            self.assertIsInstance(instance, Instance)


class TestInstance(unittest.TestCase):

    def test_get(self):
        info = {"hostName": "example.com"}
        instance = Instance(info)
        self.assertEqual("example.com", instance.get('hostName'))

    def test_get_does_not_exist(self):
        instance = Instance({})
        with self.assertRaises(KeyError):
            instance.get("hostName")

    def test_get_nested(self):
        info = {"dataCenterInfo": {"name": "MyOwn"}}
        instance = Instance(info)
        self.assertEqual("MyOwn", instance.get("dataCenterInfo.name"))

    def test_get_nested_does_not_exist(self):
        info = {"dataCenterInfo": {"name": "MyOwn"}}
        instance = Instance(info)
        with self.assertRaises(KeyError):
            instance.get("dataCenterInfo.name.data")

    def test_port(self):
        info = {"port": {"$": 8080}}
        instance = Instance(info)
        self.assertEqual(8080, instance.port)

    def test_port_enabled(self):
        info = {"port": {"@enabled": "true"}}
        instance = Instance(info)
        self.assertTrue(instance.port_enabled)

    def test_port_not_enabled(self):
        info = {"port": {"@enabled": "false"}}
        instance = Instance(info)
        self.assertFalse(instance.port_enabled)

    def test_secure_port(self):
        info = {"securePort": {"$": 8080}}
        instance = Instance(info)
        self.assertEqual(8080, instance.secure_port)

    def test_secure_port_enabled(self):
        info = {"securePort": {"@enabled": "true"}}
        instance = Instance(info)
        self.assertTrue(instance.secure_port_enabled)

    def test_secure_port_not_enabled(self):
        info = {"securePort": {"@enabled": "false"}}
        instance = Instance(info)
        self.assertFalse(instance.secure_port_enabled)

    def test_vip_address(self):
        info = {"vipAddress": "example"}
        instance = Instance(info)
        self.assertEqual("example", instance.vip_address)

    def test_secure_vip_address(self):
        info = {"secureVipAddress": "example"}
        instance = Instance(info)
        self.assertEqual("example", instance.secure_vip_address)

    def test_ip_address(self):
        info = {"ipAddr": "127.0.0.1"}
        instance = Instance(info)
        self.assertEqual("127.0.0.1", instance.ip_address)

    def test_hostname(self):
        info = {"hostName": "example"}
        instance = Instance(info)
        self.assertEqual("example", instance.hostname)


if __name__ == '__main__':
    unittest.main()
