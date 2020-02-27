'''
Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
'''

def group_by_owners(files):
    di = dict()
    for key, value in files.items():
        if value not in di.keys():
            di.setdefault(value,[key])
        else:
            fnames = []
            fnames.append(key)
            for i in range(len(di[value])):
                fnames.append(di[value][i])
            di.update([[value,fnames]])
    return di

if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy',
        'test.py':'Randy'
    }
    print(group_by_owners(files))
