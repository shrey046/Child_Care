from experta import *

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
    global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    for disease in diseases_list:
        disease_s_file = open("Disease Symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        disease_s_file = open("Disease Descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        disease_s_file = open("Disease Treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()

def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)
    # Handle key error
    return symptom_map[str(symptom_list)]

def get_details(disease):
    return d_desc_map[disease]

def get_treatments(disease):
    return d_treatment_map[disease]

def if_not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("")
    print("The most probable disease that you have is %s\n" %(id_disease))
    print("A short description of the disease is given below :\n")
    print(disease_details+"\n")
    print("The common medications and procedures suggested by other real doctors are: \n")
    print(treatments+"\n")

class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("")
        print("Hi! I am Dr.Stone, I am here to help you make your health better.")
        print("For that you'll have to answer a few questions about your conditions")
        print("Do you feel any of the following symptoms:")
        print("")
        yield Fact(action="find_disease")

    @Rule(Fact(action='find_disease'),NOT(Fact(pain_in_throat = W())),salience = 1)
    def symptom_0(self):
        self.declare(Fact(pain_in_throat=input("Pain in Throat: ")))

    @Rule(Fact(action='find_disease'),NOT(Fact(cold = W())),salience = 1)
    def symptom_1(self):
        self.declare(Fact(cold=input("Cold: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(fever = W())),salience = 1)
    def symptom_2(self):
        self.declare(Fact(fever=input("Fever: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(cough = W())),salience = 1)
    def symptom_3(self):
        self.declare(Fact(cough=input("Cough: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(burning_micturation = W())),salience = 1)
    def symptom_4(self):
        self.declare(Fact(burning_micturation=input("Burning Micturation: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(abdominal_pain = W())),salience = 1)
    def symptom_5(self):
        self.declare(Fact(abdominal_pain=input("Abdominal Pain: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(pain_in_ear = W())),salience = 1)
    def symptom_6(self):
        self.declare(Fact(pain_in_ear=input("Pain in Ear: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(headache = W())),salience = 1)
    def symptom_7(self):
        self.declare(Fact(headache=input("Headache: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(loose_motion = W())),salience = 1)
    def symptom_8(self):
        self.declare(Fact(loose_motion=input("Loose Motion: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(vomiting = W())),salience = 1)
    def symptom_9(self):
        self.declare(Fact(vomiting=input("Vomiting: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(rashes_over_body = W())),salience = 1)
    def symptom_10(self):
        self.declare(Fact(rashes_over_body=input("Rashes over body with Eruptions: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(itching = W())),salience = 1)
    def symptom_11(self):
        self.declare(Fact(itching=input("Itching: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(redness_of_eye = W())),salience = 1)
    def symptom_12(self):
        self.declare(Fact(redness_of_eye=input("Redness of Eyes: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(burning_watering = W())),salience = 1)
    def symptom_13(self):
        self.declare(Fact(burning_watering=input("Burning Watering: ")))


    @Rule(Fact(action='find_disease'),Fact(pain_in_throat="yes"),Fact(cough="yes"),Fact(cold="yes"),Fact(fever="yes"),Fact(burning_micturation="no"),Fact(abdominal_pain="no"),Fact(pain_in_ear="no"),Fact(headache="no"),Fact(loose_motion="no"),Fact(vomiting="no"),Fact(redness_of_eye="no"),Fact(rashes_over_body="no"),Fact(itching="no"),Fact(burning_watering="no"))
    def disease_0(self):
        self.declare(Fact(disease="Acute Tonsillitis"))

    @Rule(Fact(action='find_disease'),Fact(pain_in_throat="no"),Fact(cough="no"),Fact(cold="no"),Fact(fever="yes"),Fact(burning_micturation="yes"),Fact(abdominal_pain="yes"),Fact(pain_in_ear="no"),Fact(headache="no"),Fact(loose_motion="no"),Fact(vomiting="no"),Fact(redness_of_eye="no"),Fact(rashes_over_body="no"),Fact(itching="no"),Fact(burning_watering="no"))
    def disease_1(self):
        self.declare(Fact(disease="Urinary Tract Infection"))

    @Rule(Fact(action='find_disease'),Fact(pain_in_throat="no"),Fact(cough="no"),Fact(cold="yes"),Fact(fever="yes"),Fact(burning_micturation="no"),Fact(abdominal_pain="no"),Fact(pain_in_ear="yes"),Fact(headache="no"),Fact(loose_motion="no"),Fact(vomiting="no"),Fact(redness_of_eye="no"),Fact(rashes_over_body="no"),Fact(itching="no"),Fact(burning_watering="no"))
    def disease_2(self):
        self.declare(Fact(disease="Earache"))

    @Rule(Fact(action='find_disease'),Fact(pain_in_throat="no"),Fact(cough="no"),Fact(cold="yes"),Fact(fever="yes"),Fact(burning_micturation="no"),Fact(abdominal_pain="no"),Fact(pain_in_ear="no"),Fact(headache="yes"),Fact(loose_motion="no"),Fact(vomiting="no"),Fact(redness_of_eye="no"),Fact(rashes_over_body="no"),Fact(itching="no"),Fact(burning_watering="no"))
    def disease_3(self):
        self.declare(Fact(disease="Sinusitis"))

    @Rule(Fact(action='find_disease'),Fact(pain_in_throat="no"),Fact(cough="no"),Fact(cold="no"),Fact(fever="no"),Fact(burning_micturation="no"),Fact(abdominal_pain="yes"),Fact(pain_in_ear="no"),Fact(headache="no"),Fact(loose_motion="yes"),Fact(vomiting="yes"),Fact(redness_of_eye="no"),Fact(rashes_over_body="no"),Fact(itching="no"),Fact(burning_watering="no"))
    def disease_4(self):
        self.declare(Fact(disease="Gastroenteritis"))

    @Rule(Fact(action='find_disease'),Fact(pain_in_throat="no"),Fact(cough="yes"),Fact(cold="yes"),Fact(fever="no"),Fact(burning_micturation="no"),Fact(abdominal_pain="no"),Fact(pain_in_ear="no"),Fact(headache="no"),Fact(loose_motion="no"),Fact(vomiting="no"),Fact(redness_of_eye="yes"),Fact(rashes_over_body="no"),Fact(itching="yes"),Fact(burning_watering="no"))
    def disease_5(self):
        self.declare(Fact(disease="Nasal Congestion"))

    @Rule(Fact(action='find_disease'),Fact(pain_in_throat="no"),Fact(cough="no"),Fact(cold="no"),Fact(fever="yes"),Fact(burning_micturation="no"),Fact(abdominal_pain="no"),Fact(pain_in_ear="no"),Fact(headache="no"),Fact(loose_motion="no"),Fact(vomiting="no"),Fact(redness_of_eye="no"),Fact(rashes_over_body="yes"),Fact(itching="yes"),Fact(burning_watering="no"))
    def disease_6(self):
        self.declare(Fact(disease="Chicken Pox"))

    @Rule(Fact(action='find_disease'),Fact(pain_in_throat="no"),Fact(cough="yes"),Fact(cold="yes"),Fact(fever="yes"),Fact(burning_micturation="no"),Fact(abdominal_pain="no"),Fact(pain_in_ear="no"),Fact(headache="no"),Fact(loose_motion="no"),Fact(vomiting="no"),Fact(redness_of_eye="yes"),Fact(rashes_over_body="no"),Fact(itching="no"),Fact(burning_watering="yes"))
    def disease_7(self):
        self.declare(Fact(disease="Conjunctivitis"))

    @Rule(Fact(action='find_disease'),Fact(pain_in_throat="no"),Fact(cough="yes"),Fact(cold="yes"),Fact(fever="yes"),Fact(burning_micturation="no"),Fact(abdominal_pain="no"),Fact(pain_in_ear="no"),Fact(headache="no"),Fact(loose_motion="no"),Fact(vomiting="no"),Fact(redness_of_eye="no"),Fact(rashes_over_body="no"),Fact(itching="no"),Fact(burning_watering="no"))
    def disease_8(self):
        self.declare(Fact(disease="Flu viral Infection"))

    @Rule(Fact(action='find_disease'),Fact(pain_in_throat="yes"),Fact(cough="yes"),Fact(cold="no"),Fact(fever="no"),Fact(burning_micturation="no"),Fact(abdominal_pain="no"),Fact(pain_in_ear="no"),Fact(headache="yes"),Fact(loose_motion="no"),Fact(vomiting="no"),Fact(redness_of_eye="no"),Fact(rashes_over_body="no"),Fact(itching="no"),Fact(burning_watering="no"))
    def disease_9(self):
        self.declare(Fact(disease="Whooping Cough"))

    @Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("The most probable disease that you have is %s\n" %(id_disease))
        print("A short description of the disease is given below :\n")
        print(disease_details+"\n")
        print("The common medications and procedures suggested by other real doctors are: \n")
        print(treatments+"\n")

    @Rule(Fact(action='find_disease'),
          Fact(pain_in_throat=MATCH.pain_in_throat),
          Fact(burning_micturation=MATCH.burning_micturation),
          Fact(pain_in_ear=MATCH.pain_in_ear),
          Fact(headache=MATCH.headache),
          Fact(loose_motion=MATCH.loose_motion),
          Fact(rashes_over_body=MATCH.rashes_over_body),
          Fact(redness_of_eye=MATCH.redness_of_eye),
          Fact(fever=MATCH.fever),
          Fact(cold=MATCH.cold),
          Fact(cough=MATCH.cough),
          Fact(abdominal_pain=MATCH.abdominal_pain),
          Fact(vomiting=MATCH.vomiting),
          Fact(itching=MATCH.itching),
          Fact(burning_watering=MATCH.burning_watering),NOT(Fact(disease=MATCH.disease)),salience = -999)

    def not_matched(self,pain_in_throat,burning_micturation,pain_in_ear,headache,loose_motion,rashes_over_body,redness_of_eye,cold,fever,cough,abdominal_pain,vomiting,itching,burning_watering):
        print("\nDid not find any disease that matches your exact symptoms")
        lis = [pain_in_throat,burning_micturation,pain_in_ear,headache,loose_motion,rashes_over_body,redness_of_eye,cold,fever,cough,abdominal_pain,vomiting,itching,burning_watering]
        max_count = 0
        max_disease = ""
        for key,val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0,len(lis)):
                if(temp_list[j] == lis[j] and lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)


if __name__ == "__main__":
    preprocess()
    engine = Greetings()
    while(1):
        engine.reset()  # Prepare the engine for the execution.
        engine.run()  # Run it!
        print("Would you like to diagnose some other symptoms?")
        if input() == "no":
            exit()
