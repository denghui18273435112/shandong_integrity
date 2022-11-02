environment = "TP"
if  environment == "line":
    #山东诚信;url;cookie_name存在cookies中token名称;vcode_name验证码在cookies中的名称;code验证码的请求路径
    url="http://employee.sdbx.org:10252"
    cookie_name = "sd-siccms-token"
    vcode_name= "vcode"
    code_url="/base/home/VerificationCode?"
    headers_cookie = "Cookie"
    V_code_name = "Vcode"
    Login_api="/base/home/Login"
if  environment == "TP":
    #山东诚信;url;cookie_name存在cookies中token名称;vcode_name验证码在cookies中的名称;code验证码的请求路径
    url="http://employee.sdbx.org:10261"
    cookie_name = "sd-siccms-token"
    Cookies_name = "testtool-token"
    vcode_name= "vcode"
    code_url="/base/home/VerificationCode?"
    headers_cookie = "Cookie"
    V_code_name = "vcode"
    Login_api="/base/home/Login"
proxies = {"http":"http://127.0.0.1:8888"}



