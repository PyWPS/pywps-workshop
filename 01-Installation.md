# 1. Installation

### 1.1. Requirements
 
Start by checking if your system meets the [required
dependencies](http://pywps.readthedocs.io/en/latest/install.html#dependencies-and-requirements).

### 1.2. Install main library
 
Install PyWPS on your system [using
PIP](http://pywps.readthedocs.io/en/latest/install.html#download-and-install).

### 1.3. Clone flask application
 
Now [clone the pywps-flask
service](http://pywps.readthedocs.io/en/latest/install.html#the-example-service-and-its-sample-processes).
Install the service requirements by entering the folder and using `pip`:

`cd pywps-flask.git`

`sudo pip install -r requirements.txt`

Start the service by issuing the following command:  

`python demo.py`

### 1.4. Service check
 
If everything went well, the service should be running on port 5000, the
default. Try it by directing your internet browser to this address:
[http://127.0.0.1:5000](http://127.0.0.1:5000).

### 1.5. Test PyWPS 
 
Test the WPS service itself using a *GetCapabilities* request; insert this
address in your browser:
[http://127.0.0.1:5000/wps?SERVICE=WPS&REQUEST=GetCapabilities](http://127.0.0.1:5000/wps?SERVICE=WPS&REQUEST=GetCapabilities)

### 1.6. Configuration

Take some time to go through the [PyWPS configuration file
documentation](http://pywps.readthedocs.io/en/latest/configuration.html). 

Change the right fields in the configuration file so that your name and contacts
show as the service contact person. Test it again using the *GetCapabilities*
request.
