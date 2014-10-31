import json
from flask import Flask
from flask import render_template
from flask import session
from flask import request
from flask_classy import FlaskView
from flask_classy import route

from Control.Connection import Connection

class TemplateAccess(FlaskView):
    route_base = '/'
    debug = False
    port = 5000
    app = Flask(__name__)
    connection = Connection()
    
    def __init__(self):
        self.app.template_folder = '../../View/templates'
        self.app.static_folder = '../../View/static'
        self.app.secret_key = '\xa3\xb4!ItQU\xd9\xf7P\xd6\xbe=G_T\xa0=!\xfe\xf0\xc6\xf0\xc7'
        
    def checkSessions(self):
        logged_in = None
        count = 0
        for word in ['ip', 'port', 'community']:
            if word in session: 
                count += 1
        if count == 3:
            logged_in = True
            
        return logged_in
    
    @route('/index', methods=['GET'])
    @route('/', methods=['GET'])
    def index(self):
        return render_template('login.html', logged_in=self.checkSessions())

    @route('/index', methods=['GET', 'POST'])
    @route('/', methods=['GET', 'POST'])
    @route('/login', methods=['GET', 'POST'])
    def login(self):
        error = None
        logged_in = None
    
        if request.method == 'POST':
            ip = request.form.get("ip")
            port = request.form.get("port")
            community = request.form.get("community")
            
            state = self.connection.checkcon(ip, port, community)
            
            if state:
                session['ip'] = ip
                session['port'] = port
                session['community'] = community
                logged_in = True
            else: 
                error = 'Check your Login Input!'
            
        if logged_in:
            return self.rules()
        
        else:
            return render_template('login.html', error=error)
    
    def logout(self):
        session.pop('ip', None)
        session.pop('port', None)
        session.pop('community', None)
        return self.index()

    @route('/rules', methods=['GET'])
    def rules(self):
        oidtraffic = '1.3.6.1.4.1.3224.10.2.1.6'
        oidrules = '1.3.6.1.4.1.3224.10.1'
        community = session['community']
        port = session['port']
        ip = session['ip']
        tableResult = '%s' % self.connection.getbulk(oidrules, community, ip, port)
        trafficResult = '%s' % self.connection.getbulk(oidtraffic, community, ip, port)
        return render_template('overview.html', logged_in=self.checkSessions(), rules=json.dumps(tableResult), traffic=json.dumps(trafficResult))

    def registerApp(self):
        self.register(self.app)
        
    def debug(self):
        self.debug = True
        
    def run(self):
        self.app.debug = self.debug
        self.app.run(port=self.port)
