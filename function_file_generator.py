import sys
import os


def generate_file_with_same_function_name(path, name):
    # read file
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    joinable_path = f'{path}/{name}'
    file_name = os.path.join(fileDir, joinable_path)
    fo = open(file_name, "wb")

    # write to file
    function_name = name.split('.')[0]
    content = f"def {function_name}():\n\treturn 0\nif __name__ == \"__main__\":\n\tprint(\"start {function_name}.......\")"
    content_bytes = content.encode(encoding='UTF-8')
    fo.write(content_bytes)

    fo.close()


if __name__ == "__main__":
    folder_path = sys.argv[1]
    name = sys.argv[2]
    generate_file_with_same_function_name(folder_path, name)
