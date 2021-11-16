
import os
import jinja2
import uvicorn

import templates
import restapi


def create_profile(file_name: str, profile_data: dict):
    """
    Used to create a xml passpoint file

    :param file_name: Name of the file with .xml at the end
    :param profile_data: Profile data following schema profile
    :return: None
    """
    if file_name[-4:] != '.xml':
        file_name = file_name + '.xml'
    jinja_template = jinja2.Template(templates.profile_template.PROFILE_TEMPLATE)
    profile_xml = jinja_template.render(profile=profile_data)

    with open('profiles/' + file_name, 'w') as xml_file:
        xml_file.write(profile_xml)

    return None


def start_uvicorn():
    """ Starts up uvicorn with the FastAPI file listening on all interfaces over port 80  """
    profiles_folder = os.listdir('profiles')
    certificates_folder = os.listdir('certificates')
    for index, file in enumerate(profiles_folder):
        if file[-4:] == '.xml':
            break
        if index + 1 == len(profiles_folder):
            print('Missing profile files in folder profile.\n'
                  'Please upload a .xml profile into that folder or "Generate profile a file"')
            return None
    for index, file in enumerate(certificates_folder):
        if file[-4:] == '.cer':
            break
        if index + 1 == len(certificates_folder):
            print('Could not find a .cer file in the certificates folder.\n'
                  'Please upload a .cer file into that folder"')
            return None
    print('Starting up web server on port 8000.\n'
          'Please be aware that it is unsafe to send files over the internet as they are unencrypted\n'
          'Using web browser navigate to http://hostip:8000/passpoint.config')
    uvicorn.run(restapi.app, host='0.0.0.0')


def profile_generator():
    """
    Walks user through creating a passpoint profile for Android

    :return:
    """
    profile_data = {'HomeSP': {}, 'Credential': {}}
    profile_data['HomeSP'].update(
        {'FriendlyName': input('What is the friendly name of the network?')})
    profile_data['HomeSP'].update(
        {'FQDN': input('What is the domain for the network?')})
    choice = input('Does the network have a roaming consortium ID? (y/n)')
    while choice not in ['y', 'n', 'yes', 'no', 'Yes', 'No', 'true', 'false', 'True', 'False']:
        choice = input('Response: {choice} was not valid input.\n'
                       'Does the network have a roaming consortium ID? (y/n)'.format(choice=choice))
    if choice in ['y', 'yes', 'Yes', 'true', 'True']:
        choice = True
    else:
        choice = False
    if choice:
        profile_data['HomeSP'].update(
            {'RoamingConsortiumOI': input('What is the roaming consortium ID the network?')})
    profile_data['Credential'].update(
        {'Realm': input('What is the domain that the credential belongs to')})

    eap_types = 'EAP-TTLS (21), EAP-TLS (13), EAP-SIM (18), EAP-AKA (23), EAP-AKA (50)'

    choice = input('What type of credentials does this network use? (Username/Password, EAP-TLS, SIM)')
    while choice not in ['Username/Password', 'username/password', 'user/pass', 'username', 'user', 'u',
                         'EAP-TLS', 'eap-tls', 'e', 'SIM', 'sim', 's']:
        choice = input('Response: {choice} was not valid input.\n'
                       'What type of credentials does this network use?'
                       '(Username/Password, EAP-TLS, SIM)'.format(choice=choice))
    if choice in ['Username/Password', 'username/password', 'user/pass', 'username', 'user', 'u']:
        profile_data['Credential'].update({'UsernamePassword': {}})
        profile_data['Credential']['UsernamePassword'].update(
            {'Username': input('What is the username?')})
        profile_data['Credential']['UsernamePassword'].update(
            {'Password': input('What is the password?')})
        profile_data['Credential']['UsernamePassword'].update({'EAPMethod': {}})
        profile_data['Credential']['UsernamePassword']['EAPMethod'].update(
            {'EAPType': str(input('What is the EAP type for the credential?\n' + eap_types))})
        profile_data['Credential']['UsernamePassword']['EAPMethod'].update(
            {'InnerMethod': input('What is the inner method for the credential?'
                                  '(PAP, CHAP, MS-CHAP, or MS-CHAP-V2)')})
    elif choice in ['EAP-TLS', 'eap-tls', 'e']:
        profile_data['Credential'].update({'DigitalCertificate': {}})
        profile_data['Credential']['DigitalCertificate'].update(
            {'CertificateType': input('Certificate type (x509v3)') or 'x509v3'})
        profile_data['Credential']['DigitalCertificate'].update(
            {'CertSHA256Fingerprint': input('What is the fingerprint of the certificate?')})
    elif choice in ['SIM', 'sim', 's']:
        profile_data['Credential'].update({'SIM': {}})
        profile_data['Credential']['SIM'].update(
            {'IMSI': input('What is the international mobile subscriber identity?')})
        profile_data['Credential']['SIM'].update(
            {'Username': str(input('What is the EAP type for the credential?\n' + eap_types))})

    return profile_data


def main():
    choice = None
    print('Welcome to the Android Passpoint profile generator.\n'
          'Please enter the number before the option to continue with that option\n')
    while choice not in [4, '4', 'exit', 'quit', 'close', 'q']:
        choice = input('1. Instructions\n'
                       '2. Generate profile a file\n'
                       '3. Start web server\n'
                       '4. Exit\n')
        if choice in [1, "1", "Instructions", "instructions", "help", "Help"]:
            print('ToDo')
        elif choice in [2, "2"]:
            profile_generator()
        elif choice in [3, "3"]:
            start_uvicorn()
        elif choice in [4, '4', 'exit', 'quit', 'close', 'q']:
            print('Quiting...')
            break
        else:
            print('Invalid Option: {} Please choose an option below...'.format(choice))


if __name__ == '__main__':
    profile_generator()
