import os, sys
import site
 
MARGARITA_ENV_DIR = '/usr/local/updates'
 
# Use site to load the site-packages directory of our virtualenv
site.addsitedir(os.path.join(MARGARITA_ENV_DIR, 'lib/python2.7/site-packages'))

sys.path.append(MARGARITA_ENV_DIR)
sys.path.append(os.path.join(MARGARITA_ENV_DIR, 'margarita'))

from margarita import app as application