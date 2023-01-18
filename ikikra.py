def func2(arg4, arg5):
    var10 = func3(arg4, arg5)
    def func4(arg11, arg12):
        var13 = 657 - arg12 ^ 2055680432 ^ var10
        if arg11 < arg5:
            var14 = var10 ^ arg12
        else:
            var14 = var10 + arg4 ^ -1906878462 + arg5
        var15 = arg11 - arg12
        var16 = arg5 & arg11 & var13
        var17 = ((arg12 + arg11) | var15) + arg5
        var18 = arg11 ^ arg5
        var19 = var18 - var18
        var20 = arg4 | (arg11 - arg12 & var10)
        var21 = 1622453042 - arg12
        if var15 < var19:
            var22 = var21 ^ var20
        else:
            var22 = arg4 | ((arg4 ^ arg11) & arg5)
        var23 = (850 & (var17 + var15)) | var17
        var24 = (arg12 + arg5 & var23) - var17
        result = arg12 + var15 ^ arg11
        return result
    var25 = func4(var10, arg4)
    if var25 < arg4:
        var30 = class5()
    else:
        var30 = class7()
    for var31 in xrange(16):
        var30.func6(var25, var10)
    var36 = func9(var25, arg5)
    var41 = func10(var36, arg4)
    var42 = var25 | (var25 ^ var10) + 1285413493 + var10
    var43 = (var41 | arg5) & ((var36 | (831946505 - (1258629482 - var41) - (arg5 - var25 & var10 | var42) - ((((arg4 | 836) - arg4 | ((-2066164261 + var25) | var25) ^ var36) - -120) | var42 - var25))) + var10 - -303)
    var44 = var43 | (arg5 & var42 & 904162555)
    var45 = var41 & 706
    result = ((var36 & var41 + 285 - var44) & (var42 ^ var25 & var10) | var25 + var44 | var43 ^ var36) - arg5
    return result
def func10(arg37, arg38):
    var39 = 0
    for var40 in xrange(27):
        var39 += arg38 & var40
    return var39
def func9(arg32, arg33):
    var34 = 0
    for var35 in range(50):
        var34 += var35 + var34
    return var34
class class7(object):
    def func6(self, arg28, arg29):
        return 0
class class5(class7):
    def func6(self, arg26, arg27):
        return 0
def func3(arg6, arg7):
    var8 = 0
    for var9 in xrange(50):
        var8 += (var8 - arg7) ^ var8
    return var8
def func1(arg1, arg2):
    var3 = -217 - (-1455493836 - (arg1 & arg1) - ((2059798121 + -1399468794) & (arg2 | 458) ^ (((-419924692 - arg2 + (arg2 - ((arg2 - arg1) | -962554062 | 865) + 1723682345) | -700 ^ 217) - arg2 & arg2) & 1274798796)) ^ 649)
    result = ((((var3 ^ (arg1 & var3) + var3 | 774) ^ arg2) ^ arg1 | arg1 & -1856708286) | arg1) ^ -451 | 1290146971
    return result
if __name__ == "__main__":
    print 'prog_size: 0'
    print 'func_number: 2'
    print 'arg_number: 4'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 46'
    for i in xrange(25000):
        x = 5
        x = func2(x, i)
        print x,
