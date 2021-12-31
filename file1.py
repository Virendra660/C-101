import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.A_O79wg-DgZMAjsGr5_phpSkiBa9IhkPR_7RgJWetYocNZvXHtX7jZrnIB9ovhQCMwmudT6R3SQ_Sl1rCM3N_ecbFLaIgbfY0tBg8awoBMXmeOqUh08jbrl5xfyzMTzdEVxe1sydkvFi'
    transferdata=TransferData(access_token)
    file_from=input("Enter the file path to transfer: ")
    file_to=input("Enter the full path to upload to dropbox: ")
    transferdata.upload_file(file_from,file_to)
    print("File has been moved")

main()