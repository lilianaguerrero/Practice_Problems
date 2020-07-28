# Enter your code here. Read input from STDIN. Print output to STDOUT
status = "ok"
def guard_check():
    global status
    matrix = input()
    items = matrix.split(" ")
    m = int(items[0])
    n = int(items[1])
    
    matrix_copy = [input() for _ in range(n-1)]
    guards = []
    walls = []
    for line in matrix_copy:
        if line[-1] == "g":
            guard_coord = line[:-2].split(" ") 
            guard_coord = map(int, guard_coord)
            guards.append(list(guard_coord))
        if line[-1] == "w":
            wall_coord = line[:-2].split(" ") 
            wall_coord = map(int, wall_coord)
            walls.append(list(wall_coord))
    
    unguarded_rooms = []
    for i in range(m):
        for j in range(n):
            unguarded_rooms.append([i,j])
    for i in range(len(walls)):
        mwall, nwall = walls[i][0], walls[i][1] 
        if [mwall,nwall] in unguarded_rooms:
            unguarded_rooms.remove([mwall,nwall])
    for i in range(len(guards)):
        mguard, nguard = guards[i][0], guards[i][1] 
        if [mguard,nguard] in unguarded_rooms:
            unguarded_rooms.remove([mguard,nguard])
    
    def point_check(m_point,n_point):
        if [m_point,n_point] in unguarded_rooms:
            unguarded_rooms.remove([m_point,n_point])
        if [m_point,n_point] in walls:
            global status
            status = "break_loop"   
    for guard in guards:
        m_point_org = guard[0]
        n_point_org = guard[1]
        m_point = m_point_org
        n_point = n_point_org
        for m_increment in range(m-m_point_org):
            m_point += 1
            point_check(m_point,n_point)
            if status == "break_loop":
                status = "ok"
                break
        m_point = m_point_org
        for m_increment in range(m_point_org):
            m_point -= 1
            point_check(m_point,n_point)
            if status == "break_loop":
                status = "ok"
                break
        m_point = m_point_org
        for n_increment in range(n-n_point_org):
            n_point += 1
            point_check(m_point,n_point)
            if status == "break_loop":
                status = "ok"
                break
        n_point = n_point_org
        for n_increment in range(n_point_org):
            n_point -= 1
            point_check(m_point,n_point)
            if status == "break_loop":
                status = "ok"
                break
        n_point = n_point_org
    if len(unguarded_rooms) > 0:
        print('false')
        for array in unguarded_rooms:
            print(array[0],array[1])
guard_check()