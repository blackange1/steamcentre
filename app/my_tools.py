def save_file(f, name, root=''):
    if '.' in f.name:
        type_file = f.name.split('.')[-1]
        path = 'app/static/upload/' + root + name + '.' + type_file
        with open(path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return type_file
