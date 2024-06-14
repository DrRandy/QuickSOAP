"""
Generate the default structure of a progress note
"""


meta_data_definition = {
	'last name'	: "`@lastname",
	'first name'	: "`@firstname",
	'date of birth'		: "`@dob",
	'date of visit'		: "`@dov",
	'employee ID number'		: "`@eid",
	'job'		: "`@job",
	'location'	: "`@location",
	'start date'	: "`@startdate",
	'employer'	: "`@employer",
# 	'lastname'	: "`@lastname",
# 	'lastname'	: "`@lastname",
# 	'lastname'	: "`@lastname",
# 	'lastname'	: "`@lastname",
# 	'lastname'	: "`@lastname",
# 	'lastname'	: "`@lastname",
# 	'lastname'	: "`@lastname",
# 	'lastname'	: "`@lastname",
}

quick_neck_exam = """Neck Inspection: `^neckScar="not examined|no scar|scar noted" `?_neckScar:"(neckScar).is('scar noted')" `@ `_?
Neck ROM: `^neckROM="FROM|decreased ROM" `?_neckROM:"(neckROM).isNot('FROM')"
turning right: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" 
turning left: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" 
tilting right: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" 
tilting left: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" 
extension: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" 
flexion: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" `_?
Neck Tenderness: `^neckTenderness="not tested|no tenderness|tenderness is noted" `?_neckTenderness:"(neckTenderness).is('tenderness is noted')" `@ `_?
Neck Spasm: `^neckSpasm="not tested|no spasm|spasm is noted" `?_neckSpasm:"(neckSpasm).is('spasm is noted')" `^="| on the right| on the left| bilaterally" `_?
"""

quick_back_exam = """Back Inspection: `^backScar="not examined|no scar|scar noted" `?_backScar:"(backScar).is('scar noted')" `@ `_?
Back ROM: `^backROM="FROM|decreased ROM" `?_backROM:"(backROM).isNot('FROM')"
turning right: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" 
turning left: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" 
tilting right: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" 
tilting left: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" 
extension: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" 
flexion: `^="|slightly decreased|moderately decreased|markedly decreased" `^="|exacerbates pain|ameliorates pain" `_?
Back Tenderness: `^backTenderness="not tested|no tenderness|tenderness is noted" `?_backTenderness:"(backTenderness).is('tenderness is noted')" `@ `_?
Back Spasm: `^backSpasm="not tested|no spasm|spasm is noted" `?_backSpasm:"(backSpasm).is('spasm is noted')" `^="| on the right| on the left| bilaterally" `@ `_?
Straight Leg Raise: `^straightLegRaise="not tested|normal bilaterally|abnormal: " `?_straightLegRaise:"(straightLegRaise).is('abnormal: ')" 
Right side is `^="normal|negative but reproduces pain|not tolerated due to pain" `@ 
Left side is `^="normal|negative but reproduces pain|not tolerated due to pain" `@ `_?
"""

quick_neuro_exam = """`?+_showUpperExt="Upper Extremities"
Reflexes (biceps, brachioradialis) `^="not tested|1+ and symmetrical bilaterally|2+ and symmetrical bilaterally|3+ and symmetrical bilaterally|asymmetric" `@ 
Strength (all major muscle groups, hand grip, digital opposition)`^="not tested|5/5 bilaterally|abnormal" `@ `_?`?+_showLowerExt="Lower Extremities"
Reflexes (KJ, AJ) `^="not tested|1+ and symmetrical bilaterally|2+ and symmetrical bilaterally|3+ and symmetrical bilaterally|asymmetric" `@ 
Strength (all major muscle groups)`^="not tested|5/5 bilaterally|abnormal" `@ `_?`?+_showGait="Gait" `^gait="normal|abnormal" `?_gait:"(gait).is('abnormal')"`+="antalgic favoring right|antalgic favoring left|wide-based|shuffling" `@  `_? `_?
"""

physical_exam_definition = {
		"Vitals": """`@="Height   Weight   " """,
		"General Appearance": """[textarea fillable="true"]Employee is a ******comfortable-appearing ****** sitting up ******in no apparent distress; changes position (sitting/standing/lying/mounting-dismounting exam table) ******without difficulty or assistance.[/textarea]
""",
		"HEENT": {
		},
		"Neck": quick_neck_exam,			
		"Back": quick_back_exam,
		"Neuro": quick_neuro_exam,
	}

workers_comp_definition = {
	"Workers Comp Initial Visit": {
		"Subjective": {
			"History of the Present Illness": {
			},
		},
		"Objective": physical_exam_definition,
		"Assessment": {
			"Diagnoses": {
			},
			"Discussion": {
			},
		},
		"Plan": {
			"Return to Work": {
			},
			"Treatment": {
			},
			"Referrals": {
			},
			"Follow-up": {
			},
		},
	}
}


def generate_note(note_definition):
	result = ""
	result = generate_metadata()
	for key, value in note_definition.items():
		result = result + generate_note_header()
		result = result + generate_title(key)
		for section_key, section_value in value.items():
			result = result + generate_section_header(section_key)
			if section_key == "Objective":
				result = result + generate_physical_exam(physical_exam_definition)
			else:
				for subsection_key, subsection_value in section_value.items():
					result = result + generate_subsection_header(subsection_key)
					result = result + "subsection content goes here\n\n"
			result = result + "\n\n"
	return result



def generate_metadata():
	result = ""
	result = generate_metadata_variables(meta_data_definition)
	result = result + generate_physical_exam_options(physical_exam_definition)
	return result


def generate_note_header():
	result = """`@lastname, `@firstname\nDOB: `@dob\nDOV: `@dov\n\n\n"""
	return result
	

def generate_title(title):
	result = "=========================\n%s\n=========================\n\n" 
	result = result % title.upper()
	return result


def generate_section_header(section_header):
	result = "---------------------\n%s\n---------------------\n" % section_header.upper()
	return result
	

def generate_subsection_header(subsection_header):
	result = "%s\n" % subsection_header.upper()
	return result


def generate_metadata_variables(metadata):
	result = "\n"
	for key, value in metadata.items():
		result = result + """%s = %s\n""" % (key, value)
	result = result + "\n"
	return result

def generate_physical_exam_options(physical_exam):
	result = "Choose which elements of the physical exam to include in this note:\n"
	for key, value in physical_exam.items():
		element_tag = "exam_" + key.replace(' ','')
		result = result + """%s    `+%s="include"\n""" % (key, element_tag)
	result = result + "\n"
	return result

def generate_physical_exam(physical_exam):
	result = ""
	for key, value in physical_exam.items():
		element_tag = "exam_" + key.replace(' ','')
		result = result + """`?_%s:"(%s).is('include')" \n%s%s\n`_?""" % \
			(element_tag, element_tag, generate_subsection_header(key), value)
	return result
		

print(generate_note(workers_comp_definition))




