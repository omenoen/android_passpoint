
import os
import base64
import fastapi

import main
import templates
import schema.profile

app = fastapi.FastAPI()
BOUNDARY = 'l1ZMD64Ujevti9JwYOrJoLo4YmoJLJZU'  # Should be a unique string not found in any documents


@app.get('/passpoint.config')  # builds android passpoint profile
def build_wifi_profile(profile: str, certificate: str):
    """ Builds an Android Passpoint profile """
    with open('profiles/' + profile, 'r') as xml_file:
        profile_data = xml_file.read()
    profile_b64 = base64.b64encode(profile_data.encode('ascii'))
    with open('certificates/' + certificate, 'rb') as cert_file:
        certificate_data = cert_file.read()
    cert_b64 = base64.b64encode(certificate_data)

    headers = {'Content-Type': "application/x-wifi-config",
               'Content-Transfer-Encoding': 'base64'}
    payload = templates.multipart_mixed_template.BASIC_DOCUMENT_BODY.format(boundary=BOUNDARY,
                                                                            profile=profile_b64.decode('ascii'),
                                                                            certificate=cert_b64.decode('ascii'))
    return fastapi.Response(content=base64.b64encode(payload.encode('ascii')).decode('ascii'), headers=headers)


@app.post('/profiles/{file_name}')
def build_profile(file_name: str, profile: schema.profile.Profile):
    """ Add a profiles  """
    try:
        main.create_profile(file_name, profile)
        return True
    except fastapi.exceptions.FastAPIError as error:
        return error


@app.get('profiles', response_model=list)
def list_profiles():
    """ List available profiles """
    return os.listdir('profiles')
