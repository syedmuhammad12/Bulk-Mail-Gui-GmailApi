# import proxyscrape

# collector = proxyscrape.create_collector('default', 'socks5')  # Create a collector for http resources
# proxy = collector.get_proxies()  # Retrieve a united states proxy
# print(proxy)





SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://mail.google.com/', 'https://www.googleapis.com/auth/gmail.settings.basic', 'https://www.googleapis.com/auth/gmail.metadata', 'https://www.googleapis.com/auth/gmail.modify',
              'https://www.googleapis.com/auth/gmail.addons.current.message.metadata', 'https://www.googleapis.com/auth/gmail.addons.current.message.action']
    creds = None
    
    
def callback_req(request_id, response, exception):
    print("req id:", request_id)
    print("response:", response)
    print("exception:", exception)
    
    
    
newMessage['From'] = f"Hi<{service.users().getProfile(userId='me').execute()['emailAddress']}>"



http = httplib2.Http(proxy_info=httplib2.ProxyInfo(
            httplib2.socks.PROXY_TYPE_HTTP, "172.233.225.126", 8080
        ))
    authorized_http = google_auth_httplib2.AuthorizedHttp(creds, http=http)
    
    batch = service.new_batch_http_request()
    batch.add(service.users().messages().send
                    (userId="me", body=create_message), callback=callback_req)
    batch.execute(http=authorized_http)