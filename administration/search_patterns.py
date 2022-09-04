from itertools import chain
from home.models import Doctor, Patient


def one_word_even(pattern: str) -> dict:
    if pattern[-1] in ('ж', "м"):
        sex = 'f' if pattern[-1] == 'ж' else 'm'
        pattern = pattern[:-1] + sex
    
    l = list(pattern)
    contextP = Patient.objects.filter(first_name__startswith=l[0],
                                    last_name__startswith=l[1])
    contextD = Doctor.objects.filter(first_name__startswith=l[0],
                                    last_name__startswith=l[1])
    
    if len(l) >= 3:
        contextP = contextP.filter(father_name__startswith=l[2])
        contextD = contextD.filter(father_name__startswith=l[2])
    
    # match len(l):
    #     case 4:
    #         contextP = contextP.filter(gender__startswith=l[3])
    #         contextD = contextD.filter(gender__startswith=l[3])
    #     case 6:
    #         contextP = contextP.filter(date_of_birth__year=int(''.join(l[3:5])),
    #                                 gender__startswith=l[5])
    #         contextD = contextD.filter(date_of_birth__year=int(''.join(l[3:5])),
    #                                 gender__startswith=l[5])
    #     case 8:
    #         contextP = contextP.filter(date_of_birth__month=int(''.join(l[3:5])),
    #                                 date_of_birth__year=int(''.join(l[5:7])),
    #                                 gender__startswith=l[7])
    #         contextD = contextD.filter(date_of_birth__month=int(''.join(l[3:5])),
    #                                 date_of_birth__year=int(''.join(l[5:7])),
    #                                 gender__startswith=l[7])
    #     case 10:
    #         contextP = contextP.filter(date_of_birth__day=int(''.join(l[3:5])),
    #                                 date_of_birth__month=int(''.join(l[5:7])),
    #                                 date_of_birth__year=int(''.join(l[7:9])),
    #                                 gender__startswith=l[9])
    #         contextD = contextD.filter(date_of_birth__day=int(''.join(l[3:5])),
    #                                 date_of_birth__month=int(''.join(l[5:7])),
    #                                 date_of_birth__year=int(''.join(l[7:9])),
    #                                 gender__startswith=l[9])
    context = chain(contextP, contextD)
    return { 'users': context }


def one_word_odd(pattern: str) -> dict:
    l = list(pattern)
    contextP = Patient.objects.filter(first_name__startswith=l[0],
                                    last_name__startswith=l[1])
    contextD = Doctor.objects.filter(first_name__startswith=l[0],
                                    last_name__startswith=l[1])
    
    match len(l):
        case 3:
            contextP = contextP.filter(father_name__startswith=l[2])
            contextD = contextD.filter(father_name__startswith=l[2])
        # case 5:
        #     contextP = contextP.filter(date_of_birth__year=int(''.join(l[2:4])),
        #                             gender__startswith=l[4])
        #     contextD = contextD.filter(date_of_birth__year=int(''.join(l[2:4])),
        #                             gender__startswith=l[4])
        # case 7:
        #     contextP = contextP.filter(date_of_birth__month=int(''.join(l[2:4])),
        #                             date_of_birth__year=int(''.join(l[4:6])),
        #                             gender__startswith=l[6])
        #     contextD = contextD.filter(date_of_birth__month=int(''.join(l[2:4])),
        #                             date_of_birth__year=int(''.join(l[4:6])),
        #                             gender__startswith=l[6])
        # case 9:
        #     contextP = contextP.filter(date_of_birth__day=int(''.join(l[2:4])),
        #                             date_of_birth__month=int(''.join(l[4:6])),
        #                             date_of_birth__year=int(''.join(l[6:8])),
        #                             gender__startswith=l[8])
        #     contextD = contextD.filter(date_of_birth__day=int(''.join(l[2:4])),
        #                             date_of_birth__month=int(''.join(l[4:6])),
        #                             date_of_birth__year=int(''.join(l[6:8])),
        #                             gender__startswith=l[8])
    context = chain(contextP, contextD)
    return { 'users': context }


def three_words(name: str, surname: str, fathername: str) -> dict:
    return { 'users': chain(Patient.objects.filter( first_name__startswith=name,
                                                    last_name__startswith=surname,
                                                    father_name__startswith=fathername),
                            Doctor.objects.filter( first_name__startswith=name,
                                                    last_name__startswith=surname,
                                                    father_name__startswith=fathername)) }


# def four_words(name: str, surname: str, fathername: str, pattern: str) -> dict:
#     if pattern[-1] in ('ж', "м"):
#         sex = 'f' if pattern[-1] == 'ж' else 'm'
#         pattern = pattern[:-1] + sex
    
#     contextP = Patient.objects.filter(first_name__startswith=name,
#                                     last_name__startswith=surname,
#                                     father_name__startswith=fathername)
#     contextD = Doctor.objects.filter(first_name__startswith=name,
#                                     last_name__startswith=surname,
#                                     father_name__startswith=fathername)
#     l = pattern.split()
#     match len(l):
#         case 2:
#             contextP = contextP.filter(date_of_birth__year=int(''.join(l)))
#             contextD = contextD.filter(date_of_birth__year=int(''.join(l)))
#         case 3:
#             contextP = contextP.filter(date_of_birth__year=int(''.join(l[:2])),
#                                     gender__startswith=l[-1])
#             contextD = contextD.filter(date_of_birth__year=int(''.join(l[:2])),
#                                     gender__startswith=l[-1])
#         case 4:
#             contextP = contextP.filter(date_of_birth__month=int(''.join(l[:2])),
#                                     date_of_birth__year=int(''.join(l[2:4])))
#             contextD = contextD.filter(date_of_birth__month=int(''.join(l[:2])),
#                                     date_of_birth__year=int(''.join(l[2:4])))
#         case 5:
#             contextP = contextP.filter(date_of_birth__month=int(''.join(l[:2])),
#                                     date_of_birth__year=int(''.join(l[2:4])),
#                                     gender__startswith=l[-1])
#             contextD = contextD.filter(date_of_birth__month=int(''.join(l[:2])),
#                                     date_of_birth__year=int(''.join(l[2:4])),
#                                     gender__startswith=l[-1])
#         case 6:
#             contextP = contextP.filter(date_of_birth__day=int(''.join(l[:2])),
#                                     date_of_birth__month=int(''.join(l[2:4])),
#                                     date_of_birth__year=int(''.join(l[4:6])))
#             contextD = contextD.filter(date_of_birth__day=int(''.join(l[:2])),
#                                     date_of_birth__month=int(''.join(l[2:4])),
#                                     date_of_birth__year=int(''.join(l[4:6])))
#         case 7:
#             contextP = contextP.filter(date_of_birth__day=int(''.join(l[:2])),
#                                     date_of_birth__month=int(''.join(l[2:4])),
#                                     date_of_birth__year=int(''.join(l[4:6])),
#                                     gender__startswith=l[-1])
#             contextD = contextD.filter(date_of_birth__day=int(''.join(l[:2])),
#                                     date_of_birth__month=int(''.join(l[2:4])),
#                                     date_of_birth__year=int(''.join(l[4:6])),
#                                     gender__startswith=l[-1])
#     context = chain(contextP, contextD)
#     return { 'users': context }