# Processes

Go through the [PyWPS documentation on
Processes](http://pywps.readthedocs.io/en/latest/process.html). The important
concepts to retain are:
 1. The parent `Process` class.
 2. Four input/ouput classes: `ComplexInput`, `LiteralInput`, `ComplexOutput` and `LiteralOutput`
 3. The `_handler(request, response)` method
 4. The `request.inputs` and the `response.output` properties.
 
### 1. Create your first process

Create a new process that takes as input a vector map. The process should go
through each line segment in this map and return as result the total length of
all lines. The [Shapely](https://pypi.python.org/pypi/Shapely) library will be
handy for this task; take also a peek at the example [Area
process](https://github.com/geopython/pywps-flask/blob/master/processes/area.py)
for inspiration.

This workshop includes a sample dataset that you may use to test your process.
You may reference it in your request as:

`https://raw.githubusercontent.com/PyWPS/pywps-workshop/master/data/railroads.gml`

### 2. Data types and input validation

Read carefully the notes on [input
validation](http://pywps.readthedocs.io/en/latest/process.html#complexdata-format-and-input-validation).
Which data type(s) did you select for your process input? If needed, modified it
so that it taken only data types for which there is already an inbuilt
validator.


### 3. Running the process in asynchronous mode

Invoke your new process in [asynchronous
mode](http://pywps.readthedocs.io/en/latest/process.html#progress-and-status-report)
using a request like:
```
http://localhost:5000/wps?&
REQUEST=Execute&
IDENTIFIER=total_length&
SERVICE=WPS&
VERSION=1.0.0&
DATAINPUTS=lines=https%3A%2F%2Fraw.githubusercontent.com%2FPyWPS%2Fpywps-workshop%2Fmaster%2Fdata%2Frailroads.gml&
storeExecuteResponse=true&
status=true 
```

Can you identify the status URL in the response document? Use it to track down
execution status and get the results.
 
