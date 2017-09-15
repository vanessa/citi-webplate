import argparse, sys, os

parser = argparse.ArgumentParser()

parser.add_argument('--PROJECT_DIR', help='This application root folder')
parser.add_argument('--USER_NAME', help='Current user\'s username')
parser.add_argument('--IP_ADDRESS', help='The IP address your droplet is running')

args = parser.parse_args()

args_dict = {}
args_dict['{{ PROJECT_DIR }}'] = args.PROJECT_DIR
args_dict['{{ USER_NAME }}'] = args.USER_NAME
args_dict['{{ IP_ADDRESS }}'] = args.IP_ADDRESS

file_mapping = {}
file_mapping['gunicorn-config'] = 'gunicorn_start'
file_mapping['project-dir'] = args.PROJECT_DIR
file_mapping['project-dir.conf'] = '{}.conf'.format(args.PROJECT_DIR)

for filename in file_mapping.keys():
    new_file = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        for pattern in args_dict.keys():
            line = line.replace(pattern, args_dict[pattern])
        new_file.append(line)

    with open(file_mapping[filename], 'w') as f:
        f.seek(0)
        f.writelines(new_file)
