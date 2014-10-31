from Control.Converter import Converter

from pysnmp.entity.rfc3413.oneliner import cmdgen

import socket

class Connection:
    converter = Converter()
    cmdGen = cmdgen.CommandGenerator()
    
    def checkcon(self, ip, port, community):
        try:
            oid = '1.3.6.1.2.1.1.1.0'
            socket.inet_aton(ip)
            errorIndication, errorStatus, errorIndex, varBindTable = self.cmdGen.getCmd (
                cmdgen.CommunityData(community),
                cmdgen.UdpTransportTarget((ip, port)), oid
            )
            if errorIndication:
                return False
            
            else:
                return True

        except socket.error: 
            return False
        
    def get(self, oid, communityName, ipAddress, ipPort):
        errorIndication, errorStatus, errorIndex, varBindTable = self.cmdGen.getCmd (
            cmdgen.CommunityData('public', communityName),
            cmdgen.UdpTransportTarget((ipAddress, ipPort)), oid
        )
        
        return self.converter.convertData(errorIndication, errorStatus, errorIndex, varBindTable, 1)

    def getbulk(self, oid, communityName, ipAddress, ipPort):
        errorIndication, errorStatus, errorIndex, varBindTable = self.cmdGen.nextCmd (
            cmdgen.CommunityData('public', communityName),
            cmdgen.UdpTransportTarget((ipAddress, ipPort)), oid,
            lexicographicMode = False, ignoreNonIncreasingOid = False, lookupNames = True
        )

        return self.converter.convertData(errorIndication, errorStatus, errorIndex, varBindTable, 0)