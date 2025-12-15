import pytest
from url_tools import get_domain_name, get_ip_address, get_robots_txt, get_whois

import urllib.error


class TestGetDomainName:
    def test_get_domain_name_with_www(self):
        assert get_domain_name('http://www.google.com') == 'google.com'
    
    def test_get_domain_name_without_www(self):
        assert get_domain_name('https://github.com') == 'github.com'
    
    def test_get_domain_name_with_subdomain(self):
        assert get_domain_name('https://mail.google.com') == 'google.com'


class TestGetIpAddress:
    def test_get_ip_address_valid_domain(self):
        result = get_ip_address('google.com')
        assert result != ''
        assert len(result.split('.')) == 4
    
    def test_get_ip_address_returns_string(self):
        result = get_ip_address('github.com')
        assert isinstance(result, str)


class TestGetRobotsTxt:
    def test_get_robots_txt_with_trailing_slash(self):
        result = get_robots_txt('https://www.google.com/')
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_get_robots_txt_without_trailing_slash(self):
        result = get_robots_txt('https://www.google.com')
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_get_robots_txt_invalid_url(self):
        with pytest.raises(urllib.error.URLError):
            get_robots_txt('https://invalid-domain-12345.com')


class TestGetWhois:
    def test_get_whois_valid_domain(self):
        result = get_whois('google.com')
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_get_whois_returns_string(self):
        result = get_whois('github.com')
        assert isinstance(result, str)