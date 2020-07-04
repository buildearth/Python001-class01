#随机agent的生成方式
#pip install fake_useragent
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl = False)
print(ua.chrome)
print(ua.random)
