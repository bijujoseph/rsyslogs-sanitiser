An rsyslogs module to sanitize rsyslogs.

Install instructions
=====================
1. Copy the contents to /opt/rsyslogs-sanitiser/ folder
2. Copy the sanitiser.conf to /etc/rsyslog.d/ folder
3. Restart rsyslog demon.

```
 sudo chmod 777 /opt/rsyslogs-sanitiser/sanitiser.py


 sudo cp sanitiser.conf  /etc/rsyslog.d/
 sudo service rsyslog restart
```

Testing
========
The below command must send message to "/var/log/messages"

1. Standard message
  logger testmessage
  cat /var/log/messages
2. Message to a facility named "kong at info level"
   logger -p daemon.info -t kong "[KONG] Welcome Biju"
   logger -p daemon.info -t kong "[KONG] Your ssn is 111-222-8888 and telephone number is (897) 224 7689"
   tail /var/log/knog.log


Installing rsyslog on AMI
=========================
```
cd /tmp
wget https://raw.githubusercontent.com/bijujoseph/rsyslogs-sanitiser/master/rsyslog.repo
sudo cp rsyslog.repo /etc/yum.repos.d/
sudo yum upgrade rsyslog --disablerepo=amzn-main
sudo yum install rsyslog --disablerepo=amzn-main
sudo service rsyslog start
```