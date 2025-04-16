from handler.runner import run 

url = "https://example.com/app/dashboards#/view/ID?_g=(filters:!(),refreshInterval:(pause:!f,value:120000),time:(from:now-4h,to:now))"
username = "user"
password = "passwd"
tab_number = 2
name="tab_name"
zoom = 1.65
run(url, username, password, tab_number, name, zoom)
