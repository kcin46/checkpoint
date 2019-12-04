import requests, json

# Main function that handles POST requests to the Management Server
def api_call(ip_addr, port, command, json_payload, sid):
    url = 'https://' + ip_addr + ':' + port + '/web_api/' + command
    if sid == '':
        request_headers = {'Content-Type' : 'application/json'}
    else:
        request_headers = {'Content-Type' : 'application/json', 'X-chkp-sid' : sid}
    try:
        r = requests.post(url,data=json.dumps(json_payload), headers=request_headers, verify=False)
        if(r.status_code == 200):
            return r.json()
        else:
            return None
    except Exception, e:
        print("Connection error:\n")


# Attempts to login the user and return the session id upon completing successfully
def login(user, password, address):
    payload = {'user':user, 'password' : password}
    response = api_call(address, '4434', 'login',payload, '')
    
    if(response is None):
        return None
    else:
        return response["sid"]

# Logs out of the current session
def logout(ip_addr, sid):
    logout_result = api_call(ip_addr, '4434',"logout", {},sid)
    print("logout result: " + json.dumps(logout_result))

# Publish current session
def publish(ip_addr, sid):
    publish_result = api_call(ip_addr, '4434', "publish", {}, sid)
    print("publish result: " + json.dumps(publish_result))

# Add a new host object
def add_host(name, new_host_ip_addr, mgmt_ip, sid):
    payload = {'name': name, 'ip-address': new_host_ip_addr }
    new_host_result = api_call(mgmt_ip, '4434','add-host', payload ,sid)
    print(json.dumps(new_host_result))

# Delete host object
def delete_host(name, mgmt_ip, sid):
    payload = { 'name': name }
    delete_host_result = api_call(mgmt_ip, '4434', 'delete-host', payload, sid)
    print(json.dumps(delete_host_result))


