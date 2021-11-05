from cerberus import Validator
inp_data={'name':{'type':'string'},
          'age':{'type':'integer','min':18,'max':65},
          'ssn':{'type':'string'},
          'phone number':{'type':'string'}
          }
v=Validator(inp_data)

document={'name':'vadim',
         'age':}
print(v.validate(document))
