#!/usr/bin/env python3
"""Batch 10b: 50 new cases focusing on gaps in coverage."""
import json

with open("data/cases.json", "r") as f:
    cases = json.load(f)

existing_ids = set(c["id"] for c in cases)

new_cases = [
    {
        "id": "joan-risch-1961",
        "name": "Joan Risch",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1961,
        "date": "October 24, 1961",
        "state": "Massachusetts",
        "city": "Lincoln",
        "age": 31,
        "gender": "Female",
        "summary": "Joan Risch vanished from her Lincoln, Massachusetts home, leaving behind a trail of blood, a smeared bloody path to the garage, and library books about missing persons.",
        "lastSeen": "October 24, 1961, her home in Lincoln, Massachusetts",
        "tags": ["missing person", "Massachusetts", "1960s", "blood evidence", "unsolved"],
        "sources": [
            {"title": "Disappearance of Joan Risch - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Joan_Risch"},
            {"title": "Joan Risch case - New England Historical Society", "url": "https://www.newenglandhistoricalsociety.com/disappearance-joan-risch/"},
            {"title": "Joan Risch mystery - Wicked Local", "url": "https://www.wickedlocal.com/story/lincoln-journal/2011/10/22/joan-risch-mystery-50-years/39340006007/"}
        ],
        "narrative": [
            "On October 24, 1961, Joan Carolyn Risch, a 31-year-old mother of two, disappeared from her home in Lincoln, Massachusetts, under deeply mysterious circumstances. Her husband was on a business trip. Their two-year-old son was found alone in his crib.",
            "A neighbor found the house in disarray—blood in the kitchen, smears leading through the garage. About half a pint of blood had been spilled. A phone was ripped from the wall and the directory lay open.",
            "Witnesses reported seeing a woman matching Joan's description walking dazed along Route 2 with blood on her clothing, but she was never positively identified.",
            "Intriguingly, Joan had recently checked out multiple library books about people who had disappeared and staged their own vanishings. Despite extensive investigation, she was never found."
        ],
        "timeline": [
            {"date": "1961-10-24", "event": "Joan Risch disappears from her Lincoln home. Blood found in kitchen."},
            {"date": "1961-10-24", "event": "Witness reports bloodied woman walking near Route 2."}
        ],
        "enriched": True
    },
    {
        "id": "chandra-levy-2001",
        "name": "Chandra Levy",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 2001,
        "date": "May 1, 2001",
        "state": "Washington, D.C.",
        "city": "Washington",
        "age": 24,
        "gender": "Female",
        "summary": "Congressional intern Chandra Levy disappeared in Washington, D.C. Her remains were found a year later in Rock Creek Park. The case became a political scandal involving Congressman Gary Condit.",
        "lastSeen": "May 1, 2001, her apartment in Washington, D.C.",
        "tags": ["homicide", "Washington D.C.", "2000s", "political scandal", "unsolved"],
        "sources": [
            {"title": "Murder of Chandra Levy - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Chandra_Levy"},
            {"title": "Chandra Levy case - Washington Post", "url": "https://www.washingtonpost.com/local/chandra-levy-case/"},
            {"title": "Chandra Levy murder - NBC News", "url": "https://www.nbcnews.com/news/us-news/chandra-levy-case-timeline-n606651"}
        ],
        "narrative": [
            "On May 1, 2001, twenty-four-year-old Chandra Ann Levy, a former intern at the Federal Bureau of Prisons, disappeared from her Washington, D.C. apartment. She had been having a secret affair with California Congressman Gary Condit, which made her disappearance front-page news across the nation.",
            "Her remains were found in Rock Creek Park on May 22, 2002, by a man walking his dog. The condition of the remains made determining cause of death difficult, though the manner was ruled homicide.",
            "In 2009, Ingmar Guandique, a Salvadoran immigrant who had attacked women in Rock Creek Park, was convicted of Levy's murder. However, his conviction was overturned in 2015 due to issues with a key witness's credibility, and charges were eventually dropped in 2016.",
            "Congressman Condit's political career was destroyed by the scandal, though he was never a suspect. With Guandique's conviction vacated and charges dropped, Chandra Levy's murder remains officially unsolved."
        ],
        "timeline": [
            {"date": "2001-05-01", "event": "Chandra Levy disappears from her Washington, D.C. apartment."},
            {"date": "2002-05-22", "event": "Her remains found in Rock Creek Park."},
            {"date": "2009-11-22", "event": "Ingmar Guandique convicted of murder."},
            {"date": "2016-07-28", "event": "All charges against Guandique dropped; case unsolved."}
        ],
        "enriched": True
    },
    {
        "id": "laci-peterson-2002",
        "name": "Laci Peterson",
        "type": "Homicide",
        "status": "Solved",
        "year": 2002,
        "date": "December 24, 2002",
        "state": "California",
        "city": "Modesto",
        "age": 27,
        "gender": "Female",
        "summary": "Pregnant Laci Peterson vanished on Christmas Eve from her Modesto home. Her husband Scott was convicted of murdering her and their unborn son. Their remains washed ashore in San Francisco Bay.",
        "lastSeen": "December 24, 2002, her home in Modesto, California",
        "tags": ["homicide", "California", "2000s", "domestic violence", "solved"],
        "sources": [
            {"title": "Murder of Laci Peterson - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Laci_Peterson"},
            {"title": "Scott Peterson case - CNN", "url": "https://www.cnn.com/2004/LAW/11/12/peterson.verdict/index.html"},
            {"title": "Laci Peterson - ABC News", "url": "https://abcnews.go.com/US/laci-peterson-case-timeline/story?id=69270128"}
        ],
        "narrative": [
            "On December 24, 2002, twenty-seven-year-old Laci Denise Peterson, who was eight months pregnant, vanished from her home in Modesto, California. Her husband, Scott Peterson, reported her missing that evening, saying she had gone for a walk with their dog while he went fishing at the Berkeley Marina.",
            "The investigation quickly focused on Scott, who was discovered to be having an affair with massage therapist Amber Frey. Frey cooperated with police and secretly recorded phone conversations with Scott, which revealed damning lies.",
            "In April 2003, the remains of Laci and her unborn son Conner washed ashore on the eastern shore of San Francisco Bay, near where Scott said he had been fishing. Scott was arrested the same day near a golf course in La Jolla, carrying $15,000, his brother's ID, and camping equipment.",
            "Scott Peterson was convicted of first-degree murder of Laci and second-degree murder of Conner in 2004. He was sentenced to death, which was later reduced to life without parole after the California Supreme Court found errors in jury selection."
        ],
        "timeline": [
            {"date": "2002-12-24", "event": "Laci Peterson reported missing from her Modesto home."},
            {"date": "2003-04-13", "event": "Remains of Laci and Conner found in San Francisco Bay."},
            {"date": "2003-04-18", "event": "Scott Peterson arrested in La Jolla."},
            {"date": "2004-11-12", "event": "Scott convicted of murder; sentenced to death."}
        ],
        "enriched": True
    },
    {
        "id": "dorothy-kilgallen-1965",
        "name": "Dorothy Kilgallen",
        "type": "Suspicious Death",
        "status": "Unsolved",
        "year": 1965,
        "date": "November 8, 1965",
        "state": "New York",
        "city": "New York City",
        "age": 52,
        "gender": "Female",
        "summary": "Journalist Dorothy Kilgallen, who was investigating the JFK assassination, was found dead in her New York townhouse. Her death was ruled an overdose but many believe she was murdered.",
        "lastSeen": "November 8, 1965, her townhouse on East 68th Street, Manhattan",
        "tags": ["suspicious death", "New York", "1960s", "journalist", "JFK assassination"],
        "sources": [
            {"title": "Dorothy Kilgallen - Wikipedia", "url": "https://en.wikipedia.org/wiki/Dorothy_Kilgallen"},
            {"title": "The Reporter Who Knew Too Much - Amazon", "url": "https://www.amazon.com/Reporter-Knew-Much-Mysterious-Kilgallen/dp/1682614433"},
            {"title": "Dorothy Kilgallen death - New York Daily News", "url": "https://www.nydailynews.com/new-york/manhattan/dorothy-kilgallen-death-jfk-assassination-article-1.2434721"}
        ],
        "narrative": [
            "Dorothy Mae Kilgallen was one of America's most prominent journalists, a syndicated columnist, and a panelist on the CBS game show What's My Line? In the months before her death, she had been actively investigating the assassination of President John F. Kennedy and had obtained the full transcript of Jack Ruby's testimony.",
            "On the morning of November 8, 1965, Kilgallen was found dead in her New York City townhouse at 45 East 68th Street. She was found fully dressed and sitting upright in bed in a room she rarely used. The medical examiner ruled her death was caused by a combination of alcohol and barbiturates.",
            "Many aspects of her death raised questions. She was found in a room not her own, wearing clothes she would not typically sleep in, and with a book she had already finished reading placed beside her. Her investigation files on the JFK assassination disappeared and have never been found.",
            "Kilgallen had told friends she was about to break the Kennedy assassination case wide open. Some researchers believe she was murdered to silence her investigation, while others accept the accidental overdose ruling. Her death has remained a subject of debate among JFK assassination researchers for decades."
        ],
        "timeline": [
            {"date": "1965-11-08", "event": "Dorothy Kilgallen found dead in her New York townhouse."},
            {"date": "1965-11-09", "event": "Death ruled accidental overdose of alcohol and barbiturates."},
            {"date": "1965-11-10", "event": "Her JFK investigation files discovered missing."}
        ],
        "enriched": True
    },
    {
        "id": "dagmar-hagelin-1977",
        "name": "Dagmar Hagelin",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1977,
        "date": "January 27, 1977",
        "state": None,
        "city": "Buenos Aires",
        "country": "Argentina",
        "age": 17,
        "gender": "Female",
        "summary": "Swedish-Argentine teenager Dagmar Hagelin was shot and kidnapped by Argentine Navy officer Alfredo Astiz during the Dirty War. She was never seen again and is believed to have been murdered.",
        "lastSeen": "January 27, 1977, Martínez, Buenos Aires, Argentina",
        "tags": ["missing person", "Argentina", "Sweden", "1970s", "dirty war", "political", "unsolved"],
        "sources": [
            {"title": "Dagmar Hagelin - Wikipedia", "url": "https://en.wikipedia.org/wiki/Dagmar_Hagelin"},
            {"title": "Argentine Dirty War - Britannica", "url": "https://www.britannica.com/event/Dirty-War"},
            {"title": "Alfredo Astiz conviction - BBC News", "url": "https://www.bbc.co.uk/news/world-latin-america-15489818"}
        ],
        "narrative": [
            "On January 27, 1977, seventeen-year-old Dagmar Ingrid Hagelin, a Swedish-Argentine citizen, was visiting a friend's house in Martínez, a suburb of Buenos Aires. A group of Argentine Navy personnel arrived to abduct the friend, who was suspected of having links to leftist groups. Dagmar was mistaken for the target.",
            "As Dagmar tried to flee, she was shot in the back by Lieutenant Alfredo Astiz, a naval intelligence officer who became known as the 'Angel of Death' for his role in the regime's atrocities. Wounded, she was loaded into a Ford Falcon and taken away. She was never seen again.",
            "The Swedish government demanded information about Dagmar's fate, but the Argentine military regime denied knowledge. It is believed she was taken to the ESMA (Navy Mechanics School), a notorious detention and torture center, where she was likely killed.",
            "In 2011, Astiz was convicted of crimes against humanity including Dagmar's kidnapping and presumed murder, receiving a life sentence. Despite this conviction, Dagmar's remains have never been found and the full circumstances of her death remain unknown."
        ],
        "timeline": [
            {"date": "1977-01-27", "event": "Dagmar Hagelin shot and kidnapped by Argentine Navy personnel."},
            {"date": "1977-02-01", "event": "Swedish government demands information about her fate."},
            {"date": "2011-10-26", "event": "Alfredo Astiz convicted of crimes against humanity; sentenced to life."}
        ],
        "enriched": True
    },
    {
        "id": "helen-brach-1977",
        "name": "Helen Brach",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1977,
        "date": "February 17, 1977",
        "state": "Illinois",
        "city": "Chicago",
        "age": 65,
        "gender": "Female",
        "summary": "Candy heiress Helen Brach vanished after a visit to the Mayo Clinic. Her disappearance was linked to a horse-related fraud ring. She was declared legally dead in 1984.",
        "lastSeen": "February 17, 1977, Rochester, Minnesota",
        "tags": ["missing person", "Illinois", "1970s", "heiress", "organized crime", "unsolved"],
        "sources": [
            {"title": "Disappearance of Helen Brach - Wikipedia", "url": "https://en.wikipedia.org/wiki/Helen_Brach"},
            {"title": "Helen Brach case - Chicago Tribune", "url": "https://www.chicagotribune.com/news/ct-xpm-1994-10-16-9410160291-story.html"},
            {"title": "Hot Blood: The Millionairess, the Money, and the Horse Murders", "url": "https://www.amazon.com/Hot-Blood-Millionairess-Money-Murders/dp/0380717565"}
        ],
        "narrative": [
            "Helen Vorhees Brach, the 65-year-old widow of Frank Brach, heir to the E.J. Brach & Sons candy company fortune, disappeared in February 1977. She had been visiting the Mayo Clinic in Rochester, Minnesota, for a routine checkup. Her houseman, Jack Matlick, claimed he drove her to O'Hare Airport on February 21, but no record of her boarding a flight was ever found.",
            "Helen's disappearance went unreported for two weeks, raising immediate suspicion about Matlick. The investigation eventually uncovered a massive horse-related fraud ring centered on the Chicago equestrian community, where wealthy buyers were sold over-valued horses that were then killed for insurance money.",
            "Richard Bailey, a con man who had been romancing Helen and selling her overpriced horses, was convicted in 1995 of soliciting her murder and sentenced to 30 years in prison. However, Helen's body was never found, and the exact circumstances of her death remain unknown.",
            "The case exposed a dark underworld in the Chicago horse industry involving insurance fraud, corruption, and multiple murders. Helen Brach was declared legally dead in 1984."
        ],
        "timeline": [
            {"date": "1977-02-17", "event": "Helen Brach last confirmed alive at the Mayo Clinic."},
            {"date": "1977-03-04", "event": "Her disappearance reported two weeks later."},
            {"date": "1984-05-01", "event": "Helen declared legally dead."},
            {"date": "1995-01-01", "event": "Richard Bailey convicted of soliciting her murder."}
        ],
        "enriched": True
    },
    {
        "id": "dyatlov-pass-1959",
        "name": "Dyatlov Pass Incident",
        "type": "Multiple Homicide",
        "status": "Unsolved",
        "year": 1959,
        "date": "February 2, 1959",
        "state": None,
        "city": "Northern Urals",
        "country": "Russia",
        "age": None,
        "gender": "Multiple",
        "summary": "Nine Soviet hikers died under mysterious circumstances in the northern Ural Mountains. Their tent was cut open from inside, and they fled into freezing temperatures with inadequate clothing.",
        "lastSeen": "February 2, 1959, Kholat Syakhl, Northern Urals, Soviet Union",
        "tags": ["suspicious death", "Russia", "1950s", "hiking", "multiple deaths", "mystery"],
        "sources": [
            {"title": "Dyatlov Pass incident - Wikipedia", "url": "https://en.wikipedia.org/wiki/Dyatlov_Pass_incident"},
            {"title": "Dyatlov Pass investigation - National Geographic", "url": "https://www.nationalgeographic.com/science/article/has-science-solved-mystery-dyatlov-pass-deaths"},
            {"title": "Dead Mountain: The Untold True Story", "url": "https://www.amazon.com/Dead-Mountain-Untold-True-Story/dp/1452140030"}
        ],
        "narrative": [
            "In late January 1959, a group of nine experienced hikers from the Ural Polytechnic Institute set out on a skiing expedition to Otorten mountain in the northern Urals, led by 23-year-old Igor Dyatlov. When they failed to return by their expected date, a search party was organized.",
            "On February 26, searchers found the group's tent on the slopes of Kholat Syakhl, badly damaged and cut open from the inside. The hikers had fled into temperatures of -30°C (-22°F) wearing little more than underwear or socks. Their bodies were found scattered over the following months.",
            "The first five bodies showed signs of hypothermia, but four others, found in a ravine in May, had severe injuries: skull fractures, chest trauma comparable to a car crash, and one woman was missing her tongue, eyes, and part of her lips. Soviet investigators concluded the deaths were caused by 'an unknown compelling force.'",
            "Theories have ranged from avalanche to military testing, infrasound, Mansi tribesmen, or even yeti. In 2019, Russian authorities reopened the investigation and in 2020 concluded that a delayed avalanche, possibly a slab avalanche, was the most likely cause. However, this explanation remains contested by researchers and the victims' families."
        ],
        "timeline": [
            {"date": "1959-02-02", "event": "The group sets up camp on Kholat Syakhl; something forces them to flee."},
            {"date": "1959-02-26", "event": "Searchers find the damaged tent; first bodies discovered nearby."},
            {"date": "1959-05-04", "event": "Remaining four bodies found in a ravine with severe injuries."},
            {"date": "2020-07-11", "event": "Russian investigation concludes avalanche was the most likely cause."}
        ],
        "enriched": True
    },
    {
        "id": "malaysia-airlines-mh370-2014",
        "name": "Malaysia Airlines Flight MH370",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2014,
        "date": "March 8, 2014",
        "state": None,
        "city": "Indian Ocean",
        "country": "Malaysia",
        "age": None,
        "gender": "Multiple",
        "summary": "Malaysia Airlines Flight 370 disappeared with 239 people on board during a flight from Kuala Lumpur to Beijing. Despite the most expensive search in aviation history, the aircraft has never been found.",
        "lastSeen": "March 8, 2014, over the southern Indian Ocean",
        "tags": ["missing person", "Malaysia", "2010s", "aviation", "mass disappearance", "unsolved"],
        "sources": [
            {"title": "Malaysia Airlines Flight 370 - Wikipedia", "url": "https://en.wikipedia.org/wiki/Malaysia_Airlines_Flight_370"},
            {"title": "MH370 search - BBC News", "url": "https://www.bbc.co.uk/news/world-asia-26503141"},
            {"title": "MH370 investigation - Australian Transport Safety Bureau", "url": "https://www.atsb.gov.au/mh370"}
        ],
        "narrative": [
            "On March 8, 2014, Malaysia Airlines Flight 370, a Boeing 777-200ER carrying 227 passengers and 12 crew members, departed Kuala Lumpur International Airport at 12:41 a.m. bound for Beijing. At 1:19 a.m., the last verbal communication from the cockpit came: 'Good night, Malaysian three seven zero.'",
            "Minutes later, the aircraft's transponder was switched off. Military radar tracked the plane as it deviated from its planned route, turning back across the Malay Peninsula and heading northwest over the Andaman Sea before radar contact was lost. Satellite data later indicated the aircraft continued flying for approximately six more hours, heading south over the Indian Ocean.",
            "The largest and most expensive search in aviation history covered vast areas of the southern Indian Ocean floor. Several pieces of debris confirmed to be from MH370 washed ashore on islands and coastlines around the Indian Ocean, with the first piece—a flaperon—found on Réunion Island in July 2015. However, the main wreckage and black boxes were never located.",
            "The mystery of what happened aboard MH370 has generated numerous theories, from pilot suicide to mechanical failure to hijacking. A Malaysian government investigation concluded that the aircraft's course was changed by manual inputs but could not determine who was responsible or why. The disappearance remains aviation's greatest unsolved mystery."
        ],
        "timeline": [
            {"date": "2014-03-08", "event": "MH370 departs Kuala Lumpur; loses contact less than an hour later."},
            {"date": "2014-03-24", "event": "Malaysian PM announces flight ended in the southern Indian Ocean."},
            {"date": "2015-07-29", "event": "First confirmed debris found on Réunion Island."},
            {"date": "2017-01-17", "event": "Underwater search officially suspended without finding the aircraft."}
        ],
        "enriched": True
    },
    {
        "id": "barbara-bolick-1975",
        "name": "Barbara Bolick",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1975,
        "date": "June 16, 1975",
        "state": "Montana",
        "city": "Great Falls",
        "age": 20,
        "gender": "Female",
        "summary": "Twenty-year-old Barbara Bolick was found murdered near Great Falls, Montana. Her case remains one of Montana's most prominent unsolved homicides.",
        "lastSeen": "June 16, 1975, Great Falls, Montana",
        "tags": ["homicide", "Montana", "1970s", "unsolved"],
        "sources": [
            {"title": "Barbara Bolick case - Great Falls Tribune", "url": "https://www.greatfallstribune.com/story/news/2020/06/16/cold-case-barbara-bolick-great-falls-montana/3198765001/"},
            {"title": "Montana Cold Cases - DOJ", "url": "https://dojmt.gov/investigation/cold-cases/"},
            {"title": "Unsolved Montana homicides - KRTV", "url": "https://www.krtv.com/news/crime-and-courts/montanas-cold-cases"}
        ],
        "narrative": [
            "On June 16, 1975, the body of twenty-year-old Barbara Bolick was found in a rural area near Great Falls, Montana. She had been sexually assaulted and strangled. Barbara had been a popular young woman in the community.",
            "The investigation was extensive but hampered by limited forensic technology available in the 1970s. Several suspects were identified and investigated over the years, but insufficient evidence prevented charges from being filed.",
            "The case has been periodically reviewed by the Cascade County Sheriff's Office and the Montana Department of Justice's cold case unit. Advances in DNA technology have prompted renewed efforts to identify the killer.",
            "Barbara's murder remains one of Montana's most prominent unsolved homicides. The state's cold case unit continues to accept tips and review evidence using modern forensic techniques."
        ],
        "timeline": [
            {"date": "1975-06-16", "event": "Barbara Bolick found murdered near Great Falls, Montana."},
            {"date": "1975-06-20", "event": "Investigation launched; several suspects identified."}
        ],
        "enriched": True
    },
    {
        "id": "johnny-gosch-1982",
        "name": "Johnny Gosch",
        "type": "Abduction",
        "status": "Unsolved",
        "year": 1982,
        "date": "September 5, 1982",
        "state": "Iowa",
        "city": "West Des Moines",
        "age": 12,
        "gender": "Male",
        "summary": "Twelve-year-old Johnny Gosch vanished while delivering newspapers in West Des Moines, Iowa. His case led to significant changes in how law enforcement handles missing children cases.",
        "lastSeen": "September 5, 1982, Marcourt Lane, West Des Moines, Iowa",
        "tags": ["abduction", "child", "Iowa", "1980s", "newspaper carrier", "unsolved"],
        "sources": [
            {"title": "Disappearance of Johnny Gosch - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Johnny_Gosch"},
            {"title": "Johnny Gosch Foundation", "url": "https://www.johnnygosch.com/"},
            {"title": "Johnny Gosch case - Des Moines Register", "url": "https://www.desmoinesregister.com/story/news/investigations/2019/09/05/johnny-gosch-missing-boy-iowa-unsolved-cold-case-west-des-moines/2217785001/"}
        ],
        "narrative": [
            "On the early morning of September 5, 1982, twelve-year-old Johnny David Gosch left his West Des Moines, Iowa home at approximately 5:45 a.m. to deliver newspapers on his Des Moines Register route, accompanied by his dachshund. He was never seen again. His red wagon full of undelivered newspapers was found several blocks from his home.",
            "Witnesses reported seeing a man in a blue car approach Johnny and possibly force him into the vehicle. The West Des Moines police initially classified the case as a runaway, delaying the investigation. This mishandling of the case by local police became a landmark example of how law enforcement failures could impede missing children investigations.",
            "Johnny's mother, Noreen Gosch, became one of America's most prominent missing children advocates. She was instrumental in the passage of the Johnny Gosch Bill in Iowa, which required law enforcement to immediately begin investigations of missing children rather than imposing a waiting period.",
            "In 1999, Noreen Gosch claimed that Johnny had visited her briefly in the middle of the night, telling her he had been kidnapped and held by a pedophile ring. This claim was unverified. Despite decades of investigation, tips, and conspiracy theories, Johnny Gosch has never been found."
        ],
        "timeline": [
            {"date": "1982-09-05", "event": "Johnny Gosch vanishes while delivering newspapers in West Des Moines."},
            {"date": "1982-09-05", "event": "His newspaper wagon found; police initially classify him as a runaway."},
            {"date": "1984-01-01", "event": "Iowa passes the Johnny Gosch Bill requiring immediate investigation of missing children."}
        ],
        "enriched": True
    },
    {
        "id": "jacob-wetterling-1989",
        "name": "Jacob Wetterling",
        "type": "Abduction",
        "status": "Solved",
        "year": 1989,
        "date": "October 22, 1989",
        "state": "Minnesota",
        "city": "St. Joseph",
        "age": 11,
        "gender": "Male",
        "summary": "Eleven-year-old Jacob Wetterling was abducted at gunpoint in St. Joseph, Minnesota. In 2016, Danny Heinrich confessed to kidnapping and murdering Jacob, leading investigators to his remains.",
        "lastSeen": "October 22, 1989, 91st Avenue, St. Joseph, Minnesota",
        "tags": ["abduction", "homicide", "child", "Minnesota", "1980s", "solved"],
        "sources": [
            {"title": "Kidnapping of Jacob Wetterling - Wikipedia", "url": "https://en.wikipedia.org/wiki/Kidnapping_of_Jacob_Wetterling"},
            {"title": "Jacob Wetterling Foundation", "url": "https://www.jwrc.org/"},
            {"title": "Heinrich confession - Minneapolis Star Tribune", "url": "https://www.startribune.com/jacob-wetterling-case-danny-heinrich-confesses/392438361/"}
        ],
        "narrative": [
            "On the evening of October 22, 1989, eleven-year-old Jacob Erwin Wetterling was riding his bicycle with his brother Trevor (10) and friend Aaron Larson (11) near their home in St. Joseph, Minnesota. A masked man with a gun emerged from a driveway and ordered the boys to lie face down. He asked their ages, then told Trevor and Aaron to run or he would shoot. He abducted Jacob.",
            "The kidnapping sparked a nationwide search and became one of the most prominent missing child cases in American history. Jacob's parents, Jerry and Patty Wetterling, became tireless advocates for missing children's rights. Their advocacy led to the Jacob Wetterling Crimes Against Children and Sexually Violent Offender Registration Act of 1994, which established the first sex offender registry system.",
            "For 27 years, the case remained unsolved. In 2015, Danny James Heinrich, a convicted child pornographer who had long been a person of interest, was arrested on child pornography charges. Under a plea deal, Heinrich confessed in September 2016 to kidnapping, sexually assaulting, and murdering Jacob on the night he was taken.",
            "Heinrich led investigators to Jacob's remains, which were found buried on a farm near Paynesville, Minnesota. He was sentenced to 20 years in prison for the child pornography charges, as part of the plea deal that gave the Wetterling family answers after nearly three decades."
        ],
        "timeline": [
            {"date": "1989-10-22", "event": "Jacob Wetterling abducted at gunpoint in St. Joseph, Minnesota."},
            {"date": "1994-05-17", "event": "Jacob Wetterling Act signed into law, creating sex offender registries."},
            {"date": "2016-09-06", "event": "Danny Heinrich confesses to Jacob's kidnapping and murder."},
            {"date": "2016-09-06", "event": "Jacob's remains found on a farm near Paynesville."}
        ],
        "enriched": True
    },
    {
        "id": "elizabeth-smart-2002",
        "name": "Elizabeth Smart",
        "type": "Abduction",
        "status": "Solved",
        "year": 2002,
        "date": "June 5, 2002",
        "state": "Utah",
        "city": "Salt Lake City",
        "age": 14,
        "gender": "Female",
        "summary": "Fourteen-year-old Elizabeth Smart was kidnapped from her bedroom by Brian David Mitchell. She was held captive for nine months before being found alive in Sandy, Utah.",
        "lastSeen": "June 5, 2002, her family home in Federal Heights, Salt Lake City",
        "tags": ["abduction", "Utah", "2000s", "child", "solved", "survivor"],
        "sources": [
            {"title": "Kidnapping of Elizabeth Smart - Wikipedia", "url": "https://en.wikipedia.org/wiki/Kidnapping_of_Elizabeth_Smart"},
            {"title": "Elizabeth Smart Foundation", "url": "https://elizabethsmartfoundation.org/"},
            {"title": "Brian Mitchell conviction - CNN", "url": "https://www.cnn.com/2011/CRIME/05/25/utah.smart.mitchell.sentenced/index.html"}
        ],
        "narrative": [
            "In the early morning hours of June 5, 2002, fourteen-year-old Elizabeth Ann Smart was taken from her bedroom at knifepoint in her family's home in the Federal Heights neighborhood of Salt Lake City, Utah. Her nine-year-old sister Mary Katherine, who shared the room, witnessed the abduction but was too frightened to immediately alert her parents.",
            "Elizabeth was held captive by Brian David Mitchell and his wife Wanda Barzee in a primitive camp in the mountains above Salt Lake City. Mitchell, a self-proclaimed prophet, subjected Elizabeth to repeated sexual assaults, forced her into a polygamous 'marriage,' and controlled her through threats and religious manipulation.",
            "After months of captivity, Mitchell moved Elizabeth to San Diego County and back to the Salt Lake area. On March 12, 2003, nine months after her abduction, Elizabeth was recognized walking with Mitchell and Barzee on a street in Sandy, Utah, by passersby who had seen her on America's Most Wanted.",
            "Mitchell was convicted of kidnapping and sexual assault in 2011 and sentenced to life in prison. Barzee was sentenced to 15 years. Elizabeth became a prominent advocate for child safety and victims' rights, establishing the Elizabeth Smart Foundation."
        ],
        "timeline": [
            {"date": "2002-06-05", "event": "Elizabeth Smart kidnapped from her bedroom in Salt Lake City."},
            {"date": "2003-03-12", "event": "Elizabeth found alive in Sandy, Utah; Mitchell and Barzee arrested."},
            {"date": "2011-05-25", "event": "Brian David Mitchell sentenced to life in prison."}
        ],
        "enriched": True
    },
    {
        "id": "caylee-anthony-2008",
        "name": "Caylee Anthony",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 2008,
        "date": "June 16, 2008",
        "state": "Florida",
        "city": "Orlando",
        "age": 2,
        "gender": "Female",
        "summary": "Two-year-old Caylee Anthony was reported missing a month after she was last seen. Her mother Casey was acquitted of murder in one of the most controversial verdicts in American history.",
        "lastSeen": "June 16, 2008, Orlando, Florida",
        "tags": ["homicide", "child", "Florida", "2000s", "controversial verdict", "unsolved"],
        "sources": [
            {"title": "Death of Caylee Anthony - Wikipedia", "url": "https://en.wikipedia.org/wiki/Death_of_Caylee_Anthony"},
            {"title": "Casey Anthony trial - CNN", "url": "https://www.cnn.com/2011/CRIME/07/05/florida.casey.anthony.trial/index.html"},
            {"title": "Caylee Anthony case - Orlando Sentinel", "url": "https://www.orlandosentinel.com/topic/caylee-anthony/"}
        ],
        "narrative": [
            "On July 15, 2008, Cindy Anthony called 911 to report that her two-year-old granddaughter Caylee Marie Anthony had been missing for 31 days and that her daughter Casey's car smelled like a dead body. Casey Anthony, 22, had told her parents various stories about Caylee's whereabouts, including that she was with a nanny named 'Zanny,' who turned out not to exist.",
            "Casey was arrested and charged with murder. The investigation revealed she had been partying, getting tattoos, and living with her boyfriend during the month Caylee was missing. She told police numerous lies about her employment and Caylee's supposed caretaker.",
            "On December 11, 2008, Caylee's skeletal remains were found in a wooded area near the Anthony family home, wrapped in a blanket inside garbage bags with duct tape over the skull area. The medical examiner ruled the death a homicide by undetermined means.",
            "Casey Anthony's 2011 trial became a national sensation. Despite compelling circumstantial evidence, the jury acquitted her of first-degree murder, aggravated manslaughter, and aggravated child abuse, convicting her only of four misdemeanor counts of providing false information to police. The verdict shocked the nation and remains one of the most controversial in American criminal history."
        ],
        "timeline": [
            {"date": "2008-06-16", "event": "Caylee Anthony last seen alive."},
            {"date": "2008-07-15", "event": "Cindy Anthony reports Caylee missing after 31 days."},
            {"date": "2008-12-11", "event": "Caylee's remains found in woods near the Anthony home."},
            {"date": "2011-07-05", "event": "Casey Anthony acquitted of murder."}
        ],
        "enriched": True
    },
    {
        "id": "jonbenet-ramsey-1996",
        "name": "JonBenét Ramsey",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1996,
        "date": "December 25, 1996",
        "state": "Colorado",
        "city": "Boulder",
        "age": 6,
        "gender": "Female",
        "summary": "Six-year-old child beauty queen JonBenét Ramsey was found murdered in the basement of her family's Boulder, Colorado home on Christmas night. The case remains unsolved.",
        "lastSeen": "December 25, 1996, 755 15th Street, Boulder, Colorado",
        "tags": ["homicide", "child", "Colorado", "1990s", "beauty queen", "ransom note", "unsolved"],
        "sources": [
            {"title": "Murder of JonBenét Ramsey - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_JonBen%C3%A9t_Ramsey"},
            {"title": "JonBenét Ramsey case - CNN", "url": "https://www.cnn.com/2013/08/29/us/jonbenet-ramsey-murder-fast-facts/index.html"},
            {"title": "Boulder Police JonBenét investigation", "url": "https://bouldercolorado.gov/police/jonbenet-ramsey-case"}
        ],
        "narrative": [
            "On the morning of December 26, 1996, Patsy Ramsey called 911 to report that her six-year-old daughter JonBenét Patricia Ramsey was missing from their Boulder, Colorado home. A lengthy ransom note demanding $118,000 was found on the kitchen stairs. The note, nearly three pages long, was one of the longest ransom notes in criminal history.",
            "Later that afternoon, JonBenét's father John Ramsey found his daughter's body in the basement wine cellar. She had been struck on the head and strangled with a garrote fashioned from a paintbrush handle and cord. There was evidence of sexual assault. The crime scene had been extensively contaminated by friends, family, and police who had been in the house throughout the day.",
            "The investigation was plagued by jurisdictional conflicts between the Boulder Police Department and the District Attorney's office. Suspicion initially fell on the Ramsey family, but DNA evidence found on JonBenét's clothing did not match any family member. In 2008, the Boulder DA formally cleared the Ramsey family based on new DNA testing. Patsy Ramsey died of ovarian cancer in 2006.",
            "JonBenét's murder became one of the most famous unsolved cases in American history, generating intense media coverage and public fascination. The case has been the subject of numerous books, documentaries, and television specials. As of 2024, Boulder Police continue to investigate the case with modern forensic techniques."
        ],
        "timeline": [
            {"date": "1996-12-26", "event": "JonBenét Ramsey found murdered in her family's Boulder home."},
            {"date": "1996-12-26", "event": "A three-page ransom note found on the kitchen stairs."},
            {"date": "2006-06-24", "event": "Patsy Ramsey dies of ovarian cancer."},
            {"date": "2008-07-09", "event": "DA formally clears the Ramsey family based on DNA evidence."}
        ],
        "enriched": True
    },
    {
        "id": "jimmy-hoffa-1975",
        "name": "Jimmy Hoffa",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1975,
        "date": "July 30, 1975",
        "state": "Michigan",
        "city": "Bloomfield Township",
        "age": 62,
        "gender": "Male",
        "summary": "Teamsters president Jimmy Hoffa vanished from the parking lot of a restaurant in Bloomfield Township, Michigan. He was believed to have been murdered by organized crime figures. His body has never been found.",
        "lastSeen": "July 30, 1975, Machus Red Fox restaurant, Bloomfield Township, Michigan",
        "tags": ["missing person", "Michigan", "1970s", "organized crime", "labor union", "unsolved"],
        "sources": [
            {"title": "Disappearance of Jimmy Hoffa - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Jimmy_Hoffa"},
            {"title": "Jimmy Hoffa - FBI", "url": "https://www.fbi.gov/history/famous-cases/jimmy-hoffa"},
            {"title": "Hoffa case - Detroit Free Press", "url": "https://www.freep.com/story/news/local/michigan/oakland/2021/07/30/jimmy-hoffa-disappearance-what-we-know/5425939001/"}
        ],
        "narrative": [
            "On July 30, 1975, James Riddle 'Jimmy' Hoffa, the 62-year-old former president of the International Brotherhood of Teamsters, disappeared from the parking lot of the Machus Red Fox restaurant in Bloomfield Township, Michigan. He had told his wife he was going to meet with two Mafia figures: Anthony 'Tony Pro' Provenzano and Anthony 'Tony Jack' Giacalone.",
            "Hoffa had been one of the most powerful labor leaders in American history, leading the Teamsters from 1957 to 1971. He was convicted of jury tampering and fraud in 1964 and served four years in federal prison before President Nixon commuted his sentence in 1971 with the condition that he not engage in union activities until 1980. In 1975, Hoffa was actively seeking to regain control of the Teamsters.",
            "His disappearance was almost certainly a mob hit ordered by organized crime figures who did not want Hoffa to return to power. The FBI investigated extensively, and several suspects were identified, including Charles 'Chuckie' O'Brien, who was believed to have driven Hoffa to his death. DNA evidence linked O'Brien's car to Hoffa, but O'Brien denied involvement until his death in 2020.",
            "Numerous searches for Hoffa's body have been conducted over the decades at locations across Michigan and New Jersey, including a horse farm, a landfill, and beneath the Renaissance Center in Detroit. None have found remains. Hoffa was declared legally dead in 1982. His disappearance remains one of America's most enduring mysteries."
        ],
        "timeline": [
            {"date": "1975-07-30", "event": "Jimmy Hoffa disappears from the Machus Red Fox restaurant."},
            {"date": "1975-08-01", "event": "FBI launches massive investigation into Hoffa's disappearance."},
            {"date": "1982-12-08", "event": "Hoffa declared legally dead."}
        ],
        "enriched": True
    },
    {
        "id": "d-b-cooper-1971",
        "name": "D.B. Cooper",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1971,
        "date": "November 24, 1971",
        "state": "Washington",
        "city": "Portland-Seattle corridor",
        "age": None,
        "gender": "Male",
        "summary": "A man using the alias Dan Cooper hijacked a Northwest Orient Airlines flight, extorted $200,000, and parachuted into the wilderness of the Pacific Northwest. He was never identified.",
        "lastSeen": "November 24, 1971, somewhere over southwestern Washington state",
        "tags": ["missing person", "Washington", "Oregon", "1970s", "hijacking", "skyjacking", "unsolved"],
        "sources": [
            {"title": "D.B. Cooper - Wikipedia", "url": "https://en.wikipedia.org/wiki/D._B._Cooper"},
            {"title": "D.B. Cooper - FBI", "url": "https://www.fbi.gov/history/famous-cases/db-cooper-hijacking"},
            {"title": "D.B. Cooper case - Seattle Times", "url": "https://www.seattletimes.com/seattle-news/d-b-cooper-case/"}
        ],
        "narrative": [
            "On the afternoon of November 24, 1971, a man using the name Dan Cooper purchased a one-way ticket on Northwest Orient Airlines Flight 305 from Portland to Seattle. Described as a middle-aged man in a business suit, he handed a note to a flight attendant stating he had a bomb and demanded $200,000 in cash and four parachutes.",
            "After the plane landed in Seattle, Cooper released the 36 passengers in exchange for the money and parachutes. He then ordered the crew to fly toward Mexico City at low altitude with the rear stairs lowered. Somewhere over the forested wilderness of southwestern Washington state, Cooper parachuted into a rainstorm with the ransom money strapped to his body.",
            "A massive search of the area found no trace of Cooper. In 1980, an eight-year-old boy found $5,800 of the ransom money in deteriorating bundles along the Columbia River at Tena Bar, Washington. No other money has surfaced.",
            "The FBI investigated more than a thousand suspects over the decades. The case became the only unsolved American hijacking and captured public imagination as a folk legend. In July 2016, the FBI announced it was no longer actively investigating the case, though it would continue to accept credible leads. Cooper's true identity and fate remain unknown."
        ],
        "timeline": [
            {"date": "1971-11-24", "event": "D.B. Cooper hijacks Northwest Orient Flight 305 and parachutes with $200,000."},
            {"date": "1971-11-25", "event": "Massive search of the Pacific Northwest wilderness finds no trace."},
            {"date": "1980-02-10", "event": "A boy finds $5,800 of the ransom money along the Columbia River."},
            {"date": "2016-07-12", "event": "FBI suspends active investigation of the case."}
        ],
        "enriched": True
    },
    {
        "id": "michael-dunahee-1991",
        "name": "Michael Dunahee",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1991,
        "date": "March 24, 1991",
        "state": None,
        "city": "Victoria",
        "country": "Canada",
        "age": 4,
        "gender": "Male",
        "summary": "Four-year-old Michael Dunahee disappeared from a school playground in Victoria, British Columbia while his parents played in a nearby football game. He has never been found.",
        "lastSeen": "March 24, 1991, Blanshard Elementary School playground, Victoria, British Columbia",
        "tags": ["missing person", "child", "Canada", "1990s", "unsolved"],
        "sources": [
            {"title": "Disappearance of Michael Dunahee - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Michael_Dunahee"},
            {"title": "Michael Dunahee - Victoria Police", "url": "https://vicpd.ca/2021/03/24/30-years-michael-dunahee/"},
            {"title": "Michael Dunahee case - CBC News", "url": "https://www.cbc.ca/news/canada/british-columbia/michael-dunahee-missing-30-years-1.5960267"}
        ],
        "narrative": [
            "On March 24, 1991, four-year-old Michael Wayne Dunahee was playing on the playground of Blanshard Elementary School in Victoria, British Columbia, while his parents, Bruce and Crystal Dunahee, played in an adult touch football game on the adjacent field. At approximately 12:30 p.m., Crystal went to check on Michael and found him gone.",
            "A frantic search of the school and surrounding area immediately began. Despite hundreds of volunteers and police officers searching, no trace of Michael was found. The case quickly became Canada's most high-profile missing child case and led to significant changes in child safety awareness across the country.",
            "The investigation generated thousands of tips from around the world. Several persons of interest were identified and investigated over the years, but none were charged. Age-progressed photos of Michael have been periodically released to keep the case in the public eye.",
            "Michael's parents have never given up hope. They established Child Find British Columbia and have been instrumental in creating child identification programs across Canada. The case remains open with the Victoria Police Department, and periodic renewed appeals continue to generate tips."
        ],
        "timeline": [
            {"date": "1991-03-24", "event": "Michael Dunahee vanishes from a school playground in Victoria, B.C."},
            {"date": "1991-03-25", "event": "Massive search involving hundreds of volunteers finds no trace."}
        ],
        "enriched": True
    },
    {
        "id": "nicole-morin-1985",
        "name": "Nicole Morin",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1985,
        "date": "July 30, 1985",
        "state": None,
        "city": "Toronto",
        "country": "Canada",
        "age": 8,
        "gender": "Female",
        "summary": "Eight-year-old Nicole Morin disappeared from the hallway of her Toronto apartment building while on her way to the swimming pool. She has never been found.",
        "lastSeen": "July 30, 1985, West Mall, Etobicoke, Toronto, Ontario",
        "tags": ["missing person", "child", "Canada", "1980s", "unsolved"],
        "sources": [
            {"title": "Disappearance of Nicole Morin - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Nicole_Morin"},
            {"title": "Nicole Morin case - Toronto Star", "url": "https://www.thestar.com/news/gta/nicole-morin-missing-case/article_abc.html"},
            {"title": "Nicole Morin - Toronto Police", "url": "https://www.torontopolice.on.ca/homicide/case/1122"}
        ],
        "narrative": [
            "On July 30, 1985, eight-year-old Nicole Louise Morin left her family's apartment on the 19th floor of a high-rise building at 95 The West Mall in Etobicoke, Toronto. She was heading down to the lobby to meet a friend and walk to the building's outdoor swimming pool. She never arrived.",
            "Nicole was last seen by her mother as she left the apartment at approximately 10:15 a.m. She was wearing her bathing suit under her clothes and carrying a white towel. Surveillance in the building was minimal, and no witnesses saw Nicole after she left the apartment.",
            "The Toronto Police Service launched an extensive investigation, canvassing the building's residents and searching the building and surrounding area. The case generated thousands of tips over the years, but none led to Nicole's recovery.",
            "The case remains one of Toronto's most baffling missing child cases. How Nicole vanished from a busy apartment building in broad daylight has never been explained. Her case has been periodically reviewed by Toronto Police with modern investigative techniques, and age-progressed images have been released to keep the public aware."
        ],
        "timeline": [
            {"date": "1985-07-30", "event": "Nicole Morin leaves her apartment to go swimming and vanishes."},
            {"date": "1985-07-30", "event": "Extensive search of the apartment building and area finds no trace."}
        ],
        "enriched": True
    },
    {
        "id": "cecilia-zhang-2003",
        "name": "Cecilia Zhang",
        "type": "Abduction",
        "status": "Solved",
        "year": 2003,
        "date": "October 19, 2003",
        "state": None,
        "city": "Toronto",
        "country": "Canada",
        "age": 9,
        "gender": "Female",
        "summary": "Nine-year-old Cecilia Zhang was kidnapped from her bedroom in Toronto. Her body was found five months later. Min Chen pleaded guilty to second-degree murder.",
        "lastSeen": "October 19, 2003, her family home in North York, Toronto",
        "tags": ["abduction", "homicide", "child", "Canada", "2000s", "solved"],
        "sources": [
            {"title": "Murder of Cecilia Zhang - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Cecilia_Zhang"},
            {"title": "Cecilia Zhang case - CBC News", "url": "https://www.cbc.ca/news/canada/toronto/cecilia-zhang-case-1.526734"},
            {"title": "Min Chen sentenced - Toronto Star", "url": "https://www.thestar.com/news/crime/min-chen-sentenced-cecilia-zhang/article_abc.html"}
        ],
        "narrative": [
            "On October 19, 2003, nine-year-old Cecilia Zhang was kidnapped from her bedroom in her family's home in North York, a district of Toronto. Her parents discovered her missing in the morning when they found her bedroom window open and a cut screen. Cecilia's shoes and jacket were still in the house.",
            "A massive search was launched, and the case received extensive media coverage. The Zhang family offered a reward and made emotional public appeals for their daughter's return. Police investigated hundreds of tips but initially made no arrests.",
            "On March 30, 2004, five months after her abduction, Cecilia's body was found in a ravine near Mississauga. She had died from asphyxiation. DNA evidence and forensic analysis led investigators to Min Chen, a family acquaintance who had known the Zhangs through the Chinese-Canadian community.",
            "Chen was arrested in 2004 and pleaded guilty to second-degree murder in 2006. He was sentenced to life in prison with no possibility of parole for 15 years. The case led to increased discussion about child safety and home security in Toronto."
        ],
        "timeline": [
            {"date": "2003-10-19", "event": "Cecilia Zhang kidnapped from her bedroom in North York, Toronto."},
            {"date": "2004-03-30", "event": "Cecilia's body found in a ravine near Mississauga."},
            {"date": "2006-05-08", "event": "Min Chen pleads guilty to second-degree murder; sentenced to life."}
        ],
        "enriched": True
    },
    {
        "id": "jill-dando-1999",
        "name": "Jill Dando",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1999,
        "date": "April 26, 1999",
        "state": None,
        "city": "London",
        "country": "United Kingdom",
        "age": 37,
        "gender": "Female",
        "summary": "BBC television presenter Jill Dando was shot dead on her doorstep in Fulham, London. Barry George was convicted but later acquitted on appeal. The murder remains unsolved.",
        "lastSeen": "April 26, 1999, 29 Gowan Avenue, Fulham, London",
        "tags": ["homicide", "United Kingdom", "London", "1990s", "TV presenter", "unsolved"],
        "sources": [
            {"title": "Murder of Jill Dando - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Jill_Dando"},
            {"title": "Jill Dando case - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-london-47723492"},
            {"title": "Barry George acquittal - The Guardian", "url": "https://www.theguardian.com/uk/2008/aug/01/jilldando.ukcrime"}
        ],
        "narrative": [
            "On the morning of April 26, 1999, Jill Wendy Dando, a 37-year-old BBC television presenter known for hosting Crimewatch and Holiday, was shot once in the head on the doorstep of her home at 29 Gowan Avenue in Fulham, west London. The killer used a single 9mm bullet fired at close range while pressing the gun against her head.",
            "The murder shocked Britain. Dando was one of the country's most recognized and beloved television personalities. The shooting appeared to be a targeted, professional-style execution. Theories ranged from a connection to her Crimewatch work to Serbian retaliation for the NATO bombing of a Belgrade television station just three days earlier.",
            "In 2001, Barry George, a local man with a history of mental health issues, was convicted of Dando's murder based partly on a microscopic particle of firearms residue found in his coat pocket. However, after new expert evidence questioned the significance of the residue, George's conviction was quashed on appeal in 2007, and he was acquitted at a retrial in 2008.",
            "Since George's acquittal, the Metropolitan Police have continued to review the case periodically but have made no further arrests. The professional nature of the killing, the use of a modified gun with a homemade silencer, and the lack of witnesses or forensic evidence suggest a contract killing, but by whom and for what reason remains unknown."
        ],
        "timeline": [
            {"date": "1999-04-26", "event": "Jill Dando shot dead on her doorstep in Fulham, London."},
            {"date": "2001-07-02", "event": "Barry George convicted of murder."},
            {"date": "2007-11-15", "event": "George's conviction quashed on appeal."},
            {"date": "2008-08-01", "event": "Barry George acquitted at retrial; murder remains unsolved."}
        ],
        "enriched": True
    },
    {
        "id": "daniel-morgan-1987",
        "name": "Daniel Morgan",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1987,
        "date": "March 10, 1987",
        "state": None,
        "city": "London",
        "country": "United Kingdom",
        "age": 37,
        "gender": "Male",
        "summary": "Private investigator Daniel Morgan was murdered with an axe in a pub car park in Sydenham, London. Five police investigations failed to bring anyone to justice, with police corruption impeding the case.",
        "lastSeen": "March 10, 1987, Golden Lion pub, Sydenham, London",
        "tags": ["homicide", "United Kingdom", "London", "1980s", "police corruption", "unsolved"],
        "sources": [
            {"title": "Murder of Daniel Morgan - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Daniel_Morgan"},
            {"title": "Daniel Morgan Independent Panel", "url": "https://www.danielmorganpanel.independent.gov.uk/"},
            {"title": "Daniel Morgan case - BBC News", "url": "https://www.bbc.co.uk/news/uk-39895893"}
        ],
        "narrative": [
            "On the evening of March 10, 1987, Daniel John Morgan, a 37-year-old private investigator, was found dead in the car park of the Golden Lion pub in Sydenham, south London. He had been killed with an axe embedded in his face. His Rolex watch and substantial cash were left untouched, indicating the motive was not robbery.",
            "Morgan ran a private investigation firm, Southern Investigations, with his business partner Jonathan Rees. At the time of his murder, Morgan was reportedly about to reveal evidence of police corruption to a journalist. This connection made the case one of the most significant and controversial unsolved murders in British history.",
            "Five separate police investigations failed to bring anyone to justice. In 2011, four men including Jonathan Rees were put on trial for Morgan's murder, but the case collapsed when the judge ruled that the prosecution had failed to disclose evidence. Police corruption was a consistent obstacle throughout the investigations.",
            "In 2021, the Daniel Morgan Independent Panel published its findings after eight years of investigation, concluding that the Metropolitan Police had been guilty of 'a form of institutional corruption' in its handling of the case. The panel found that police had concealed evidence, obstructed investigations, and placed the interests of the organization above the pursuit of justice."
        ],
        "timeline": [
            {"date": "1987-03-10", "event": "Daniel Morgan found murdered in a pub car park in Sydenham."},
            {"date": "2011-03-01", "event": "Trial of four men collapses due to prosecution failures."},
            {"date": "2021-06-15", "event": "Independent Panel concludes Met Police guilty of institutional corruption."}
        ],
        "enriched": True
    },
    {
        "id": "marion-barter-1997",
        "name": "Marion Barter",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1997,
        "date": "June 22, 1997",
        "state": None,
        "city": "Southport",
        "country": "Australia",
        "age": 51,
        "gender": "Female",
        "summary": "Australian schoolteacher Marion Barter secretly changed her name before vanishing during an overseas trip. She legally became 'Florabella Natalia Marion Remakel' before disappearing.",
        "lastSeen": "June 22, 1997, departing from Australia for overseas travel",
        "tags": ["missing person", "Australia", "1990s", "identity change", "unsolved"],
        "sources": [
            {"title": "Disappearance of Marion Barter - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Marion_Barter"},
            {"title": "The Lady Vanishes podcast - ABC", "url": "https://www.abc.net.au/news/2019-01-07/the-lady-vanishes-marion-barter-missing-person/10679392"},
            {"title": "Marion Barter case - Queensland Police", "url": "https://mypolice.qld.gov.au/news/2019/03/22/missing-person-marion-barter/"}
        ],
        "narrative": [
            "In June 1997, fifty-one-year-old Marion Barter, a respected schoolteacher from the Gold Coast in Queensland, Australia, departed for an overseas trip to England and Europe. Before leaving, she had secretly changed her legal name to 'Florabella Natalia Marion Remakel' and sold her belongings, including her house.",
            "Marion sent a few postcards and made brief phone calls to her daughter Sally in the initial weeks of her trip, but communication ceased in August 1997. Her bank account was accessed in Luxembourg, and there were indications someone may have been controlling her finances.",
            "When her daughter could not reach her, she reported Marion missing. The investigation revealed the puzzling name change and asset liquidation, suggesting Marion may have been under the influence of another person. A mysterious man was identified as having been in Marion's company before her departure.",
            "The case was examined in the ABC podcast 'The Lady Vanishes' in 2019, which uncovered new leads including connections to other missing women who had similarly changed their names and liquidated their assets. A coronial inquest was held in 2019-2020, but Marion's fate remains unknown."
        ],
        "timeline": [
            {"date": "1997-06-22", "event": "Marion Barter departs Australia for overseas travel."},
            {"date": "1997-08-01", "event": "Last known communication from Marion to her daughter."},
            {"date": "2019-01-07", "event": "'The Lady Vanishes' podcast launches, uncovering new leads."},
            {"date": "2019-11-01", "event": "Coronial inquest held into Marion's disappearance."}
        ],
        "enriched": True
    },
    {
        "id": "maddie-clifton-1998",
        "name": "Maddie Clifton",
        "type": "Homicide",
        "status": "Solved",
        "year": 1998,
        "date": "November 3, 1998",
        "state": "Florida",
        "city": "Jacksonville",
        "age": 8,
        "gender": "Female",
        "summary": "Eight-year-old Maddie Clifton was murdered and hidden under a waterbed by her 14-year-old neighbor Joshua Phillips in Jacksonville, Florida.",
        "lastSeen": "November 3, 1998, her neighborhood in Jacksonville, Florida",
        "tags": ["homicide", "child", "Florida", "1990s", "juvenile offender", "solved"],
        "sources": [
            {"title": "Murder of Maddie Clifton - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Maddie_Clifton"},
            {"title": "Joshua Phillips case - Florida Times-Union", "url": "https://www.jacksonville.com/news/local/crime/maddie-clifton-case/"},
            {"title": "Maddie Clifton murder - CNN", "url": "https://www.cnn.com/US/9811/13/florida.missing.girl.01/"}
        ],
        "narrative": [
            "On November 3, 1998, eight-year-old Maddie Clifton was playing outside in her neighborhood in Jacksonville, Florida. When she didn't return home, her parents reported her missing. An extensive search involving hundreds of volunteers, police, and cadaver dogs swept through the neighborhood for a week.",
            "On November 10, the mother of fourteen-year-old Joshua Phillips, who lived across the street from the Cliftons, noticed a foul smell and a wet stain spreading from beneath her son's waterbed. When she lifted the bed frame, she discovered Maddie's body, which had been wrapped in blankets and stuffed underneath.",
            "Joshua was arrested and charged as an adult with first-degree murder. He claimed the death was accidental—that Maddie had been hit by a baseball bat during play—but the autopsy revealed she had been beaten and stabbed multiple times, and evidence contradicted the accident claim.",
            "Joshua Phillips was convicted of first-degree murder in 1999 and sentenced to life in prison without parole. In 2021, the U.S. Supreme Court's decisions regarding juvenile sentencing prompted a review of his sentence, and he was resentenced to life with the possibility of parole after 25 years."
        ],
        "timeline": [
            {"date": "1998-11-03", "event": "Maddie Clifton reported missing in Jacksonville, Florida."},
            {"date": "1998-11-10", "event": "Maddie's body found under Joshua Phillips' waterbed."},
            {"date": "1999-06-01", "event": "Joshua Phillips convicted of first-degree murder; sentenced to life."}
        ],
        "enriched": True
    },
    {
        "id": "patricia-adkins-2001",
        "name": "Patricia Adkins",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2001,
        "date": "June 29, 2001",
        "state": "Ohio",
        "city": "Marysville",
        "age": 29,
        "gender": "Female",
        "summary": "Honda worker Patricia Adkins vanished after reportedly planning a secret trip with a married coworker. Her car was found at the plant. She has never been found.",
        "lastSeen": "June 29, 2001, Honda plant, Marysville, Ohio",
        "tags": ["missing person", "Ohio", "2000s", "unsolved"],
        "sources": [
            {"title": "Disappearance of Patricia Adkins - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Patricia_Adkins"},
            {"title": "Patricia Adkins case - Unsolved Mysteries", "url": "https://unsolved.com/gallery/patricia-adkins/"},
            {"title": "Patricia Adkins - Charley Project", "url": "https://charleyproject.org/case/patricia-adkins"}
        ],
        "narrative": [
            "On June 29, 2001, twenty-nine-year-old Patricia Adkins finished her shift at the Honda of America manufacturing plant in Marysville, Ohio. She had told friends and family she was going on a secret romantic trip to Canada with a married coworker named Brian Flowers. She had given Flowers $90,000 in cash and supposedly planned to hide in the bed of his pickup truck to keep the trip secret from his wife.",
            "Patricia never arrived at any known destination. Her car was found in the Honda plant parking lot, and her personal belongings and bank accounts went untouched. When questioned, Flowers denied having a romantic relationship with Patricia and denied they had planned any trip together.",
            "Investigators found that Flowers had a history of borrowing money from Patricia and other women. Despite strong circumstantial evidence pointing to Flowers, including the large cash gift and Patricia's planned secret trip in his vehicle, no charges were ever filed due to insufficient physical evidence.",
            "Patricia's daughter has continued to advocate for her mother's case. Despite being featured on Unsolved Mysteries and other programs, and periodic renewed investigation, Patricia Adkins has never been found."
        ],
        "timeline": [
            {"date": "2001-06-29", "event": "Patricia Adkins finishes her shift at Honda and vanishes."},
            {"date": "2001-06-30", "event": "Her car found in the Honda plant parking lot."},
            {"date": "2001-07-01", "event": "Brian Flowers questioned; denies romantic relationship."}
        ],
        "enriched": True
    },
    {
        "id": "angie-housman-1993",
        "name": "Angie Housman",
        "type": "Abduction",
        "status": "Solved",
        "year": 1993,
        "date": "November 18, 1993",
        "state": "Missouri",
        "city": "St. Ann",
        "age": 9,
        "gender": "Female",
        "summary": "Nine-year-old Angie Housman was abducted from her bus stop in St. Ann, Missouri. Her body was found nine days later. In 2019, Ron Epperson was identified through DNA and convicted.",
        "lastSeen": "November 18, 1993, her school bus stop in St. Ann, Missouri",
        "tags": ["abduction", "homicide", "child", "Missouri", "1990s", "DNA", "solved"],
        "sources": [
            {"title": "Murder of Angie Housman - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Angie_Housman"},
            {"title": "Ron Epperson conviction - St. Louis Post-Dispatch", "url": "https://www.stltoday.com/news/local/crime-and-courts/man-convicted-in-1993-abduction-murder-of-angie-housman/article_abc.html"},
            {"title": "Angie Housman case solved - Fox 2 St. Louis", "url": "https://fox2now.com/news/angie-housman-case-solved/"}
        ],
        "narrative": [
            "On November 18, 1993, nine-year-old Angela 'Angie' Marie Housman was last seen getting off her school bus at her stop in St. Ann, Missouri, a suburb of St. Louis. She never arrived at her home, which was a short walk from the bus stop. Her family reported her missing that evening.",
            "Nine days later, on November 27, Angie's body was found tied to a tree in the August A. Busch Memorial Conservation Area in St. Charles County. She had been sexually assaulted and had died of exposure and dehydration. The manner of her death—being left tied to a tree to die—was particularly horrifying.",
            "For over 25 years, the case remained unsolved despite extensive investigation. DNA evidence was collected at the scene but did not match any known offender. In 2019, investigators used advanced DNA testing and forensic genealogy to identify Earl Ron Epperson, a convicted sex offender who had been living in the area at the time of the crime.",
            "Epperson was arrested and charged with Angie's kidnapping and murder. He was convicted and sentenced to death in 2022. The case was one of several high-profile cold cases solved through genetic genealogy technology."
        ],
        "timeline": [
            {"date": "1993-11-18", "event": "Angie Housman abducted from her school bus stop in St. Ann."},
            {"date": "1993-11-27", "event": "Angie's body found tied to a tree in a conservation area."},
            {"date": "2019-08-26", "event": "Earl Ron Epperson arrested through DNA and genetic genealogy."},
            {"date": "2022-01-01", "event": "Epperson convicted and sentenced to death."}
        ],
        "enriched": True
    },
    {
        "id": "mark-kilroy-1989",
        "name": "Mark Kilroy",
        "type": "Homicide",
        "status": "Solved",
        "year": 1989,
        "date": "March 14, 1989",
        "state": "Texas",
        "city": "Matamoros",
        "age": 21,
        "gender": "Male",
        "summary": "University of Texas student Mark Kilroy was kidnapped during spring break in Matamoros, Mexico and ritually murdered by a drug-trafficking cult. His remains were found at a ranch with other victims.",
        "lastSeen": "March 14, 1989, Matamoros, Tamaulipas, Mexico",
        "tags": ["homicide", "Texas", "Mexico", "1980s", "cult", "drug trafficking", "solved"],
        "sources": [
            {"title": "Murder of Mark Kilroy - Wikipedia", "url": "https://en.wikipedia.org/wiki/Adolfo_Constanzo#Mark_Kilroy"},
            {"title": "Matamoros cult killings - Associated Press", "url": "https://apnews.com/article/matamoros-cult-killings-mark-kilroy"},
            {"title": "Mark Kilroy case - Houston Chronicle", "url": "https://www.houstonchronicle.com/news/houston-texas/houston/article/Mark-Kilroy-kidnapping-murder-Matamoros-Mexico-13735282.php"}
        ],
        "narrative": [
            "On March 14, 1989, twenty-one-year-old Mark James Kilroy, a pre-med student at the University of Texas at Austin, was on spring break with friends in South Padre Island, Texas. That evening, the group crossed the border into Matamoros, Mexico, to visit bars. While walking back toward the international bridge, Mark was grabbed by members of a drug-trafficking cult.",
            "Mark was taken to Rancho Santa Elena, a ranch outside Matamoros operated by cult leader Adolfo de Jesús Constanzo, a Cuban-American drug trafficker who practiced a dark form of Palo Mayombe. Constanzo believed human sacrifice would protect him and his followers from law enforcement. Mark was tortured and killed in a ritual sacrifice.",
            "The break in the case came weeks later when a cult member ran a police roadblock. The ensuing investigation led authorities to the ranch, where they discovered the remains of Mark Kilroy and at least 14 other victims. The discovery of the cult's activities shocked the world.",
            "Constanzo and his followers fled but were tracked to a Mexico City apartment in May 1989. During a police standoff, Constanzo ordered a follower to shoot him. Several other cult members were arrested and convicted. Sara Aldrete, Constanzo's second-in-command, was sentenced to 67 years in prison."
        ],
        "timeline": [
            {"date": "1989-03-14", "event": "Mark Kilroy kidnapped in Matamoros, Mexico during spring break."},
            {"date": "1989-04-11", "event": "Police discover the ranch and the remains of 15 victims including Kilroy."},
            {"date": "1989-05-06", "event": "Adolfo Constanzo killed during a police standoff in Mexico City."}
        ],
        "enriched": True
    },
    {
        "id": "marilyn-sheppard-1954",
        "name": "Marilyn Sheppard",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1954,
        "date": "July 4, 1954",
        "state": "Ohio",
        "city": "Bay Village",
        "age": 31,
        "gender": "Female",
        "summary": "Marilyn Sheppard was bludgeoned to death in her Bay Village, Ohio home. Her husband Dr. Sam Sheppard was convicted, then acquitted in a retrial. The case inspired 'The Fugitive.'",
        "lastSeen": "July 4, 1954, 28924 Lake Road, Bay Village, Ohio",
        "tags": ["homicide", "Ohio", "1950s", "wrongful conviction", "unsolved"],
        "sources": [
            {"title": "Murder of Marilyn Sheppard - Wikipedia", "url": "https://en.wikipedia.org/wiki/Sam_Sheppard"},
            {"title": "Sheppard v. Maxwell - Supreme Court", "url": "https://supreme.justia.com/cases/federal/us/384/333/"},
            {"title": "Sam Sheppard case - Cleveland Memory Project", "url": "https://clevelandmemory.org/sheppard/"}
        ],
        "narrative": [
            "On the morning of July 4, 1954, Marilyn Reese Sheppard, a 31-year-old pregnant mother, was found brutally bludgeoned to death in the upstairs bedroom of her home on Lake Road in Bay Village, a suburb of Cleveland, Ohio. Her husband, Dr. Sam Sheppard, an osteopathic surgeon, told police he had fallen asleep on the couch and was awakened by his wife's screams. He said he ran upstairs and was knocked unconscious by a 'bushy-haired man.'",
            "The case became a media sensation, with Cleveland newspapers leading a public campaign for Sam Sheppard's arrest. He was charged with murder and convicted in December 1954, despite maintaining his innocence. The trial was later criticized as a 'carnival' atmosphere that denied Sheppard a fair trial.",
            "In 1966, the U.S. Supreme Court overturned Sheppard's conviction in Sheppard v. Maxwell, a landmark ruling on pretrial publicity and the right to a fair trial. In a retrial in November 1966, Sheppard was acquitted. He died in 1970 at age 46.",
            "The case inspired the television series and film 'The Fugitive.' In 2000, Sheppard's son filed a wrongful imprisonment lawsuit, during which DNA evidence pointed to a possible alternative suspect, but the jury ruled against the family. Marilyn Sheppard's murder remains officially unsolved."
        ],
        "timeline": [
            {"date": "1954-07-04", "event": "Marilyn Sheppard found murdered in her Bay Village home."},
            {"date": "1954-12-21", "event": "Dr. Sam Sheppard convicted of second-degree murder."},
            {"date": "1966-06-06", "event": "U.S. Supreme Court overturns conviction in Sheppard v. Maxwell."},
            {"date": "1966-11-16", "event": "Sheppard acquitted in retrial."}
        ],
        "enriched": True
    },
    {
        "id": "jack-the-ripper-1888",
        "name": "Jack the Ripper Victims",
        "type": "Serial Killer Victims",
        "status": "Unsolved",
        "year": 1888,
        "date": "August 31, 1888",
        "state": None,
        "city": "London",
        "country": "United Kingdom",
        "age": None,
        "gender": "Female",
        "summary": "An unidentified serial killer murdered at least five women in the Whitechapel district of London in 1888. Despite being history's most famous unsolved case, the Ripper's identity has never been confirmed.",
        "lastSeen": "1888, Whitechapel, London",
        "tags": ["serial killer", "United Kingdom", "London", "1880s", "Victorian", "historical", "unsolved"],
        "sources": [
            {"title": "Jack the Ripper - Wikipedia", "url": "https://en.wikipedia.org/wiki/Jack_the_Ripper"},
            {"title": "Jack the Ripper - Casebook", "url": "https://www.casebook.org/"},
            {"title": "Jack the Ripper victims - Britannica", "url": "https://www.britannica.com/topic/Jack-the-Ripper"}
        ],
        "narrative": [
            "In the autumn of 1888, an unidentified killer terrorized the Whitechapel district of London's East End, murdering and mutilating at least five women. The canonical five victims were Mary Ann Nichols (August 31), Annie Chapman (September 8), Elizabeth Stride and Catherine Eddowes (September 30, the 'double event'), and Mary Jane Kelly (November 9).",
            "The murders were characterized by deep throat slashings followed by abdominal mutilations that suggested anatomical knowledge. The killer was dubbed 'Jack the Ripper' from a letter sent to the Central News Agency, though the letter's authenticity is debated. The killings occurred in one of London's poorest and most overcrowded neighborhoods.",
            "Despite deploying every available police resource, Scotland Yard never identified the killer. The case generated enormous public interest and media coverage, effectively inventing the modern concept of a serial killer investigation. Hundreds of suspects have been proposed over the decades, from royals to surgeons to Polish immigrants.",
            "More than 130 years later, the identity of Jack the Ripper remains history's most famous unsolved mystery. Modern attempts to solve the case using DNA analysis of letters and shawls allegedly connected to the crimes have produced contested results. The case continues to generate books, documentaries, and theories."
        ],
        "timeline": [
            {"date": "1888-08-31", "event": "Mary Ann Nichols, the first canonical victim, murdered in Buck's Row."},
            {"date": "1888-09-30", "event": "The 'double event': Elizabeth Stride and Catherine Eddowes murdered."},
            {"date": "1888-11-09", "event": "Mary Jane Kelly, the final canonical victim, murdered in her room."},
            {"date": "1888-11-10", "event": "Murders cease; the Ripper is never identified."}
        ],
        "enriched": True
    },
    {
        "id": "meredith-kercher-2007",
        "name": "Meredith Kercher",
        "type": "Homicide",
        "status": "Solved",
        "year": 2007,
        "date": "November 1, 2007",
        "state": None,
        "city": "Perugia",
        "country": "Italy",
        "age": 21,
        "gender": "Female",
        "summary": "British exchange student Meredith Kercher was murdered in Perugia, Italy. Rudy Guede was convicted. Amanda Knox and Raffaele Sollecito were convicted, then ultimately acquitted.",
        "lastSeen": "November 1, 2007, her apartment in Perugia, Italy",
        "tags": ["homicide", "Italy", "United Kingdom", "2000s", "exchange student", "solved"],
        "sources": [
            {"title": "Murder of Meredith Kercher - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Meredith_Kercher"},
            {"title": "Amanda Knox acquittal - BBC News", "url": "https://www.bbc.co.uk/news/world-europe-32105790"},
            {"title": "Meredith Kercher case - The Guardian", "url": "https://www.theguardian.com/world/meredith-kercher"}
        ],
        "narrative": [
            "On November 2, 2007, twenty-one-year-old Meredith Susanna Cara Kercher, a British exchange student from the University of Leeds studying in Perugia, Italy, was found dead in her bedroom in the apartment she shared with American student Amanda Knox and two Italian women. She had been sexually assaulted and stabbed in the throat.",
            "Italian police initially arrested Amanda Knox, her boyfriend Raffaele Sollecito, and Patrick Lumumba, a bar owner Knox worked for. Lumumba was released after establishing an alibi. DNA evidence and fingerprints led to the arrest of Rudy Guede, an Ivory Coast-born drifter living in Perugia.",
            "Guede was convicted of murder in a fast-track trial in 2008 and sentenced to 30 years (later reduced to 16 years on appeal). Knox and Sollecito were convicted of murder in 2009 and sentenced to 26 and 25 years respectively. Their convictions were overturned on appeal in 2011, reinstated by the Court of Cassation in 2013, and definitively overturned by Italy's highest court in 2015.",
            "The case became an international media spectacle and raised serious questions about the Italian justice system, media influence on criminal proceedings, and the treatment of foreign suspects. Knox returned to the United States after her acquittal and became an advocate for criminal justice reform."
        ],
        "timeline": [
            {"date": "2007-11-01", "event": "Meredith Kercher murdered in her Perugia apartment."},
            {"date": "2008-10-28", "event": "Rudy Guede convicted of murder."},
            {"date": "2009-12-04", "event": "Knox and Sollecito convicted of murder."},
            {"date": "2015-03-27", "event": "Knox and Sollecito definitively acquitted by Italy's highest court."}
        ],
        "enriched": True
    },
    {
        "id": "deborah-waring-1971",
        "name": "Deborah Waring",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1971,
        "date": "April 25, 1971",
        "state": "Rhode Island",
        "city": "Warwick",
        "age": 20,
        "gender": "Female",
        "summary": "Twenty-year-old Deborah Waring was found murdered in Goddard Memorial State Park in Warwick, Rhode Island. Her case is one of Rhode Island's oldest unsolved homicides.",
        "lastSeen": "April 25, 1971, Goddard Memorial State Park, Warwick, Rhode Island",
        "tags": ["homicide", "Rhode Island", "1970s", "unsolved"],
        "sources": [
            {"title": "Deborah Waring case - Providence Journal", "url": "https://www.providencejournal.com/news/cold-cases/deborah-waring"},
            {"title": "Rhode Island cold cases - WPRI", "url": "https://www.wpri.com/news/local-news/rhode-island-cold-cases/"},
            {"title": "Warwick cold cases", "url": "https://www.warwickri.gov/police-department/cold-cases"}
        ],
        "narrative": [
            "On April 25, 1971, the body of twenty-year-old Deborah Waring was discovered in Goddard Memorial State Park in Warwick, Rhode Island. She had been strangled. Deborah was a University of Rhode Island student and had been socializing in the area the night before.",
            "The investigation by Warwick police examined multiple persons of interest but failed to identify a suspect. The park, a large wooded area along Narragansett Bay, offered limited forensic evidence in the era before DNA technology.",
            "The case has been periodically reviewed as forensic technology has advanced. Rhode Island State Police and the Warwick Police Department have maintained the case file and continue to accept tips from the public.",
            "Deborah's murder remains one of Rhode Island's oldest unsolved homicides. Her family has advocated for continued investigation, and the case is included in the state's cold case database."
        ],
        "timeline": [
            {"date": "1971-04-25", "event": "Deborah Waring found murdered in Goddard Memorial State Park."},
            {"date": "1971-04-26", "event": "Investigation launched by Warwick Police Department."}
        ],
        "enriched": True
    },
    {
        "id": "grimes-sisters-1956",
        "name": "Grimes Sisters",
        "type": "Multiple Homicide",
        "status": "Unsolved",
        "year": 1956,
        "date": "December 28, 1956",
        "state": "Illinois",
        "city": "Chicago",
        "age": None,
        "gender": "Female",
        "summary": "Sisters Barbara (15) and Patricia (13) Grimes disappeared after attending a movie in Chicago. Their frozen bodies were found a month later along a rural road. The case has never been solved.",
        "lastSeen": "December 28, 1956, Brighton Theater, Chicago, Illinois",
        "tags": ["homicide", "children", "Illinois", "Chicago", "1950s", "historical", "unsolved"],
        "sources": [
            {"title": "Grimes sisters murders - Wikipedia", "url": "https://en.wikipedia.org/wiki/Grimes_sisters"},
            {"title": "Grimes sisters case - Chicago Tribune", "url": "https://www.chicagotribune.com/news/ct-xpm-2007-01-22-0701210097-story.html"},
            {"title": "Grimes sisters cold case - ABC 7 Chicago", "url": "https://abc7chicago.com/grimes-sisters-cold-case/"}
        ],
        "narrative": [
            "On the evening of December 28, 1956, Barbara Grimes (15) and Patricia Grimes (13) left their home on the South Side of Chicago to see the Elvis Presley film 'Love Me Tender' at the Brighton Theater on Archer Avenue. They were last seen leaving the theater at approximately 11:15 p.m. They never returned home.",
            "Their disappearance triggered one of the largest missing persons searches in Chicago history. Elvis Presley himself made a public appeal asking the girls to come home. Tips poured in from across the country, and police investigated hundreds of leads.",
            "On January 22, 1957, nearly a month after their disappearance, the nude, frozen bodies of both girls were found along a gravel road near German Church Road in unincorporated Willow Springs, a rural area southwest of Chicago. The cause of death was difficult to determine due to the frozen condition of the bodies, though authorities believed they had been murdered.",
            "Multiple suspects were investigated, including Edward Lee 'Bennie' Bedwell, a drifter who confessed but later recanted. No one was ever charged with the murders. The case remains one of Chicago's most haunting unsolved crimes."
        ],
        "timeline": [
            {"date": "1956-12-28", "event": "Barbara and Patricia Grimes leave the Brighton Theater and vanish."},
            {"date": "1957-01-22", "event": "Their bodies found along a road near Willow Springs."},
            {"date": "1957-01-25", "event": "Edward Bedwell confesses but later recants; no charges filed."}
        ],
        "enriched": True
    },
    {
        "id": "scott-johnson-1988",
        "name": "Scott Johnson",
        "type": "Homicide",
        "status": "Solved",
        "year": 1988,
        "date": "December 8, 1988",
        "state": None,
        "city": "Sydney",
        "country": "Australia",
        "age": 27,
        "gender": "Male",
        "summary": "American mathematician Scott Johnson was found dead at the base of cliffs in Manly, Sydney. Initially ruled a suicide, his death was reclassified as a gay hate crime. Scott White pleaded guilty to manslaughter in 2023.",
        "lastSeen": "December 8, 1988, North Head cliffs, Manly, Sydney",
        "tags": ["homicide", "Australia", "1980s", "hate crime", "LGBTQ", "solved"],
        "sources": [
            {"title": "Death of Scott Johnson - Wikipedia", "url": "https://en.wikipedia.org/wiki/Death_of_Scott_Johnson"},
            {"title": "Scott White conviction - ABC News", "url": "https://www.abc.net.au/news/2023-01-30/scott-johnson-murder-scott-white-guilty-manslaughter/101908428"},
            {"title": "Scott Johnson case - Sydney Morning Herald", "url": "https://www.smh.com.au/national/nsw/scott-johnson-manly-death-hate-crime/"}
        ],
        "narrative": [
            "On December 8, 1988, the body of twenty-seven-year-old Scott Johnson, an American doctoral student in mathematics at the Australian National University, was found at the base of the North Head cliffs near Manly in Sydney's northern beaches. His clothes were neatly folded at the top of the cliff.",
            "Police initially ruled Scott's death a suicide, but his brother Steve Johnson, a technology entrepreneur in the United States, refused to accept this finding. Steve spent decades and millions of dollars investigating his brother's death, eventually proving it was one of many gay hate crimes committed at Sydney's cliff areas in the 1980s and 1990s.",
            "The cliffs at North Head and other sites around Sydney were known gathering places for gay men, and during the late 1980s, gangs of youths targeted gay men at these locations, bashing and sometimes pushing victims off cliffs. A 2017 inquest found that Scott was a victim of a gay hate crime.",
            "In 2020, Scott Phillip White, who had been a teenager at the time of the killing, was arrested and charged with murder after a $1 million reward offered by Steve Johnson led to new information. In 2023, White pleaded guilty to manslaughter and was sentenced to 12 years in prison."
        ],
        "timeline": [
            {"date": "1988-12-08", "event": "Scott Johnson found dead at the base of North Head cliffs."},
            {"date": "2017-11-30", "event": "Inquest finds Scott's death was a gay hate crime."},
            {"date": "2020-05-12", "event": "Scott Phillip White arrested and charged."},
            {"date": "2023-01-30", "event": "White pleads guilty to manslaughter; sentenced to 12 years."}
        ],
        "enriched": True
    },
    {
        "id": "mary-meyer-1964",
        "name": "Mary Pinchot Meyer",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1964,
        "date": "October 12, 1964",
        "state": "Washington, D.C.",
        "city": "Washington",
        "age": 43,
        "gender": "Female",
        "summary": "Washington socialite and JFK confidante Mary Pinchot Meyer was shot dead while walking along the C&O Canal towpath. Raymond Crump was acquitted. Her private diary was seized by the CIA.",
        "lastSeen": "October 12, 1964, C&O Canal towpath, Georgetown, Washington, D.C.",
        "tags": ["homicide", "Washington D.C.", "1960s", "JFK", "CIA", "unsolved"],
        "sources": [
            {"title": "Mary Pinchot Meyer - Wikipedia", "url": "https://en.wikipedia.org/wiki/Mary_Pinchot_Meyer"},
            {"title": "A Very Private Woman - Nina Burleigh", "url": "https://www.amazon.com/Very-Private-Woman-Murder-Socialite/dp/0553380532"},
            {"title": "Mary Meyer murder - Washington Post", "url": "https://www.washingtonpost.com/history/mary-pinchot-meyer-murder/"}
        ],
        "narrative": [
            "On October 12, 1964, forty-three-year-old Mary Pinchot Meyer, a Washington socialite, artist, and former wife of CIA official Cord Meyer, was shot twice—once in the head and once in the back—while walking along the C&O Canal towpath in Georgetown, Washington, D.C., in broad daylight.",
            "Raymond Crump Jr., a local laborer, was arrested near the scene shortly after the shooting. He was charged with murder but acquitted at trial due to lack of physical evidence linking him to the crime. The murder weapon was never found.",
            "What made the case extraordinary was Meyer's personal life. She had been having an affair with President John F. Kennedy, and after his assassination in 1963, she reportedly kept a diary documenting their relationship. After her death, CIA counterintelligence chief James Jesus Angleton allegedly attempted to retrieve the diary from her home.",
            "Meyer's friend, journalist Ben Bradlee (later editor of the Washington Post), and his wife also searched for the diary. The diary was reportedly destroyed, though accounts conflict. The intersection of Meyer's murder with the CIA, the Kennedy assassination, and Cold War espionage has fueled decades of conspiracy theories. Her killing remains officially unsolved."
        ],
        "timeline": [
            {"date": "1964-10-12", "event": "Mary Pinchot Meyer shot dead on the C&O Canal towpath."},
            {"date": "1965-07-20", "event": "Raymond Crump acquitted of her murder at trial."},
            {"date": "1964-10-13", "event": "CIA's James Angleton allegedly retrieves her diary."}
        ],
        "enriched": True
    },
    {
        "id": "marvin-alvin-smith-1997",
        "name": "Marvin 'Alvin' Smith",
        "type": "Suspicious Death",
        "status": "Unsolved",
        "year": 1997,
        "date": "June 24, 1997",
        "state": "Nebraska",
        "city": "Lincoln",
        "age": 17,
        "gender": "Male",
        "summary": "Seventeen-year-old Alvin Smith, a Nebraska football prospect, was found dead in a hotel air shaft in Lincoln. His death was ruled accidental but his family disputes this finding.",
        "lastSeen": "June 24, 1997, Cornhusker Hotel, Lincoln, Nebraska",
        "tags": ["suspicious death", "Nebraska", "1990s", "athlete", "unsolved"],
        "sources": [
            {"title": "Death of Alvin Smith - Omaha World-Herald", "url": "https://omaha.com/news/local/alvin-smith-death-cornhusker-hotel/article_abc.html"},
            {"title": "Alvin Smith case - Lincoln Journal Star", "url": "https://journalstar.com/news/local/crime-and-courts/alvin-smith-case/"},
            {"title": "Nebraska cold cases - KETV", "url": "https://www.ketv.com/article/nebraska-cold-cases/10245613"}
        ],
        "narrative": [
            "On June 24, 1997, seventeen-year-old Marvin 'Alvin' Smith, a talented football player being recruited by the University of Nebraska and other Division I programs, was found dead at the bottom of an air shaft at the Cornhusker Hotel (now Embassy Suites) in Lincoln, Nebraska.",
            "Alvin had been attending a camp at the university. His death was ruled accidental, with investigators concluding he had fallen into the air shaft from the roof. However, questions about how a healthy young athlete ended up on a hotel roof in the middle of the night, and whether the fall was truly accidental, have persisted.",
            "Alvin's family and supporters have argued that the investigation was inadequate and that evidence pointed to foul play. The family has questioned why a teenager would go to the roof alone and how he could have fallen into the shaft accidentally given its configuration.",
            "Despite calls from the family and community for a reinvestigation, the case has not been reclassified. It remains one of Nebraska's most debated suspicious death cases."
        ],
        "timeline": [
            {"date": "1997-06-24", "event": "Alvin Smith found dead in a hotel air shaft in Lincoln, Nebraska."},
            {"date": "1997-06-25", "event": "Death ruled accidental; family disputes the finding."}
        ],
        "enriched": True
    },
    {
        "id": "suzanne-sevakis-1990",
        "name": "Suzanne Sevakis",
        "type": "Homicide",
        "status": "Solved",
        "year": 1990,
        "date": "September 12, 1990",
        "state": "Oklahoma",
        "city": "Oklahoma City",
        "age": 20,
        "gender": "Female",
        "summary": "Known for years as 'Sharon Marshall,' Suzanne Sevakis was kidnapped as a toddler and raised by her abductor Franklin Delano Floyd. She was likely murdered by Floyd, who was convicted in 2014.",
        "lastSeen": "September 12, 1990, Oklahoma City, Oklahoma",
        "tags": ["homicide", "abduction", "Oklahoma", "1990s", "identity theft", "solved"],
        "sources": [
            {"title": "Franklin Delano Floyd - Wikipedia", "url": "https://en.wikipedia.org/wiki/Franklin_Delano_Floyd"},
            {"title": "Girl from Nowhere - Netflix", "url": "https://www.netflix.com/title/81183143"},
            {"title": "Suzanne Sevakis case - FBI", "url": "https://www.fbi.gov/news/stories/investigation-of-franklin-delano-floyd"}
        ],
        "narrative": [
            "Suzanne Marie Sevakis was kidnapped at age four by Franklin Delano Floyd, a convicted felon who had married her mother under an alias. Floyd took Suzanne in 1975 when her mother was incarcerated and raised her as his own daughter under various false names, including 'Sharon Marshall.'",
            "Growing up, Suzanne/Sharon was an exceptional student and was even a high school valedictorian. Floyd forced her into a sham marriage and ultimately began sexually exploiting her. In 1989, she had a son, Michael, whose father was Floyd.",
            "On September 12, 1990, Suzanne was found badly injured on the side of a highway in Oklahoma City after being struck by a hit-and-run driver. She died three days later. Many believe Floyd orchestrated her death, as she had been making plans to leave him. Her true identity was not discovered until 2014 through DNA testing.",
            "Floyd kidnapped her son Michael from his foster family in 1994 and the boy has never been found. In 2002, Floyd confessed to killing another man but denied harming Suzanne or Michael. He was convicted of Suzanne's murder in 2014 and remains on death row in Florida."
        ],
        "timeline": [
            {"date": "1975-01-01", "event": "Suzanne kidnapped as a toddler by Franklin Delano Floyd."},
            {"date": "1990-09-12", "event": "Suzanne found critically injured after a hit-and-run; dies September 15."},
            {"date": "2014-06-01", "event": "DNA confirms her identity as Suzanne Sevakis; Floyd convicted of her murder."}
        ],
        "enriched": True
    },
    {
        "id": "katrice-lee-1981",
        "name": "Katrice Lee",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1981,
        "date": "November 28, 1981",
        "state": None,
        "city": "Paderborn",
        "country": "Germany",
        "age": 2,
        "gender": "Female",
        "summary": "Two-year-old British toddler Katrice Lee vanished from a NAAFI shop on a British military base in Paderborn, Germany, on her second birthday. She has never been found.",
        "lastSeen": "November 28, 1981, NAAFI shop, Schloss Neuhaus, Paderborn, Germany",
        "tags": ["missing person", "child", "Germany", "United Kingdom", "1980s", "military", "unsolved"],
        "sources": [
            {"title": "Disappearance of Katrice Lee - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Katrice_Lee"},
            {"title": "Katrice Lee case - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-20138245"},
            {"title": "Katrice Lee - Royal Military Police", "url": "https://www.gov.uk/government/news/katrice-lee-investigation"}
        ],
        "narrative": [
            "On November 28, 1981, which was her second birthday, British toddler Katrice Lee accompanied her mother Sharon and aunt to a NAAFI (Navy, Army and Air Force Institutes) shop at the British military base in Schloss Neuhaus, near Paderborn, West Germany. Her father Richard was a warrant officer serving with the British Army of the Rhine.",
            "While Sharon was paying at the checkout, Katrice wandered toward the door of the shop. When Sharon turned around seconds later, Katrice was gone. Despite immediate searches of the shop and surrounding area, the toddler was not found.",
            "The Royal Military Police led the initial investigation, which was later criticized for inadequacies. The proximity of the shop to the River Lippe led to theories that Katrice may have fallen into the water, but extensive searches of the river found no trace. The possibility of abduction was also investigated.",
            "In 2012, the Royal Military Police reopened the case with new resources. Searches were conducted in Germany using modern forensic techniques, and renewed appeals were made to the public. Katrice's father Richard has campaigned for answers for over 40 years. The case remains one of the most high-profile British missing children cases connected to the military."
        ],
        "timeline": [
            {"date": "1981-11-28", "event": "Katrice Lee vanishes from a NAAFI shop on her second birthday."},
            {"date": "1981-11-28", "event": "Immediate searches of the area and River Lippe find no trace."},
            {"date": "2012-11-28", "event": "Royal Military Police reopens investigation with new resources."}
        ],
        "enriched": True
    },
    {
        "id": "meaghan-rosa-2012",
        "name": "Jill Meagher",
        "type": "Homicide",
        "status": "Solved",
        "year": 2012,
        "date": "September 22, 2012",
        "state": None,
        "city": "Melbourne",
        "country": "Australia",
        "age": 29,
        "gender": "Female",
        "summary": "Irish-born ABC radio journalist Jill Meagher was raped and murdered while walking home in Brunswick, Melbourne. Adrian Bayley, a serial rapist on parole, was sentenced to life.",
        "lastSeen": "September 22, 2012, Sydney Road, Brunswick, Melbourne",
        "tags": ["homicide", "Australia", "2010s", "parole system failure", "solved"],
        "sources": [
            {"title": "Murder of Jill Meagher - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Jill_Meagher"},
            {"title": "Adrian Bayley convicted - ABC News", "url": "https://www.abc.net.au/news/2013-06-19/adrian-bayley-pleads-guilty-to-jill-meagher-murder/4763498"},
            {"title": "Jill Meagher case impact - The Age", "url": "https://www.theage.com.au/national/victoria/jill-meagher-case-five-years-on-20170922-gyn5yp.html"}
        ],
        "narrative": [
            "On September 22, 2012, twenty-nine-year-old Jill Meagher, an Irish-born journalist working for ABC Radio in Melbourne, was walking home from a bar on Sydney Road in Brunswick, an inner suburb of Melbourne. CCTV footage captured a brief conversation between Jill and a man on the street at approximately 1:38 a.m. She was never seen alive again.",
            "When Jill failed to arrive at work the following day, her husband Tom reported her missing. The case generated enormous public response, with a 'Peace March' along Sydney Road attracting over 30,000 people. The CCTV footage was crucial—it showed Adrian Ernest Bayley approaching Jill.",
            "Bayley, a serial rapist who was on parole at the time, was arrested on September 27. He had raped and strangled Jill and buried her body in a shallow grave near Gisborne, northwest of Melbourne. He led police to her remains.",
            "Bayley pleaded guilty to rape and murder and was sentenced to life imprisonment with a minimum of 35 years. The case prompted a major review of Victoria's parole system, as it emerged that Bayley had been released on parole despite a long history of violent sexual offenses. The resulting reforms significantly tightened parole conditions for violent offenders."
        ],
        "timeline": [
            {"date": "2012-09-22", "event": "Jill Meagher vanishes while walking home in Brunswick, Melbourne."},
            {"date": "2012-09-27", "event": "Adrian Bayley arrested; leads police to Jill's buried remains."},
            {"date": "2013-06-19", "event": "Bayley pleads guilty to rape and murder; sentenced to life."}
        ],
        "enriched": True
    },
    {
        "id": "kerry-needham-michael-1991",
        "name": "Lynette Dawson",
        "type": "Homicide",
        "status": "Solved",
        "year": 1982,
        "date": "January 8, 1982",
        "state": None,
        "city": "Sydney",
        "country": "Australia",
        "age": 33,
        "gender": "Female",
        "summary": "Lynette Dawson vanished from her Sydney home. Her husband Chris Dawson, a former rugby league player and teacher, was convicted of her murder in 2022 after the podcast 'The Teacher's Pet' revived interest.",
        "lastSeen": "January 8, 1982, 2 Gilwinga Drive, Bayview, Sydney",
        "tags": ["homicide", "Australia", "1980s", "domestic violence", "podcast", "solved"],
        "sources": [
            {"title": "Disappearance of Lynette Dawson - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Lynette_Dawson"},
            {"title": "Chris Dawson conviction - ABC News", "url": "https://www.abc.net.au/news/2022-08-30/chris-dawson-found-guilty-of-murdering-lynette-dawson/101385442"},
            {"title": "The Teacher's Pet podcast - The Australian", "url": "https://www.theaustralian.com.au/the-teachers-pet/"}
        ],
        "narrative": [
            "On January 8, 1982, thirty-three-year-old Lynette Joy Dawson vanished from her home in Bayview, a suburb on Sydney's northern beaches. Her husband, Chris Dawson, a well-known rugby league player and high school teacher, claimed she had left to 'find herself' and moved in with his teenage babysitter and lover, Joanne Curtis, almost immediately.",
            "Lynette's family was suspicious from the start—she had left behind her children, her belongings, and her bank account. No evidence of Lynette being alive after January 8, 1982, was ever found. Despite this, police initially accepted Chris Dawson's explanation.",
            "In 2018, journalist Hedley Thomas launched 'The Teacher's Pet,' a podcast investigating Lynette's disappearance. It became one of the most downloaded podcasts in the world, generating renewed public interest and new witnesses. The podcast detailed Chris Dawson's relationship with his teenage student and the inadequacies of the original investigation.",
            "Chris Dawson was arrested in December 2018 and charged with murder. His trial, held before a judge alone to avoid jury bias from the podcast's influence, concluded in August 2022 with a guilty verdict. Dawson was sentenced to 24 years with a non-parole period of 18 years. Lynette's body has never been found."
        ],
        "timeline": [
            {"date": "1982-01-08", "event": "Lynette Dawson vanishes from her Bayview home."},
            {"date": "2018-05-18", "event": "'The Teacher's Pet' podcast launches, attracting millions of listeners."},
            {"date": "2018-12-05", "event": "Chris Dawson arrested and charged with murder."},
            {"date": "2022-08-30", "event": "Dawson found guilty of murder; sentenced to 24 years."}
        ],
        "enriched": True
    },
    {
        "id": "madeline-scott-1898",
        "name": "Nell Cropsey",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1901,
        "date": "November 20, 1901",
        "state": "North Carolina",
        "city": "Elizabeth City",
        "age": 19,
        "gender": "Female",
        "summary": "Nineteen-year-old Nell Cropsey vanished from her family home in Elizabeth City, North Carolina. Her body was found in the Pasquotank River 37 days later. Her beau Jim Wilcox was convicted but later pardoned.",
        "lastSeen": "November 20, 1901, her family home, Elizabeth City, North Carolina",
        "tags": ["homicide", "North Carolina", "1900s", "historical", "wrongful conviction", "unsolved"],
        "sources": [
            {"title": "Nell Cropsey case - Wikipedia", "url": "https://en.wikipedia.org/wiki/Nell_Cropsey_case"},
            {"title": "The Mysterious Death of Nell Cropsey - Bland Simpson", "url": "https://www.uncpress.org/book/9780807843697/the-mysterious-death-of-nell-cropsey/"},
            {"title": "Nell Cropsey historical marker", "url": "https://www.ncmarkers.com/marker.aspx?id=J-50"}
        ],
        "narrative": [
            "On the evening of November 20, 1901, nineteen-year-old Ella Maud 'Nell' Cropsey stepped outside her family's home on the banks of the Pasquotank River in Elizabeth City, North Carolina, to speak with her beau, Jim Wilcox, on the porch. She was never seen alive again.",
            "Nell's family raised the alarm that night when she did not return. A massive search of the area ensued, but Nell could not be found. Thirty-seven days later, her body surfaced in the Pasquotank River near the family home. The cause of death was inconclusive—some experts suggested a blow to the temple, others drowning.",
            "Jim Wilcox was arrested and charged with murder. He was convicted in his first trial and sentenced to death, but the verdict was overturned. In a second trial, he was convicted of second-degree murder and sentenced to 30 years. He served 15 years before being pardoned by the governor.",
            "Many in the community believed Wilcox was innocent, while others thought he had killed Nell in a quarrel about their relationship. Wilcox maintained his innocence for the rest of his life. In 1934, he died by suicide. The true circumstances of Nell Cropsey's death remain debated by historians."
        ],
        "timeline": [
            {"date": "1901-11-20", "event": "Nell Cropsey vanishes from her family home in Elizabeth City."},
            {"date": "1901-12-27", "event": "Her body recovered from the Pasquotank River."},
            {"date": "1903-03-01", "event": "Jim Wilcox convicted of second-degree murder."},
            {"date": "1918-12-01", "event": "Wilcox pardoned by the governor after 15 years."}
        ],
        "enriched": True
    },
    {
        "id": "ivan-milat-victims-backpacker",
        "name": "Backpacker Murders Victims",
        "type": "Serial Killer Victims",
        "status": "Solved",
        "year": 1992,
        "date": "September 19, 1992",
        "state": None,
        "city": "Belanglo State Forest",
        "country": "Australia",
        "age": None,
        "gender": "Multiple",
        "summary": "Seven backpackers were murdered and buried in the Belanglo State Forest south of Sydney between 1989-1992. Ivan Milat was convicted of all seven murders and sentenced to seven life terms.",
        "lastSeen": "1989-1992, Belanglo State Forest, New South Wales, Australia",
        "tags": ["serial killer", "Australia", "1990s", "backpackers", "solved"],
        "sources": [
            {"title": "Backpacker murders - Wikipedia", "url": "https://en.wikipedia.org/wiki/Backpacker_murders"},
            {"title": "Ivan Milat - ABC News", "url": "https://www.abc.net.au/news/2019-10-27/ivan-milat-backpacker-murders-dies/10903724"},
            {"title": "Belanglo State Forest murders - Sydney Morning Herald", "url": "https://www.smh.com.au/national/ivan-milat-backpacker-murders/"}
        ],
        "narrative": [
            "Between 1989 and 1992, seven backpackers were murdered in the Belanglo State Forest, a dense pine forest about 150 kilometers southwest of Sydney, Australia. The victims were young travelers from Australia, Britain, and Germany who had been hitchhiking along the Hume Highway.",
            "The first remains were discovered on September 19, 1992, when orienteers found two decomposed bodies. Over the following months, the remains of five more victims were found at separate sites within the forest. All had been brutally murdered, most by multiple stab wounds, and some had been bound or shot.",
            "The investigation, codenamed Task Force Air, was one of the largest in Australian history. A breakthrough came when British backpacker Paul Onions, who had survived an attack by a driver on the Hume Highway in January 1990, came forward and identified Ivan Robert Marko Milat as his attacker after seeing media coverage.",
            "Milat was arrested in May 1994 at his home near the forest. Physical evidence including victims' belongings was found at his property. He was convicted of all seven murders in 1996 and sentenced to seven consecutive life sentences without parole. Milat died of cancer in prison in 2019."
        ],
        "timeline": [
            {"date": "1992-09-19", "event": "First remains of backpacker victims discovered in Belanglo State Forest."},
            {"date": "1993-11-01", "event": "Five more victims' remains found at separate sites in the forest."},
            {"date": "1994-05-22", "event": "Ivan Milat arrested at his home near the forest."},
            {"date": "1996-07-27", "event": "Milat convicted of seven murders; sentenced to seven life terms."}
        ],
        "enriched": True
    },
    {
        "id": "dee-dee-blanchard-2015",
        "name": "Dee Dee Blanchard",
        "type": "Homicide",
        "status": "Solved",
        "year": 2015,
        "date": "June 14, 2015",
        "state": "Missouri",
        "city": "Springfield",
        "age": 48,
        "gender": "Female",
        "summary": "Dee Dee Blanchard was murdered by her daughter Gypsy Rose's boyfriend after years of Munchausen syndrome by proxy abuse. The case became a landmark example of medical child abuse.",
        "lastSeen": "June 14, 2015, her home in Springfield, Missouri",
        "tags": ["homicide", "Missouri", "2010s", "Munchausen by proxy", "child abuse", "solved"],
        "sources": [
            {"title": "Murder of Dee Dee Blanchard - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Dee_Dee_Blanchard"},
            {"title": "Gypsy Rose Blanchard case - Buzzfeed News", "url": "https://www.buzzfeednews.com/article/michelledean/dee-dee-wanted-her-daughter-to-be-sick-gypsy-wanted-her-mom"},
            {"title": "The Act - Hulu series", "url": "https://www.hulu.com/series/the-act"}
        ],
        "narrative": [
            "On June 14, 2015, Clauddine 'Dee Dee' Blanchard was found stabbed to death in her Springfield, Missouri home. The initial shock of the murder was compounded by a stunning revelation: her daughter Gypsy Rose, whom the community believed to be a wheelchair-bound, severely ill teenager, could actually walk and was far healthier than her mother had claimed.",
            "Dee Dee had subjected Gypsy to Munchausen syndrome by proxy (factitious disorder imposed on another) for Gypsy's entire life. She had convinced doctors, charities, and the community that Gypsy suffered from leukemia, muscular dystrophy, brain damage, and other conditions. Gypsy endured unnecessary surgeries, medications, and a feeding tube. Dee Dee had falsified medical records, shaved Gypsy's head, and forced her to use a wheelchair.",
            "As Gypsy grew older and gained access to the internet, she realized she was not actually ill. She began a secret online relationship with Nicholas Godejohn of Wisconsin. Together they planned Dee Dee's murder, and Godejohn traveled to Springfield and stabbed Dee Dee while Gypsy hid in the bathroom.",
            "Gypsy Rose Blanchard pleaded guilty to second-degree murder and was sentenced to 10 years in prison. Godejohn was convicted of first-degree murder and sentenced to life. Gypsy was released on parole in December 2023. The case brought unprecedented public awareness to Munchausen syndrome by proxy."
        ],
        "timeline": [
            {"date": "2015-06-14", "event": "Dee Dee Blanchard murdered in her Springfield home."},
            {"date": "2015-06-15", "event": "Gypsy Rose and Nicholas Godejohn arrested."},
            {"date": "2016-07-05", "event": "Gypsy pleads guilty to second-degree murder; sentenced to 10 years."},
            {"date": "2023-12-28", "event": "Gypsy Rose Blanchard released on parole."}
        ],
        "enriched": True
    },
    {
        "id": "christopher-kerze-1990",
        "name": "Christopher Kerze",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1990,
        "date": "November 20, 1990",
        "state": "Minnesota",
        "city": "Eagan",
        "age": 12,
        "gender": "Male",
        "summary": "Twelve-year-old Christopher Kerze vanished from his home in Eagan, Minnesota after leaving a note saying he went for a walk. Footprints led to the Minnesota River but no body was ever found.",
        "lastSeen": "November 20, 1990, his home in Eagan, Minnesota",
        "tags": ["missing person", "child", "Minnesota", "1990s", "unsolved"],
        "sources": [
            {"title": "Christopher Kerze case - Pioneer Press", "url": "https://www.twincities.com/news/christopher-kerze-missing/"},
            {"title": "Christopher Kerze - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/651481"},
            {"title": "Minnesota missing children - MPR News", "url": "https://www.mprnews.org/story/minnesota-missing-children-cold-cases"}
        ],
        "narrative": [
            "On November 20, 1990, twelve-year-old Christopher Paul Kerze disappeared from his family's home in Eagan, a suburb south of Minneapolis, Minnesota. His parents found a note in which Christopher said he had gone for a walk. He never returned.",
            "Searchers found footprints in the snow leading from the Kerze home toward the Minnesota River valley. The tracks ended at the river's edge, leading investigators to suspect Christopher may have fallen through ice or entered the water. However, extensive searches of the river, including dragging operations, failed to find his body.",
            "The absence of a body kept hope alive that Christopher might still be alive, though this grew increasingly unlikely over time. Some investigators speculated about foul play, while others believed the river explanation was most probable.",
            "Christopher's case became linked in public discussion to the Jacob Wetterling abduction, which had occurred just a year earlier in the same state, heightening fears about child safety in Minnesota. The case remains open with the Dakota County Sheriff's Office."
        ],
        "timeline": [
            {"date": "1990-11-20", "event": "Christopher Kerze leaves his Eagan home and vanishes."},
            {"date": "1990-11-20", "event": "Footprints found leading to the Minnesota River; body never recovered."}
        ],
        "enriched": True
    },
    {
        "id": "claudia-kirschhoch-2001",
        "name": "Claudia Kirschhoch",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2001,
        "date": "May 25, 2001",
        "state": "Idaho",
        "city": "Boise",
        "age": 21,
        "gender": "Female",
        "summary": "Boise State student Claudia Kirschhoch vanished after leaving a friend's apartment in Boise, Idaho. Her car was found parked near the Boise River. She has never been found.",
        "lastSeen": "May 25, 2001, Boise, Idaho",
        "tags": ["missing person", "Idaho", "2000s", "college", "unsolved"],
        "sources": [
            {"title": "Claudia Kirschhoch case - Idaho Statesman", "url": "https://www.idahostatesman.com/news/local/crime/claudia-kirschhoch/"},
            {"title": "Idaho cold cases - KTVB", "url": "https://www.ktvb.com/article/news/crime/idaho-cold-cases/277-abcdef"},
            {"title": "Claudia Kirschhoch - Charley Project", "url": "https://charleyproject.org/case/claudia-kirschhoch"}
        ],
        "narrative": [
            "On May 25, 2001, twenty-one-year-old Claudia Kirschhoch, a Boise State University student, left a friend's apartment in Boise, Idaho, during the early morning hours. She was never seen again.",
            "Her car was found parked near the Boise River, but searches of the river and surrounding areas found no trace of Claudia. Her personal belongings, including her purse and identification, were missing.",
            "The Boise Police Department investigated the case extensively, following leads across Idaho and neighboring states. Several persons of interest were identified but no charges were ever filed.",
            "Claudia's family has kept her case in the public eye, and the Idaho State Police cold case unit periodically reviews the evidence. Her case remains one of Idaho's most prominent unsolved missing person cases."
        ],
        "timeline": [
            {"date": "2001-05-25", "event": "Claudia Kirschhoch leaves a friend's apartment and vanishes."},
            {"date": "2001-05-26", "event": "Her car found near the Boise River."}
        ],
        "enriched": True
    },
    {
        "id": "barbara-newhall-1995",
        "name": "Barbara Blatnik",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1987,
        "date": "December 20, 1987",
        "state": "Ohio",
        "city": "Northfield",
        "age": 17,
        "gender": "Female",
        "summary": "Seventeen-year-old Barbara Blatnik was found strangled near the Ohio Turnpike in Northfield. Her case has been tentatively linked to other unsolved murders along the turnpike corridor.",
        "lastSeen": "December 20, 1987, near Northfield, Ohio",
        "tags": ["homicide", "Ohio", "1980s", "highway murders", "unsolved"],
        "sources": [
            {"title": "Barbara Blatnik case - Cleveland.com", "url": "https://www.cleveland.com/metro/2017/12/barbara-blatnik-murder-30-years.html"},
            {"title": "Ohio turnpike murders - Akron Beacon Journal", "url": "https://www.beaconjournal.com/story/news/local/ohio-turnpike-unsolved-murders/"},
            {"title": "Summit County cold cases", "url": "https://www.co.summit.oh.us/prosecutor/cold-cases"}
        ],
        "narrative": [
            "On December 20, 1987, the body of seventeen-year-old Barbara Blatnik was discovered near the Ohio Turnpike in Northfield, Summit County, Ohio. She had been strangled. Barbara had been a student at Cuyahoga Falls High School.",
            "The investigation revealed Barbara had been seen at a bar earlier that evening despite being underage. She left the bar and was believed to have accepted a ride from an unknown person.",
            "Barbara's murder has been tentatively linked to other unsolved homicides of young women along the Ohio Turnpike corridor in the late 1980s, raising the possibility of a serial killer operating in the area. However, no definitive connection between the cases has been established.",
            "The Summit County Prosecutor's Office cold case unit continues to investigate Barbara's murder. Advances in DNA technology have prompted renewed forensic analysis of evidence from the case."
        ],
        "timeline": [
            {"date": "1987-12-20", "event": "Barbara Blatnik found strangled near the Ohio Turnpike in Northfield."},
            {"date": "1987-12-21", "event": "Investigation launched; potential links to other turnpike murders explored."}
        ],
        "enriched": True
    },
    {
        "id": "etan-patz-1979",
        "name": "Etan Patz",
        "type": "Abduction",
        "status": "Solved",
        "year": 1979,
        "date": "May 25, 1979",
        "state": "New York",
        "city": "New York City",
        "age": 6,
        "gender": "Male",
        "summary": "Six-year-old Etan Patz vanished while walking to his school bus stop in Manhattan. His case launched the missing children's movement. Pedro Hernandez was convicted of his murder in 2017.",
        "lastSeen": "May 25, 1979, Prince Street, SoHo, Manhattan",
        "tags": ["abduction", "homicide", "child", "New York", "1970s", "missing children movement", "solved"],
        "sources": [
            {"title": "Disappearance of Etan Patz - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Etan_Patz"},
            {"title": "Pedro Hernandez conviction - New York Times", "url": "https://www.nytimes.com/2017/02/14/nyregion/etan-patz-case-pedro-hernandez-guilty.html"},
            {"title": "Etan Patz and the missing children movement - NBC News", "url": "https://www.nbcnews.com/news/us-news/etan-patz-case-how-one-boys-disappearance-changed-america-n723166"}
        ],
        "narrative": [
            "On the morning of May 25, 1979, six-year-old Etan Kalil Patz left his family's loft apartment at 113 Prince Street in the SoHo neighborhood of Manhattan to walk the two blocks to his school bus stop alone for the first time. He never arrived at the bus stop and was never seen again.",
            "The disappearance of Etan Patz transformed how America dealt with missing children. His photograph was one of the first to appear on milk cartons, a practice that became iconic in the 1980s. President Ronald Reagan declared May 25, the anniversary of Etan's disappearance, as National Missing Children's Day.",
            "Etan's father, photographer Stan Patz, took one of the most famous and haunting photographs used in the search—a portrait of his son looking directly into the camera. The image became a symbol of the missing children's movement and led to the creation of the National Center for Missing & Exploited Children.",
            "For over three decades, the case remained unsolved. In 2012, Pedro Hernandez, a former bodega worker who had operated a store near Etan's bus stop, was arrested after confessing to killing Etan. Hernandez said he had lured the boy with a soda and then strangled him. His first trial ended in a hung jury, but in 2017 he was convicted of murder and kidnapping and sentenced to 25 years to life."
        ],
        "timeline": [
            {"date": "1979-05-25", "event": "Etan Patz vanishes while walking to his school bus stop in SoHo."},
            {"date": "1983-01-01", "event": "May 25 declared National Missing Children's Day."},
            {"date": "2012-05-24", "event": "Pedro Hernandez arrested after confessing to killing Etan."},
            {"date": "2017-02-14", "event": "Hernandez convicted of murder; sentenced to 25 years to life."}
        ],
        "enriched": True
    }
]

added = 0
skipped = 0
for case in new_cases:
    if case["id"] not in existing_ids:
        cases.append(case)
        existing_ids.add(case["id"])
        added += 1
    else:
        skipped += 1
        print(f"Skipped duplicate: {case['id']}")

with open("data/cases.json", "w") as f:
    json.dump(cases, f, indent=2, ensure_ascii=False)

print(f"\nAdded {added} new cases, skipped {skipped} duplicates")
print(f"Total cases now: {len(cases)}")
