# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
physical_exam = {
    "Constitutional": {
        "id": "peconst",
        "components": {
            "Vitals": {
                "id": "peconstvitals",
                },
            "General Appearance": {
                "id": "peconstgenapp",
                },
            },
        },
    "HEENT": {
        "id": "peHEENT",
        "components": {},
        },
    "Respiratory": {
        "id": "peresp",
        "components": {},
        },
    "Cardiovascular": {
        "id": "pecardio",
        "components": {},
        },
    "Gastrointestinal": {
        "id": "pegi",
        "components": {},
        },
    "Genitourinary": {
        "id": "pegu",
        "components": {},
        },
    "Dermatologic": {
        "id": "pederm",
        "components": {},
        },
    "Musculoskelatal": {
        "id": "pemsk",
        "components": {},
        },
    "Neurological": {
        "id": "peneuro",
        "components": {
            "Mental Status": {
                "id": "peneuroms",
                "Orientation": {},
                "Three-Level Command": {},
                "SLUMS": {},
                },
            "Cranial Nerves": {
                "id": "peneurocn",
                },
            "Motor": {
                "id": "peneuromotor",
                "Upper Extremity Strength": {},
                "Lower Extremity Strength": {},
                },
            "Sensory": {
                "id": "peneurosensory",
                "Upper Extremity Sensation": {},
                "Lower Extremity Sensation": {},
                },
            "Reflexes": {
                "id": "peneuroreflex",
                "Upper Extremity Reflexes": {},
                "Lower Extremity Reflexes": {},
                "Other Reflexes": {},
                },
            "Cerebellar": {
                "id": "peneurocerebellar",
                "Gait": {},
                "Balance": {},
                "Tremors": {},
                "Finger-to-Nose": {},
                },
            },
        },
    "Psychiatric": {
        "id": "pepsych",
        "components": {},
        }
    }


quick_output = ""
section_template = f"""\n`?+_%s="%s" """

for key, item in physical_exam.items():
    line = section_template % (item['id'], key)
    quick_output = quick_output + line
    if "components" in item:
        for key2, item2 in item['components'].items():
            line = section_template % (item2['id'], key2)
            quick_output = quick_output + line + " `_? "
    quick_output = quick_output + " `_? "

print(quick_output)

