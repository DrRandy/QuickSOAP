"""
Generate the default structure of a progress note
"""

def note():
    result = ""
    result = result + subjective_section()
    # result = result + objective_section()
    # result = result + assessment_section()
    # result = result + plan_section()
    return result

def subjective_section():
    result = section("SUBJECTIVE") 
    result = result + cc_subsection() + hpi_subsection() + subjective_optional_subsections()
    return result
