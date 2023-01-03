def load_level(filename):
    filename = "Data/" + filename
    level = {}
    with open(filename, 'r') as mapFile:
        level['Background'] = mapFile.readline().rstrip().split(' / ')[1:]
        for line in mapFile.readlines():
            objects = line.rstrip().split(' / ')
            object_type, params = objects[0], objects[1:]
            if object_type == 'Map_size':
                level['Map_size'] = list(map(int, params[0].split(', ')))
            elif object_type == 'Player':
                level['Player'] = list(map(int, params[0].split(', ')))
            else:
                level[object_type] = []
                for object in params:
                    level[object_type].append(list(map(int, object.split(', '))))
    return level