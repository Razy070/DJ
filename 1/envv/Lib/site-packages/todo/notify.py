
import os

def __register_cron(crontab_cmd):
    os.system('(crontab -l; echo "%s" ) | crontab - ' % crontab_cmd)

def schedule(title, body, cron=None):        
    __register_cron(' '.join(['%s' % cron,
        'export DBUS_SESSION_BUS_ADDRESS=\\"%s\\"' % os.environ['DBUS_SESSION_BUS_ADDRESS'],
        '&&', 
        '/usr/bin/notify-send \\"%s\\" \\"%s\\"' % (title, body),
        ''
    ]))

