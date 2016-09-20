# coding=UTF-8

from sheet import *


if __name__=="__main__":
    print("====Start====")
    matrix8=[[5,1,3,8,7,1,5,8]
            ,[4,3,2,1,5,7,3,2]
            ,[8,6,8,5,4,2,7,1]
            ,[6,2,2,3,1,4,4,4]
            ,[8,7,6,3,4,1,2,7]
            ,[7,8,4,2,3,5,3,3]
            ,[2,6,7,4,6,6,8,6]
            ,[5,5,2,5,8,3,1,6]]
    matrix16=[[16,10,15,13,6,6,6,4,7,7,1,9,2,8,5,15,2]
              ,[9,9,9,2,4,8,14,5,10,10,10,17,12,16,6,11,13]
              ,[14,17,5,1,2,7,7,7,6,3,12,10,4,11,11,11,16]
              ,[2,5,12,6,8,5,14,10,17,13,10,16,10,15,4,7,1]
              ,[7,1,13,15,6,4,9,11,16,13,3,16,2,11,13,13,13]
              ,[5,16,4,11,11,11,2,9,13,15,14,6,17,10,1,12,7]
              ,[16,12,6,8,15,11,16,13,5,7,2,1,10,6,16,1,3]
              ,[12,8,1,3,5,16,1,7,15,17,13,11,17,4,17,8,5]
              ,[1,13,17,7,16,10,3,17,10,11,4,14,14,13,5,2,8]
              ,[11,3,7,16,17,2,6,12,9,5,9,14,10,7,8,10,4]
              ,[6,5,10,14,8,10,13,1,9,4,6,1,7,5,15,6,3]
              ,[15,11,1,7,13,14,13,2,9,6,9,8,8,12,10,3,14]
              ,[6,2,16,13,10,4,4,3,12,2,7,14,15,9,9,9,17]
              ,[17,4,3,1,7,15,10,6,5,2,10,7,13,14,6,9,12]
              ,[10,6,1,9,7,10,12,1,2,5,5,12,13,17,8,4,12]
              ,[7,5,9,17,7,1,5,14,10,16,10,13,11,5,13,5,6]
              ,[8,2,6,10,12,13,6,11,1,6,16,4,3,10,14,5,9]]
    sheet=Sheet(matrix16)
    sheet.solve()
    print("=====End=====")