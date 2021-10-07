# increase the number of request to handle

# increase the uper limt
exec { 'increase-upper-limit':
        command => "/bin/sed -i /etc/default/nginx -e 's/15/4000/'"
}

# restart the nginx service

exec { 'restart-nginx':
        command => '/usr/sbin/service nginx restart',
        require => Exec['increase-upper-limit']
}
