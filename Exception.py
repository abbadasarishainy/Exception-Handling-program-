try:
    n=int(input())
    d=int(input())   
    r=n+d
    print(r)
except ZeroDivisionError:
    print("zeroDivisionError")
except ValueError:
    print("ValueError Error occured")
except:
    print("Unknown Errors")
else:
    print("else block executed only when no error")
finally:
    print("Finally Block Executed always")
