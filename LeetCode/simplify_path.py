def simplifyPath(path: str) -> str:
        stack = []
        ans = path.split("/")
        for n in ans:
            if n == ".." and stack:
                stack.pop()
            elif n == "." or n == '':
                continue
            elif n != "..":
                stack.append(n)
        return "/" + "/".join(stack)

# Example usage:
if __name__ == "__main__":
    path = "/a/./b/../../c/"
    print(simplifyPath(path))  # Output: "/c"
    path = "/home//foo/"
    print(simplifyPath(path))  # Output: "/home/foo"
    path = "/../"
    print(simplifyPath(path))  # Output: "/"
    path = "/a//b////c/d//././/.."
    print(simplifyPath(path))  # Output: "/a/b/c"