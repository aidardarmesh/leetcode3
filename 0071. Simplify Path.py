def simplifyPath(path):
    path = [str_ for str_ in path.split('/') if str_]
    stack = []

    for dir_ in path:
        if dir_ == "..":
            if stack:
                stack.pop()
            else:
                continue
        elif dir_ == ".":
            continue
        else:
            stack.append(dir_)
    
    return '/' + '/'.join(stack)

path = "/home/"
print(simplifyPath(path))

path = "/home//foo/"
print(simplifyPath(path))

path = "/home/user/Documents/../Pictures"
print(simplifyPath(path))

path = "/../"
print(simplifyPath(path))

path = "/.../a/../b/c/../d/./"
print(simplifyPath(path))

