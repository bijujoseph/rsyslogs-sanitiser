An rsyslogs module to sanitize rsyslogs.

Install instructions
=====================
1. Copy the contents to /opt/rsyslogs-sanitiser/ folder
2. Copy the sanitiser.conf to /etc/rsyslog.d/ folder
3. Restart rsyslog demon. 

Testing
========
The below command must send message to "/var/log/messages"

1. Standard message
  logger testmessage
  cat /var/log/messages
2. Message to a facility named "kong at info level"
   logger -p kong.info "Welcome Biju"
   logger -p kong.info "Your ssn is 111-222-8888 and telephone number is (897) 224 7689"
   tail /var/log/knog.log
