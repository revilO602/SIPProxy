# Oliver Leontiev, 2022, MTAA Zadanie 1

import sipfullproxy.sipfullproxy as sipfullproxy
import sys
import logging
import socketserver

PORT = 5060
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s:%(message)s', filename='call_diary.log', level=logging.INFO,
                        datefmt='%d.%m.%Y %H:%M:%S')
    host = sys.argv[1]
    logging.info(f'Proxy server started at <{host}:{PORT}>')
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (host, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (host, PORT)
    server = socketserver.UDPServer((host, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

