# fin error and fix it ith puppet
exec {
    command  => sudo sed -i 's\define('WP_DEBUG', false);\define('WP_DEBUG', true);' /var/www/html/wp-config,
    provider =>  shell,
}