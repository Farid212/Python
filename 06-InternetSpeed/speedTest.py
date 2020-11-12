import speedtest
from tabulate import tabulate

class Network_Details(object):
    def __init__(self):
        self.parser = psutil.net_if_addrs()
        self.speed_parser = speedtest.Speedtest()
        seld.interfaces = self.interface()[0]

    def interface(self):
        interface = []
        for interface_name, _ in self.parser.items():
            interfaces.append(str(interface_name))
        return interfaces

    def __repr__(self):
        down = str(round(self.speed_parser.download() / 1000000, 2))
        up = str(round(self.speed_parser.upload() / 1000000, 2))
        interface = self.interfaces
        data = {"Interface:" : [interface],
                "Download:" : [down],
                "Upload:" : [up]}
        table = tabulate(data, headers="keys", tablefmt="pretty")
        return table

if __name__ == "__main__":
    print(Network_Details())
