This is a basic web service status page, similar to StatusPage.io.

It is written in Django for Python 2.7 and 3.3.

Setup
=====
1. Clone the repository into a virutualenv (optional but recommended).
2. Install the required packages with pip for your environment: e.g. `pip install requirements/production.txt`
3. Install the supplied configs (assumes using uwsgi and nginx on an EC2 instance). Adjust as required.
4. Copy `status/settings/production.py.dist` to `status/settings/production.py` and fill it out.
5. Compile the stylesheet (using Stylus).

Use
===
Use `./manage.py sync` to setup the database and create an admin user.

Configure your components and incidents in `status.example.com/admin`.

You can embed charts to show on the dashboard page. If you use a site monitoring service such as New Relic, placed the chart HTML there.
