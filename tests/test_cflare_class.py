import unittest
from mkvhost.cflare import *

class TestCFlare(unittest.TestCase):
   
    # zone_name = 'mikecase.us'
    def setUp(self):
        self.cf = CFlare('mikecase.us')
        self.zone_id = 'c4f876ffa36284d86ce9145148994eee'
        self.record_id = ''
        self.payload = json.dumps({
                "type": "A",
                "name": 'testing',
                "content": "45.79.42.59",
                "ttl": "1",
                "proxied": True,
            })

    def test_get_zones(self):
        self.assertEqual(self.cf.show_zones()['result']['name'], 'mikecase.us')

    def test_get_zone_id(self):
        self.assertEqual(self.cf.get_zone_id(), self.zone_id)

    def test_get_dns_records(self):
        self.assertIsNotNone(self.cf.get_records())
        records = self.cf.get_records()
        self.assertEqual(records['success'], True)

    def test_add_dns_record(self):
        test = self.cf.add_record(self.payload, self.zone_id)
        self.assertEqual(test['success'], True)

    def test_del_dns_record(self):
        record_name = self.cf.get_record_by_name(self.zone_id, 'testing.mikecase.us')['result'][0]['name']
        test = self.cf.del_record(self.zone_id, record_name)
        self.assertEqual(test['success'], True)

    