# Android Passpoint 802.11u Generator
This project was designed to help with building 802.11u Passpoint profiles for Android.
## Introduction
Building Passpoint profiles for Android can be difficult as it not as simple as creating an XML file and uploading a 
certificate to your device. <br />
A lot of other opperating systems have tools that make it easy to generate Hot Spot 2.0/Passpoint configurations.
So, I wanted to create a tool that can do that for Android. I wanted it to be easy to use, but keep the code simple so 
that it can be used by inexperience developer. <br />
I followed Google's documentation on how to build a [Passpoint (Hotspot 2.0)](https://source.android.com/devices/tech/connect/wifi-passpoint) 
profile, and used some details from this [parser](https://android.googlesource.com/platform/prebuilts/fullsdk/sources/android-29/+/refs/heads/androidx-sqlite-release/android/net/wifi/hotspot2/omadm/PpsMoParser.java). The document describes building the configurations for the network in XML and converting it to Base64. It also
talks about getting the certificate for the network authenication and having it be in Base64 for also (.cer file). Once
both pieces of data are in Base64 they will need to be put into a **multipart/mixed** MIME type. The multipart/mixed
than must be converted to Base64 also. To deliver the Passpoint profile to Android it must be sent from a website using 
**application/x-wifi-config** content type.
## Usage
### CLI Tool
CLI based tool to walk a user through generating and starting up a web server. Will still need to put .cer files into
the certificate folder. (optional). <br />
``` python main.py```<br />
### Just Web Server
Both the profile xml file and the RADIUS server .cer file will need to be supplied.<br />
Profiles<br />
```/profiles/<profile>.xml``` <br />
Certificates<br />
```/certificates/<certificate>.cer```<br />
Start web server<br />
``` python -m uvicorn --host 0.0.0.0 restapi:app```
## Uploading to Android
Using chrome navigate to `http://{serverIP}:8000/passpoint.config?profile={profile.xml}&certificate={certificate}` <br />
This should prompt you to install the profile. If there was any error the Android device will return a generic error.
## Additional tool
For examples on using the API navigate to `http://{serverIP}:8000/docs`