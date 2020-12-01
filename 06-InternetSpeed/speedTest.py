import psutil
import pyspeedtest
from tabulate import tabulate

class Network_Details(object):
    def __init__(self):
        self.parser = psutil.net_if_addrs()
        self.speed_parser = pyspeedtest.SpeedTest()
        self.interfaces = self.interface()[0]

    def interface(self):
        interfaces = []
        for interface_name, _ in self.parser.items():
            interfaces.append(str(interface_name))
        return interfaces

    def __repr__(self):
        down = str(f"{round(self.speed_parser.download() / 1000000, 2)} Mbps")
        up = str(f"{round(self.speed_parser.upload() / 1000000, 2)} Mbps")
        interface = self.interfaces
        data = {"Interface:" : [interface],
                "Download:" : [down],
                "Upload:" : [up]}
        table = tabulate(data, headers="keys", tablefmt="pretty")
        return table

if __name__ == "__main__":
    print(Network_Details())
