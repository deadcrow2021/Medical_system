from itertools import chain
from home.models import Doctor, Patient


def one_word_even(pattern: str) -> dict:
    return { 'users': chain(Patient.objects.filter(), Doctor.objects.filter()) }


def one_word_odd(pattern: str) -> dict:
    pass


def three_words(name: str, surname: str, fathername: str) -> dict:
    return { 'users': chain(Patient.objects.filter( first_name__startswith=name,
                                                    last_name__startswith=surname,
                                                    father_name__startswith=fathername),
                            Doctor.objects.filter(  first_name__startswith=name,
                                                    last_name__startswith=surname,
                                                    father_name__startswith=fathername)) }


def four_words(name: str, surname: str, fathername: str, pattern: str) -> dict:
    
    return { 'users': chain(Patient.objects.filter( first_name__startswith=name,
                                                    last_name__startswith=surname,
                                                    father_name__startswith=fathername),
                            Doctor.objects.filter(  first_name__startswith=name,
                                                    last_name__startswith=surname,
                                                    father_name__startswith=fathername)) }
