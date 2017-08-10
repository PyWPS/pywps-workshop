# 5. Deployment

Deployment is production is best done using Apache2.4 or Nginx as front end HTTP
server / reverse proxy / load balancer.  Explain why. Refer to Flask
documentation.

**From the docs:**
> While lightweight and easy to use, **Flask’s built-in server is not suitable
> for production** as it doesn't scale well and by default serves only one
> request at a time.

WSGI (Web Server Gateway Interface) is an universal specification connecting web
services to web app, meaning connecting the HTTP server to the python app, the
WSGI is reponsible for loading the app, loading Python interpreter and creating
threads/workers etc.


### 1. Nginx+Gunicorn

First step, open: `https://github.com/geopython/pywps-flask/blob/master/wsgi/pywps.wsgi` 

This is a python file that creates as PyWPS service and returns an application
object, this is the  standard way to integrate with a WSGI server

Nginx doesnt have a native WSGI support, it is necessary to setup uWSGI or
Gunicorn as WSGI server between Nginx and PyWPS

[Deployment-Nginx-Gunicorn](http://pywps.readthedocs.io/en/latest/deployment.html#deployment-on-nginx-gunicorn) 

Gunicorn is pecular in the fact that it load the application interface as a
python module, therefore it is necessary to copy or link the pywps.wsgi to
python file.
 
``` cd /pywps-flask/wsgi ln -s ./pywps.wsgi ./pywps_app.py ``` 

And then putting the green unicorn server up
```
gunicorn3 -b 127.0.0.1:8081  --workers $((2*`nproc --all`)) --log-syslog
--pythonpath /pywps-flask wsgi.pywps_app:application
```

Then we have the following problem: How to set up the server so it restarts
green unicorn on reboot. It is possible to use the following options

- [Runit](http://docs.gunicorn.org/en/stable/deploy.html#runit)
- [Supervisor](http://docs.gunicorn.org/en/stable/deploy.html#supervisor)
- [Upstart](http://docs.gunicorn.org/en/stable/deploy.html#upstart) 

Currentely ubuntu 16.04 is using `systemcltd` and we suggest using it

When gunicorn is running and acessible by IP or socket we need to implement
Nginx as a reverse proxy.  This is done on the site configuration file
`/etc/nginx/sites-enabled` 

The configuration file will set up a location (normally /wps or another URI) and forward request to gunicorn. 

 
```
  location /wps {
             # with try_files active there will be problems
             #try_files $uri $uri/ =404;

             proxy_set_header Host $host;
             proxy_redirect          off;
             proxy_set_header        X-NginX-Proxy true;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_pass http://127.0.0.1:8081;
             }

```

Restarting nginx we should have a service like this:

```
http://localhost/wps?request=GetCapabilities&service=wps
```

### 2. Apache 2.4

Apache2.4 has native WSGI support by using the libapache2-mod-wsgi module that
can be enable using the a2enmod command and with the following configuration

```
WSGIDaemonProcess pywps home=/pywps-flask user=www-data group=www-data processes=2 threads=5
WSGIScriptAlias /wps /pywps-flask/wsgi/pywps.wsgi process-group=pywps

<Directory /pywps-flask/>
    WSGIScriptReloading On
    WSGIProcessGroup pywps
    WSGIApplicationGroup %{GLOBAL}
    Require all granted
</Directory>
```

Apache has the advantage of not requiring extra servers like green unicorn
