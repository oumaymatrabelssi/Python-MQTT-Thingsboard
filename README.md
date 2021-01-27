# Python-MQTT-Thingsboard

Hello there :wave: :wave:, In this repository I will implement the [Eclipse Paho](http://eclipse.org/paho/) MQTT Python client library to publish temperature and humidity data to a device that I create on  [Thingsboard](https://thingsboard.io/). The instructions below are used on Windows 10/64-bit.

:exclamation: Don't forget to install MQTT Python client library [paho-mqtt](https://pypi.org/project/paho-mqtt/).
 
Okey, Let's start   :muscle:!

## Install Java 8 (OpenJDK)

ThingsBoard service is running on Java 8. Follow this instructions to install OpenJDK 8.

-   Visit  [Open JDK Download Page](https://adoptopenjdk.net/index.html)  to download latest  **OpenJDK 8 (LTS)**  MSI package.
-   Run the downloaded MSI package and follow the instructions. Make sure you have selected “**Add to PATH**” and “**Set JAVA_HOME variable**” options to “Will be installed on local hard drive” state.

You can check the installation using the following command (using Command Prompt):

```
java -version

```
Expected command output is:

```
C:\Users\User>java -version
openjdk version "1.8.0_212"
OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_212-b04)
OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.212-b04, mixed mode)
```
## Thingsboard 

In this tutorial, we will set up Thingsboard Sources on IntelliJ Community Edition to do so we need to:

 - Clone the Thingsboard  [repository](https://github.com/thingsboard/thingsboard).
 - Install Intellij Idea from  [here](https://www.jetbrains.com/idea/download/download-thanks.html?platform=windows&code=IIC).
 - Open thingsboard repo and download the needed packages proposed by the intellij editor.
 
 ## Install Apache Maven
We will use Maven to easly build Thingboard source code:
 - Get Maven from [here](https://maven.apache.org/download.cgi).
 -  Go to the directory where you have cloned  thingsboard repository and run the command bellow: 
 ```
>> mvn clean install -DskipTests
``` 
  
:point_up: If you are not familiar with Maven please refer to [this tutorial](http://objis.com/tutoriel-maven-n1-installation-et-phases/) before we continue. 
