Incident ID: INC-001

Title: Unauthorized SSH Brute Force Attack

Severity: HIGH

Detection Source: Wazuh Host-Based Intrusion Detection System (HIDS)

Affected Asset: Ubuntu Server (192.168.56.102 / vtcsec)

Attacker IP: 192.168.56.103 (Kali Linux)

MITRE ATT&CK Mapping: T1110 (Brute Force), T1110.001 (Password Guessing)

1. Executive Summary
A high volume of repeated failed SSH login attempts was detected originating from host 192.168.56.103 targeting the Ubuntu server (192.168.56.102). The activity was flagged by the Wazuh Agent monitoring /var/log/auth.log and escalated to the SIEM dashboard. The pattern matches an automated password guessing attack intended to gain unauthorized shell access.

2. Indicators of Compromise (IoCs)
Source IP: 192.168.56.103

Target Port: 22/TCP (SSH)

Target Account: marlinspike / root

Log Artifact: Failed password for marlinspike from 192.168.56.103 port <port> ssh2

3. Attack Timeline
19:55 - 20:25: Initial burst of failed SSH authentication attempts captured by auth.log.

20:25: Wazuh trigger threshold reached, generating Rule ID 5712 (SSH brute force attempt) alerts.

20:35: Secondary verification scan detected and logged in the Wazuh Threat Hunting module.

4. Technical Investigation
Examination of the endpoint authentication logs on vtcsec confirmed rapid connection attempts within a short interval.

Plaintext
Sep  4 20:24:12 vtcsec sshd[2841]: Failed password for marlinspike from 192.168.56.103 port 41232 ssh2
Sep  4 20:24:13 vtcsec sshd[2843]: Failed password for marlinspike from 192.168.56.103 port 41234 ssh2
Sep  4 20:24:14 vtcsec sshd[2845]: Failed password for marlinspike from 192.168.56.103 port 41236 ssh2
The high frequency of connection requests from a single external IP indicates the use of an automated credential-stuffing tool (such as Hydra or Medusa). No successful logins were observed from 192.168.56.103 during this window.

5. Impact & Root Cause
Impact: Low system impact, no system breach or compromise occurred. Authentication services experienced minor resource consumption.

Root Cause: SSH password authentication was left exposed to the internal network without connection throttling or public key authentication requirements.