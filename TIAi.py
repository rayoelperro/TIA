from subprocess import Popen, PIPE

info = {"name": "desconocido"}
handlers = {}
saves = {}

def isPIPInstall():
    p = Popen(['pip'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    if output.startswith("\nUsage:"):
        return True
    else:
        return False

def installPackages(*pks):
    for p in pks:
        p = Popen(['pip','install',p], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        print output
        print err