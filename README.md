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
 - Install Intellij Idea from  [here](https://www.jetbrains.com/idea/download/download-thanks.html?platform=windows&code=IIC), we will need it later.
 
 ## Install Apache Maven
We will use Maven to easly build Thingboard source code:
 - Get Maven from [here](https://maven.apache.org/download.cgi).
 -  Go to the directory where you have cloned  thingsboard repository and run the command below: 
 ```
>> mvn clean install -DskipTests
``` 
  
:point_up: If you are not familiar with Maven please refer to [this tutorial](http://objis.com/tutoriel-maven-n1-installation-et-phases/) before we continue. 

:exclamation: This command will take few minutes, please wait till it finish.

## Install PostgreSQL
With thingboard you have the possibility to use either with [Apache Cassandra DB ](https://cassandra.apache.org/) or [PostgreSQL](https://www.postgresql.org/), we will use postgresql db for this tutorial, so if you need to use other database just refer [ here](https://thingsboard.io/docs/).
Let's install and configure Postgresql:

 - Download the installation file [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows) and follow the installation instructions.
 ##### :exclamation: During PostgreSQL installation, you will be prompted for superuser (postgres) password. Don’t forget this password. It will be used later. For simplicity, we will substitute it with “postgres”.
 - Once installed, launch the “pgAdmin” software and login as superuser (postgres). Open your server and create database “thingsboard” with owner “postgres”.
 - Navigate to the thingsboard repo and: 
 ```
>> cd Thingsboard\thingsboard\application\target\windows
>> install_dev_db.bat
``` 

## Run Thingsboard
Open IntelliJ and import the thingsboard repo previously cloned, here you may need to download the packages proposed first and navigate tothis file and click on RUN:
```
application>src>main>java>ThingsboardServerApplication.java
``` 
Once running, navigate to http://YOUR_IP_ADDRESS:8080/ on your browser and use the creadentials below to login successfully:

 - System Administrator: sysadmin@thingsboard.org / sysadmin
 - Tenant Administrator: tenant@thingsboard.org / tenant
 - Customer User: customer@thingsboard.org / customer
## Publish data to thingsboard
 - Create a device on thingsboard [like this](https://thingsboard.io/docs/user-guide/ui/devices/).
 - Copy the device access token and pass it to the code.
 - Run this command:
 ```
>> python publish_thingsboard.py
``` 
Expected command output is: 
```
> Message was published
```
