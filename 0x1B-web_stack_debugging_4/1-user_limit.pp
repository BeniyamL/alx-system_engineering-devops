# enable holberton user to open a file without error

# increas hard limt
exec { 'increase-hard-limt':
        command => 'sed -i "/holberton hard/s/5/40000" /etc/security/limits.conf',
        path    => '/usr/local/bin/:/bin/'
}

# increase soft limit
exec { 'increase-soft-limit':
        command => 'sed -i "holberton soft/s/4/40000" /etc/security/limits.conf',
        path    => '/usr/local/bin/:/bin/'
}
