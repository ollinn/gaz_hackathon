from db_interface import get_departments_tree
from functions.print_functions import print_tree

if __name__ == '__main__':
    print_tree(get_departments_tree())
