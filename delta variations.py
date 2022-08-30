n = int(input())
system = []
child_list = [] # first name per line
parent_list = [] # second name per line
parent_list_copy = []
obj = {}
versions = []

def is_ancestor(a, b, ver_num):
    t_state = versions[ver_num]
    
    if a == b:
        return True
    
    parent_a = t_state.parent[t_state.child.index(a)]
    if type parent_a == None:
        return False
    
    if parent_a == b:
        return True
    
    return is_ancestor(parent_a, b, ver_num)

for i in range(n):
    r = input().split()
    child_list[i] = r[0]
    parent_list[i] = r[1]
    parent_list_copy[i] = parent_list[i]

versions[0] = {
    "child": [*child_list],
    "parent": [*parent_list]
}

e = int(input())
 
for j in range(e):
    s = input().split()
    # make copies of the list
    # record
    parent_list_copy[j] = s[1]
    parent_list[child_list.index(s[0])] = s[1]
    versions.push({
        "child": [*child_list],
        "parent": [*parent_list]
    })

q = int(input())
for k in range(q):
    q_list = input().split()
    question = is_ancestor(q_list[1], q_list[2], int(q_list[0]))
    if (question == True):
        print("Yes")
    else:
        print("No")