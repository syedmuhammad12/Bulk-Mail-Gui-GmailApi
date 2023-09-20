import proxyscrape

collector = proxyscrape.create_collector('default', 'socks5')  # Create a collector for http resources
proxy = collector.get_proxies()  # Retrieve a united states proxy
print(proxy)