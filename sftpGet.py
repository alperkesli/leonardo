import pysftp
def sftpExample():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  
    with pysftp.Connection('192.168.1.223', username='test', password='12345678', cnopts=cnopts) as sftp:
        sftp.get('/files/text.txt', '/Users/user/text.txt')  # upload file to public/ on remote
        sftp.close()

sftpExample()