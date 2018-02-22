# EMTerms

## Installation

```
pip install git+git://github.com/guyao/EMTerms.git
```

or

```
git clone https://github.com/guyao/EMTerms.git
cd EMTerms
pip install .
```

## Usage

```
>>> from EMTerms import load_emterms
>>> emt = load_emterms()
>>> emt.findall("Text GIVE 12696 to 80088 to donate $10 to help 5000 Families affected by Typhoon #Bopha in the #Philippines: http://t.co/8dccO6lI")
['C01', 'C08', 'O01', 'O02', 'T01', 'T02', 'T03', 'T05', 'T06', 'T07', 'T11']
```

## EMTerms Categories

```
C01 Children's well being and education
C02 Needs food, or able to provide food
C03 Mental, physical, emotional well being and health
C04 Logistics and transportation
C05 Need of shelters, including location and conditions of shelters and camps
C06 Availability and access to water, sanitation, and hygiene
C07 Safety and security, protection of people and property
C08 Telecommunications, mobile and landline networks, Internet
O01 Weather conditions
O02 Response agencies present at the crisis location
O03 Witnesses' accounts
O04 Impact of the crisis
T01 Caution, advice, warnings issued or lifted
T02 Injured people
T03 Dead people
T04 Infrastructure, buildings, or roads damaged or operational; utilities/services interrupted or restored
T05 Money requested, donated or spent
T06 Need of/offered supplies, such as food, water, clothing, medical supplies or blood
T07 Volunteer or professional services needed or offered
T08 Missing, found, or trapped people
T09 Displaced, relocated, and evacuated people
T10 Animal management. Pets and animals, living, missing, displaced, or injured/dead.
T11 Personal updates, updates about loved ones, sympathy
```
