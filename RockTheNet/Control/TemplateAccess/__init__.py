import json
from flask import Flask
from flask import render_template
from flask import session
from flask import request
from flask_classy import FlaskView
from flask_classy import route
from flask import Response, redirect
import random

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
            return redirect("rules")
        
        else:
            return render_template('login.html', error=error)
    
    def logout(self):
        session.pop('ip', None)
        session.pop('port', None)
        session.pop('community', None)
        return self.index()

    def parserZones(self, data):
        rv = []
        for i in range(0,10):
            rv.append([])
        for i in range(0,len(data),10):
            for j, x in enumerate(rv):
                r = i/10
                if r == 0 or r == 1 or r == 2 or r == 3 or r == 4:
                    x.append(data[i+j])
        return rv

    @route('/zones', methods=['GET'])
    def zones(self):
        oidzones = '1.3.6.1.4.1.3224.8.1'
        community = session['community']
        port = session['port']
        ip = session['ip']
        zonesResult = self.connection.getbulk(oidzones, community, ip, port)
        return render_template('zones.html', logged_in=self.checkSessions(), services=self.parserZones(zonesResult))

    def parserServices(self, data):
        rv = []
        for i in range(0,72):
            rv.append([])
        for i in range(0,len(data),72):
            for j, x in enumerate(rv):
                r = i/72
                if r == 0 or r == 1 or r == 2:
                    x.append(data[i+j])
        return rv

    @route('/services', methods=['GET'])
    def services(self):
        oidservices = '1.3.6.1.4.1.3224.13.1'
        community = session['community']
        port = session['port']
        ip = session['ip']
        serviceResult = self.connection.getbulk(oidservices, community, ip, port)
        return render_template('services.html', logged_in=self.checkSessions(), services=self.parserServices(serviceResult))

    def parserRules(self, data):
        rv = []
        for i in range(0,12):
            rv.append([])
        for i in range(0,len(data),12):
            for j, x in enumerate(rv):
                r = i/12
                if r == 0 or r == 1 or r == 2 or r == 3 or r == 4 or r == 5 or r == 6 or r == 7 or r == 8 or r == 9 or r == 10 or r == 13:
                    x.append(data[i+j])
        return rv

    @route('/rules', methods=['GET'])
    def rules(self):
        oidtraffic = '1.3.6.1.4.1.3224.10.2.1.6'
        oidrules = '1.3.6.1.4.1.3224.10.1'
        community = session['community']
        port = session['port']
        ip = session['ip']
        tableResult = self.connection.getbulk(oidrules, community, ip, port)
        #return render_template('overview.html', logged_in=self.checkSessions(), rules=tableResult, traffic=trafficResult)
        return render_template('overview.html', logged_in=self.checkSessions(), rules=self.parserRules(tableResult), traffic=None)
        #return pasa(tableResult)

    @route('/trafficjson/<int:rid>', methods=['GET'])
    def trafficJSON(self, rid):
        oidtraffic = '1.3.6.1.4.1.3224.10.2.1.6'
        community = session['community']
        port = session['port']
        ip = session['ip']
        trafficResult = self.connection.getbulk(oidtraffic, community, ip, port)
        #tableResult = '%s' % self.connection.getbulk(oidrules, community, ip, port)
        #trafficResult = '%s' % self.connection.getbulk(oidtraffic, community, ip, port)
        #return render_template('overview.html', logged_in=self.checkSessions(), rules=tableResult, traffic=trafficResult)
        bPS = int(trafficResult[rid])
        return Response(json.dumps({"bPS":bPS}), mimetype='application/json')

    def registerApp(self):
        self.register(self.app)
        
    def debug(self):
        self.debug = True
        
    def run(self):
        self.app.debug = self.debug
        self.app.run(port=self.port)
