#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
import tarfile
from unrar import rarfile
import zipfile
import sys
import shutil
#解压tgz压缩包
def un_tgz(filename):
    tar = tarfile.open(filename)
    if os.path.isdir(os.path.splitext(filename)[0]):
        pass
    else:
        os.mkdir(os.path.splitext(filename)[0])
    tar.extractall(os.splitext(filename)[0])
    tar.close()
	
#解压rar压缩包
def un_rar(filename):
    rar=rarfile.RarFile(filename)
    if os.path.isdir(os.path.splitext(filename)[0]):
        pass
    else:
        os.mkdir(os.path.splitext(filename)[0])
    rar.extractall(os.splitext(filename)[0])
#解压zip压缩包
def un_zip(filename):
    zip_file=zipfile.ZipFile(filename)
    if os.path.isdir(os.path.splitext(filename)[0]):
        pass
    else:
        os.mkdir(os.path.splitext(filename)[0])
    for names in zip_file.namelist():
        zip_file.extract(names,os.path.splitext(filename)[0])
    zip_file.close()
	
#寻找关键字文件
def findfile(keyword,root):
    filelist=[]
    rfilelist=[]
    for root,dirs,files in os.walk(root):
        for name in files:
            filelist.append(os.path.join(root,name))
    for i in filelist:
        if os.path.isfile(i):
            if keyword in os.path.basename(os.path.splitext(i)[0]):
                rfilelist.append(i)
            else:
                pass
        else:
            pass
    return rfilelist
#判断并选择解压函数
def choose_func(allpath):
    postfix=os.path.splitext(allpath)[1]
    if postfix == '.tgz':
        un_tgz(allpath)
    elif postfix == '.rar':
        un_rar(allpath)
    elif postfix == '.zipp':
        un_zip(allpath)
    else :
        print 'This formart is not exits! '
#判断是否保留解压包
def is_hold():
	hold='yse'
	if len(sys.argv)>1:
		if (sys.argv[1]).lower() == 'no':
			hold = 'no'
		else:
			pass
	else:
		pass

#删除解压文件函数
def delete_unzip(filelist):
	thfile=filelist
	for i in thfile:
		shutil.rmtree(os.path.splitext(i)[0])
		



if __name__ == '__main__':
	#获取当前目录
    current_path= os.getcwd()
	#保存message文件的list
    message=[]
	hold=is_hold()
    filel=findfile('thl',current_path)
    for i in filel:
        choose_func(i)
        messagefile=findfile('message',os.path.splitext(i)[0])
        for j in messagefile:
            message.append(j)
    if hold == 'no':
		delete_unzip(filel)
	else :
		pass
