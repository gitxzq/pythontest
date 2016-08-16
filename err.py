# class FooError(StandardError):
#     pass
#
# def foo(s):
#     n=int(s)
#     if n==0:
#         raise FooError('invalid value: %s'%s)
#     return 10/n
#
# foo(0)

# def foo(s):
#     n=int(s)
#     assert n!=0,'n is zero'
#     return 10/n
#
# def main():
#     foo('0')
#
# main()

# import logging
#
#
# s='0'
# n=int(s)
# logging.info('n= %d'%n)
# print 10/n

s='0'
n=int(s)
print (10/n)