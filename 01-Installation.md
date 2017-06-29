# Installation

 1. Start by checking if your system meets the [required dependencies](http://pywps.readthedocs.io/en/latest/install.html#dependencies-and-requirements).
 
 2. Install PyWPS on your system [using PIP](http://pywps.readthedocs.io/en/latest/install.html#download-and-install).
 
 3. Now [clone the pywps-flask service](http://pywps.readthedocs.io/en/latest/install.html#the-example-service-and-its-sample-processes). Start the service issue the following command within the `pywps-flask` folder:  `python demo.py`.
 
 4. If everything went well, the service should be running on port 5000, the default. Try it by directing your internet browser to this address: [http://127.0.0.1:5000](http://127.0.0.1:5000).
 
 5. Test the WPS service itself using a *GetCapabilities* request; insert this address in your browser: [http://127.0.0.1:5000/wps?SERVICE=WPS&REQUEST=GetCapabilities](http://127.0.0.1:5000/wps?SERVICE=WPS&REQUEST=GetCapabilities)

 6. Take some time to go through the [PyWPS configuration file documentation](http://pywps.readthedocs.io/en/latest/configuration.html). Change the right fields in the configuration file so that your name and contacts show as the service contact person. Test it again using the *GetCapabilities* request.