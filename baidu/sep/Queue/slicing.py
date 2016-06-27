#encoding=utf-8
#对http://www.something.com形式的url进行分割
url = raw_input("Please input an url:")
domin = url[11:-4]#截取字段，含头不含尾
print "Domin name is " + domin