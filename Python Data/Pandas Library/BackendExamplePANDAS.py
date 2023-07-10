# import pandas as pd
import pathlib
# import numpy as np
class dataframe():
    def __init__(self):
        self.parent_list=[]
    def csv_read(self, path):
        g=open(path,'r')
        for x in g.readlines():
            child_list = x.split(",")
            self.parent_list.append(child_list)
            # print(self.parent_list)
        # pl = np.array(self.parent_list,dtype=object)
        # print(pl)
    def prints(self):      
        for i in range(len(self.parent_list)):
        # print(i)
        # print(lst[i])
            for j in range(len(self.parent_list[i])):
                # print(j)
                print(self.parent_list[i][j], end='\t')    
      
        
                        

class panda(dataframe):
    # def __init__(self):#,ndf
    #         # self.ndf=ndf
    #         # # self.s=s

    def heads(self,s=5):
        y = 0
        # print(self.parent_list)
        while (y<=s):
            # print(y)
            string = ""
            # print(self.parent_list[y])
            for x in self.parent_list[y]:
                string += str(x) + "\t"
            print(string)
            y += 1
            # for y in range(s):
            #     print("----")
            #     print(y)
            #     # a = str(y)+"\t"
            #     for x in range(self.ndf.shape[1]):
            #         print(self.ndf.iloc[y,x])
            #     #     a += str(self.ndf.iloc[y,x]) + "\t"
            #     # print(a)
    def tails(self,s=5):
        last = 0
        start = -(s)
        # print(self.parent_list)
        while (last>=start):
            # print(last)
            string = ""
            # print(self.parent_list[last])
            for x in self.parent_list[last]:
                string += str(x) + "\t"
            print(string)
            last -= 1
    #         LAST = self.ndf.shape[0]
    #         START = LAST - s
    #         for y in range(START,LAST):
    #             print("----")
    #             print(y)
    #             # a = str(y)+"\t"
    #             for x in range(self.ndf.shape[1]):
    #                 print(self.ndf.iloc[y,x])
                #     a += str(self.ndf.iloc[y,x]) + "\t"
                # print(a)
    def coloumns(self):
        self.parent_list[0][-1] = self.parent_list[0][-1].strip('\n')
        self.coloumn = self.parent_list[0]
        return self.coloumn
    def shapes(self):
        rows = len(self.parent_list) - 1
        cols = len(self.parent_list[0])
        tup = (rows,cols)
        return tup


 
pATH = pathlib.Path(__file__).parent.resolve()
path = str(pATH.as_posix())
pds = panda()
pds.csv_read(path+"/PC_import_2014_2015.csv")
# pds.prints()
# pds.heads()
# pds.tails()
# print(pds.coloumns())
# print(pds.shapes())

# nf = pd.read_csv(path+"/PC_import_2014_2015.csv")
# df = panda(nf)
# df.heads(10)
# print("====================================================================================================")
# df.tails()