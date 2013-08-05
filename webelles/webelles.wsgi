activate_this = '/var/www/html/webelles/virt/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from sys import path
path.insert(0, "/var/www/html/webelles/")

from webelles import APP as application
