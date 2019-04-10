from typing import Union
import us


def build_acs_url(year: Union[int, str] = '2017', 
                 survey: Union[str, int] = '1-Year', 
                 person_or_household: str = 'person',
                 state: str = 'California',
                 ):
    """
    Builds CENSUS FTP-server URL where you can download ACS 1-, 3-, or 5- year estimates. 
    """
    
    # Building URL
    BASE_URL = "https://www2.census.gov/programs-surveys/acs/data/pums/"
    
    ## YEAR 
    try:
        year = int(year)
    except ValueError:
        raise ValueError('year must be a number.')
        
    if ((0 <= year) & (year <= 17)):
        year += 2000
    
    if not ((2000 <= year) & (year <= 2017)):
        raise ValueError("Year must be between 2000 and 2017.")
    
    ## SURVEY
    if type(survey) == str:
        survey = survey.title()
    ####### TO DO ########
    # make sure that it's either 1-Year
    # or for certain years 3- or 5- year
    
    ### IF YEAR < 2007 there is no option to choose 1- 3- or 5- year surveys
    if year < 2007:
        survey = ''
    
    ## PERSON OR HOUSEHOLD
    person_or_household = person_or_household.lower()
    
    if ((person_or_household == 'person') or (person_or_household == 'household')):
        person_or_household = person_or_household[0]
        
    ## STATE
    if us.states.lookup(state) is not None:
        state_abbr = us.states.lookup(state).abbr.lower()
        
    
    ## URL
    YEAR_URL = f'{str(year)}/'
    SURVEY_URL = f"{survey}/" if survey else ""
    STATE_URL = f'csv_{person_or_household}{state_abbr}.zip'
    
    
    FINAL_URL = BASE_URL + YEAR_URL + SURVEY_URL + STATE_URL
    
    #
    return FINAL_URL