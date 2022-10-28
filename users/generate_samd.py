from med_system.settings import BASE_DIR
import requests
import os

def medical_services_provision_referral():
    with open(os.path.join(BASE_DIR, 'users/samd/SMSV1.xml'), 'r', encoding='utf-8') as f:
        return (f.read(), requests.get('https://ips-test.rosminzdrav.ru/9d15f52ee7f2c?wsdl', verify=False))


def instrumental_research_protocol():
    with open(os.path.join(BASE_DIR, 'users/samd/SMSV2.xml'), 'r', encoding='utf-8') as f:
        return (f.read(), requests.get('https://ips-test.rosminzdrav.ru/9d15f52ee7f2c?wsdl', verify=False))


def laboratory_test_protocol():
    with open(os.path.join(BASE_DIR, 'users/samd/SMSV3.xml'), 'r', encoding='utf-8') as f:
        return (f.read(), requests.get('https://ips-test.rosminzdrav.ru/9d15f52ee7f2c?wsdl', verify=False))


def patient_examination_consultation():
    with open(os.path.join(BASE_DIR, 'users/samd/SMSV5.xml'), 'r', encoding='utf-8') as f:
        return (f.read(), requests.get('https://ips-test.rosminzdrav.ru/9d15f52ee7f2c?wsdl', verify=False))


def treatment_in_hospital():
    with open(os.path.join(BASE_DIR, 'users/samd/SMSV8.xml'), 'r', encoding='utf-8') as f:
        return (f.read(), requests.get('https://ips-test.rosminzdrav.ru/9d15f52ee7f2c?wsdl', verify=False))


def maternity_hospital_discharge_epicrisis():
    with open(os.path.join(BASE_DIR, 'users/samd/SMSV17.xml'), 'r', encoding='utf-8') as f:
        return (f.read(), requests.get('https://ips-test.rosminzdrav.ru/9d15f52ee7f2c?wsdl', verify=False))


def cytological_examination_protocol():
    with open(os.path.join(BASE_DIR, 'users/samd/SMSV5.xml'), 'r', encoding='utf-8') as f:
        return (f.read(), requests.get('https://ips-test.rosminzdrav.ru/9d15f52ee7f2c?wsdl', verify=False))


def medical_death_certificate():
    with open(os.path.join(BASE_DIR, 'users/samd/SampleCDADocumentRuMedSertOfDeath_adult_max.xml'), 'r', encoding='utf-8') as f:
        return (f.read(), requests.get('https://ips-test.rosminzdrav.ru/9d15f52ee7f2c?wsdl', verify=False))


def medical_perinatal_death_certificate():
    with open(os.path.join(BASE_DIR, 'users/samd/SampleCDADocumentRuMedSertOfPerinatalDeath.xml'), 'r', encoding='utf-8') as f:
        return (f.read(), requests.get('https://ips-test.rosminzdrav.ru/9d15f52ee7f2c?wsdl', verify=False))
