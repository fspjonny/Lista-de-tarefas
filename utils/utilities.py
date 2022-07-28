import re
import unicodedata

from django.core.exceptions import ValidationError


def makeUsernameLowerCase(texto):
   removed_accents= unicodedata.normalize(
      'NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
   return removed_accents.replace(' ', "_",20).lower()



def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
    
    if not regex.match(password):
        raise ValidationError(
            ('A senha deve conter letras, números e caracteres'
            ' e ter um tamanho maior que 8 caracteres.'
            ),
            code='invalid',
        )
        
def correct_email(email):
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    )
    
    if not regex.match(email):
        return False
    return True
