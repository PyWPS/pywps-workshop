# 5. GRASS GIS

Let's rewrite the process, so that [GRASS GIS](http://grass.osgeo.org) modules
are used. 

PyWPS will manage GRASS Location and Mapset structure for you, all you need is
to configure it, see
[documentation](http://pywps.readthedocs.io/en/latest/external-tools.html#grass-gis).

First, we modify the process class, by adding `grass_location` attribute. 

Then we can import Python GRASS interface and start coding. Use the [v.report](https://grass.osgeo.org/grass73/manuals/v.report.html) module to get length information.

Do not forget to set propper [configuration](http://pywps.readthedocs.io/en/latest/configuration.html#grass).

## Note

You can have a look at the `grassbuffer.py` process, for your inspiration.
