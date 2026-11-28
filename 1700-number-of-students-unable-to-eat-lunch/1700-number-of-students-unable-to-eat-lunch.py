class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
    #   '''
    # remmeber :- 0 defines circular sandwich 
    #         whereas 1- defines rectangular sandwich 
    #     '''
        count_0=students.count(0)
        count_1=students.count(1)
        for sandwich in sandwiches :
            if sandwich ==0:
                if count_0==0:
                    break
                count_0-=1#decrease is liye kar rhe kyuki student ne circular wali sandwich leke agya hai 
            else:
                if count_1==0:
                    break
                count_1-=1#yaha decrease is liye hua kyuki studnet ne rectangular wali sandiwcjh lkee gaya hai 
        return count_0+count_1 #last merin jo sandiwhc bach gayi decrease hone ke bad unki total count hi hme return karni hai 

