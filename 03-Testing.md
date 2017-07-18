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
wget http://127.0.0.1:5000/wps?SERVICE=WPS&REQUEST=GetCapabilities
```

Using the same command parse the result and print out the line where your name
appears (as inserted in the [Installation](01-Installation.md) section.

#### 3.1.2. *Execute*

Use the same requests in the [Process](02-Process.md) and invoke your new
process again in asynchronous mode. Store both the response document and the
result in new files.

### 3.2. Poster

As requests and data become more structure and lengthy, concatenating all
parameters into a URL for a GET type request becomes difficult or impossible.
For this reason the WPS standard allows the definition of [requests as XML
documents](http://geoprocessing.info/wpsdoc/1x0ExecutePOST) sent to the server
using the POST method of the HTTP protocol.

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


