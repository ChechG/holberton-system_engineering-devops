# Install nginx with puppet

exec {'puppet_header':
    command  =>  'sudo apt-get update -y; sudo apt-get install nginx -y;
                  sudo sed -i "46i\add_header X-Served-By \$HOSTNAME ;" /etc/nginx/sites-available/default'
    provider =>   shell,
}