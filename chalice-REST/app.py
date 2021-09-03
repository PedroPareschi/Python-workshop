import gzip
import json

from chalice import Chalice, BadRequestError, NotFoundError, Response, CORSConfig
from urllib.parse import urlparse, parse_qs

app = Chalice(app_name='helloworld')
app.debug = True
app.api.binary_types.append('application/json')

CITIES_TO_STATE = {
    'seattle': 'WA',
    'portland': 'OR',
}


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/cities/{city}')
def state_of_city(city):
    try:
        return {'state': CITIES_TO_STATE[city]}
    except KeyError:
        raise BadRequestError("Unknown city '%s', valid choices are: %s" % (
            city, ', '.join(CITIES_TO_STATE.keys())))


@app.route('/resource/{value}', methods=['PUT'])
def put_test(value):
    return {"value": value}


@app.route('/myview', methods=['POST', 'PUT'])
def myview():
    pass


OBJECTS = {

}


@app.route('/objects/{key}', methods=['GET', 'PUT'])
def myobject(key):
    request = app.current_request
    if request.method == 'PUT':
        OBJECTS[key] = request.json_body
    elif request.method == 'GET':
        try:
            return {key: OBJECTS[key]}
        except KeyError:
            raise NotFoundError(key)


@app.route('/introspect')
def introspect():
    return app.current_request.to_dict()


@app.route('/', methods=['POST'], content_types=['application/x-www-form-urlencoded'])
def index():
    parsed = parse_qs(app.current_request.raw_body.decode())
    return {
        'states': parsed.get('states', [])
    }


@app.route('/text')
def index():
    return Response(body='hello world!',
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})


@app.route('/compressed')
def index():
    blob = json.dumps({'hello': 'world'}).encode('utf-8')
    payload = gzip.compress(blob)
    custom_headers = {
        'Content-Type': 'application/json',
        'Content-Enconding': 'gzip'
    }
    return Response(body=payload,
                    status_code=200,
                    headers=custom_headers)


@app.route('/supports-cors', methods=['PUT'], cors=True)
def supports_cors():
    return {}


cors_config = CORSConfig(
    allow_origin='https://foo.example.com',
    allow_headers=['X-Special-Header'],
    max_age=600,
    expose_headers=['X-Special-Header'],
    allow_credentials=True
)


@app.route('/custom-cors', methods=['GET'], cors=cors_config)
def supports_custom_cors():
    return {'cors': True}


_ALLOWED_ORIGINS = set([
    'http://allowed1.example.com',
    'http://allowed2.example.com',
])


@app.route('/cors_multiple_origins', methods=['GET', 'OPTIONS'])
def supports_cors_multiple_origins():
    method = app.current_request.method
    if method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Method': 'GET,OPTIONS',
            'Access-Control-Allow-Origin': ','.join(_ALLOWED_ORIGINS),
            'Access-Control-Allow-Headers': 'X-Some-Header',
        }
        origin = app.current_request.headers.get('origin', '')
        if origin in _ALLOWED_ORIGINS:
            headers.update({'Access-Control-Allow-Origin': origin})
        return Response(body=None, headers=headers)
    elif method == 'GET':
        return 'Foo'
