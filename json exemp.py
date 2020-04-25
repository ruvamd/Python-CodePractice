import json

person_dict={'first':'chris','second':'harr'}
person_dict['city']='seattle'

languages_list=['csharp','python','js']

person_dict['language']=languages_list
person_json=json.dumps(person_dict)  