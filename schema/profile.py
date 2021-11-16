
import typing
import pydantic


class SIMCred(pydantic.BaseModel):
    IMSI: str
    EAPType: str


class DigitalCertificateCred(pydantic.BaseModel):
    """ Defines EAP-TLS credential that is used for the network """
    CertificateType: str
    CertSHA256Fingerprint: str


class UsernamePasswordEAP(pydantic.BaseModel):
    """ Defines the EAP method that will be used for username and password """
    EAPType: str
    InnerMethod: str


class UsernamePasswordCred(pydantic.BaseModel):
    """ Username and password (EAP-TTLS) credential """
    Username: str
    Password: str
    EAPMethod: UsernamePasswordEAP


class CredentialData(pydantic.BaseModel):
    """ Defines the credentials that will be used for the profile """
    Realm: str
    UsernamePassword: typing.Optional[UsernamePasswordCred]
    DigitalCertificate: typing.Optional[DigitalCertificateCred]
    SIM: typing.Optional[SIMCred]


class HomeServiceProviderData(pydantic.BaseModel):
    """ Home service provider data """
    FriendlyName: str
    FQDN: str
    RoamingConsortiumOI: typing.Optional[str]


class Profile(pydantic.BaseModel):
    """ Base for the connection profile """
    HomeSP: HomeServiceProviderData
    Credential: CredentialData

