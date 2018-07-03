# 2. Processes

In PyWPS a process is a python class that has the following structure    


 1. The parent `Process` class.
 2. Four input/ouput classes: `ComplexInput`, `LiteralInput`,
    `BoundingBoxInput`, `ComplexOutput`
    and `LiteralOutput`, `BoundingBoxOutput`
 3. The `_handler(request, response)` method
 4. The `request.inputs` and the `response.output` properties.

Since ComplexIO and LiteralIO require considerable information and configuration
they are also classes

Go through the [PyWPS documentation on
Processes](http://pywps.readthedocs.io/en/latest/process.html).


### 2.1. Create your first process

*Let's create a new process that takes as input a vector map. The process should go
through each line segment in this map and return as result the total length of
all lines.*

The [OGR](https://pcjericks.github.io/py-gdalogr-cookbook/vector_layers.html#iterate-over-features)
library could be handy for this task; take also a peek at the example [Area
process](https://github.com/geopython/pywps-flask/blob/master/processes/area.py). 

But you can also use [Fiona](http://toblerity.org/fiona/) and
[Shapely](http://toblerity.org/shapely/manual.html) libraries.

You will need to:

1. Create new file with the process class, which should inherit from
   `pywps.Process`
2. You will have to define `inputs` and `outputs` list of `pywps.ComplexInput`,
   `pywps.ComplexOutput` and `pywps.LiteralInput` classes, you can check [the
   documentation](http://pywps.readthedocs.io/en/master/process.html#declaring-inputs-and-outputs)
3. Define the `handler(request, response)` function, which will do the job,
   [check the documentation](http://pywps.readthedocs.io/en/master/process.html#accessing-the-inputs-and-outputs-in-the-handler-method)
4. Import the new process to `demo.py` and register new process class


The pywps-flask service includes a sample dataset that you may use to test your 
process. You may reference it in your request as:

`https://raw.githubusercontent.com/geopython/pywps-flask/master/data/railroads.gml`

### 2.2. Data types and input validation

Read carefully the notes on [input
validation](http://pywps.readthedocs.io/en/latest/process.html#complexdata-format-and-input-validation).
Which data type(s) did you select for your process input? If needed, modified it
so that it takes only data types for which there is already an inbuilt
validator.


### 2.3. Running the process in asynchronous mode

Invoke your new process in [asynchronous
mode](http://pywps.readthedocs.io/en/latest/process.html#progress-and-status-report)
using a request like:
```
http://localhost:5000/wps?&
REQUEST=Execute&
IDENTIFIER=total_length&
SERVICE=WPS&
VERSION=1.0.0&
DATAINPUTS=layer=@xlink:href=https://raw.githubusercontent.com/geopython/pywps-flask/master/data/railroads.gml&
storeExecuteResponse=true&
status=true 
```

Can you identify the status URL in the response document? Use it to track down
execution status and get the results.

*NOTE:* We need to indicate, that the layer data input is a link to a content
(@xlink:href), The ***server running*** PyWPS will fetch the content of the
request and feed it to the processes. Passing inputs by reference is extremely
useful for inputs that are big and stored remotely
 
### 2.4 Final tip

If it is getting really hard to code the total line length process, there is an 
[example](https://github.com/PyWPS/pywps-workshop/tree-save/master/total_length.py) 
to draw inspiration from. 

The folder processes contains examples of other processes, the logic is very similar:

- Import PyWPS contents
- Set I/O and auxiliary classes (e.g Metadata)
- Create a handler (where your code runs)

