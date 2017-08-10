# 3. Testing

As you develop more complex process and use more structured datasets, using
simply a web browser to test becomes impractical. In this chapter you get
acquainted with alternative tools to interact with a PyWPS instance.

### 3.1. `wget` 

This is a popular command line tool to send GET type request through the HTTP
protocol. It is useful to store PyWPS responses in files and parse them. `wget`
comes installed by default in many Linux distributions.

#### 3.1.1. *GetCapabilities*

Start by trying the *GetCapabilities* request:

```
wget -q -O - "http://127.0.0.1:5000/wps?SERVICE=WPS&REQUEST=GetCapabilities"  
```

Important question: Why -q, -O -  and " in the comnand  

***-q*** &nbsp;&nbsp;&nbsp;&nbsp; quit output no verbose information about requests

***-O -*** &nbsp; Output to file, but since the file is - the content will be dumped into the prompt   

***"*** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Otherwise wget would not consider ***&*** as part of the URL and would cut it

#### 3.1.2. *Execute*

Use the same requests in the [Process](02-Process.md) and invoke your new
process again in asynchronous mode. Store both the response document and the
result in new files.

### 3.2. XML Requests using Poster

As requests and data become more structure and lengthy, concatenating all
parameters into a URL for a GET type request becomes difficult or impossible.
For this reason the WPS standard allows the definition of [requests as XML
documents](http://geoprocessing.info/wpsdoc/1x0ExecutePOST) sent to the server
using the POST method of the HTTP protocol.

It is also possible to use wget (or curl) for POST requests but then the command line because to extensive. 

Poster is an add-on for various popular web browsers that allows the creation
and execution of HTTP POST requests. 

#### 3.2.1. Install Poster in your browser: 

 - [Chromium](https://chrome.google.com/webstore/detail/chrome-poster/cdjfedloinmbppobahmonnjigpmlajcd)
 - [Firefox](https://addons.mozilla.org/en-US/firefox/addon/poster/)

#### 3.2.2. XML-encoded requests

Create and send XML requests for the same *GetCapabilities* and *Execute*
requests used above.  

For more details on how to build WPS requests as XML documents check the [IEEE
Earth
Wiki](http://wiki.ieee-earth.org/Documents/GEOSS_Tutorials/GEOSS_Provider_Tutorials/Web_Processing_Service_Tutorial_for_GEOSS_Providers/Section_2%3a_Introduction_to_WPS).

Something wrong (see next point) ??? Proper solution in file `getcapabilities.xml`     


#### 4. Exceptions

ExceptionReport is an important feature of WPS. In WPS1.0.0 we have the following exceptions:

- **MissingParameterValue**: The request does not include a parameter value or a default cannot be found

- **InvalidParameterValue**: The request contains an invalid parameter value

- **NoApplicableCode**: Generic exception, no other code could be applied

- **NotEnoughStorage**: The server does not have enough space available

In point 3.2.2 the exception was:

```xml
<ows:ExceptionText>Unknown request '{http://www.opengis.net/ows/1.1}GetCapabilities'</ows:ExceptionText>
```

Something was wrong in `ows:GetCapabilities`, the namespace is incorrect it should be `wps:GetCapabilities` 

In case of python error in the called process, pywps will dump the python stack into the ExceptionReport