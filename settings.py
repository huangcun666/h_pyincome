import logging
import tornado
import tornado.template
import os
from tornado.options import define, options

import environment
import logconfig

# Make filepaths relative to settings.
path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=9000, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
# define("mysql_host", default="127.0.0.18:3306", help="blog database host")
#define("mysql_host", default="120.77.170.45:3306", help="blog database host")
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_host_building", default="building.gzfaye.com:3306", help="blog database host")

define("mysql_database", default="db_income2", help="database name")
define("mysql_database_customer", default="db_customer", help="database name")
define("mysql_database_building", default="db_building", help="database name")
define("mysql_database_company", default="db_company", help="database name")


define("mysql_user", default="root", help="database user")
define("mysql_password", default="deng", help="database password")
# define("mysql_password", default="123", help="database password")
define("login_url", default="/login", help="database password")
define("upload_path", default=ROOT+"/media", help="upload path")

tornado.options.parse_command_line()

MEDIA_ROOT = path(ROOT, 'media')
TEMPLATE_ROOT = path(ROOT, 'templates')

# Deployment Configuration

class DeploymentType:
    PRODUCTION = "PRODUCTION"
    DEV = "DEV"
    SOLO = "SOLO"
    STAGING = "STAGING"
    dict = {
        SOLO: 1,
        PRODUCTION: 2,
        DEV: 3,
        STAGING: 4
    }

if 'DEPLOYMENT_TYPE' in os.environ:
    DEPLOYMENT = os.environ['DEPLOYMENT_TYPE'].upper()
else:
    DEPLOYMENT = DeploymentType.SOLO

settings = {}
settings['debug'] = DEPLOYMENT != DeploymentType.PRODUCTION or options.debug
settings['static_path'] = MEDIA_ROOT
settings['cookie_secret'] = "your-cookie-secrsadasdsadsadsadsaet"
settings['xsrf_cookies'] = True
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
settings['login_url'] ="/login"
SYSLOG_TAG = "boilerplate"
SYSLOG_FACILITY = logging.handlers.SysLogHandler.LOG_LOCAL2

# See PEP 391 and logconfig for formatting help.  Each section of LOGGERS
# will get merged into the corresponding section of log_settings.py.
# Handlers and log levels are set up automatically based on LOG_LEVEL and DEBUG
# unless you set them here.  Messages will not propagate through a logger
# unless propagate: True is set.
LOGGERS = {
   'loggers': {
        'boilerplate': {},
    },
}

if settings['debug']:
    LOG_LEVEL = logging.DEBUG
else:
    LOG_LEVEL = logging.INFO
USE_SYSLOG = DEPLOYMENT != DeploymentType.SOLO

logconfig.initialize_logging(SYSLOG_TAG, SYSLOG_FACILITY, LOGGERS,
        LOG_LEVEL, USE_SYSLOG)

if options.config:
    tornado.options.parse_config_file(options.config)
