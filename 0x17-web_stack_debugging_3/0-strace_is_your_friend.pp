# fin error and fix it ith puppet
exec {
    command  => 'sudo sed -i "s\phpp\p" /var/www/html/wp-settings.php',
    provider =>  shell,
}