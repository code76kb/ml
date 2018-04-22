
import numpy as np
from Full_Snake import Full_Snake
import random



class Breading_Room:

    OFFSPRINGS = 2

    def __init__(self, snak_len):
        self.snak_len = snak_len
        print("Breading_Room is reqdy")



    def make_love(self,mates_array):
        print("MAking love total MAtes:",len(mates_array))
        male_Snaks = []
        female_Snaks= []
        topHalfs = []
        lowHalf = []
        newBread = []
        sortedByFitness = sorted(mates_array,key=lambda x:x.fitness, reverse=True)
        topHalfs = sortedByFitness[:len(mates_array)/2]
        lowHalf = sortedByFitness[len(mates_array)/2:]

        print("topHalfs size :",len(topHalfs))

        # for i in xrange(0,len(topHalfs)):
        #     print("\nSorted by fitness",sortedByFitness[i].fitness)
        #     if i%2 == 0:
        #         male_Snaks.append(topHalfs[abs(len(topHalfs)-i)])
        #     else:
        #         female_Snaks.append(topHalfs[abs(len(topHalfs)-i)])
        female_Snaks = topHalfs
        male_Snaks = topHalfs[::-1]

        print("Total Femals :",len(female_Snaks))
        print("Total Males :",len(male_Snaks))
        pair = len(male_Snaks) if(len(female_Snaks)>len(male_Snaks)) else len(female_Snaks)

        for j in xrange(0,len(topHalfs)):
            weight_H_female = female_Snaks[j].nural_Net.weight_matrix_hidden
            weight_H_male = male_Snaks[j].nural_Net.weight_matrix_hidden
            weight_O_female = female_Snaks[j].nural_Net.weight_matrix_output
            weight_O_male = male_Snaks[j].nural_Net.weight_matrix_output

            # print("\n Femals H:",weight_H_female)
            # print("\n Femals O:",weight_O_female)
            # print("\n Mals H:",weight_H_male)
            # print("\n Mals O:",weight_O_male)

            # print("\n Split::",np.array_split(weight_H_female,2))

            w_h_F_UpearHELF = np.array_split(weight_H_female,2)[0] #4*2
            w_h_F_LowerHELF = np.array_split(weight_H_female,2)[1] #4*3

            w_h_M_UpearHELF = np.array_split(weight_H_male,2)[0] #4*2
            w_h_M_LowerHELF = np.array_split(weight_H_male,2)[1] #4*3


            w_o_F_UpearHELF = np.array_split(weight_O_female,2)[0] #5*2
            w_o_F_LowerHELF = np.array_split(weight_O_female,2)[1] #5*2

            w_o_M_UpearHELF = np.array_split(weight_O_female,2)[0] #5*2
            w_o_M_LowerHELF = np.array_split(weight_O_female,2)[1] #5*2

            #Boy
            w_h_B = np.vstack((w_h_M_UpearHELF, w_h_F_LowerHELF))
            w_o_B = np.vstack((w_o_M_UpearHELF, w_o_F_LowerHELF))

            #mutation
            r = (w_h_B.shape[0])-1
            c = (w_h_B.shape[1])-1

            m1 =  1 / (1 + np.e ** -w_h_B[random.randint(0,r),random.randint(0,c)])
            # print('Mutation b1 by:',m1)
            w_h_B[random.randint(0,r),random.randint(0,c)] =  m1

            r = (w_o_B.shape[0])-1
            c = (w_o_B.shape[1])-1
            m2 = 1 / (1 + np.e ** -w_o_B[random.randint(0,r),random.randint(0,c)])
            # print('Mutation b2 by:',m2)
            w_o_B[random.randint(0,r),random.randint(0,c)] =  m2


            newSnak = Full_Snake(self.snak_len)
            newSnak.nural_Net.weight_matrix_hidden = w_h_B
            newSnak.nural_Net.weight_matrix_output = w_o_B

            newBread.append(newSnak)

            #Girl
            w_h_G = np.vstack((w_h_M_UpearHELF, w_h_F_LowerHELF))
            w_o_G = np.vstack((w_o_M_UpearHELF, w_o_F_LowerHELF))

            #mutation
            r = (w_h_G.shape[0])-1
            c = (w_h_G.shape[1])-1
            m3 = 1 / (1 + np.e ** -w_h_G[random.randint(0,r),random.randint(0,c)])
            # print('Mutation g1 by:',m3)
            w_h_G[random.randint(0,r),random.randint(0,c)] =  m3

            r = (w_o_G.shape[0])-1
            c = (w_o_G.shape[1])-1
            m4 =  1 / (1 + np.e ** -w_o_G[random.randint(0,r),random.randint(0,c)])
            # print('Mutation G2 by:',m4)
            w_o_G[random.randint(0,r),random.randint(0,c)] = m4

            newSnak = Full_Snake(self.snak_len)
            newSnak.nural_Net.weight_matrix_hidden = w_h_G
            newSnak.nural_Net.weight_matrix_output = w_o_G

            # print("\n BOY H:",w_h_B)
            # print("\n BOY O:",w_o_B)
            # print("\n GIRL H:",w_h_G)
            # print("\n GIRL O:",w_o_G)

            newBread.append(newSnak)

        print("new Bread popolation :",len(newBread))
        return newBread
