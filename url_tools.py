import os
import urllib.request
import io
from tld import get_fld


def get_domain_name(url):
    """
    Return the domain name for the given url.

    Args:
        url: fully formed valid url
    """
    domain_name = get_fld(url)
    return domain_name



def get_ip_address(url):
    """
    Return the ip address for the given url.
        nslookup returns the "Non-authoritative answer:" message when using a non-authoritative server

    Args:
        url: fully formed valid url
    """
    command = "nslookup " + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find(url)
    return results[marker + 11 + len(url):].splitlines()[0]


def get_robots_txt(url):
    """
    Return the robots.txt file for the given url if it exists.

    Args:
        url: fully formed valid url
    """
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')

    return data.read()



def get_whois(url):
    """
    Return the WhoIs for the given url.  The host os must be able to perform a 'whois'.

    Args:
        url: fully formed valid url
    """
    command = 'whois ' + url
    process = os.popen(command)
    results = str(process.read())
    return results

