from wxpy import *
def login():
    print('状态:登录成功  ',end='')
def login_out():
    print('微信已退出!')
bot=Bot(login_callback=login,logout_callback=login_out,cache_path='login.pkl',qr_path='login_qr.png')
print('当前用户:'+bot.self.name)
bot.auto_mark_read()#自动清除手机端消息红点提示
bot.enable_puid(path='wxpy_puid.pkl')#启用puid属性 具有稳定性的标识