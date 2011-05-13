from Client import UDPClient, TCPClient
from Server import UDPServer, TCPServer
import Server
import Client

class Rammbock(object):

    def __init__(self):
        self._servers = {}
        self._clients = {}

    def start_udp_server(self, nwinterface, port, name=Server.DEFAULT_SERVER_NAME):
        self._servers[name] = UDPServer()
        self._servers[name].server_startup(nwinterface, port)

    def start_tcp_server(self, nwinterface, port, name=Server.DEFAULT_SERVER_NAME):
        self._servers[name] = TCPServer()
        self._servers[name].server_startup(nwinterface, port)

    def check_server_status(self, name=Server.DEFAULT_SERVER_NAME):
        return name in self._servers

    def connect_to_udp_server(self, host, port, ifname = False):
        self._client = UDPClient()
        self._client.establish_connection_to_server(host, port, ifname)

    def connect_to_tcp_server(self, host, port, ifname = False):
        self._client = TCPClient()
        self._client.establish_connection_to_server(host, port, ifname)

    def accept_tcp_connection(self, name=Server.DEFAULT_SERVER_NAME):
        self._servers[name].accept_connection()

    def close_server(self, name=Server.DEFAULT_SERVER_NAME):
        self._servers[name].close()
        del self._servers[name]

    def create_udp_client(self, name=Client.DEFAULT_CLIENT_NAME):
        self._clients[name] = UDPClient(name)

    def create_tcp_client(self, name=Client.DEFAULT_CLIENT_NAME):
        self._clients[name] = TCPClient(name)

    def close_client(self):
        self._client.close()

    def client_sends_data(self, packet): 
        self._client.send_packet(packet)

    def server_receives_data(self, name=Server.DEFAULT_SERVER_NAME):
        return self._servers[name].server_receives_data()

    def client_receives_data(self):
        return self._client.receive_data()

    def server_sends_data(self, packet, name=Server.DEFAULT_SERVER_NAME): 
        self._servers[name].send_data(packet)
