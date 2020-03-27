import subprocess

def processing(pathImage, pathSaveSCV):
    '''
    ОТправляет данные в программу на С#
    :param pathImage:
    :param pathSaveSCV:
    :return:
    '''
    command = "programm\Save2CSV.exe {} {}".format(pathImage, pathSaveSCV)
    p1 = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    out = p1.stdout.read()
    print(out)


if __name__ == '__main__':
    pathImage = r'D:\Teplo\Industrial\photo\DJI_0004.jpg'
    pathSaveSCV = r'D:\Teplo\Industrial\photo\DJI_0004.csv'
    processing(pathImage, pathSaveSCV)