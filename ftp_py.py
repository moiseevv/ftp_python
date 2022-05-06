import ftplib
import codecs

def ftp_upload(ftp_obj, path, ftype='TXT'):
    """
    Функция для загрузки файлов на FTP-сервер
    @param ftp_obj: Объект протокола передачи файлов
    @param path: Путь к файлу для загрузки
    """
    if ftype == 'TXT':
        with open(path, "rb") as fobj:
            print('после open')
            ftp_obj.storlines('STOR ' + path, fobj)
            print('после передачи')
    else:
        with open(path,"rb") as fobj:
            print('после open2')
            ftp_obj.storbinary('STOR ' + path, fobj, 1024)
            print('после передачи2')
            


if __name__ == '__main__':
    ftp = ftplib.FTP('192.168.x.x')
    ftp.login('x', 'x')  # login and password ftp 
    ftp.retrlines('LIST')
    
    path = 'wee.xlsx'
    print(" path = ", path)
    ftp_upload(ftp, path, ftype='PDF')

    ftp.retrlines('LIST')
    ftp.quit()