# increase the number of request to handle

# increase the uper limt
exec { 'increase-upper-limit':
        command => 'sed -i "s/15/4000" /etc/default/nginx',
        path    => '/usr/local/bin/:/bin/'
}

# restart the nginx service

exec { 'restart-nginx':
        command => 'nginx restart',
        path    => '/etc/init.d/',
        require => Exec['increase-upper-limit']
}
