import os
import json

# copy
os.system('cp -r ../course_3.0_with_solutions/* ./')

# clear output, answers
for (dir, _, files) in os.walk("./"):
    for f in files:
        path = os.path.join(dir, f)
        if '.ipynb' not in path:
            continue
        # output cells
        os.system(f'jupyter nbconvert --clear-output --inplace {path}')
        # cells following "Show / Hide" markdown
        with open(path, 'r') as fp:
            jobj = json.loads(fp.read())
        for icell, cell in enumerate(jobj['cells']):
            if cell['cell_type'] == 'markdown' and 'Show / Hide' in ''.join(cell['source']):
                next_cell = jobj['cells'][icell + 1]
                assert next_cell['cell_type'] == 'code'
                next_cell['source'] = []
                print(f'Cleared an answer in {path}')
        with open(path, 'w') as fp:
            fp.write(json.dumps(jobj))
