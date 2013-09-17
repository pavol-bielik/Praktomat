# Settings for development in the source tree

from os.path import join, dirname

# The name that will be displayed on top of the page and in emails.
SITE_NAME = 'Praktomat'

# Identifie this Praktomat among multiple installation on one webserver
PRAKTOMAT_ID = 'default' 

# The URL where this site is reachable. 'http://localhost:8000/' in case of the
# developmentserver.
BASE_HOST = 'http://localhost:8000'
BASE_PATH = '/'

# Absolute path to the directory that shall hold all uploaded files as well as
# files created at runtime.
# Example: "/home/media/media.lawrence.com/"
UPLOAD_ROOT = join(dirname(dirname(dirname(__file__))),'data')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = UPLOAD_ROOT+'/Database'   # Or path to database file if using sqlite3.

# This failed here (ulimit -f in checker/scripts/execute showed 0) (FIXME)
TEST_MAXFILESIZE = None

PRIVATE_KEY = join(dirname(dirname(dirname(__file__))), 'examples', 'certificates', 'privkey.pem')


# Finally load defaults for missing setttings.
import defaults
defaults.load_defaults(globals())

