import pandas as pd
import numpy as np
from list_save import list_file
from learing import learn
import win_unicode_console
win_unicode_console.enable()


class read_csv:

    

    #get the csv name
    def __init__ (self,input_name):
        self.name =input_name
    
    #read the all the data
    def read(self):
        self.file  = pd.read_csv(self.name,na_filter=True,header=None)
        self.file.ix[:,1].to_csv('temp.csv',index = False)

    #read the label
    def read_label(self):
        self.file_set = set(self.file.ix[:,0])

    
    #read the data
    def read_data(self):
        self.data_set = self.file.ix[:,1]
        self.word_set = set()
        self.all_list =[]
        for i in self.data_set:
            tmp = str(i)
            for word in tmp.split(' '):
                self.all_list.append(word)
            
        self.word_set = set(self.all_list)
    def get_numpy(self):
        self.read()
        self.read_label()
        self.read_data()
        self.data_list =list(self.word_set)
        self.label_list = list(self.file_set)
    #get 500f fist
    def get_temp(self):
        self.get_numpy()
        self.dist_list = list(self.word_set)
        list_tmp = range((len(self.all_list)))
        self.dist_dict = dict(zip(self.dist_list,list_tmp))
        cout = np.zeros((1,len(self.word_set)))
        for i in self.all_list:
            x = self.dist_dict[i]
            cout[0,x] =cout[0,x]+1
        self.dict_tmp =list(cout[0,:])

        self.temp_dct = dict(zip(self.dist_list,self.dict_tmp))

        #sort
        d = self.temp_dct
        I =sorted(d.items(), key=lambda d:-d[1])
        #print(I) 
        ### the data show wo need  64 data
        dict_begin =[]
        for i in I:
            dict_begin.append(i[0])
        self.dict = dict_begin[:100]
        list_write = list_file(self.dict,'list_name.txt') 
        list_write.list_save()
        label_write = list_file(self.label_list,'label_name.txt')
        label_write.list_save()




    def creat_numpy(self):
        self.get_temp()
        list_tmp0 = range((len(self.dict)))
        self.tmp_dict = dict(zip(self.dict,list_tmp0))
        self.data_numpy = np.zeros((len(self.file.ix[:,0]),100))
        xx=0
        for i in self.data_set:
            str_tmp = str(i)
            word = str_tmp.split(" ")
            yy = 0
            for j in self.dict:
                self.data_numpy[xx,yy] = word.count(j)
                yy = yy+1
            xx =xx+1
            #print(xx)
        return self.data_numpy


    def get_lable(self):
        self.get_numpy()
        print(len(self.file.ix[:,0]))
        self.out =np.zeros((len(self.file.ix[:,0]),len(self.label_list)))
  

        #for i in range(len(self.file.ix[:,0])):
        for i in range(len(self.file.ix[:,0])):
            self.out[i,self.label_list.index(self.file.ix[i,0])] =1
        return self.out
    

        

    
if __name__ == '__main__':
    tty = read_csv("shuffled-full-set-hashed.csv")
    #tty.read()
    #tty.read_data()
    label = tty.get_lable()
    data = tty.creat_numpy()
    mod = learn(data,label)
    mod.run()


