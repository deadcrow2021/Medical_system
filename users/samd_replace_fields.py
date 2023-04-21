from base64 import b64encode


def generate_samd(samd_text, patient_obj):
    replace_tags = (('{% passport_series %}', str(patient_obj.card.series_number_pass)[:4] if patient_obj.card.series_number_pass else ''),
                    ('{% passport_number %}', str(patient_obj.card.series_number_pass)[4:] if patient_obj.card.series_number_pass else ''),
                    ('{% IssueOrgName %}', patient_obj.card.when_whom_issued if patient_obj.card.when_whom_issued else ''),
                    ('{% IssueOrgCode %}', ''),
                    ('{% oms_series %}', ''),
                    ('{% oms_number %}', patient_obj.card.oms_policy if patient_obj.card.oms_policy else ''),
                    ('{% residence_address %}', patient_obj.card.residence_address if patient_obj.card.residence_address else ''),
                    ('{% work_phone %}', patient_obj.card.work_phone if patient_obj.card.work_phone else ''),
                    ('{% mobile_phone %}', str(patient_obj.card.mobile_phone) if patient_obj.card.mobile_phone else ''),
                    ('{% email %}', patient_obj.email if patient_obj.email else ''),
                    ('{% last_name %}', patient_obj.last_name if patient_obj.last_name else ''),
                    ('{% first_name %}', patient_obj.first_name if patient_obj.first_name else ''),
                    ('{% Father_name %}', patient_obj.father_name if patient_obj.father_name else ''),
                    ('{% birth_date %}', patient_obj.card.date_of_birth.strftime('%m/%d/%Y') if patient_obj.card.date_of_birth else ''),
                    ('{% reception_code %}', ''),
                    ('\t', '....'))
    
    for tag in replace_tags:
        try:
            samd_text = samd_text.replace(tag[0], tag[1])
        except:
            samd_text = samd_text.replace(tag[0], '')
            
    return samd_text


def encode_samd(samd_text):
    samd_text = f'{samd_text}'.encode()
    gfg = b64encode(samd_text)
    return gfg.decode('utf-8')
