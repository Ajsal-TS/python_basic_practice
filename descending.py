def funct(s:list[str],lists=[]): 
    # [lists.append(i.casefold()) for i in s]
    # lists.sort(reverse=True)
    return sorted([i.casefold() for i in s])

print(funct(["Aasjd","AHDasdf","hsdJSDB","FXEsdgdh"]))
