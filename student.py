class Student:

 
    def __init__(self, full_name, hometown, state, guests, major):
        # Talk to Tom, change these based on what they actually get for Majors
        BUSINESS = ['accounting','bachelor of business administration (management)', 'business (pre)', 'pre-business', 'business analytics and information systems', 'economics', 'economics: analytical', 'economics: business', 'economics: policy', 'enterprise leadership', 'entrepreneurial management', 'finance', 'international business', 'management', 'nonprofit management', 'risk management and insurance']
        CLAS = [ 'actuarial science', 'african american studies', 'aging and longevity studies', 'american indian and native studies', 'american sign language and deaf studies', 'american studies', 'ancient civilization', 'anthropology', 'applied physics', 'art', 'art history', 'arts entrepreneurship', 'asian languages and literature', 'astronomy', 'bachelor of applied studies', 'biochemistry', 'biology', 'chemistry', 'cinema', 'classical languages', 'communication studies', 'comparative literature', 'computer science', 'criminology, law and justice', 'critical cultural competence', 'dance', 'english', 'english and creative writing', 'environmental policy and planning', 'environmental sciences', 'french', 'fundraising and philanthropy communication', "gender, women's, and sexuality studies", 'geography', 'geoscience', 'german', 'history', 'informatics', 'interdepartmental studies', 'italian', 'journalism and mass communication', 'latin american studies', 'leadership studies', 'linguistics', 'mathematics: progam a', 'mathematics: program b', 'mathematics: program c', 'medieval studies', 'microbiology', 'mortuary science (pre)', 'museum studies', 'music', 'open major', 'philosophy', 'physics', 'portuguese', 'psychology', 'religious studies', 'russian', 'social justice', 'social work interest', 'sociology', 'spanish', 'sport studies', 'sport and recreation management', 'statistics', 'sustainability', 'technological entrepreneurship', 'theatre arts', 'wind energy']
        EDUCATION = ['education', 'elementary education', 'elementary education interest', 'science education', 'secondary education interest']
        ENGINEERING = ['biomedical engineering', 'chemical engineering', 'chemical engineering: oil and gas engineering', 'civil engineering', 'computer science and engineering', 'electrical engineering', 'engineering', 'industrial engineering', 'mechanical engineering']
        HEALTH = ['chiropractic (pre)', 'pre-chiropractic', 'dentistry (pre)', 'prer-dentistry','disability studies', 'global health studies', 'health and human physiology: health promotion', 'human physiology', 'leisure studies (therapeutic recreation)', 'medical laboratory science', 'medicine (pre)', 'pre-medicine', 'neuroscience', 'nuclear medicine technology', 'nuclear medicine technology interest', 'nursing', 'nursing (rn-bsn program for currently licensed nurses)', 'occupational therapy (pre)', 'pre-occupational therapy', 'optometry (pre)', 'pre-optometry', 'pharmacy (pre)', 'pre-pharmacy', 'physical therapy (pre)', 'pre-physical therapy', 'physician assistant (pre)', 'pre-physician assistant', 'podiatric medicine (pre)', 'pre-podiatric medicine', 'public health', 'public health interest', 'radiation sciences', 'radiation sciences interest', 'speech and hearing science', 'threrapeutic recreation interest', 'veterinary medicine (pre)', 'pre-veterinary medicine']
        LAW = ['ethics and public policy', 'human rights', 'international relations', 'international studies', 'international studies: international human rights', 'law (pre)', 'pre-law', 'political science']
        
        self.full_name = full_name
        self.hometown = hometown.title()
        self.state = state.upper()
        self.guests = int(guests)
        self.major = major.lower()
        self.group = 0
        self.area = "CLAS"
        self.total_people = int(guests) + 1
        self.local = (self.state == 'IA') or (self.state == 'IL')

        if self.major in BUSINESS:
            self.area = "Business"
        elif self.major in EDUCATION:
            self.area = "Education"
        elif self.major in ENGINEERING:
            self.area = "Engineering"
        elif self.major in HEALTH:
            self.area = "Health"
        elif self.major in LAW:
            self.area = "Law"

    def __str__(self):
        return self.full_name + ", " + self.area + ", " + self.state
    def __repr__(self):
        return self.full_name + ", " + self.area + ", " + self.state
