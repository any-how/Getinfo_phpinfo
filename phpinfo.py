#coding:utf-8
import requests
import re
import sys
import winsound
import ctypes
STD_OUTPUT_HANDLE= -11 
FOREGROUND_BLUE = 0x09 # text color contains blue.  
FOREGROUND_GREEN= 0x02 # text color contains green.  

class ColorPrinter:   
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)  

    def set_cmd_color(self, color, handle=std_out_handle):   
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)  
        return bool
    def reset_color(self):  
        self.set_cmd_color(FOREGROUND_BLUE)

    def print_green_text(self, print_text):  
        self.set_cmd_color(FOREGROUND_GREEN)  
        print print_text 
        self.reset_color()

colorPrinter = ColorPrinter()

try:
	url = sys.argv[1]
except:
	colorPrinter.print_green_text(u"usage:python getinfo.py http://ssss/info.php")
	exit(0)

r = requests.get(url)
text = r.content

def findinfo(regex):
	p = re.findall(regex,text) 
	if p:
		return p[0].replace("</td><td class=\"v\">","|").replace("<i>","").replace("</i>","")
	else:
		return "No finding"
version = r'PHP Logo" /></a><h1 class="p">(.*)</h1>'
#version = r'PHP Version </td><td class="v">(.*)</td>'
system = r'System </td><td class="v">(.*)</td>'
path = r'SCRIPT_FILENAME"]</td><td class="v">(.*)</td>'
real_ip = r'SERVER_ADDR"]</td><td class="v">(.*)</td>'
ini = r'Loaded Configuration File </td><td class="v">(.*)</td>'
ini1 = r'Configuration File \(php.ini\) Path </td><td class="v">(.*)</td>'
allow_include = r'allow_url_include</td><td class="v">(.*)</td>'
allow_url_fopen = r'allow_url_fopen</td><td class="v">(.*)</td>'
disable_func = r'disable_functions</td><td class="v">(.*)</td>'
open_basedir = r'open_basedir</td><td class="v">(.*)</td>'
short_open_tag = r'short_open_tag</td><td class="v">(.*)</td>'
protocols = r'Protocols </td><td class="v">(.*)</td>'
php_streams = r'Registered PHP Streams</td><td class="v">(.*)</td>'
php_streams1 = r'Registered PHP Streams </td><td class="v">(.*)</td>'
system_path = r'PATH"]</td><td class="v">(.*)</td>'

colorPrinter.print_green_text(u"---------PHP版本----------")
print findinfo(version)
colorPrinter.print_green_text(u"---------网站路径---------")
print findinfo(path)
colorPrinter.print_green_text(u"---------真实IP-----------")
print findinfo(real_ip)
colorPrinter.print_green_text(u"---------php.ini----------")
print findinfo(ini)
print findinfo(ini1)
colorPrinter.print_green_text(u"---------allow_url_include")
print findinfo(allow_include)
colorPrinter.print_green_text(u"---------allow_url_open---")
print findinfo(allow_url_fopen)
colorPrinter.print_green_text(u"---------禁用函数---------")
print findinfo(disable_func)
colorPrinter.print_green_text(u"---------open_basedir-----")
print findinfo(open_basedir)
colorPrinter.print_green_text(u"---------short_open_tag---")
print findinfo(short_open_tag)
colorPrinter.print_green_text(u"---------协议-------------")
print findinfo(protocols)
colorPrinter.print_green_text(u"---------php streams流----")
print findinfo(php_streams)
print findinfo(php_streams1)
colorPrinter.print_green_text(u"---------系统-------------")
print findinfo(system)
colorPrinter.print_green_text(u"---------系统环境变量-----")
print findinfo(system_path).decode('utf_8')
