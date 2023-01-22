S = input()

# CAUTION: order of replaced
replaced = S.replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")
if replaced:
    print("NO")
else:
    print("YES")
