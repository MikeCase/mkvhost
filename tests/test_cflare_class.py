import pytest
from mkvhost.cflare import *
from main import test_payload, email, token, zone_name, zone_id
import os
import dotenv

dotenv.load_dotenv()

# email = os.getenv('email')
# token = os.getenv('token')
# server_ip = os.getenv('server_ip')
# host_name = os.getenv('host_name')
# test_payload = json.dumps(os.getenv('test_payload'))
test_record = os.getenv('test_record')
z_id = zone_id
tcf = CFlare(zone_name, email, token)

def test_connection_to_api_endpoint():
    assert tcf.get_zone_id() == z_id

def test_show_zones():
    zones = tcf.show_zones()
    assert zones == list([z_id])

def test_get_zone_id():
    zone_id = tcf.get_zone_id()
    assert zone_id == z_id

def test_get_record_by_name():
    record_id = tcf.get_record_by_name(z_id, test_record)
    # breakpoint()
    assert record_id['success'] == True

def test_add_record_to_dns():
    payload = json.dumps(test_payload)
    result = tcf.add_record(payload, z_id)
    assert result['success'] == True


def test_del_record_from_dns():
    result = tcf.del_record(z_id, test_record)
    # breakpoint()
    assert result['success'] == True
