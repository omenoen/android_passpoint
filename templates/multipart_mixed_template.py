
BASIC_DOCUMENT_BODY = '''Content-Type: multipart/mixed; boundary={boundary}
Content-Transfer-Encoding: base64

--{boundary}
Content-Type: application/x-passpoint-profile
Content-Transfer-Encoding: base64

{profile}
--{boundary}
Content-Type: application/x-x509-ca-cert
Content-Transfer-Encoding: base64

{certificate}
--{boundary}--
'''
