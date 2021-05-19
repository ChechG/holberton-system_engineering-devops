# fin error and fix it ith puppet
exec {
    command  => 'sudo sed -i "s\define('WP_DEBUG', false);\define('WP_DEBUG', true);" /var/www/html/wp-config;
                sudo sed -i "s\phpp\p" /var/www/html/wp-settings.php',
    provider =>  shell,
}