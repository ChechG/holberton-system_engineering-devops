# --- Web stack debugging #2 ---

**Background Context**
-------------
Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.

**Test and verify your assumptions**
-------------
The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

    Is the web server started? - You can check using the service manager, also double check by checking process list.
    On what port should it listen? - Check your web server configuration
    Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see the process for each listening port
    It is listening on the correct server IP? - netstat is also your friend here
    Is there a firewall enabled?
    Have you looked at logs? - usually in /var/log and tail -f is your friend
    Can I connect to the HTTP port from the location I am browsing from? - curl is your friend

There is a good chance that at this point you will already have found part of the issue.

**Requirements**
-------------
**General**
    - All your files will be interpreted on Ubuntu 14.04 LTS
    - All your files should end with a new line
    - A README.md file at the root of the folder of the project is mandatory
    - All your Bash script files must be executable
    - Your Bash scripts must pass Shellcheck without any error
    - Your Bash scripts must run without error
    - The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
    - The second line of all your Bash scripts should be a comment explaining what is the script doing

**Tasks**
-------------
- 0 - Run software as another user:
    The user root is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the root user, as if you fat finger a command and for example run rm -rf /, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the root user can do, just need to use a specific command that you need to discover.

    For the containers that you are given in this project as well as the checker, everything is run under the root user, which has the ability to run anything as another user.

    Requirements:

    write a Bash script that accepts one argument
    the script should run the whoami command under the user passed as an argument
    make sure to try your script by passing different users
    Example:

            root@ubuntu:~# whoami
            root
            root@ubuntu:~# ./0-iamsomeoneelse www-data
            www-data
            root@ubuntu:~# whoami
            root
            root@ubuntu:~#
