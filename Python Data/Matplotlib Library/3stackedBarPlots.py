import numpy as np
import matplotlib.pyplot as plt

# N=5
# menMeans=(20,35,30,35,27)
# womenMeans=(25,32,34,20,25)
# ind=np.arange(N)   # the x location of the groups
# width=0.35  # the width of the bars :can also be len(x) sequence
# p1=plt.bar(ind,menMeans,width)
# p2=plt.bar(ind,womenMeans,width,bottom=menMeans)  #x position is same for both plots,so we get stacked bar
# plt.ylabel('scores')
# plt.title('scores by group and gender')
# plt.xticks(ind,('g1','g2','g3','g4','g5'))  # xticks- gives x range and name each group in x axis
# # plt.legend((p1,p2),('Men','Women'))
# plt.legend(('Men','Women'))
# plt.show()

#########################
# yticks-to set a y range

menMeans=(20,35,30,35,27)
womenMeans=(25,32,34,20,25)
menstd=(2,3,4,1,2)
womenstd=(3,5,2,3,3)
#
ind=np.arange(len(menMeans))   # the x location for the groups
width=0.35
# p1=plt.bar(ind,menMeans,width,yerr=menstd)
# p2=plt.bar(ind,womenMeans,width,
#            bottom=menMeans,yerr=womenstd)
# plt.ylabel("scores")
# plt.title("scores by group and gender")
# plt.xticks(ind,('g1','g2','g3','g4','g5'))  # for name the x axis field
# plt.yticks(np.arange(0,81,10))
# plt.legend(('Men','Women'))
# plt.show()

#########################
# we can define legend in bar plot statement itself

# p1=plt.bar(ind,menMeans,width,yerr=menstd,label="men")
# p2=plt.bar(ind,womenMeans,width,
#            bottom=menMeans,yerr=womenstd,label="women")
# plt.ylabel('scores')
# plt.title("scores by group and gender")
# plt.xticks(ind,('g1','g2','g3','g4','g5'))
# plt.yticks(np.arange(0,81,10))
# plt.legend()
# plt.show()

############################
# bars side by side

# p1=plt.bar(ind-.25,menMeans,width,yerr=menstd,label="men")
# p2=plt.bar(ind+.15,womenMeans,width,yerr=womenstd,label="women")
# plt.ylabel('scores')
# plt.title("scores by group and gender")
# plt.xticks(ind,('g1','g2','g3','g4','g5'))
# plt.yticks(np.arange(0,81,10))
# plt.legend()
# plt.show()

############################
# horizontal bar

# p1 = plt.barh(ind-.15, menMeans, width, xerr=menstd,label="men")   # by using barh & xerr
# p2 = plt.barh(ind+.15, womenMeans, width, xerr=womenstd,label="women")
# #
# plt.xlabel('Scores')
# plt.title('Scores by group and gender')
# plt.yticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
# plt.xticks(np.arange(0, 81, 10))
# plt.legend()
# plt.show()


#############################

