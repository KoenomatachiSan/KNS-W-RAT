from flask import Flask, request, jsonify
import os
########################
# Import Modules
########################
from src.modules.database.database_module import check_database_kns


app = Flask(__name__)

@app.route('/order', methods=['GET'])
def order():
    return {
        "keep_alive":True
    }

@app.route('/keep_alive', methods=['POST'])
def keep_alive():
    result = request.get_json()
    return result

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