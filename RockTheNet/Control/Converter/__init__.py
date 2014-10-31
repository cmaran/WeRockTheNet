class Converter:
    def convertData(self, errorIndication, errorStatus, errorIndex, varBindTable, check):
        if errorIndication:
            return errorIndication
        else:
            if errorStatus:
                return None
            else:
                results = None
                if check:
                    for oid, value in varBindTable:
                        results = '%s' % value
                else:
                    results = []
                    for varBindTableRow in varBindTable:
                        for oid, value in varBindTableRow:
                            results.append('%s' % value)
                return results