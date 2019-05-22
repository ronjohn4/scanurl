import os


def get_ip_address(url):
    command = "nslookup " + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find(url)
    return results[marker + 11 + len(url):].splitlines()[0]


print(get_ip_address('https://www.google.com'))
