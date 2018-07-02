# 5. Deployment

For deployment in production it is necessary to have a server like Apache2.4 or
Nginx as front end HTTP server / reverse proxy / load balancer. The explanation
can be found in the Flask project deployment
[documents](http://flask.pocoo.org/docs/0.12/deploying/)

**From the docs:**
> While lightweight and easy to use, **Flask’s built-in server is not suitable
> for production** as it doesn't scale well and by default serves only one
> request at a time.

WSGI (Web Server Gateway Interface) is an universal specification connecting web
services to web app, meaning connecting the HTTP server to the python app, the
WSGI is responsible for loading the app, loading Python interpreter and creating
threads/workers etc.

**Tip**: To avoid problems in OSGeo-Live with the nginx install, it is better to stop Apache 2 and release port 80

```
sudo service apache2 stop 
```

### 1. Nginx+Gunicorn

First step, look into folder `wsgi/` and  open: `pywps.wsgi` (or in [github](https://github.com/geopython/pywps-flask/blob/master/wsgi/)) 

This is a Python file that creates as PyWPS service (based on the listed processes and `pywps.cfg`) and returns an application
object, this application object in the is based on the WSGI standard.

[Nginx HTTP server](https://www.nginx.com/resources/wiki/) doesn't have a native WSGI support, it is necessary to setup uWSGI or
Gunicorn as WSGI server between Nginx and PyWPS (yet another component)

```
apt install gunicorn
```

(or gunicorn3 for python3)


Gunicorn is peculiar in the fact that it load the application interface as a
python module, therefore it is necessary to copy or link the pywps.wsgi to
python file.
 
``` 
cd /home/user/pywps-flask/wsgi 
touch __init__.py
ln -s ./pywps.wsgi ./pywps_app.py 
``` 

Question why do we create a __init__.py file with no content??


And then the generic gunicorn command:

```
gunicorn3 -b <LOCALHOST_IP>:<PORT>  --workers $((2*`nproc --all`)) --log-syslog
--pythonpath <PATH TO WSGI FOOLDER> wsgi.pywps_app:application
```

In our case

```
gunicorn3 -b 127.0.0.1:8081  --workers $((2*`nproc --all`)) --log-syslog
--pythonpath /home/user/pywps-flask/wsgi wsgi.pywps_app:application
```

Then we have the following problem: How to set up the server so it restarts
green unicorn on reboot. It is possible to use the following options

- [Runit](http://docs.gunicorn.org/en/stable/deploy.html#runit)
- [Supervisor](http://docs.gunicorn.org/en/stable/deploy.html#supervisor)
- [Upstart](http://docs.gunicorn.org/en/stable/deploy.html#upstart) 

Currently ubuntu 16.04 is using `systemcltd` and we suggest using it

When Gunicorn is running and accessible by IP or socket we need to implement
Nginx as a reverse proxy.  This is done on the site configuration file
`/etc/nginx/sites-enabled` 


apt install nginx

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

For more extensive information look at: [Deployment-Nginx-Gunicorn](http://pywps.readthedocs.io/en/latest/deployment.html#deployment-on-nginx-gunicorn) 

### 2. Apache 2.4

Apache2.4 has native WSGI support by using the libapache2-mod-wsgi module that
can be enable using the a2enmod command and with the following configuration. These modules are already installed in OSGeo-Live, if needed

```
sudo apt install libapache2-mod-wsgi && a2enmod wsgi

```
<br/>

```
WSGIDaemonProcess pywps home=/home/user/pywps-flask user=www-data group=www-data processes=2 threads=5
WSGIScriptAlias /wps /home/user/pywps-flask/wsgi/pywps.wsgi process-group=pywps

<Directory /home/user/pywps-flask/>
    WSGIScriptReloading On
    WSGIProcessGroup pywps
    WSGIApplicationGroup %{GLOBAL}
    Require all granted
</Directory>
```

On the first run it is likely that Apache will report an internal error.  The code on folder `pywps-flask` needs to have read/write permission to user www-data (Apache)

Apache has the advantage of not requiring extra servers like green unicorn
