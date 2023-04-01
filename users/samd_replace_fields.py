from base64 import b64encode


def generate_samd(samd_text, patient_obj):
    try:
        samd_text = (samd_text.replace('{% passport_series %}', patient_obj.card.series_number_pass[:4] if patient_obj.card.series_number_pass else '')
                            .replace('{% passport_number %}', patient_obj.card.series_number_pass[4:] if patient_obj.card.series_number_pass else '')
                            .replace('{% IssueOrgName %}', patient_obj.card.when_whom_issued if patient_obj.card.when_whom_issued else '')
                            .replace('{% IssueOrgCode %}', '')
                            .replace('{% oms_series %}', '')
                            .replace('{% oms_number %}', patient_obj.card.oms_policy if patient_obj.card.oms_policy else '')
                            .replace('{% residence_address %}', patient_obj.card.residence_address if patient_obj.card.residence_address else '')
                            .replace('{% work_phone %}', patient_obj.card.work_phone if patient_obj.card.work_phone else '')
                            .replace('{% mobile_phone %}', str(patient_obj.card.mobile_phone) if patient_obj.card.mobile_phone else '')
                            .replace('{% email %}', patient_obj.email if patient_obj.email else '')
                            .replace('{% last_name %}', patient_obj.last_name if patient_obj.last_name else '')
                            .replace('{% first_name %}', patient_obj.first_name if patient_obj.first_name else '')
                            .replace('{% Father_name %}', patient_obj.father_name if patient_obj.father_name else '')
                            .replace('{% birth_date %}', patient_obj.card.date_of_birth.strftime('%m/%d/%Y') if patient_obj.card.date_of_birth else '')
                            .replace('{% reception_code %}', '')
                            .replace('\t', '....'))
    except:
        samd_text = (samd_text.replace('{% passport_series %}', '')
                            .replace('{% passport_number %}', '')
                            .replace('{% IssueOrgName %}', '')
                            .replace('{% IssueOrgCode %}', '')
                            .replace('{% oms_series %}', '')
                            .replace('{% oms_number %}', '')
                            .replace('{% residence_address %}', '')
                            .replace('{% work_phone %}', '')
                            .replace('{% mobile_phone %}', '')
                            .replace('{% email %}', '')
                            .replace('{% last_name %}', '')
                            .replace('{% first_name %}', '')
                            .replace('{% Father_name %}', '')
                            .replace('{% birth_date %}', '')
                            .replace('{% reception_code %}', '')
                            .replace('\t', '....'))
    return samd_text


def encode_samd(samd_text):
    samd_text = f'{samd_text}'.encode()
    gfg = b64encode(samd_text)
    return gfg.decode('utf-8')
