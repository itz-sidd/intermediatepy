# myList=["apple","banana","mango"]
# print(myList)
# myList.append("orange")
# print(myList)
# item=myList.append("lemon")
# print(item)
# for i in myList :
#     print(i)

# nums=[1,3,4,7,3,43,56,98]
# nums.sort()
# print(nums)

# arrt=[9]*3
# print(arrt)

# mylist=["apple","litchy","orange"]
# item=mylist
# #print(item)
# for i in item:
#     print(item)
    
# print(len(mylist))

# mylist.insert(1,"mango")
# print(mylist)
# mylist.pop()
# print(mylist)

# mylist.remove("litchy")
# print(mylist)
# mylist.clear()
# print(mylist)
# listy=[1,2,3,4,-1,-4,-9]
# listy.sort()
# print(listy)
# kko=[3]*3
# print(kko)
# kkk=[1,2,3,4,5]
# ook=kko+kkk
# print(ook)

# lio=[1,2,3,4,5,6,7,8,9]
# aa=lio[1::-1]
# print(aa)

# dod=["banana","cherry","lemon"]
# dod_copy=dod
# dod_copy.append("litchy")
# print(dod_copy)
# print(dod)
# mm=[1,2,3,4,5]
# nn=[i*i for i in mm]

# print(mm)
# print(nn)


#TUPLES
# myu=("max",28,"Boston")#brackets are optional
# print(myu)
# print(type(myu))

# yty=tuple(["max",45,"NYC"])
# # print(yty)

# # rtr=yty[2]
# # print(rtr)
# for d in yty:
#     print(d)

# if "max" in yty:
#     print("yes")
# else: 
#     print("no")      

# ggg=['q','w','e','t','y']
# print(len(ggg))  
# print(ggg.count('w'))
# print(ggg.index('q'))
# gggh=list(ggg)
# print(gggh)

# ww=(1,2,3,4,5,6,7,8,9)
# ee=ww[0:3]
# print(ee)
# re=ww[::-1]
# print(re)

# ty="max",56,"nyc"
# name,age,city=ty
# print(name)
# print(age)
# print(city)

# yui=(1,2,3,4,5)
# i1,*i2,i3=yui
# print(i1)
# print(*i2)
# print(i3)

# import sys
# ty=[0,1,2,"hello",True]
# ytrt=(0,1,2,"hello",True)
# print(sys.getsizeof(ty),"bytes")
# print(sys.getsizeof(ytrt),"bytes")

#DICTONARIES
# re={"name":"max","age":39,"city":"NYC"}
# # print(re)

# # er=dict(name="harry",age=45,city="Delhi")
# # print(er)
# val=re["name"]
# print(val)
# re["email"]="max@efh.com"
# print(re)

# # del re["email"]
# # print(re)
# # re.pop("name")
# # print(re)
# # if "name" in re:
# #     print("yes")
# # else:
# #     print("no")  
# # try:
# #     print(re["ages"])
# # except:
# #     print("error")
# # for key,value in re.items():
# #     print(key,value)

# re_cpy=re
# re_cpy["sex"]="male"
# print(re_cpy)
# print(re)
# yuu={3:9,6:36,9:81}
# print(yuu)
# tut=(8,7)
# fgf={tut:15}
# print(fgf)

#SETS
# er={1,2,3,4}
# print(er)
# myset=set("hlo")
# print(myset)
# mm=set()
# mm.add(1)
# mm.add(89)
# mm.add(7)
# print(mm)
# #mm.discard(7)
# # print(mm)
# #mm.clear()
# # print(mm)
# for i in mm:
#     print(mm)

# if 1 in mm:
#     print("yes")
# else:
#     print("no") 
# odd={1,3,5,7,9}
# even={0,2,4,6,8}
# primes={2,3,5,7}
# u=odd.union(even)
# print(u)
# ii=odd.intersection(primes)
# print(ii)       
# ass={1,2,3,4,5,6,7,8}
# asss={1,2,3,4,5}
# # dif=ass.difference(asss)
# # print(dif)
# # fid=ass.symmetric_difference(asss)
# # print(fid)
# # ass.intersection_update(asss)
# # print(ass)
# # print(asss.issubset(ass))
# # print(asss.issuperset(ass))
# cd={9,10}
# yt=cd
# yt.add(1)
# print(yt)
# print(cd)
# aa=frozenset([1,2,3,4])

#STRINGS


# strr="Hy she's mary"
# df='defefef'
# jh="""hello
# world"""
# print(strr)
# print(df)
# print(jh)
# dsd="Hello bobsy"
# char=dsd[4]
# print(char)
# suf=dsd[0:5]
# print(suf)
# dse=dsd[::-1]
# print(dse)
# tg="bYe"
# name="ROBY"
# sent=tg+" "+name
# #print(sent)
# # for y in tg:
# #     print(y)
# if 'b' in tg:
#     print("yes")
# else:
#     print("no") 
# bg='Hy vow'
# print(bg)   
# # bg=bg.strip()
# # print(bg)
# print(bg.upper())
# print(bg.lower())
# print(bg.startswith('H'))
# print(bg.endswith('vow'))
# print(bg.find('df'))
# print(bg.replace('vow','fire'))
# kk='how,are,you,doing'
# io=kk.split(',')
# print(io)
# pp=''.join(io)
# print(pp)

# from timeit import default_timer as timer
# sdd=['a']*1000000
# #print(sdd)

# start=timer()
# ee=''
# for i in sdd:
#     ee+=i
# #print(ee)  
# stop=timer() 
# print(stop-start) 

# start=timer()
# qw=''.join(sdd)
# stop=timer()
# print(stop-start)

# var="Roby"
# ss=3
# fgf=6.7666233
# dd="the variable is %f" %fgf
# print(dd)
# bb=3.134568
# ll=9
# sss="it is a {:.2f} and {}" .format(bb,ll)
# print(sss)
# ssd=f"it is a {bb*2} and {ll*2}" 
# print(ssd)

#COLLECTIONS

# from collections import Counter
# a = "aaaabbbccc"
# dd=Counter(a)
# print(dd.values())
# print(dd.most_common(2))
# print(dd.most_common(1)[0][0])
# print(dd.elements())

# from collections import namedtuple
# pp=namedtuple('Point','x,y')
# pt=pp(1,-4)
# print(pt)
# print(pt.x,pt.y)

# from collections import OrderedDict
# er=OrderedDict()
# er['a']=1
# er['b']=4
# er['c']=3
# er['d']=2
# print(er)

# from collections import defaultdict
# d=defaultdict(int)
# d['a']=1
# d['b']=2
# print(d)
# print(d['a'])


# from collections import deque
# d=deque()
# d.append(1)
# d.append(2)
# d.appendleft(3)
# print(d)
# # d.pop()
# # print(d)
# # d.popleft
# # print(d)
# d.extendleft([4,5,6])
# print(d)
# d.rotate(1)
# print(d)

#ITERTOOLS
# from itertools import product
# a=[1,2]
# b=[3]
# prod=product(a,b ,repeat=2)
# print(list(prod))

# from itertools import permutations
# a=[1,2,3]
# per=permutations(a, 2)
# print(list(per))

# from itertools import combinations,combinations_with_replacement
# a=[1,2,3,4]
# per=combinations(a, 2)
# print(list(per))
# com=combinations_with_replacement(a,2)
# print(list(com))

# from itertools import accumulate
# import operator
# a=[1,2,3,4]
# acc=accumulate(a, func=operator.mul)
# print(a)
# print(list(acc))

# from itertools import groupby
# # def smallerthan3(x):
# #     return x<3
# per=[{'name':'dod','age':20},{'name':'marx','age':20},{'name':'dolly','age':24}]

# # a=[1,2,3,4]
# # grp=groupby(a, key=smallerthan3)
# # for key,value in grp:
# pp=groupby(per, key=lambda x:x['age'])
# for key,value in pp:
#     print(key,list(value))

# from itertools import count,cycle,repeat

# # for i in count(10):
# #     print(i)
# #     if i==15:
# #         break
# a=[1,2,3]
# for e in repeat(1,4):
#     print(e)

#LAMBDA
# add10=lambda x:x+10
# print(add10(5))

# def ad10fuc(x):
#     return x+10

# mult=lambda x,y:x+y
# print(mult(2,4))

# pt20=[(1,2),(15,1),(5,-1),(10,4)]

# # def sr(x):
# #     return x[1]
# pt20sort=sorted(pt20, key=lambda x:x[0]+x[1])

# print(pt20)
# print(pt20sort)

#MAP FUNCTION
# a=[1,2,3,4,5]
# b=map(lambda x:x*2,a)
# print(list(b))

# c=[x*2 for x in a]
# print(c)

#FILTER FUNCTION

# a=[1,2,3,4,5,6]
# b=filter(lambda x: x%2==0,a)
# print(list(b))

# c=[x for x in a if x%2==0]
# print(c)

#REDUCE FUNCTION

# from functools import reduce
# a=[1,2,3,4]
# prod=reduce(lambda x,y: x*y,a)
# print(prod)

#ERRORS AND EXCEPTIONS
# x=5
# if x<0:
#     raise Exception('x should be negative')

# z=5
# assert (z>=0),'z is not posotive'

# try:
#     a=5/0
#     b=a+'10'
# except ZeroDivisionError as e:
#     print('an error occoured')    
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine')
# finally:
#     print('cleaning up...')    

# class valueTOOHighError(Exception):
#     pass

# class valueTOOSmallError(Exception):
#     def __init__(self,message,value):
#         self.message=message
#         self.value=value

# def tt_val(x):
#     if x>100:
#         raise valueTOOHighError('value is too high')
#     if x<5:
#         raise valueTOOSmallError('value is too small',x)
    
# try:
#     tt_val(4)
# except valueTOOHighError as e:
#     print(e)
# except valueTOOSmallError as e:
#     print(e.message,e.value)

# import logging
# import traceback
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')
# import helper
# logger=logging.getLogger(__name__)

# #creating handler
# stream_h=logging.StreamHandler()
# file_h=logging.FileHandler('file.log')

# #level and format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter=logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('this is an error')
# logger.error('this is ane error')

# try:
#     a[1,2,3]
#     val=a[4]
# except:
#     logging.error("this is %s",traceback.format_exc() )

# import logging
# import time
# from logging.handlers import TimedRotatingFileHandler

# logger=logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


# handler=TimedRotatingFileHandler('timed_test.log',when='m',interval=1,backupCount=5)
# logger.addHandler(handler)

# for _ in range(6):
#     logger.info('Hello')
#     time.sleep(3)
   
# import random


# # a=random.normalvariate(0,1)
# # print(a)
# # myl=list("ABCDEFG")
# # # a=random.sample(myl,k=3)
# # # print(a)
# # random.shuffle(myl)
# # print(myl)

# random.seed(1)
# print(random.random())
# print(random.randint(1,10))
# random.seed(2)
# print(random.random())
# print(random.randint(1,10))

# random.seed(1)
# print(random.random())
# print(random.randint(1,10))
# random.seed(2)
# print(random.random())
# print(random.randint(1,10))


# import secrets

# jj=list("ASDFGHJKL")
# a=secrets.choice(jj)
# #1010 4 diff binary values
# print(a)

# import numpy as np

# arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)
# np.random.shuffle(arr)
# print(arr)

#%##np.random.seed(1)s
# print(np.random.rand(3,3))
# np.random.seed(1)
# print(np.random.rand(3,3))

#DECORATORS

# @mydecorator
# def dos():
#     pass

# def start_end_deco(func):

#     def wrapper(*args,**kwargs):
#         print('start')
#         func(*args,**kwargs)
#         print('end')
#         return __name__
#     return wrapper    

# @start_end_deco
# def add5(x):
#     return x+5
# # def print_name():
# #     print("Aria")

# #print_name=start_end_deco(print_name)

# # print_name()

# #add5(10)
# print(help(add5(10)))
# print(add5.__name__)

# import functools


# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             for _ in range(num_times):
#                 result=func(*args,**kwargs)
#             return result
#         return wrapper
#     return decorator_repeat    


# def start_end_decorator(func):
#     def wrapper(*args, **kwargs):
#         # Add functionality before the original function call
#         result = func(*args, **kwargs)
#         # Add functionality after the original function call
#         return result
#     return wrapper

# @debug
# @start_end_decorator
# def greet(name):
#     greeting='Hello {name}'
#     print(greeting)
#     return greeting

# greet('Aros')    

# class CountCalls:

#     def __init__(self,func):
#         self.func=func
#         self.num_calls=0

#     def __call__(self,*args,**kwargs):
#         self.num_calls+=1
#         print(f'Thi is executed {self.num_calls} times')
#         return self.func(*args,**kwargs)

# # cc=CountCalls(None)
# # cc()

# @CountCalls
# def say_hello(name):
#     print(name)

# say_hello('Ass')
# say_hello('Saa')

#GENERATORS

# def mygenerator():
#     yield 1
#     yield 2
#     yield 3

# g=mygenerator()
# for i in g :
#      print(i)
# value=next(g)
# print(value)

# value=next(g)
# print(value)


# value=next(g)
# print(value)

# print(sum(g))
# print(sorted(g))

# def CountDown(num):
#     print('Starting')
#     while num>0:
#         yield num
#         num-=1

# cd=CountDown(4)

# value=next(cd)
# print(value)

# print(next(cd))

# import sys

# def firstn(n):
#     nums=[]
#     num=0
#     while num<n:
#         nums.append(num)
#         num+=1
#     return nums

# def firstn_generator(n):
#     num=0
#     while num<n:
#         yield num
#         num+=1


# print(firstn(10))
# print(sum(firstn_generator(10)))
# print(sys.getsizeof(firstn(100000)))
# print(sys.getsizeof(firstn_generator(100000)))

# def finonacci(limit):
#     a,b=0,1
#     while a<limit:
#         yield a
#         a,b=b,a+b

# fib=finonacci(30)
# for i in fib:
#     print(i)      
# 

# import sys

# mygenerator=(i for i in range(10) if i%2==0)
# print(sys.getsizeof(mygenerator))
# # for i in mygenerator:
# #     print(i)
# mylist=(i for i in range(10) if i%2==0)
# print(sys.getsizeof(mylist))

#THREADING AND MULTIPROCESSING

# from multiprocessing import process
# import os
# import time

# def square_numbers():
#     for i in range(100):
#         i*1
#         #time.sleep(0.1)

# pr=[]
# numpr=os.cpu_count()

# for i in range(numpr):
#     p=process(target=square_numbers)
#     pr.append(p)

# for p in pr:
#     p.start()

# for p in pr:
#     p.join()

# print('end main')

# from multiprocessing import Process
# import os

# def square_numbers():
#     for i in range(100):
#         i * i  # Just a dummy operation

# pr = []
# numpr = os.cpu_count()  # Get number of CPU cores

# for i in range(numpr):
#     p = Process(target=square_numbers)  # Use Process class correctly
#     pr.append(p)

# for p in pr:
#     p.start()  # Start each process

# for p in pr:
#     p.join()  # Wait for all processes to finish

# print('End main')

# from threading import Thread
# import os
# import time


# def square_numbers():
#     for i in range(1000):
#         i*1
#         #time.sleep(0.1)

# if __name__=='__main__':
#     threads=[]
#     num_threads=10


# threads=[]
# num_threads=10

# for i in range(num_threads):
#     t=Thread(target=square_numbers)
#     threads.append(t)

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()

# print('End main')

# from threading import Thread,Lock
# import time

# database_value=0

# def increase(lock):
#     global database_value

#     lock.acquire()
#     local_copy=database_value

#     local_copy+=1
#     time.sleep(0.1)
#     database_value=local_copy
#     lock.release()

# if __name__=='__main__':

    
#     lock=Lock()
#     print('Start value',database_value)

#     thread1=Thread(target=increase,args=(lock,))
#     thread2=Thread(target=increase,args=(lock,))

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print('End value',database_value)

#     print('End main')

# from threading import Thread,Lock,current_thread
# from queue import Queue
# import time


# def worker(q):
#     while True:
#         value=q.get()

#         print(f' in {current_thread().name} got {value}')
#         q.task_done()

# if __name__=='__main__':

#     q=Queue()

#     num_threads=10

#     for i in range(num_threads):
#         thread=Thread(target=worker,args=(q,))
#         thread.daemon=True
#         thread.start()

#     for i in range(1,21):
#         q.put(i)

#     q.join()

#     # q.put(1)
#     # q.put(2)
#     # q.put(3)

#     # first=q.get()
#     # print(first)

#     # print(q.empty())
#     # print(q.task_done())
#     # print(q.join)
#     print('End main')


# MULTIPROCESSING

# from multiprocessing import Process,Value,Array,Lock
# from multiprocessing import Queue
# import time

# # def add_100(numbers,lock):
# #     for i in range(100):
# #         time.sleep(0.01)
# #         # for number in numbers:
# #         #     number+=1
# #         for i in range(len(numbers)):
# #             with lock:
# #                 numbers[i]=1
# #         # with lock():
#         #     number.value+=1


# def square(numbers,queue):
#     for i in numbers:
#         queue.put(i*1)

# def make_negative(numbers,queue):
#     for i in numbers:
#         queue.put(-1*i)


# if __name__=="__main__":

#     # lock=Lock()
#     # #shared_number=Value('i',0)
#     # shared_array=Array('d',[0.0,100.0,200.0])
#     # print('Array at beginning is',shared_array[:])

#     # p1=Process(target=add_100,args=(shared_array,lock))
#     # p2=Process(target=add_100,args=(shared_array,lock))

#     # p1.start()
#     # p2.start()

#     # p1.join()
#     # p2.join()

#     # print('Array at the end is',shared_array[:])


#     # #print('number at end is',shared_number.value)

#     numbers=range(1,6)
#     q=Queue()

#     p1=Process(target=square,args=(numbers,q))
#     p2=Process(target=make_negative,args=(numbers,q))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     while not q.empty():
#         print(q.get())


# from multiprocessing import Pool

# def cube(number):
#     return number*number*number

# if __name__=="__main__":

#     numbers=range(10)
#     pool=Pool()

#     result=pool.map(cube,numbers)
#     # pool.apply(cube,numbers[0])

#     pool.close()
#     pool.join()

#     print(result)


# def pname(name):
#     print(name)

# pname('Sid')

# def foo(a,b,c):
#     print(a,b,c)

# foo(a=1,b=2,c=3)
# foo(c=3,b=1,a=2)

# def foo(a,b,c,d=4):
#     print(a,b,c,d)

# foo(1,2,3,5)

# def foo(a,b,*args,**kwargs):
#     print(a,b)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key,kwargs[key])

# foo(1,2,3,4,5,six=6,seven=7)
# foo(1,2,3,4)

# def foo(a,b,*,c,d):
#     print(a,b,c,d)

# foo(1,2,c=3,d=4)

# def foo(*args,last):
#     for arg in args:
#         print(arg)
#     print(last)

# foo(1,2,3,last=100)

# def foo(a,b,c):
#     print(a,b,c)

# # my_list=[0,1,2]
# # foo(*my_list)

# # my_list=(0,1,2)
# # foo(*my_list)

# my_dict={'a':1,'b':2,'c':3}
# foo(**my_dict)

# def foo():
#     global number
#     x = number
#     number=3
#     print('number inside function',x)

# number=0
# foo()
# print(number)


# def foo(x):
#     x=5

# var=10
# foo(var)
# print(var)

# def foo(a_list):
#     # a_list+=[200,300,400]
#     a_list=a_list+[100,200,300]
#     # a_list.append(4)
#     # a_list[0]=-100

# my_list=[1,2,3]
# foo(my_list)
# print(my_list)

# result=5*7
# print(result)

# er=4**2
# print(er)

# zeros=[1]*10
# print(zeros)

# ee="AB"*5
# print(ee)

# def foo(a,b,*args,**kwargs):
#     print(a)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key,kwargs[key])

# foo(1,2,3,4,5,six=6,seven=7)

# def foo(a,b,*,c):
#     print(a,b,c)

# foo(1,2,c=3)

# def foo(a,b,c):
#     print(a,b,c)

# # my_list=[1,2,3]
# # foo(*my_list)

# my_dict={'a':1,'b':2,'c':3}
# foo(*my_dict)

# numbers=[1,2,3,4,5,6]

# # *beginning,last=numbers
# # print(beginning)
# # print(last)

# beginning,*middle,secondlast,last=numbers
# print(beginning)
# print(middle)
# print(secondlast)
# print(last)

# my_tuple=(1,2,3)
# # my_list=[4,5,6]
# my_set={4,5,6}

# # new_list=[*my_tuple,*my_list]
# new_list=[*my_tuple,*my_set]
# print(new_list)
# dict_a={'a':1,'b':2,}
# dict_b={'c':3,'d':4}
# my_dict={**dict_a,**dict_b}
# print(my_dict)


# org=5
# cpy=org
# # print(cpy)
# cpy=6
# print(cpy)
# print(org)

# org=[1,2,3,4,5,6]
# cpy=org
# cpy[0]=-10
# print(cpy)
# print(org)

# import copy
# org=[1,2,3,4,5,6]
# # cpy=copy.copy(org)
# cpy=org[:]
# cpy[0]=-10
# print(cpy)
# print(org)

# import copy
# org=[[1,2,3,4,5,6],[7,8,9,10]]
# cpy=copy.deepcopy(org)

# cpy[0][1]=-10
# print(cpy)
# print(org)

# import copy
# class Person:
#     def __inti__(self,name,age):
#         self.name=name
#         self.age=age

# p1=Person('Alex',32)
# p2=p1

# p2.age=34
# print(p2.age)
# print(p1.age)

# with open('notes.txt','w') as file:
#     file.write('some to do....')

# file=open('notes.txt','w')
# try:
#     file.write('some todoo...')
# finally:
#     file.close()

# from threading import Lock
# lock=Lock()

# lock.acquire()

# lock.release()

# with lock:
#     #....

class ManagedFile:
    def __init__(self,filename):
        self.filename=filename

    def __enter__(self):
        print('enter')
        self.file=open(self.filename,'w')
        return self.file
    
    def __exit__(self,exc_type,exc_value,exc_traceback):
        if self.file:
            self.file.close()
        print('exc:',exc_type,exc_value)
        print('exit')

with ManagedFile('notes.txt') as file:
    print('do some stuffs..')
    file.write('some todo...')
print('continuing here')