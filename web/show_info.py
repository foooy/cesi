import os
from flask import Flask, render_template
import getProcInfo 
from getProcInfo import Config, Connection
import xmlrpclib

app = Flask(__name__)
app.config.from_object(__name__)

connection = Connection(Config.host, Config.port, Config.username, Config.password).getConnection()

@app.route('/')
def show_info():
    info_list = []
    lis = connection.supervisor.getAllProcessInfo()
    for i in lis:
        one = getProcInfo.ProcInfo(i)
        info_list.append(one)
    return render_template('show_info.html', info_list = info_list)


@app.route('/process/stop/<process_name>')
def startProcess(process_name):
    rv = connection.supervisor.stopProcess(process_name)
    if rv == True:
        return "yes"
    else:
        return "no"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
