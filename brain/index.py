from flask import Flask, request, jsonify
from prettytable import PrettyTable
import logging
import os


########################
# Import Modules
########################
from src.modules.database.database_module import check_database_kns
from src.modules.arms.create import create_arm
from src.modules.arms.list import list_arm


app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/order', methods=['GET'])
def order():
    return {
        "keep_alive":True
    }

@app.route('/keep_alive', methods=['POST'])
def keep_alive():
    result = request.get_json()
    return result

@app.route('/arms', methods=['POST'])
def arms():
    try:
        create_arm(request.get_json())
        homePanel()
        return {
        "sucess":True
        }
    except NameError:
        return NameError


def homePanel():
    os.system("clear")
    print(""" 
\033[32m============================================================================ \033[0m
    \033[31m _  ___   _ ____    ____      _  _____ 
    \033[31m| |/ / \ | / ___|  |  _ \    / \|_   _|
    \033[31m| ' /|  \| \___ \  | |_) |  / _ \ | |  
    \033[31m| . \| |\  |___) | |  _ <  / ___ \| |  
    \033[31m|_|\_\_| \_|____/  |_| \_\/_/   \_\_|  \033[0m developed by: \033[31mKoenomatachi San \033[0m

\033[32m============================================================================ \033[0m
    """)
    data_source_arms = list_arm()
    table = PrettyTable(['Name', 'Description', 'Created At'],)
    for arm in data_source_arms:
        table.add_row([arm['name'], arm['description'], arm['created_at']])
    print(table)


if __name__ == '__main__':
    os.system("clear")
    print(""" 
    \033[32m============================================================================ \033[0m
        \033[31m _  ___   _ ____    ____      _  _____ 
        \033[31m| |/ / \ | / ___|  |  _ \    / \|_   _|
        \033[31m| ' /|  \| \___ \  | |_) |  / _ \ | |  
        \033[31m| . \| |\  |___) | |  _ <  / ___ \| |  
        \033[31m|_|\_\_| \_|____/  |_| \_\/_/   \_\_|  \033[0m developed by: \033[31mKoenomatachi San \033[0m

    \033[32m============================================================================ \033[0m
    """)
    print('--> Verify Database integrity : ', end="")
    try:
        check_database_kns()
        print('\033[32m[SUCCESS]\033[0m')
    except:
        print('\033[31m[ERROR]\033[0m')
    app.run(host='0.0.0.0', port=5000, debug=True)