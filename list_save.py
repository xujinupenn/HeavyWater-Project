

#author:xu jin
#date:4/7
#document:
#   this class purpose is to save the str_list
#   the main is a test
#   list_file.list_save:save a list
#   list_file.list_read:read a list
class list_file:

    def __init__(self,list_name,file_name):
        self.list_name =list_name
        self.file_name =file_name

    def list_save(self):
        fp = open(self.file_name,'w+')
        for line in self.list_name:
            line_str = str(line)
            fp.write(line_str+'\n')
        fp.close()

    def list_read(self):
        self.list_out=[]
        fp = open(self.file_name,'r')
        lines = fp.readlines()
        for line in lines:
            tmp =line.replace('\n','')
            self.list_out.append(tmp)
        return self.list_out
            


if __name__ == '__main__':
    list_test =list(['peihongliang','lihaibo','zhaozhijian','lihuan'])
    list_write = list_file(list_test,'list_name.txt')
    print(list_write.list_read())
