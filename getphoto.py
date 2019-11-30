import os
from urllib.request import urlretrieve

IMAGE_UR='./_imageUrls'
#reconnectfile=open('./reconnect.txt','r+')
Num = 0 #文件数量
allFileNum = 1 #分类数量

def urllib_download(IMAGE_URL, n):

    print(IMAGE_URL)
    path='./img/Group' + str(allFileNum)
    if(os.path.exists(path)==False):
        os.mkdir('./img/Group' + str(allFileNum))
    urlretrieve(IMAGE_URL, './img/Group' +str(allFileNum)+'/image'+ str(n) + '.jpg')  # whole document


def printPath(level, path):
    global allFileNum
    global Num
    '''''
    打印一个目录下的所有文件夹和文件
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称
    files = os.listdir(path)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if (os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if (f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if (os.path.isfile(path + '/' + f)):
            # 添加文件
            fileList.append(f)

    for fl in fileList:
        print(fl)
        f = open('./_imageUrls/' + fl)
        line = f.readline()
        line = line.strip('\n')
        while line:
            Num = Num + 1
            if(os.path.exists( './img/Group' +str(allFileNum)+'/image'+ str(Num) + '.jpg')==False):
                urllib_download(line, Num)
            line = f.readline()
            line=line.strip('\n')

        allFileNum = allFileNum + 1
        print(allFileNum)


if __name__ == '__main__':
    printPath(1, './_imageUrls')
