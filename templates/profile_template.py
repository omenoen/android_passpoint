
PROFILE_TEMPLATE = """<MgmtTree xmlns="syncml:dmddf1.2">
  <VerDTD>1.2</VerDTD>
  <Node>
    <NodeName>PerProviderSubscription</NodeName>
    <RTProperties>
      <Type>
        <DDFName>urn:wfa:mo:hotspot2dot0-perprovidersubscription:1.0</DDFName>
      </Type>
    </RTProperties>
    <Node>
      <NodeName>i001</NodeName>
      <Node>
        <NodeName>HomeSP</NodeName>
        <Node>
          <NodeName>FriendlyName</NodeName>
          <Value>{{ profile.HomeSP.FriendlyName }}</Value>
        </Node>
        <Node>
          <NodeName>FQDN</NodeName>
          <Value>{{ profile.HomeSP.FQDN }}</Value>
        </Node>
        {%- if profile.HomeSP.RoamingConsortiumOI is defined %}
        <Node>
          <NodeName>RoamingConsortiumOI</NodeName>
          <Value>{{ profile.HomeSP.RoamingConsortiumOI }}</Value>
        </Node>
        {%- endif %}
      </Node>
      <Node>
        <NodeName>Credential</NodeName>
        <Node>
          <NodeName>Realm</NodeName>
          <Value>{{ profile.Credential.Realm }}</Value>
        </Node>
        {%- if profile.Credential.UsernamePassword is defined %}
        <Node>
          <NodeName>UsernamePassword</NodeName>
          <Node>
            <NodeName>Username</NodeName>
            <Value>{{ profile.Credential.UsernamePassword.Username }}</Value>
          </Node>
          <Node>
            <NodeName>Password</NodeName>
            <Value>{{ profile.Credential.UsernamePassword.Password }}</Value>
          </Node>
          <Node>
            <NodeName>EAPMethod</NodeName>
            <Node>
              <NodeName>EAPType</NodeName>
              <Value>{{ profile.Credential.UsernamePassword.EAPMethod.EAPType }}</Value>
            </Node>
            <Node>
              <NodeName>InnerMethod</NodeName>
              <Value>{{ profile.Credential.UsernamePassword.EAPMethod.InnerMethod }}</Value>
            </Node>
          </Node>
        </Node>
        {%- endif %}
        {%- if profile.Credential.DigitalCertificate is defined %}
        <Node>
          <NodeName>DigitalCertificate</NodeName>
          <Node>
            <NodeName>CertificateType</NodeName>
            <Value>{{ profile.Credential.DigitalCertificate.CertificateType }}</Value>
          </Node>
          <Node>
            <NodeName>CertSHA256Fingerprint</NodeName>
            <Value>{{ profile.Credential.DigitalCertificate.CertificateType }}</Value>
          </Node>
        </Node>
        {%- endif %}
        {%- if profile.Credential.SIM is defined %}
        <Node>
          <NodeName>SIM</NodeName>
          <Node>
            <NodeName>IMSI</NodeName>
            <Value>{{ profile.Credential.SIM.IMSI }}</Value>
          </Node>
          <Node>
            <NodeName>EAPType</NodeName>
            <Value>{{ profile.Credential.SIM.EAPType }}</Value>
          </Node>
        </Node>
        {%- endif %}
      </Node>
    </Node>
  </Node>
</MgmtTree>
"""
