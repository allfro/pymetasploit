# Handles the MetaSploit Framework Remote Procedure Call Daemon (MSFRPCD) for *nix machines

import os, psutil, signal, time

def msfrpcdStart(password):
	if checkMsfrpcdRunning(): return "MetaSploit Framework Remote Procedure Call Daemon is already running."
	else:
		response = os.system("msfrpcd -P "+password+" -n -a 127.0.0.1")
		time.sleep(10)
		if checkMsfrpcdRunning(): return "MetaSploit Framework Remote Procedure Call Daemon running."
		else: return "There was an issue: MetaSploit Framework Remote Procedure Call Daemon did not start."

def checkMsfrpcdRunning():
	for socket in psutil.net_connections():
		if socket.laddr[1] == 55553: return socket.pid

def msfrpcdRestart(password):
	pid = checkMsfrpcdRunning()
	if pid:
		os.kill(socket.pid, signal.SIGKILL)
		print "Old MSFRPCD process killed."
	response = os.system("msfrpcd -P "+password+" -n -a 127.0.0.1")
	time.sleep(10)
	if checkMsfrpcdRunning(): return "MetaSploit Framework Remote Procedure Call Daemon running."
	else: return "There was an issue: MetaSploit Framework Remote Procedure Call Daemon did not start."
			
if __name__ == "__main__":
	print msfrpcdStart('pass123')
