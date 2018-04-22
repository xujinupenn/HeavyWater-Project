from list_save import list_file
class list_read:
    def get_list(self):
        tty = []
        list_get = list_file(tty,'list_name.txt')
        return list_get.list_read()
    def get_label(self):
        test=[]
        label_get = list_file(test,'label_name.txt')
        return label_get.list_read()

if __name__ == '__main__':
    tty = list_read()
    print(tty.get_list())