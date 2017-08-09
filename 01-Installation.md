# 1. Installation

### 1.1. Requirements
 
Start by checking if your system meets the [required
dependencies](http://pywps.readthedocs.io/en/latest/install.html#dependencies-and-requirements). 

Most of the depencies are python packages, the most problematic packages are GDAL and lxml since they require compilation of C/C++ code and specific bindings (normally is enough to install them using linux package managers). The GDAL package is not required by pywps but a high number of processes require it 

```
apt install python-gdal
apt install python-lxml
``` 

The file `requirements.txt` is  used in python as a list of packages and source codes neceessary to run a system. If you are a developer it is advisable to install the `requirements-dev.txt` packages, those packages (e.g flake8) are convernient for code check and validation.

### 1.2. Install main library
 
Install PyWPS on your system [using
PIP](http://pywps.readthedocs.io/en/latest/install.html#download-and-install).

Or git clone and `setup.py`

```
git clone -b master https://github.com/geopython/pywps.git
cd pywps.git
python setup.py install
```


This will install pywps as a python library. Now in a python console should be possible to call the pywps module:
```
python -c "import pywps"
```

This bash command will load the pywps library and close the console. If the install was properly done no error messages will appear

### 1.3. Clone flask application
 
 
Now [clone the pywps-flask
service](http://pywps.readthedocs.io/en/latest/install.html#the-example-service-and-its-sample-processes).
Install the service requirements by entering the folder and using `pip`:

`git clone https://github.com/geopython/pywps-flask.git` 

`cd pywps-flask.git`

`sudo pip install -r requirements.txt`

Start the service by issuing the following command:  

`python demo.py`

Note, to use python3 it is necessary to use `pip3` instead of `pip`  and from the console run:

`python3 demo.py`

PyWPS-4.0 is build on top of [werkzeug](http://werkzeug.pocoo.org/) this library deals with HTTP requests and extra functionality. Normally we integrate PyWPS-4.0 into Flask webframe work for convenience.

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
