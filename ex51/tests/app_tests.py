from nose.tools import *
from app import app
from tests.tools import assert_response

client = app.test_client() #create a testing client (like a fake web browser)
client.testing = True # enable this so that errors in your web app bubble up to the testing client

def test_index():
    global client # let python know you want to use the global client variable in this function
    # Check that we get a 404 on the / URL
    resp = client.get('/')
    assert_response(resp, status=404)

    #test to make sure a GET request to /hello works (returns a 200 status code)
    resp = client.get('/hello')
    assert_response(resp)

    #make sure the default values work when POST has no data
    resp = client.post('/hello')
    assert_response(resp)

    #make sure the default values work when POST has no data
    resp = client.post('/hello')
    assert_response(resp, contains = "Nobody") # the request should contain "Hello, Nobody!"

    #test that we get an expected response for specific input data
    testdata = {'name': 'Jon', 'greet': 'Hola'}
    resp = client.post('/hello', data=testdata)
    assert_response(resp, contains="Jon") # the request should contain "Hola, Jon!"
