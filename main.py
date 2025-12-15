import url_tools
import os

ROOT_DIR = 'companies'


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


def gather_info(name, url):
    robots_txt = url_tools.get_robots_txt(url)
    domain_name = url_tools.get_domain_name(url)
    ip_address = url_tools.get_ip_address(domain_name)
    whois = url_tools.get_whois(domain_name)

    create_report(name, url, domain_name, robots_txt, ip_address, whois)


def create_report(name, url, domain_name, robots_txt, ip_address, whois):
    project_dir = ROOT_DIR + "/" + name
    create_dir(project_dir)

    write_file(project_dir + '/full_url.txt', url)
    write_file(project_dir + '/robots_txt.txt', robots_txt)
    write_file(project_dir + '/ip_address.txt', ip_address)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/whois.txt', whois)


create_dir(ROOT_DIR)
gather_info('google', 'https://www.google.com')
gather_info('facebook', 'https://www.facebook.com')
