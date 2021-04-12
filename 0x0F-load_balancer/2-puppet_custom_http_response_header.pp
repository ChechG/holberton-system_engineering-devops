# Install nginx with puppet

exec { 'puppet_header':
    command  =>  'sudo apt-get -y update; sudo apt-get -y install nginx;
                sudo sed -i "46i\add_header X-Served-By $HOSTNAME ;" /etc/nginx/sites-available/default'
    provider =>  shell,
}