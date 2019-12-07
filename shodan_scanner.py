

import shodan

a = shodan.Shodan("Your API Key")
while True:
    print(
        """
    1. get your ip
    2. Shodan Search to scan IPs, Hostnames, ports
    3. Scanning a specific Host
    0. quit
        """
    )
    x = int(input("your option : "))
    if x == 2:
        s = input("what would you like to search ? ")
        results = a.search(s)
        for result in results['matches']:
            print( result["ip_str"],"\t",end = '')
            print(str(result["port"]),"\t",end = '')
            print( result["org"],"\t",end = '')
            print(result["location"]["country_name"],"\t",end = '')
            print()
            print()
    if x == 3:
        k = input("enter an ip addrs : ")
        ipinfo = a.host(k)
        print("host name:"," "*8,ipinfo['hostnames'],"\n",
              "city :"," "*11,ipinfo["city"], "\n",
              "country :"," "*8,ipinfo["country_name"],"\n",
              "organization :"," "*3,ipinfo["org"], "\n",
              "port :"," "*11,ipinfo['data'][0]['port'],"\n"
              )
    if x ==1:
        print(a.tools.myip())
    if x == 0:
        break
