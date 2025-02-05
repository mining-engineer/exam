import os

def list_files(startpath):
    with open('project_structure.txt', 'w') as f:
        for root, dirs, files in os.walk(startpath):
            # Исключаем папки venv и .git
            if 'venv' in root or '.git' in root or '__pycache__' in root or 'migrations' in root:
                continue
            
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write('{}{}\n'.format(subindent, file))

if __name__ == "__main__":
    project_path = os.path.dirname(os.path.abspath(__file__))  # Путь к текущему каталогу
    list_files(project_path)