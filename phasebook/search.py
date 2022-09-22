from contextlib import nullcontext
from types import NoneType
from flask import Blueprint, request

from .data.search_data import USERS

from flask import request


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200




def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    if len(args) == 0:
        return USERS

    id = request.args.get('id', default='0', type=str)

    name = request.args.get('name', default='0', type=str)

    age = request.args.get('age', default='0', type=str)

    occupation = request.args.get('occupation', default='0', type=str)



    id2 = [i for i in USERS if i['id'] == id]

    name2 = [n for n in USERS if name in n['name']]

    age2 = [a for a in USERS if a['age'] == int(age)or a['age'] == int(age) - 1 or a['age'] == int(age) + 1]

    occupation2 = [o for o in USERS if occupation in o['occupation']]


    
    final = id2 + name2 + age2 + occupation2
    
    final2 = []


    for f in range(len(final)):
        if final[f] not in final[f + 1:]:
            final2.append(final[f])

    return sorted(final2, key=lambda d: d['id'])  


    # Bonus Challenge

    # return final2 
    
    


    




    
