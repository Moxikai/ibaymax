import sae

sae.add_vendor_dir('site-packages')

from manage import app

application = sae.create_wsgi_app(app)