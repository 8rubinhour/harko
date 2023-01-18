def func2(arg5, arg6):
    var13 = var9(arg6, arg5)
    var16 = class6()
    for var17 in xrange(36):
        var18 = var16.func7
        var18(var13, var13)
    def func8(arg19, arg20):
        var21 = arg20 ^ (-127 - 644 ^ arg5 | arg20)
        var22 = (((((var13 - (366488613 ^ arg19 - (var21 - 43)) + var13 + -1599392990 ^ arg6 | var21) ^ (arg5 & ((((arg5 + arg20) + arg5) & arg19) - -826186378) | -392)) + arg20 | arg20) | arg19 - arg6) + arg20) | arg6
        var23 = (var22 + arg6) & (-707 & (var21 ^ var22 | arg20 | var21) - arg5 + (var21 & arg19))
        result = ((var21 ^ (var23 - arg19) | arg5 - arg19 & arg6) + (var21 + (423900146 | var21) + var13 | arg20)) ^ arg6
        return result
    var24 = func8(arg6, var13)
    var25 = func11()
    if arg6 < var13:
        var30 = class12()
    else:
        var30 = class14()
    for var31 in range(1):
        var32 = var30.func13
        var32(var24, var31)
    var33 = var13 & arg5
    var34 = -99 ^ 1774264017
    result = 99 & var13
    return result
class class14(object):
    def func13(self, arg28, arg29):
        return 0
class class12(class14):
    def func13(self, arg26, arg27):
        result = (((arg27 ^ -258817909) | arg27 - arg27) ^ -1682253826 - arg27) - -1410344771
        return result
def func11():
    func9()
    result = len(range(22))
    func10()
    return result
def func10():
    global len
    del len
def func9():
    global len
    len = lambda x : 8
class class6(object):
    def func7(self, arg14, arg15):
        return 0
def func5(arg10, arg11):
    var12 = (arg11 ^ 18 & -570421547) + ((arg11 + arg10 | arg10 + 189 | (-1986531323 + arg10) - arg10 & (((-605055130 - (((((arg10 & 870) ^ -1513770912) ^ arg11) - arg10) & arg10 ^ 33)) + -655212867) & arg11)) - -90722466) - 11726274
    result = arg11 - arg11
    return result
def func4():
    closure = [5]
    def func3(arg7, arg8):
        closure[0] += func5(arg7, arg8)
        return closure[0]
    func = func3
    return func
var9 = func4()
def func1(arg1, arg2):
    var3 = -1089549491 | 502579595
    var4 = 931147868 - (1134137279 - 1944941072)
    result = (var3 | (-656 - arg2) ^ -348964098 - arg2 | arg2 + (var3 - -1009279474 + (arg2 & 922817813) - arg2)) | var3
    return result
if __name__ == "__main__":
    print 'prog_size: 0'
    print 'func_number: 2'
    print 'arg_number: 5'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 16'
    print 'arg_number: 35'
    for i in xrange(25000):
        x = 5
        x = func2(x, i)
        print x,
