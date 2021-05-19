# fin error and fix it ith puppet
exec { 'fix':
    command  => 'sudo sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    provider =>  'shell',
}
