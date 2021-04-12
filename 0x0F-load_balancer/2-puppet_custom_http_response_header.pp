# Install nginx with puppet

package {
    ensure   => present,
    provider => 'apt'
    name     => 'nginx'
}



file_line { 'add line':
  path   => '/etc/nginx/sites-available/default',
  line   => "request as file, then\nadd_header X-Served-By $HOSTNAME",
  match  => "request as file, then",
}