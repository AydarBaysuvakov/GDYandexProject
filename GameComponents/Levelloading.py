def load_level(filename):
    filename = "data/" + filename
    level = {}
    with open(filename, 'r') as mapFile:
        level['Background'] = mapFile.readline().rstrip().split(' / ')[1:]
        obj = mapFile.readlines()
        if obj[0].startswith('Map_size'):
            params = obj[0].rstrip().split(' / ')[1]
            level['Map_size'] = map(int, params.split(', '))
        for line in obj:
            objects = line.rstrip().split(' / ')
            object_type, params = objects[0], objects[1:]
            level[object_type] = []
            for object in params:
                level[object_type].append(map(int, object.split(', ')))
    return level