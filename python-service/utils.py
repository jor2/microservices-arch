import os
import requests


# noinspection PyBroadException
def invoke_service(service, page_name="", id="", headers=None):
    if headers is None:
        headers = {}
    url = create_url_for_service(service, page_name, id)
    try:
        res = requests.get(url, headers=headers)
    except Exception:
        return "Error with {url}.".format(url=url)
    try:
        response = res.json()
    except ValueError:
        try:
            return res
        except Exception:
            return "Response from {url} won't parse to json or return the response(if already json)".format(url=url)
    return response


def create_url_for_service(service, page_name="", id=""):
    print("Creating url for service {}".format(service))
    config = {
        "python-service": {
            "host": os.getenv("PYTHON-SERVICE-SERVICE-HOST", '{service}'.format(service=service)),
            "port": os.getenv("PYTHON-SERVICE-SERVICE-PORT", '5000'),
        },
        "go-service": {
            "host": os.getenv("GO-SERVICE-SERVICE-HOST", '{service}'.format(service=service)),
            "port": os.getenv("GO-SERVICE-SERVICE-PORT", '6000'),
        },
        "javascript-service": {
            "host": os.getenv("JAVASCRIPT-SERVICE-SERVICE-HOST", '{service}'.format(service=service)),
            "port": os.getenv("JAVASCRIPT-SERVICE-SERVICE-PORT", '4000'),
        },
    }

    be_host = config[service]["host"]
    be_port = config[service]["port"]
    url = 'http://{host}:{port}/{page_name}/{id}'.format(host=be_host, port=be_port, page_name=page_name, id=id)
    print("The following url was created: {}".format(url))
    return url