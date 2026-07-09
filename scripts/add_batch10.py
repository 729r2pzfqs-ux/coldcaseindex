#!/usr/bin/env python3
import json

with open("data/cases.json", "r") as f:
    cases = json.load(f)

existing_ids = set(c["id"] for c in cases)

new_cases = [
    {
        "id": "beaumont-children-1966",
        "name": "Beaumont Children",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1966,
        "date": "January 26, 1966",
        "state": None,
        "city": "Glenelg",
        "country": "Australia",
        "age": None,
        "gender": "Multiple",
        "summary": "Jane (9), Arnna (7), and Grant (4) Beaumont vanished from Glenelg Beach in Adelaide, South Australia. Despite one of Australia's largest investigations, the children were never found.",
        "lastSeen": "January 26, 1966, Glenelg Beach, Adelaide, South Australia",
        "tags": ["missing person", "children", "Australia", "1960s", "abduction", "unsolved"],
        "sources": [
            {"title": "Beaumont children disappearance - Wikipedia", "url": "https://en.wikipedia.org/wiki/Beaumont_children_disappearance"},
            {"title": "The Beaumont Children - Australian Federal Police", "url": "https://www.afp.gov.au/news-centre/media-release/beaumont-children"},
            {"title": "Beaumont children case - ABC News Australia", "url": "https://www.abc.net.au/news/2016-01-26/beaumont-children-disappearance-50th-anniversary/7113382"}
        ],
        "narrative": [
            "On Australia Day, January 26, 1966, Jane Beaumont (9), Arnna Beaumont (7), and Grant Beaumont (4) left their home in Somerton Park, Adelaide, to catch a bus to nearby Glenelg Beach, a trip they had made many times before. Their mother, Nancy Beaumont, expected them home by noon, but they never returned.",
            "Witnesses reported seeing the three children at the beach with a tall, thin, blond man in his mid-thirties. The children appeared to be comfortable with the man, laughing and playing. A shopkeeper reported that Jane had purchased pastries and a meat pie with a one-pound note, far more money than the children had been given by their mother, suggesting the man had given them money.",
            "When the children failed to return home, their father Jim drove to the beach to search for them but found no trace. Police were called and a massive search was launched. Despite extensive investigations spanning decades, hundreds of leads, and multiple suspects, the Beaumont children were never found. The case profoundly changed Australian attitudes toward child safety and remains the country's most infamous missing persons case.",
            "Several suspects have been investigated over the years, including convicted child killer Bevan Spencer von Einem, but no charges have ever been laid in connection with the disappearance. In 2018, police excavated a factory site in Adelaide's western suburbs based on new information but found no remains. The case remains open and is periodically reviewed by South Australia Police."
        ],
        "timeline": [
            {"date": "1966-01-26", "event": "The three Beaumont children leave home for Glenelg Beach and vanish."},
            {"date": "1966-01-26", "event": "Witnesses see the children with an unknown man at the beach."},
            {"date": "1966-01-27", "event": "Massive search operation begins across Adelaide."},
            {"date": "2018-02-01", "event": "Police excavate a factory site in Adelaide but find no remains."}
        ],
        "enriched": True
    },
    {
        "id": "tamam-shud-1948",
        "name": "Somerton Man",
        "type": "Suspicious Death",
        "status": "Solved",
        "year": 1948,
        "date": "December 1, 1948",
        "state": None,
        "city": "Adelaide",
        "country": "Australia",
        "age": None,
        "gender": "Male",
        "summary": "An unidentified man was found dead on Somerton Beach, Adelaide, with a scrap of paper reading 'Tamám Shud' in his pocket. In 2022, DNA analysis identified him as Carl 'Charles' Webb, an electrical engineer from Melbourne.",
        "lastSeen": "December 1, 1948, Somerton Beach, Adelaide, South Australia",
        "tags": ["suspicious death", "unidentified", "Australia", "1940s", "espionage", "solved", "DNA"],
        "sources": [
            {"title": "Tamam Shud case - Wikipedia", "url": "https://en.wikipedia.org/wiki/Tamam_Shud_case"},
            {"title": "Somerton Man identified - ABC News", "url": "https://www.abc.net.au/news/2022-07-26/somerton-man-cold-case-identity-revealed/101272182"},
            {"title": "Somerton Man case solved - The Guardian", "url": "https://www.theguardian.com/australia-news/2022/jul/26/somerton-man-mystery-solved-identity-revealed"}
        ],
        "narrative": [
            "On the morning of December 1, 1948, a well-dressed man was found dead on Somerton Beach in Adelaide, South Australia. He was lying with his head resting against the seawall, legs extended and feet crossed. Despite extensive efforts, police could not identify him. All labels had been removed from his clothing, and he carried no identification.",
            "In a hidden pocket sewn into his trousers, investigators found a tiny scrap of paper with the printed words 'Tamám Shud,' meaning 'ended' or 'finished' in Persian, torn from the final page of a copy of the Rubaiyat of Omar Khayyam. The book from which the page was torn was eventually located, and on its back cover was a faint penciled code that has never been definitively deciphered.",
            "The case attracted theories involving Cold War espionage, poisoning, and secret identities. An autopsy found no clear cause of death, though poisoning was suspected. A phone number found in the book led to a nurse named Jessica Thomson, who denied knowing the man, though her behavior suggested otherwise.",
            "For over 70 years, the Somerton Man's identity remained one of Australia's greatest mysteries. In 2022, Professor Derek Abbott of the University of Adelaide, who had spent over a decade researching the case, announced that DNA analysis had identified the man as Carl 'Charles' Webb, an electrical engineer and instrument maker born in Melbourne in 1905. While the identity was finally resolved, the circumstances of his death remain unexplained."
        ],
        "timeline": [
            {"date": "1948-12-01", "event": "Unidentified man found dead on Somerton Beach."},
            {"date": "1949-01-14", "event": "A suitcase belonging to the man found at Adelaide Railway Station."},
            {"date": "1949-06-01", "event": "The 'Tamám Shud' scrap of paper discovered in a hidden pocket."},
            {"date": "2022-07-26", "event": "DNA analysis identifies the man as Carl 'Charles' Webb of Melbourne."}
        ],
        "enriched": True
    },
    {
        "id": "lord-lucan-1974",
        "name": "Lord Lucan",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1974,
        "date": "November 7, 1974",
        "state": None,
        "city": "London",
        "country": "United Kingdom",
        "age": 39,
        "gender": "Male",
        "summary": "Richard John Bingham, 7th Earl of Lucan, disappeared after the murder of his children's nanny Sandra Rivett. He was never found and was declared legally dead in 1999.",
        "lastSeen": "November 7, 1974, 46 Lower Belgrave Street, London",
        "tags": ["homicide", "missing person", "United Kingdom", "London", "aristocracy", "1970s", "fugitive"],
        "sources": [
            {"title": "Lord Lucan - Wikipedia", "url": "https://en.wikipedia.org/wiki/Lord_Lucan"},
            {"title": "Lord Lucan mystery - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-london-46143049"},
            {"title": "Murder of Sandra Rivett - The Guardian", "url": "https://www.theguardian.com/uk-news/2017/feb/03/lord-lucan-declared-dead-42-years-mystery"}
        ],
        "narrative": [
            "On the evening of November 7, 1974, Sandra Rivett, the 29-year-old nanny employed by Lord and Lady Lucan to care for their three children, was bludgeoned to death in the basement of 46 Lower Belgrave Street, Belgravia, London. Her body was found inside a canvas mail sack. Lady Lucan, Veronica, was also attacked and sustained severe head injuries but managed to escape to a nearby pub, where she cried out that her husband had murdered the nanny.",
            "Police believe that Lord Lucan, who was embroiled in a bitter custody battle with his estranged wife, had intended to kill Lady Lucan but mistakenly attacked the nanny in the darkened basement kitchen. When Lady Lucan came downstairs to investigate, he attacked her too, but she fought back and escaped.",
            "Lord Lucan drove to the home of friends in Uckfield, East Sussex, where he wrote letters claiming that he had interrupted an attacker in the basement and had been trying to help his wife. He then vanished. His car was later found abandoned at the port of Newhaven with bloodstains inside. Despite an international manhunt, Lord Lucan was never found.",
            "An inquest in 1975 named Lord Lucan as Sandra Rivett's murderer, the last time a coroner's jury was allowed to name a suspect. He was officially declared dead in 1999. Alleged sightings have been reported from Africa, Australia, South America, and elsewhere, but none have been confirmed. The case remains one of Britain's most famous unsolved mysteries."
        ],
        "timeline": [
            {"date": "1974-11-07", "event": "Sandra Rivett is murdered; Lady Lucan is attacked. Lord Lucan disappears."},
            {"date": "1974-11-08", "event": "Lord Lucan's car found abandoned at Newhaven port."},
            {"date": "1975-06-19", "event": "Inquest names Lord Lucan as Sandra Rivett's murderer."},
            {"date": "1999-12-11", "event": "Lord Lucan officially declared dead."}
        ],
        "enriched": True
    },
    {
        "id": "suzy-lamplugh-1986",
        "name": "Suzy Lamplugh",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1986,
        "date": "July 28, 1986",
        "state": None,
        "city": "London",
        "country": "United Kingdom",
        "age": 25,
        "gender": "Female",
        "summary": "Estate agent Suzy Lamplugh vanished after leaving her office to meet a client known as 'Mr. Kipper.' She was declared dead in 1994. Convicted murderer John Cannan is the prime suspect.",
        "lastSeen": "July 28, 1986, Fulham, London",
        "tags": ["missing person", "United Kingdom", "London", "1980s", "presumed dead", "unsolved"],
        "sources": [
            {"title": "Disappearance of Suzy Lamplugh - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Suzy_Lamplugh"},
            {"title": "Suzy Lamplugh case - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-36901838"},
            {"title": "Suzy Lamplugh Trust", "url": "https://www.suzylamplugh.org/about-suzy"}
        ],
        "narrative": [
            "On July 28, 1986, 25-year-old Susannah 'Suzy' Lamplugh, an estate agent working at Sturgis & Co. in Fulham, London, left her office at lunchtime to show a property at 37 Shorrolds Road to a client she had noted in her diary as 'Mr. Kipper.' She was never seen again.",
            "Suzy's white Ford Fiesta was found abandoned about a mile from the property, with its doors unlocked and her purse inside. There were no signs of a struggle at either the property or the car. Her disappearance prompted one of the largest missing person investigations in British history.",
            "The prime suspect in Suzy's disappearance is John Cannan, a convicted rapist and murderer who was released from a hostel in the Fulham area just days before Suzy vanished. Cannan was known to use the nickname 'Kipper,' and his physical appearance matched witness descriptions. However, despite extensive investigation, police have never found sufficient evidence to charge him with Suzy's murder.",
            "Suzy was officially declared dead, presumed murdered, in 1994. Her disappearance led her mother, Diana Lamplugh, to establish the Suzy Lamplugh Trust, a charity promoting personal safety that became one of the UK's leading organizations advocating for workplace safety legislation. The case remains open."
        ],
        "timeline": [
            {"date": "1986-07-28", "event": "Suzy Lamplugh leaves her office to meet 'Mr. Kipper' and vanishes."},
            {"date": "1986-07-28", "event": "Suzy's car found abandoned about a mile from the property."},
            {"date": "1994-11-01", "event": "Suzy officially declared dead, presumed murdered."},
            {"date": "2000-11-01", "event": "Police formally name John Cannan as the prime suspect."}
        ],
        "enriched": True
    },
    {
        "id": "madeleine-mccann-2007",
        "name": "Madeleine McCann",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2007,
        "date": "May 3, 2007",
        "state": None,
        "city": "Praia da Luz",
        "country": "Portugal",
        "age": 3,
        "gender": "Female",
        "summary": "Three-year-old Madeleine McCann disappeared from her family's holiday apartment in Praia da Luz, Portugal. German national Christian Brückner was identified as a suspect in 2020.",
        "lastSeen": "May 3, 2007, Apartment 5A, Ocean Club resort, Praia da Luz, Algarve, Portugal",
        "tags": ["missing person", "child", "Portugal", "United Kingdom", "2000s", "international", "unsolved"],
        "sources": [
            {"title": "Disappearance of Madeleine McCann - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Madeleine_McCann"},
            {"title": "Madeleine McCann case - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-20782055"},
            {"title": "Operation Grange - Metropolitan Police", "url": "https://www.met.police.uk/advice/advice-and-information/madeleine-mccann/"}
        ],
        "narrative": [
            "On the evening of May 3, 2007, three-year-old Madeleine Beth McCann disappeared from her bed in apartment 5A of the Ocean Club resort in Praia da Luz, a seaside village in the Algarve region of Portugal. Her parents, Kate and Gerry McCann, both British doctors, had been dining with friends at a nearby tapas restaurant, with the group taking turns checking on the children every 30 minutes.",
            "When Kate McCann went to check on the children at approximately 10:00 p.m., she discovered Madeleine missing and the bedroom window and shutter open. Portuguese police launched an immediate search, but no trace of the child was found. The case quickly became one of the most heavily reported missing person cases in modern history.",
            "The Portuguese investigation was criticized for early missteps, including the failure to properly secure the crime scene. In 2007, the Portuguese police controversially named Kate and Gerry McCann as arguidos (formal suspects), though these designations were later dropped due to lack of evidence. The case was shelved in 2008 but reopened in 2013 when the UK's Metropolitan Police launched Operation Grange.",
            "In June 2020, German prosecutors identified Christian Brückner, a convicted sex offender who had been living in the Algarve at the time of Madeleine's disappearance, as a suspect. As of 2024, Brückner has not been charged in connection with Madeleine's case. The investigation continues on both the British and German sides, but Madeleine has never been found."
        ],
        "timeline": [
            {"date": "2007-05-03", "event": "Madeleine McCann disappears from the holiday apartment in Praia da Luz."},
            {"date": "2007-09-07", "event": "Kate and Gerry McCann named as arguidos (suspects) by Portuguese police."},
            {"date": "2008-07-21", "event": "Portuguese investigation is shelved."},
            {"date": "2013-07-04", "event": "UK Metropolitan Police launches Operation Grange."},
            {"date": "2020-06-03", "event": "German prosecutors identify Christian Brückner as a suspect."}
        ],
        "enriched": True
    },
    {
        "id": "amber-hagerman-1996",
        "name": "Amber Hagerman",
        "type": "Abduction",
        "status": "Unsolved",
        "year": 1996,
        "date": "January 13, 1996",
        "state": "Texas",
        "city": "Arlington",
        "age": 9,
        "gender": "Female",
        "summary": "Nine-year-old Amber Hagerman was abducted while riding her bicycle in Arlington, Texas. Her body was found four days later. Her case inspired the creation of the AMBER Alert system.",
        "lastSeen": "January 13, 1996, parking lot near E. Abram Street, Arlington, Texas",
        "tags": ["abduction", "homicide", "child", "Texas", "1990s", "AMBER Alert", "unsolved"],
        "sources": [
            {"title": "Murder of Amber Hagerman - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Amber_Hagerman"},
            {"title": "AMBER Alert history - Department of Justice", "url": "https://amberalert.ojp.gov/about"},
            {"title": "Amber Hagerman case - NBC News", "url": "https://www.nbcnews.com/news/us-news/amber-hagerman-case-25-years-later-n1254266"}
        ],
        "narrative": [
            "On January 13, 1996, nine-year-old Amber Rene Hagerman was riding her bicycle in a parking lot of an abandoned grocery store near her grandparents' home in Arlington, Texas, when a man driving a black pickup truck grabbed her off her bike. A neighbor, Jimmie Kevil, witnessed the abduction and called 911, reporting that he saw a man pull the girl off her bicycle and throw her into the truck.",
            "Despite an immediate search, Amber was not found. Four days later, on January 17, a man walking his dog discovered her body in a drainage ditch in north Arlington, about four miles from the abduction site. She had been sexually assaulted and her throat had been cut. The medical examiner determined she had been alive for at least two days after her abduction.",
            "The investigation yielded few leads. Despite the eyewitness account, the suspect was never identified. The truck description was common, and forensic evidence was limited. Over the years, hundreds of tips have been investigated, and several persons of interest have been questioned, but no arrests have been made.",
            "Amber's abduction and murder had a profound impact on child safety in the United States. Diana Simone, a Dallas radio broadcaster, spearheaded the creation of the AMBER Alert system (America's Missing: Broadcast Emergency Response), which uses broadcast media to notify the public when a child has been abducted. The system was first implemented in the Dallas-Fort Worth area in 1996 and has since been adopted nationwide and internationally."
        ],
        "timeline": [
            {"date": "1996-01-13", "event": "Amber Hagerman is abducted from a parking lot in Arlington, Texas."},
            {"date": "1996-01-17", "event": "Amber's body is found in a drainage ditch in north Arlington."},
            {"date": "1996-07-01", "event": "The AMBER Alert system is established in the Dallas-Fort Worth area."},
            {"date": "2003-04-30", "event": "PROTECT Act makes AMBER Alert a nationwide system."}
        ],
        "enriched": True
    },
    {
        "id": "asha-degree-2000",
        "name": "Asha Degree",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2000,
        "date": "February 14, 2000",
        "state": "North Carolina",
        "city": "Shelby",
        "age": 9,
        "gender": "Female",
        "summary": "Nine-year-old Asha Degree left her home in Shelby, North Carolina in the early morning hours during a storm and was never seen again. In 2024, two suspects were indicted in connection with her disappearance.",
        "lastSeen": "February 14, 2000, Highway 18 near Shelby, North Carolina",
        "tags": ["missing person", "child", "North Carolina", "2000s", "unsolved"],
        "sources": [
            {"title": "Disappearance of Asha Degree - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Asha_Degree"},
            {"title": "Asha Degree - FBI", "url": "https://www.fbi.gov/wanted/kidnap/asha-degree"},
            {"title": "Asha Degree case developments - Charlotte Observer", "url": "https://www.charlotteobserver.com/news/local/crime/article289987284.html"}
        ],
        "narrative": [
            "In the early morning hours of February 14, 2000, nine-year-old Asha Degree left her family's home on Oakcrest Drive in Shelby, North Carolina, during a severe thunderstorm. Why she left and where she intended to go remains unknown. Multiple motorists reported seeing a young girl walking alone along Highway 18 south of Shelby between 3:30 and 4:15 a.m. One driver turned around to check on her, but the girl ran into the woods.",
            "When Asha's parents discovered she was missing that morning, a massive search was launched. Tracking dogs followed her scent to Highway 18 before losing the trail. Items from Asha's home, including a pencil, a marker, and candy wrappers, were found in a shed near the highway, suggesting she may have sheltered there briefly.",
            "In August 2001, Asha's book bag was found double-wrapped in plastic bags and buried at a construction site along Highway 18 in Burke County, about 26 miles north of Shelby. The bag's condition suggested it had been deliberately preserved. Despite extensive investigation, no further trace of Asha was found for years.",
            "In a major development in 2024, Roy Lee Dedmon and his daughter AnnaLee Ramirez were indicted on charges related to Asha's disappearance. Dedmon was charged with concealment of a body and obstruction. While the indictments suggest authorities believe Asha is dead, the full circumstances of what happened to her remain unclear as the investigation continues."
        ],
        "timeline": [
            {"date": "2000-02-14", "event": "Asha Degree leaves her home during a thunderstorm and vanishes."},
            {"date": "2000-02-14", "event": "Multiple motorists report seeing a girl walking on Highway 18."},
            {"date": "2001-08-01", "event": "Asha's book bag found buried along Highway 18 in Burke County."},
            {"date": "2024-11-01", "event": "Roy Lee Dedmon and AnnaLee Ramirez indicted in connection with the case."}
        ],
        "enriched": True
    },
    {
        "id": "daniel-morcombe-2003",
        "name": "Daniel Morcombe",
        "type": "Abduction",
        "status": "Solved",
        "year": 2003,
        "date": "December 7, 2003",
        "state": None,
        "city": "Palmwoods",
        "country": "Australia",
        "age": 13,
        "gender": "Male",
        "summary": "Thirteen-year-old Daniel Morcombe disappeared while waiting for a bus on the Sunshine Coast, Queensland. In 2011, Brett Peter Cowan was arrested and later convicted of his murder.",
        "lastSeen": "December 7, 2003, Kiel Mountain Road underpass, Woombye, Queensland",
        "tags": ["abduction", "homicide", "child", "Australia", "2000s", "solved"],
        "sources": [
            {"title": "Murder of Daniel Morcombe - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Daniel_Morcombe"},
            {"title": "Daniel Morcombe Foundation", "url": "https://www.danielmorcombe.com.au/"},
            {"title": "Cowan conviction - ABC News", "url": "https://www.abc.net.au/news/2014-03-13/brett-peter-cowan-found-guilty-of-daniel-morcombe-murder/5318456"}
        ],
        "narrative": [
            "On December 7, 2003, thirteen-year-old Daniel James Morcombe was waiting at a bus stop beneath the Kiel Mountain Road overpass on the Sunshine Coast, Queensland, Australia. He was heading to a shopping centre to buy Christmas presents. When a bus passed without stopping due to running late, Daniel was left waiting for the next one. He was never seen again.",
            "Daniel's disappearance sparked one of Queensland's largest missing person investigations. Despite extensive searches, public appeals, and the establishment of a dedicated task force, no trace of Daniel was found for years. His parents, Bruce and Denise Morcombe, became prominent advocates for child safety, founding the Daniel Morcombe Foundation.",
            "In 2011, a covert police operation targeting convicted child sex offender Brett Peter Cowan led to a breakthrough. Undercover officers posing as members of a criminal organization befriended Cowan, who eventually confessed to abducting, sexually assaulting, and murdering Daniel. He led officers to Daniel's remains in bushland near the Glass House Mountains.",
            "Cowan was arrested in August 2011 and stood trial in 2014. He was found guilty of murder, indecent treatment of a child, and interfering with a corpse, and was sentenced to life imprisonment with a non-parole period of 20 years. The case led to significant reforms in child protection legislation in Queensland."
        ],
        "timeline": [
            {"date": "2003-12-07", "event": "Daniel Morcombe disappears from a bus stop on the Sunshine Coast."},
            {"date": "2011-08-13", "event": "Brett Peter Cowan arrested after covert police operation."},
            {"date": "2011-08-01", "event": "Daniel's skeletal remains found in bushland near Glass House Mountains."},
            {"date": "2014-03-13", "event": "Cowan found guilty of murder; sentenced to life imprisonment."}
        ],
        "enriched": True
    },
    {
        "id": "william-tyrrell-2014",
        "name": "William Tyrrell",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2014,
        "date": "September 12, 2014",
        "state": None,
        "city": "Kendall",
        "country": "Australia",
        "age": 3,
        "gender": "Male",
        "summary": "Three-year-old William Tyrrell, wearing a Spider-Man costume, vanished from his foster grandmother's garden in Kendall, New South Wales. He has never been found.",
        "lastSeen": "September 12, 2014, Benaroon Drive, Kendall, New South Wales",
        "tags": ["missing person", "child", "Australia", "2010s", "unsolved"],
        "sources": [
            {"title": "Disappearance of William Tyrrell - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_William_Tyrrell"},
            {"title": "William Tyrrell inquest - ABC News", "url": "https://www.abc.net.au/news/2022-11-09/william-tyrrell-inquest-begins/101627496"},
            {"title": "William Tyrrell case - Sydney Morning Herald", "url": "https://www.smh.com.au/national/nsw/the-disappearance-of-william-tyrrell-what-we-know-20211115-p599n2.html"}
        ],
        "narrative": [
            "On September 12, 2014, three-year-old William Tyrrell was playing in the front garden of his foster grandmother's home on Benaroon Drive in Kendall, a small town on the mid-north coast of New South Wales, Australia. He was wearing his favorite Spider-Man costume and was playing a game of 'roar' with his foster mother. When she went inside briefly, William vanished.",
            "An immediate search of the surrounding bushland and properties found no trace of the boy. The case prompted one of the largest investigations in New South Wales police history, with hundreds of officers and volunteers searching the area. Despite extensive media coverage and a $1 million reward, William was never found.",
            "The investigation explored multiple theories, including abduction by a stranger, involvement by someone known to the family, and the possibility that William wandered into the dense bushland and succumbed to the elements. In 2021, police conducted extensive searches of bushland near the foster grandmother's home, including excavating areas of ground, but no remains were found.",
            "A coronial inquest into William's disappearance began in 2019 and continued through 2022, examining various persons of interest and investigative leads. The inquest heard evidence about William's foster parents and biological family, as well as known sex offenders in the area. The case remains one of Australia's most prominent missing child cases."
        ],
        "timeline": [
            {"date": "2014-09-12", "event": "William Tyrrell vanishes from his foster grandmother's garden in Kendall."},
            {"date": "2014-09-12", "event": "Major search operation launched in surrounding bushland."},
            {"date": "2021-11-18", "event": "Police conduct major forensic search of bushland near Kendall."},
            {"date": "2022-11-09", "event": "Coronial inquest continues examining evidence and persons of interest."}
        ],
        "enriched": True
    },
    {
        "id": "sarah-everard-2021",
        "name": "Sarah Everard",
        "type": "Homicide",
        "status": "Solved",
        "year": 2021,
        "date": "March 3, 2021",
        "state": None,
        "city": "London",
        "country": "United Kingdom",
        "age": 33,
        "gender": "Female",
        "summary": "Sarah Everard was kidnapped, raped, and murdered by Metropolitan Police officer Wayne Couzens while walking home in south London. Couzens received a whole-life sentence.",
        "lastSeen": "March 3, 2021, Clapham Common, London",
        "tags": ["homicide", "abduction", "United Kingdom", "London", "2020s", "police officer", "solved"],
        "sources": [
            {"title": "Murder of Sarah Everard - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Sarah_Everard"},
            {"title": "Wayne Couzens sentenced - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-london-58729077"},
            {"title": "Sarah Everard case impact - The Guardian", "url": "https://www.theguardian.com/uk-news/2021/oct/01/sarah-everard-murder-wayne-couzens-sentenced-whole-life-order"}
        ],
        "narrative": [
            "On the evening of March 3, 2021, 33-year-old Sarah Everard left a friend's house in Clapham, south London, to walk home to Brixton Hill, a journey of about 50 minutes. She was seen on CCTV walking along the A205 Poynders Road near Clapham Common at approximately 9:30 p.m. She never arrived home.",
            "Sarah's boyfriend reported her missing the following day when she failed to arrive at work. A major investigation was launched, and CCTV footage revealed that Sarah had been stopped near Clapham Common by a man who had used his Metropolitan Police warrant card and handcuffs to carry out a fake arrest, claiming she had violated COVID-19 lockdown restrictions.",
            "The man was identified as Wayne Couzens, a serving Metropolitan Police diplomatic protection officer. He had hired a rental car for the abduction. Phone and CCTV evidence traced Couzens' movements as he drove Sarah to Kent, where he raped and strangled her. He burned her body in a refrigerator in an area of woodland near Ashford, Kent, where her remains were discovered on March 10.",
            "Couzens was arrested on March 9 and charged with kidnap and murder. He pleaded guilty to both charges and on September 30, 2021, was sentenced to a whole-life order, meaning he will never be released from prison. The case provoked widespread outrage, vigils, and protests across the UK, sparking a national conversation about women's safety and leading to significant scrutiny of the Metropolitan Police's vetting procedures and culture."
        ],
        "timeline": [
            {"date": "2021-03-03", "event": "Sarah Everard disappears while walking home in Clapham, south London."},
            {"date": "2021-03-09", "event": "Wayne Couzens, a serving police officer, is arrested."},
            {"date": "2021-03-10", "event": "Sarah's remains found in woodland near Ashford, Kent."},
            {"date": "2021-09-30", "event": "Couzens sentenced to whole-life imprisonment."}
        ],
        "enriched": True
    },
    {
        "id": "jenny-lin-1994",
        "name": "Jenny Lin",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1994,
        "date": "May 27, 1994",
        "state": "California",
        "city": "Castro Valley",
        "age": 14,
        "gender": "Female",
        "summary": "Fourteen-year-old Jenny Lin was murdered in her Castro Valley, California home while her parents were at work. The case remains unsolved despite DNA evidence.",
        "lastSeen": "May 27, 1994, her home in Castro Valley, California",
        "tags": ["homicide", "child", "California", "1990s", "unsolved", "DNA evidence"],
        "sources": [
            {"title": "Murder of Jenny Lin - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Jenny_Lin"},
            {"title": "Jenny Lin case - Mercury News", "url": "https://www.mercurynews.com/2019/05/27/jenny-lin-murder-castro-valley-25-years/"},
            {"title": "Jenny Lin Foundation", "url": "https://www.jennylin.org/"}
        ],
        "narrative": [
            "On May 27, 1994, fourteen-year-old Jenny Lin was home alone in her family's house in Castro Valley, an unincorporated community in Alameda County, California. Her parents, John and Mei-Lian Lin, were both at work. When Mei-Lian returned home that evening, she discovered her daughter had been brutally murdered.",
            "Jenny had been stabbed multiple times and her body showed signs of a violent struggle. Evidence suggested she had been practicing the flute when she was attacked. The killer had entered the home through a window. Despite extensive investigation by the Alameda County Sheriff's Office, no suspect was identified in the immediate aftermath.",
            "The case remained cold for years. DNA evidence was collected from the crime scene, and as forensic technology advanced, investigators periodically re-examined the evidence. In 2019, on the 25th anniversary of Jenny's murder, the Alameda County Sheriff's Office announced they were using genetic genealogy techniques to identify the killer through the DNA evidence.",
            "Jenny's parents channeled their grief into advocacy, establishing the Jenny Lin Foundation to provide educational and extracurricular opportunities for youth. The foundation has grown into a significant community organization. Despite advances in forensic technology and periodic renewed investigation efforts, Jenny's killer has never been identified."
        ],
        "timeline": [
            {"date": "1994-05-27", "event": "Jenny Lin is murdered in her Castro Valley home."},
            {"date": "1994-06-01", "event": "Investigation launched by Alameda County Sheriff's Office."},
            {"date": "2019-05-27", "event": "On 25th anniversary, sheriff announces genetic genealogy efforts."}
        ],
        "enriched": True
    },
    {
        "id": "mikelle-biggs-1999",
        "name": "Mikelle Biggs",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1999,
        "date": "January 2, 1999",
        "state": "Arizona",
        "city": "Mesa",
        "age": 11,
        "gender": "Female",
        "summary": "Eleven-year-old Mikelle Biggs vanished while riding her bicycle in front of her Mesa, Arizona home while waiting for an ice cream truck. She has never been found.",
        "lastSeen": "January 2, 1999, outside her home on East Emerald Avenue, Mesa, Arizona",
        "tags": ["missing person", "child", "Arizona", "1990s", "unsolved"],
        "sources": [
            {"title": "Disappearance of Mikelle Biggs - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Mikelle_Biggs"},
            {"title": "Mikelle Biggs - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/848489"},
            {"title": "Mikelle Biggs case - AZ Central", "url": "https://www.azcentral.com/story/news/local/mesa/2019/01/02/mikelle-biggs-disappeared-mesa-20-years-ago/2462116002/"}
        ],
        "narrative": [
            "On the afternoon of January 2, 1999, eleven-year-old Mikelle Biggs was riding her bicycle outside her family's home on East Emerald Avenue in Mesa, Arizona. She and her younger sister Kimber were waiting for the ice cream truck, which they could hear approaching. When Kimber went inside briefly to get money, she returned to find Mikelle gone, her bicycle lying on its side in the street.",
            "The disappearance happened in broad daylight on a residential street. Despite immediate searches by family, neighbors, and police, no trace of Mikelle was found. The ice cream truck driver was questioned and cleared. A massive investigation followed, involving the Mesa Police Department, FBI, and National Center for Missing & Exploited Children.",
            "Over the years, numerous tips and leads have been investigated without result. In 2011, Mesa police searched a property belonging to a registered sex offender who lived near the Biggs family, but nothing was found. The case has been featured on America's Most Wanted and other programs seeking public assistance.",
            "Mikelle's family has kept her case in the public eye, and law enforcement periodically reviews the evidence with advancing forensic technologies. A $100,000 reward has been offered for information leading to Mikelle's recovery. She remains listed with the National Center for Missing & Exploited Children."
        ],
        "timeline": [
            {"date": "1999-01-02", "event": "Mikelle Biggs vanishes while riding her bicycle in front of her Mesa home."},
            {"date": "1999-01-02", "event": "Massive search launched; Mikelle's bicycle found in the street."},
            {"date": "2011-01-01", "event": "Police search property of a registered sex offender near the Biggs home."}
        ],
        "enriched": True
    },
    {
        "id": "kyron-horman-2010",
        "name": "Kyron Horman",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2010,
        "date": "June 4, 2010",
        "state": "Oregon",
        "city": "Portland",
        "age": 7,
        "gender": "Male",
        "summary": "Seven-year-old Kyron Horman vanished from Skyline Elementary School in Portland, Oregon. His stepmother Terri Horman was the last known person to see him and remains a person of interest.",
        "lastSeen": "June 4, 2010, Skyline Elementary School, Portland, Oregon",
        "tags": ["missing person", "child", "Oregon", "2010s", "school", "unsolved"],
        "sources": [
            {"title": "Disappearance of Kyron Horman - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Kyron_Horman"},
            {"title": "Kyron Horman case - The Oregonian", "url": "https://www.oregonlive.com/kyron-horman/"},
            {"title": "Kyron Horman - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/1175498"}
        ],
        "narrative": [
            "On June 4, 2010, seven-year-old Kyron Horman attended a science fair at Skyline Elementary School in the West Hills of Portland, Oregon. His stepmother, Terri Moulton Horman, drove him to school that morning and was photographed with him at his science fair display about red-eyed tree frogs. According to Terri, she left the school at approximately 8:45 a.m. after walking Kyron to his classroom.",
            "Kyron was never seen again. When he failed to get off the school bus that afternoon, his family contacted the school, which had marked him absent. A massive search was launched across the rural, heavily forested area surrounding the school, involving hundreds of searchers, dogs, and aircraft.",
            "Suspicion quickly focused on Terri Horman, who gave inconsistent accounts of her activities that morning. Investigators discovered she had a troubled relationship with Kyron's father, Kaine Horman, and had allegedly attempted to hire a landscaper to kill Kaine months before Kyron's disappearance. Kaine filed for divorce and obtained a restraining order against Terri. However, Terri was never charged, and she has maintained her innocence.",
            "The case became one of the most extensive missing child investigations in Oregon history. Despite thousands of tips, extensive searches, and continued investigation by the Multnomah County Sheriff's Office, Kyron has never been found. A grand jury was convened in 2014 but no indictments were issued."
        ],
        "timeline": [
            {"date": "2010-06-04", "event": "Kyron Horman disappears from Skyline Elementary School."},
            {"date": "2010-06-25", "event": "Kaine Horman files for divorce and restraining order against Terri."},
            {"date": "2010-09-01", "event": "Multnomah County Sheriff acknowledges criminal investigation."},
            {"date": "2014-01-01", "event": "Grand jury convened but issues no indictments."}
        ],
        "enriched": True
    },
    {
        "id": "relisha-rudd-2014",
        "name": "Relisha Rudd",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2014,
        "date": "March 1, 2014",
        "state": "Washington, D.C.",
        "city": "Washington",
        "age": 8,
        "gender": "Female",
        "summary": "Eight-year-old Relisha Rudd disappeared from a homeless shelter in Washington, D.C. Janitor Khalil Tatum, the prime suspect, was found dead of a self-inflicted gunshot wound.",
        "lastSeen": "March 1, 2014, Washington, D.C.",
        "tags": ["missing person", "child", "Washington D.C.", "2010s", "homeless shelter", "unsolved"],
        "sources": [
            {"title": "Disappearance of Relisha Rudd - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Relisha_Rudd"},
            {"title": "Relisha Rudd case - Washington Post", "url": "https://www.washingtonpost.com/local/relisha-rudd-case/2014/03/01/"},
            {"title": "Relisha Rudd - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/1202477"}
        ],
        "narrative": [
            "Relisha Tenau Rudd was an eight-year-old girl living with her family at the DC General family shelter, a large homeless shelter in Washington, D.C. In early 2014, she came under the attention of Khalil Tatum, a 51-year-old janitor who worked at the shelter. Tatum began spending time with Relisha, buying her gifts and taking her on outings, a situation that went largely unchecked by shelter staff and social services.",
            "Relisha was last seen on surveillance footage at a Holiday Inn Express with Tatum on March 1, 2014. When school officials noted Relisha had been absent for weeks, they discovered forged doctor's notes excusing her absences. The school contacted authorities, triggering an investigation.",
            "On March 20, 2014, Tatum's wife, Andrea Tatum, was found shot to death in a motel room in Prince George's County, Maryland. Khalil Tatum became the prime suspect in both his wife's murder and Relisha's disappearance. An arrest warrant was issued for him, and a massive search was launched.",
            "On March 31, 2014, Tatum's body was found in a park in Kenilworth, Washington, D.C., dead from a self-inflicted gunshot wound. Relisha was not with him, and her whereabouts remain unknown. The case highlighted systemic failures in the child welfare system and the conditions at DC General shelter, which was subsequently closed. Annual searches for Relisha continue."
        ],
        "timeline": [
            {"date": "2014-03-01", "event": "Relisha Rudd last seen on surveillance footage with Khalil Tatum."},
            {"date": "2014-03-19", "event": "School alerts authorities about Relisha's prolonged absence."},
            {"date": "2014-03-20", "event": "Andrea Tatum found murdered in a motel room."},
            {"date": "2014-03-31", "event": "Khalil Tatum found dead of self-inflicted gunshot wound."}
        ],
        "enriched": True
    },
    {
        "id": "sodder-children-1945",
        "name": "Sodder Children",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1945,
        "date": "December 24, 1945",
        "state": "West Virginia",
        "city": "Fayetteville",
        "age": None,
        "gender": "Multiple",
        "summary": "Five of the ten Sodder children disappeared during a Christmas Eve house fire in Fayetteville, West Virginia. No remains were found, leading the family to believe they survived and were kidnapped.",
        "lastSeen": "December 24, 1945, Sodder residence, Route 21, Fayetteville, West Virginia",
        "tags": ["missing person", "children", "West Virginia", "1940s", "fire", "unsolved", "historical"],
        "sources": [
            {"title": "Sodder children disappearance - Wikipedia", "url": "https://en.wikipedia.org/wiki/Sodder_children_disappearance"},
            {"title": "Sodder children - Smithsonian Magazine", "url": "https://www.smithsonianmag.com/history/the-children-who-went-up-in-smoke-172429802/"},
            {"title": "What happened to the Sodder children? - Atlas Obscura", "url": "https://www.atlasobscura.com/articles/what-happened-to-the-sodder-children"}
        ],
        "narrative": [
            "On Christmas Eve, December 24, 1945, a fire broke out at the Sodder family home on Route 21 near Fayetteville, West Virginia. George and Jennie Sodder escaped with four of their ten children. Five children—Maurice (14), Martha (12), Louis (9), Jennie (8), and Betty (5)—were unaccounted for and presumed to have perished in the blaze.",
            "However, several facts troubled the family and investigators. Despite the intense fire, no bones, teeth, or other remains of the children were ever found in the ashes. A coal delivery driver reported that the fire had not burned hot enough to completely consume human remains. The fire department did not arrive until eight hours after the fire started, and the phone lines had been cut prior to the blaze.",
            "George Sodder noticed other suspicious details: the ladder he kept against the house had been moved, and his two vehicles had been tampered with and wouldn't start. Witnesses reported seeing the children in a passing car during the fire. In the months and years that followed, the family received tips suggesting the children had survived and been kidnapped, possibly connected to threats George had received from the local Mafia related to his outspoken criticism of Mussolini's Italy.",
            "In 1968, the family received an envelope containing a photo of a young man who they believed resembled their son Louis, with a cryptic message on the back. Despite hiring private investigators and spending decades searching, the Sodder family never found their missing children. George died in 1969 and Jennie in 1989, both still believing the children were alive. The case remains one of America's most enduring mysteries."
        ],
        "timeline": [
            {"date": "1945-12-24", "event": "Fire destroys the Sodder home; five children unaccounted for."},
            {"date": "1945-12-25", "event": "No remains found in the ashes of the destroyed home."},
            {"date": "1968-01-01", "event": "Family receives a photo believed to be of their missing son Louis."},
            {"date": "1989-01-01", "event": "Jennie Sodder dies, still believing the children survived."}
        ],
        "enriched": True
    },
    {
        "id": "claudia-lawrence-2009",
        "name": "Claudia Lawrence",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2009,
        "date": "March 18, 2009",
        "state": None,
        "city": "York",
        "country": "United Kingdom",
        "age": 35,
        "gender": "Female",
        "summary": "University of York chef Claudia Lawrence vanished on her walk to work. Police believe she was murdered, but her body has never been found and no one has been charged.",
        "lastSeen": "March 18, 2009, Heworth area, York, England",
        "tags": ["missing person", "United Kingdom", "York", "2000s", "presumed dead", "unsolved"],
        "sources": [
            {"title": "Disappearance of Claudia Lawrence - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Claudia_Lawrence"},
            {"title": "Claudia Lawrence case - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-york-north-yorkshire-26595077"},
            {"title": "Claudia Lawrence investigation - North Yorkshire Police", "url": "https://www.northyorkshire.police.uk/news/claudia-lawrence/"}
        ],
        "narrative": [
            "Claudia Elizabeth Lawrence, a 35-year-old chef at the University of York's Goodricke College, was last seen on CCTV near her home in the Heworth area of York on the evening of March 18, 2009. She had spoken to her parents by phone that evening and sent text messages to friends. She failed to arrive at work the following morning, and colleagues raised the alarm.",
            "Police found Claudia's home on Heworth Road apparently undisturbed, with her phone, keys, and rucksack missing, suggesting she had left for work as normal. However, she never arrived at the university, a 25-minute walk from her home. CCTV footage showed a man near her house on the night she disappeared, but he was never identified.",
            "North Yorkshire Police launched a major investigation, treating the case as a suspected murder. Multiple persons of interest were identified and questioned, and several arrests were made in 2014-2015, but all suspects were released without charge. The investigation revealed that Claudia had a complex private life that she kept hidden from family and friends.",
            "In 2021, Claudia was declared legally dead. Her father, Peter Lawrence, became a prominent campaigner for the rights of families of missing people, leading to 'Claudia's Law,' formally the Guardianship (Missing Persons) Act 2017, which allows families of missing people to manage their financial and property affairs. Despite continued investigation, Claudia has never been found."
        ],
        "timeline": [
            {"date": "2009-03-18", "event": "Claudia Lawrence last seen on CCTV near her home in York."},
            {"date": "2009-03-20", "event": "Claudia reported missing after failing to attend work."},
            {"date": "2014-05-01", "event": "Several arrests made in connection with the case; all later released."},
            {"date": "2021-06-01", "event": "Claudia declared legally dead."}
        ],
        "enriched": True
    },
    {
        "id": "brianna-maitland-2004",
        "name": "Brianna Maitland",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2004,
        "date": "March 19, 2004",
        "state": "Vermont",
        "city": "Montgomery",
        "age": 17,
        "gender": "Female",
        "summary": "Seventeen-year-old Brianna Maitland vanished after leaving her job at the Black Lantern Inn in Montgomery, Vermont. Her car was found backed into an abandoned farmhouse.",
        "lastSeen": "March 19, 2004, Black Lantern Inn, Montgomery, Vermont",
        "tags": ["missing person", "Vermont", "2000s", "teenager", "unsolved"],
        "sources": [
            {"title": "Disappearance of Brianna Maitland - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Brianna_Maitland"},
            {"title": "Brianna Maitland - FBI", "url": "https://www.fbi.gov/wanted/kidnap/brianna-maitland"},
            {"title": "Brianna Maitland case - Burlington Free Press", "url": "https://www.burlingtonfreepress.com/story/news/2019/03/19/brianna-maitland-missing-vermont-15-years/3210424002/"}
        ],
        "narrative": [
            "On the evening of March 19, 2004, seventeen-year-old Brianna Maitland finished her shift as a dishwasher at the Black Lantern Inn in Montgomery, Vermont, a small town near the Canadian border. She left the inn at approximately 11:20 p.m. to drive home. She was never seen again.",
            "The following day, a state trooper discovered Brianna's 1985 Oldsmobile backed into the side of an abandoned farmhouse on Route 118, about a mile from the inn. The car's rear was embedded in the building, and some of Brianna's personal belongings were found inside and outside the vehicle. The scene suggested a possible struggle, but there were no witnesses.",
            "The investigation uncovered that Brianna had been involved in a dispute with another girl in the weeks before her disappearance, and that she had been associating with individuals connected to drug activity in the area. Multiple persons of interest were identified and investigated, including individuals with criminal records, but no charges were ever filed.",
            "Vermont State Police and the FBI have continued to investigate the case. In 2016, the FBI issued a renewed appeal for information. The case has been featured on multiple television programs and podcasts. Despite extensive investigation, Brianna's fate remains unknown, and she has never been found."
        ],
        "timeline": [
            {"date": "2004-03-19", "event": "Brianna Maitland leaves work at the Black Lantern Inn and vanishes."},
            {"date": "2004-03-20", "event": "Her car found backed into an abandoned farmhouse on Route 118."},
            {"date": "2016-01-01", "event": "FBI issues renewed appeal for information."}
        ],
        "enriched": True
    },
    {
        "id": "holly-bobo-2011",
        "name": "Holly Bobo",
        "type": "Abduction",
        "status": "Solved",
        "year": 2011,
        "date": "April 13, 2011",
        "state": "Tennessee",
        "city": "Darden",
        "age": 20,
        "gender": "Female",
        "summary": "Nursing student Holly Bobo was abducted from her home in rural Tennessee. Her remains were found in 2014. Zachary Adams was convicted of her murder in 2017.",
        "lastSeen": "April 13, 2011, her home in Darden, Decatur County, Tennessee",
        "tags": ["abduction", "homicide", "Tennessee", "2010s", "solved"],
        "sources": [
            {"title": "Murder of Holly Bobo - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Holly_Bobo"},
            {"title": "Holly Bobo trial - Tennessean", "url": "https://www.tennessean.com/story/news/crime/2017/09/22/holly-bobo-trial-zachary-adams-verdict/693095001/"},
            {"title": "Holly Bobo case - CNN", "url": "https://www.cnn.com/2017/09/22/us/holly-bobo-murder-trial-verdict/index.html"}
        ],
        "narrative": [
            "On the morning of April 13, 2011, twenty-year-old Holly Bobo, a nursing student at the University of Tennessee at Martin, was abducted from the carport of her family's home in Darden, a rural community in Decatur County, Tennessee. Her brother Clint saw Holly being led into the woods by a man wearing camouflage and initially thought she was walking with her boyfriend.",
            "When the family realized Holly was missing, they found blood on the carport floor and in the garage. A massive search was launched across the rural, heavily wooded terrain of Decatur County, involving hundreds of searchers, dogs, and aerial surveillance. Despite extensive efforts, Holly was not found.",
            "In February 2014, nearly three years after her disappearance, Zachary Adams and Jason Autry were arrested and charged with especially aggravated kidnapping and first-degree murder. A third man, John Dylan Adams (Zachary's brother), was also charged. Holly's skull was discovered in September 2014 in woods in Decatur County, confirming she had been killed.",
            "Zachary Adams stood trial in September 2017 and was convicted of first-degree felony murder, especially aggravated kidnapping, and aggravated rape. He was sentenced to life in prison plus 50 years. Jason Autry pleaded guilty and testified against Adams in exchange for a reduced sentence. The case highlighted the challenges of investigating crimes in remote, rural areas."
        ],
        "timeline": [
            {"date": "2011-04-13", "event": "Holly Bobo is abducted from her home in Darden, Tennessee."},
            {"date": "2014-02-01", "event": "Zachary Adams and Jason Autry arrested and charged."},
            {"date": "2014-09-01", "event": "Holly's skull found in woods in Decatur County."},
            {"date": "2017-09-22", "event": "Zachary Adams convicted of murder; sentenced to life plus 50 years."}
        ],
        "enriched": True
    },
    {
        "id": "karen-silkwood-1974",
        "name": "Karen Silkwood",
        "type": "Suspicious Death",
        "status": "Unsolved",
        "year": 1974,
        "date": "November 13, 1974",
        "state": "Oklahoma",
        "city": "Crescent",
        "age": 28,
        "gender": "Female",
        "summary": "Nuclear plant worker and whistleblower Karen Silkwood died in a suspicious car crash while en route to meet a journalist with documents about safety violations at the Kerr-McGee plutonium plant.",
        "lastSeen": "November 13, 1974, Highway 74, Crescent, Oklahoma",
        "tags": ["suspicious death", "Oklahoma", "1970s", "whistleblower", "nuclear", "conspiracy"],
        "sources": [
            {"title": "Karen Silkwood - Wikipedia", "url": "https://en.wikipedia.org/wiki/Karen_Silkwood"},
            {"title": "Karen Silkwood case - Atomic Heritage Foundation", "url": "https://ahf.nuclearmuseum.org/ahf/profile/karen-silkwood/"},
            {"title": "Silkwood v. Kerr-McGee - Justia", "url": "https://supreme.justia.com/cases/federal/us/464/238/"}
        ],
        "narrative": [
            "Karen Gay Silkwood was a 28-year-old chemical technician at the Kerr-McGee Cimarron plutonium fuel fabrication plant near Crescent, Oklahoma. A member of the Oil, Chemical and Atomic Workers International Union, Silkwood became increasingly concerned about health and safety violations at the plant, including faulty fuel rods, inadequate worker protections, and falsified quality control records.",
            "In the summer and fall of 1974, Silkwood began gathering evidence of the safety violations. She was tasked by her union to document the problems, and she had been in contact with New York Times reporter David Burnham. In early November, Silkwood was found to be contaminated with plutonium under mysterious circumstances, with contamination found in her apartment and on her person on multiple occasions.",
            "On the evening of November 13, 1974, Silkwood left a union meeting at the Hub Cafe in Crescent to drive to Oklahoma City to meet with Burnham and union official Steve Wodka. She was reportedly carrying a folder of documents and photographs. She never arrived. Her car was found crashed into a concrete culvert on Highway 74. She was dead at the scene.",
            "An accident investigator hired by the union found evidence that Silkwood's car had been struck from behind, suggesting she had been run off the road. The documents she was reportedly carrying were never found. The official investigation ruled the death a one-car sleeping-at-the-wheel accident, though she had taken a stimulant. The Silkwood estate later won an $11.5 million judgment against Kerr-McGee for plutonium contamination, upheld by the U.S. Supreme Court."
        ],
        "timeline": [
            {"date": "1974-11-05", "event": "Silkwood found contaminated with plutonium at the plant."},
            {"date": "1974-11-13", "event": "Silkwood dies in a car crash en route to meet a journalist."},
            {"date": "1979-05-18", "event": "Jury awards Silkwood estate $10.5 million in damages against Kerr-McGee."},
            {"date": "1984-01-11", "event": "U.S. Supreme Court upholds the judgment in Silkwood v. Kerr-McGee."}
        ],
        "enriched": True
    },
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
        "summary": "Joan Risch vanished from her Lincoln, Massachusetts home, leaving behind a trail of blood, a smeared bloody path to the garage, and library books about missing persons. She was never found.",
        "lastSeen": "October 24, 1961, her home in Lincoln, Massachusetts",
        "tags": ["missing person", "Massachusetts", "1960s", "blood evidence", "unsolved"],
        "sources": [
            {"title": "Disappearance of Joan Risch - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Joan_Risch"},
            {"title": "Joan Risch case - New England Historical Society", "url": "https://www.newenglandhistoricalsociety.com/disappearance-joan-risch/"},
            {"title": "Joan Risch mystery - Wicked Local", "url": "https://www.wickedlocal.com/story/lincoln-journal/2011/10/22/joan-risch-mystery-50-years/39340006007/"}
        ],
        "narrative": [
            "On October 24, 1961, Joan Carolyn Risch, a 31-year-old mother of two, disappeared from her home in Lincoln, Massachusetts, under deeply mysterious circumstances. Her husband, Martin Risch, was away on a business trip, and their two-year-old son David was left at home while their four-year-old daughter Lillian was at a neighbor's house.",
            "When a neighbor came to check on Joan in the afternoon, she found two-year-old David alone in his crib and the house in disarray. There was blood in the kitchen and a trail of blood smears leading through the garage. Investigators estimated that approximately half a pint of blood had been spilled. A phone had been ripped from the wall, and the phone directory was open.",
            "Witnesses reported seeing a woman matching Joan's description walking along Route 2 near the Risch home, appearing dazed and with blood on her clothing. The woman was heading in the direction of a nearby highway, but she was never positively identified as Joan.",
            "One of the most intriguing aspects of the case was Joan's reading habits. In the weeks before her disappearance, she had checked out multiple library books about people who had disappeared, including accounts of people who had staged their own vanishings. This led to theories that Joan may have orchestrated her own disappearance, though the blood evidence suggested violence. Despite extensive investigation, Joan Risch has never been found, and her fate remains unknown."
        ],
        "timeline": [
            {"date": "1961-10-24", "event": "Joan Risch disappears from her Lincoln, Massachusetts home."},
            {"date": "1961-10-24", "event": "Blood found in the kitchen; trail leads to the garage."},
            {"date": "1961-10-24", "event": "Witness reports seeing a bloodied woman walking near Route 2."}
        ],
        "enriched": True
    },
    {
        "id": "peter-falconio-2001",
        "name": "Peter Falconio",
        "type": "Homicide",
        "status": "Solved",
        "year": 2001,
        "date": "July 14, 2001",
        "state": None,
        "city": "Barrow Creek",
        "country": "Australia",
        "age": 28,
        "gender": "Male",
        "summary": "British tourist Peter Falconio was shot on a remote Australian highway. His girlfriend Joanne Lees escaped. Bradley Murdoch was convicted of murder in 2005, though Falconio's body was never found.",
        "lastSeen": "July 14, 2001, Stuart Highway near Barrow Creek, Northern Territory, Australia",
        "tags": ["homicide", "Australia", "2000s", "outback", "tourist", "solved"],
        "sources": [
            {"title": "Murder of Peter Falconio - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Peter_Falconio"},
            {"title": "Bradley Murdoch trial - ABC News", "url": "https://www.abc.net.au/news/2005-12-13/murdoch-guilty-of-falconio-murder/758260"},
            {"title": "Peter Falconio case - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-35099498"}
        ],
        "narrative": [
            "On the evening of July 14, 2001, British tourists Peter Falconio, 28, and his girlfriend Joanne Lees, 27, were driving their Volkswagen Kombi van along the remote Stuart Highway near Barrow Creek in the Northern Territory of Australia. A man in a pickup truck flagged them down, indicating there was something wrong with their vehicle.",
            "When Peter got out to inspect the rear of the van, Joanne heard what she believed was a gunshot. The man then appeared at her window with a gun, bound her hands with cable ties, and forced her into his vehicle. Joanne managed to escape by hiding in bushland for hours before flagging down a passing truck for help.",
            "Peter's body was never found despite extensive searches of the harsh outback terrain. DNA evidence found on Joanne's T-shirt and on cable ties at the scene eventually led investigators to Bradley John Murdoch, a mechanic and drug runner who frequented the Stuart Highway.",
            "Murdoch was arrested in 2003 and stood trial in the Supreme Court of the Northern Territory in 2005. Despite the absence of Peter's body, the DNA evidence, Joanne's identification, and other circumstantial evidence convinced the jury. Murdoch was convicted of murder and sentenced to life imprisonment with a non-parole period of 28 years. He has continued to protest his innocence."
        ],
        "timeline": [
            {"date": "2001-07-14", "event": "Peter Falconio is shot on the Stuart Highway; Joanne Lees escapes."},
            {"date": "2001-07-15", "event": "Massive search of outback terrain begins; Peter's body not found."},
            {"date": "2003-11-14", "event": "Bradley Murdoch arrested in South Australia."},
            {"date": "2005-12-13", "event": "Murdoch convicted of murder; sentenced to life imprisonment."}
        ],
        "enriched": True
    },
    {
        "id": "disappearance-of-ben-needham-1991",
        "name": "Ben Needham",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1991,
        "date": "July 24, 1991",
        "state": None,
        "city": "Kos",
        "country": "Greece",
        "age": 1,
        "gender": "Male",
        "summary": "Twenty-one-month-old British toddler Ben Needham vanished on the Greek island of Kos. Police believe he may have been accidentally killed by a digger operator, but his remains have never been found.",
        "lastSeen": "July 24, 1991, Iraklise, Kos, Greece",
        "tags": ["missing person", "child", "Greece", "United Kingdom", "1990s", "unsolved"],
        "sources": [
            {"title": "Disappearance of Ben Needham - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Ben_Needham"},
            {"title": "Ben Needham case - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-south-yorkshire-37470053"},
            {"title": "South Yorkshire Police - Ben Needham investigation", "url": "https://www.southyorkshire.police.uk/find-out/news-and-appeals/2016/october-2016/ben-needham-investigation-update/"}
        ],
        "narrative": [
            "On July 24, 1991, twenty-one-month-old Ben Needham, a British toddler, vanished from outside a farmhouse in the village of Iraklise on the Greek island of Kos. His family had moved to the island, and his grandparents were renovating a property. Ben was playing outside in the yard while his grandmother was inside.",
            "When his family realized Ben was missing, a frantic search began. Greek police and local residents scoured the area, but no trace of the boy was found. The case became one of the UK's most prominent missing child investigations, with Ben's mother Kerry Needham launching a tireless campaign for answers.",
            "For years, the primary theory was that Ben had been abducted, possibly sold to a childless family. However, in 2016, South Yorkshire Police announced they believed Ben may have been accidentally killed by a digger operator, Konstantinos 'Dino' Barkas, who was working near the farmhouse that day. Barkas had died in 2015, and police conducted an extensive excavation of the area near the farmhouse, finding items including blood-stained fabric, but no conclusive remains.",
            "Despite the police belief that Ben died in an accident on the day he disappeared, no remains have been found and the case remains officially open. Kerry Needham has expressed skepticism about the accident theory and continues to hope her son is alive. The case has been the subject of multiple police investigations involving both British and Greek authorities."
        ],
        "timeline": [
            {"date": "1991-07-24", "event": "Ben Needham vanishes from outside a farmhouse on Kos, Greece."},
            {"date": "2012-10-01", "event": "South Yorkshire Police granted funding for a major new investigation."},
            {"date": "2016-10-01", "event": "Police announce they believe Ben may have been killed in a digger accident."},
            {"date": "2016-10-17", "event": "Excavation near the farmhouse finds items but no conclusive remains."}
        ],
        "enriched": True
    },
    {
        "id": "brandy-hall-2006",
        "name": "Brandy Hall",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2006,
        "date": "August 17, 2006",
        "state": "Florida",
        "city": "Volusia County",
        "age": 32,
        "gender": "Female",
        "summary": "Volusia County firefighter Brandy Hall vanished during her shift at a fire station in DeBary, Florida. Her personal belongings were left behind, and she has never been found.",
        "lastSeen": "August 17, 2006, Volusia County Fire Station 57, DeBary, Florida",
        "tags": ["missing person", "Florida", "2000s", "firefighter", "unsolved"],
        "sources": [
            {"title": "Disappearance of Brandy Hall - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Brandy_Hall"},
            {"title": "Brandy Hall case - Orlando Sentinel", "url": "https://www.orlandosentinel.com/news/os-xpm-2006-08-24-hallcase-story.html"},
            {"title": "Brandy Hall - Charley Project", "url": "https://charleyproject.org/case/brandy-nichole-hall"}
        ],
        "narrative": [
            "On August 17, 2006, Brandy Nichole Hall, a 32-year-old Volusia County firefighter and paramedic, vanished during her overnight shift at Fire Station 57 in DeBary, Florida. She was last seen at approximately 1:00 a.m. when she told a colleague she was going outside. When the crew awoke the next morning, Brandy was gone.",
            "Her wallet, cell phone, car keys, and personal vehicle were all left behind at the station. Her firefighting gear and uniform were found neatly arranged. There were no signs of a struggle at the fire station. Surveillance cameras at the station were not functioning at the time of her disappearance.",
            "The investigation revealed that Brandy had been having a relationship with a married man, and her personal life had been turbulent in the period before her disappearance. The Volusia County Sheriff's Office investigated multiple persons of interest but was unable to develop enough evidence for charges.",
            "In 2009, a grand jury was convened to investigate the case but did not return any indictments. Brandy's family has continued to press for answers, and her case has been featured on television crime programs. Despite periodic review of evidence and new leads, Brandy Hall has never been found and no arrests have been made."
        ],
        "timeline": [
            {"date": "2006-08-17", "event": "Brandy Hall vanishes during her overnight shift at Fire Station 57."},
            {"date": "2006-08-18", "event": "Her personal belongings and vehicle found at the station."},
            {"date": "2009-01-01", "event": "Grand jury convened; no indictments returned."}
        ],
        "enriched": True
    },
    {
        "id": "maura-murray-2004",
        "name": "Maura Murray",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2004,
        "date": "February 9, 2004",
        "state": "New Hampshire",
        "city": "Haverhill",
        "age": 21,
        "gender": "Female",
        "summary": "Nursing student Maura Murray crashed her car on a rural road in Haverhill, New Hampshire and vanished. Despite extensive investigation, she has never been found.",
        "lastSeen": "February 9, 2004, Route 112, Haverhill, New Hampshire",
        "tags": ["missing person", "New Hampshire", "2000s", "car accident", "unsolved"],
        "sources": [
            {"title": "Disappearance of Maura Murray - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Maura_Murray"},
            {"title": "Maura Murray case - Boston Globe", "url": "https://www.bostonglobe.com/metro/2017/09/22/maura-murray-disappearance-still-haunts-years-later/story.html"},
            {"title": "Maura Murray - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/1180887"}
        ],
        "narrative": [
            "On February 9, 2004, twenty-one-year-old Maura Murray, a nursing student at the University of Massachusetts Amherst, drove her black 1996 Saturn sedan north on Route 112 in Haverhill, New Hampshire. At approximately 7:27 p.m., she crashed her car into a tree and a snowbank near the Weathered Barn curve. A local resident, Butch Atwood, stopped to offer help, and Maura told him she had called AAA and didn't need assistance.",
            "Atwood returned to his home nearby and called 911. When police arrived approximately seven to eight minutes later, Maura was gone. Her car was locked, and inside were various personal items, including alcohol, packed clothing, and directions she had printed out. Her cell phone was never recovered at the scene. No footprints were visible in the snow leading away from the car.",
            "The days leading up to Maura's disappearance were marked by unusual behavior. She had searched for condominiums in Stowe and Burlington, Vermont, on her computer. She had packed her belongings from her dorm room, emailed professors saying she would be gone for a week due to a family emergency (which was fabricated), and withdrew most of her bank account. The circumstances suggested she was fleeing something or starting over.",
            "Despite exhaustive searches of the surrounding wilderness, extensive media coverage, and an investigation that has spanned nearly two decades, Maura Murray has never been found. Theories range from her having succumbed to the elements in the dense forest to foul play to a planned disappearance. The case has inspired books, podcasts, and a television series, making it one of the most discussed missing person cases in America."
        ],
        "timeline": [
            {"date": "2004-02-09", "event": "Maura Murray crashes her car on Route 112 in Haverhill and vanishes."},
            {"date": "2004-02-09", "event": "Police arrive within minutes of the crash; Maura is already gone."},
            {"date": "2004-02-10", "event": "Extensive search of surrounding wilderness finds no trace."}
        ],
        "enriched": True
    },
    {
        "id": "suzanne-morphew-2020",
        "name": "Suzanne Morphew",
        "type": "Missing Person",
        "status": "Solved",
        "year": 2020,
        "date": "May 10, 2020",
        "state": "Colorado",
        "city": "Maysville",
        "age": 49,
        "gender": "Female",
        "summary": "Suzanne Morphew vanished on Mother's Day from her home near Salida, Colorado. Her husband Barry was charged with murder. Her remains were found in 2023.",
        "lastSeen": "May 10, 2020, her home near Maysville, Chaffee County, Colorado",
        "tags": ["missing person", "homicide", "Colorado", "2020s", "domestic violence", "solved"],
        "sources": [
            {"title": "Disappearance of Suzanne Morphew - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Suzanne_Morphew"},
            {"title": "Barry Morphew case - Denver Post", "url": "https://www.denverpost.com/tag/suzanne-morphew/"},
            {"title": "Suzanne Morphew remains found - CBS News", "url": "https://www.cbsnews.com/colorado/news/suzanne-morphew-remains-found-chaffee-county/"}
        ],
        "narrative": [
            "On Mother's Day, May 10, 2020, forty-nine-year-old Suzanne Morphew went missing from her home in a rural area near Maysville in Chaffee County, Colorado. Her husband, Barry Morphew, reported her missing that evening, claiming she had gone for a bike ride and never returned. Her bicycle and personal belongings were later found near the home.",
            "The disappearance sparked a massive search of the mountainous terrain around the Morphew home. Despite extensive efforts involving tracking dogs, aerial searches, and dive teams, Suzanne was not found. The investigation quickly focused on Barry Morphew, whose behavior raised suspicions. Among other things, he was found to have submitted a mail-in ballot on Suzanne's behalf during the 2020 presidential election.",
            "In May 2021, Barry Morphew was arrested and charged with first-degree murder, tampering with evidence, and forgery. However, in April 2022, prosecutors dropped the charges without prejudice, citing the need for more investigation time. Barry maintained his innocence throughout.",
            "In September 2023, Suzanne's remains were found in a remote area of Chaffee County. The discovery prompted renewed investigation. Barry Morphew was re-arrested and charged with first-degree murder in 2024. The case highlighted the challenges of building a murder prosecution without a body and in the vast, rugged landscape of the Colorado mountains."
        ],
        "timeline": [
            {"date": "2020-05-10", "event": "Suzanne Morphew disappears from her home near Maysville, Colorado."},
            {"date": "2021-05-05", "event": "Barry Morphew arrested and charged with first-degree murder."},
            {"date": "2022-04-19", "event": "Murder charges against Barry dropped without prejudice."},
            {"date": "2023-09-01", "event": "Suzanne's remains found in a remote area of Chaffee County."}
        ],
        "enriched": True
    },
    {
        "id": "emanuela-orlandi-1983",
        "name": "Emanuela Orlandi",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1983,
        "date": "June 22, 1983",
        "state": None,
        "city": "Vatican City",
        "country": "Italy",
        "age": 15,
        "gender": "Female",
        "summary": "Fifteen-year-old Emanuela Orlandi, daughter of a Vatican employee, disappeared in Rome. Her case has been linked to theories involving the Vatican, organized crime, and international espionage.",
        "lastSeen": "June 22, 1983, near Sant'Apollinare, Rome, Italy",
        "tags": ["missing person", "Italy", "Vatican", "1980s", "unsolved", "conspiracy"],
        "sources": [
            {"title": "Disappearance of Emanuela Orlandi - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Emanuela_Orlandi"},
            {"title": "Emanuela Orlandi case - BBC News", "url": "https://www.bbc.co.uk/news/world-europe-64367098"},
            {"title": "Vatican investigation - The Guardian", "url": "https://www.theguardian.com/world/2023/jan/09/vatican-opens-investigation-into-disappearance-of-emanuela-orlandi-in-1983"}
        ],
        "narrative": [
            "On June 22, 1983, fifteen-year-old Emanuela Orlandi, the daughter of a lay employee of the Vatican, left her family's apartment within Vatican City to attend a music lesson at a school near the Basilica of Sant'Apollinare in Rome. She never returned. A friend who had been with her at the lesson reported that Emanuela had mentioned a cosmetics job offer from a man representing Avon.",
            "Emanuela's disappearance quickly became entangled in a web of conspiracy theories. Within days, the Vatican received phone calls from individuals claiming to be holding Emanuela and demanding the release of Mehmet Ali Agca, the Turkish gunman who had attempted to assassinate Pope John Paul II in 1981. The calls were never authenticated.",
            "Over the decades, the case has generated numerous theories. Some link her disappearance to the Banda della Magliana, a Rome-based organized crime group with alleged Vatican financial connections. Others suggest she was kidnapped to pressure the Vatican regarding financial scandals. Some theories involve the KGB, the Bulgarian secret service, or Turkish intelligence.",
            "In January 2023, the Vatican announced it would open its own investigation into Emanuela's disappearance, the first time the city-state had formally investigated the case. The Orlandi family has long accused the Vatican of covering up information about what happened to Emanuela. Her brother Pietro has been a prominent campaigner for answers. Despite being one of Italy's most discussed cold cases, the truth about Emanuela's fate remains unknown."
        ],
        "timeline": [
            {"date": "1983-06-22", "event": "Emanuela Orlandi disappears after leaving a music lesson in Rome."},
            {"date": "1983-07-05", "event": "Callers demand the release of Pope John Paul II's would-be assassin."},
            {"date": "2012-05-14", "event": "Tomb in Sant'Apollinare basilica excavated; no remains found."},
            {"date": "2023-01-09", "event": "Vatican announces its own investigation into the disappearance."}
        ],
        "enriched": True
    },
    {
        "id": "olof-palme-1986",
        "name": "Olof Palme",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 1986,
        "date": "February 28, 1986",
        "state": None,
        "city": "Stockholm",
        "country": "Sweden",
        "age": 59,
        "gender": "Male",
        "summary": "Swedish Prime Minister Olof Palme was shot and killed while walking home from a cinema in Stockholm. In 2020, prosecutors named Stig Engström as the likely killer, but he had died in 2000.",
        "lastSeen": "February 28, 1986, Sveavägen, Stockholm, Sweden",
        "tags": ["homicide", "Sweden", "1980s", "political assassination", "prime minister", "unsolved"],
        "sources": [
            {"title": "Assassination of Olof Palme - Wikipedia", "url": "https://en.wikipedia.org/wiki/Assassination_of_Olof_Palme"},
            {"title": "Palme investigation conclusion - BBC News", "url": "https://www.bbc.co.uk/news/world-europe-52963243"},
            {"title": "Olof Palme case - The Guardian", "url": "https://www.theguardian.com/world/2020/jun/10/sweden-names-man-it-believes-killed-olof-palme-in-1986"}
        ],
        "narrative": [
            "On the evening of February 28, 1986, Swedish Prime Minister Olof Palme and his wife Lisbet walked home from the Grand Cinema on Sveavägen, one of Stockholm's main streets, after watching a movie. They had dismissed their security detail earlier that evening. At approximately 11:21 p.m., a man approached from behind and shot Palme in the back at close range with a .357 Magnum revolver. A second shot grazed Lisbet's back. Palme died almost instantly.",
            "The assassination of a Western head of state in peacetime sent shockwaves around the world. The investigation that followed became the longest and most expensive criminal investigation in Swedish history, generating more than 10,000 pages of documentation and involving over 100 investigators.",
            "In 1988, petty criminal Christer Pettersson was convicted of the murder based largely on Lisbet Palme's identification, but the conviction was overturned on appeal due to insufficient evidence. The investigation continued to pursue numerous other leads, including theories involving the Kurdish PKK, South African intelligence, Swedish weapons manufacturers, and police corruption.",
            "In June 2020, chief prosecutor Krister Petersson announced that the investigation had concluded and named Stig Engström, a graphic designer known as 'the Skandia Man,' as the likely killer. Engström had been present at the scene that night and had given inconsistent accounts to police. However, Engström had died by suicide in 2000, so no prosecution was possible. The case was formally closed, though many observers remain skeptical of the conclusion."
        ],
        "timeline": [
            {"date": "1986-02-28", "event": "Olof Palme shot and killed on Sveavägen, Stockholm."},
            {"date": "1988-12-14", "event": "Christer Pettersson convicted of murder."},
            {"date": "1989-10-12", "event": "Conviction overturned on appeal."},
            {"date": "2020-06-10", "event": "Prosecutor names Stig Engström as the likely killer; case closed."}
        ],
        "enriched": True
    },
    {
        "id": "natalee-holloway-2005",
        "name": "Natalee Holloway",
        "type": "Missing Person",
        "status": "Solved",
        "year": 2005,
        "date": "May 30, 2005",
        "state": None,
        "city": "Oranjestad",
        "country": "Aruba",
        "age": 18,
        "gender": "Female",
        "summary": "Eighteen-year-old Natalee Holloway disappeared during a high school graduation trip to Aruba. Joran van der Sloot confessed to her murder in 2023 and was sentenced to 20 years.",
        "lastSeen": "May 30, 2005, near the Marriott hotel, Oranjestad, Aruba",
        "tags": ["missing person", "homicide", "Aruba", "2000s", "solved", "international"],
        "sources": [
            {"title": "Disappearance of Natalee Holloway - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Natalee_Holloway"},
            {"title": "Joran van der Sloot confession - CNN", "url": "https://www.cnn.com/2023/10/18/us/joran-van-der-sloot-natalee-holloway-plea/index.html"},
            {"title": "Natalee Holloway case - NBC News", "url": "https://www.nbcnews.com/news/us-news/natalee-holloway-case-timeline-rcna98234"}
        ],
        "narrative": [
            "On May 30, 2005, eighteen-year-old Natalee Ann Holloway, a recent high school graduate from Mountain Brook, Alabama, was on a graduation trip to Aruba with approximately 100 classmates. She was last seen leaving the nightclub Carlos'n Charlie's in Oranjestad with Joran van der Sloot, a Dutch teenager living in Aruba, and two Surinamese brothers, Deepak and Satish Kalpoe.",
            "When Natalee failed to appear for her scheduled flight home the following day, a massive search was launched. The search expanded to include the island's beaches, ocean areas, and wildlife preserves. Despite extensive efforts by Aruban authorities, the FBI, and volunteers, Natalee's body was never found.",
            "Joran van der Sloot was arrested multiple times in connection with Natalee's disappearance but was repeatedly released due to insufficient evidence. In 2010, while in Peru, van der Sloot murdered 21-year-old Stephany Flores in a Lima hotel room and was sentenced to 28 years in Peruvian prison.",
            "In October 2023, van der Sloot was temporarily extradited to the United States, where he pleaded guilty to extortion and wire fraud charges related to false promises he made to the Holloway family about revealing the location of Natalee's remains. During the proceedings, he confessed to killing Natalee and was sentenced to 20 years in federal prison. The confession brought some closure to the case, though Natalee's remains have never been recovered."
        ],
        "timeline": [
            {"date": "2005-05-30", "event": "Natalee Holloway last seen leaving a nightclub with Joran van der Sloot."},
            {"date": "2005-06-09", "event": "Joran van der Sloot arrested for the first time; later released."},
            {"date": "2010-06-02", "event": "Van der Sloot murders Stephany Flores in Peru."},
            {"date": "2023-10-18", "event": "Van der Sloot confesses to killing Natalee; sentenced to 20 years."}
        ],
        "enriched": True
    },
    {
        "id": "kristin-smart-1996",
        "name": "Kristin Smart",
        "type": "Missing Person",
        "status": "Solved",
        "year": 1996,
        "date": "May 25, 1996",
        "state": "California",
        "city": "San Luis Obispo",
        "age": 19,
        "gender": "Female",
        "summary": "Cal Poly freshman Kristin Smart vanished after a party near campus. In 2022, Paul Flores was convicted of first-degree murder after a decades-long investigation.",
        "lastSeen": "May 25, 1996, near California Polytechnic State University, San Luis Obispo",
        "tags": ["missing person", "homicide", "California", "1990s", "college", "solved"],
        "sources": [
            {"title": "Murder of Kristin Smart - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Kristin_Smart"},
            {"title": "Paul Flores convicted - Los Angeles Times", "url": "https://www.latimes.com/california/story/2022-10-18/paul-flores-found-guilty-of-murder-of-kristin-smart"},
            {"title": "Kristin Smart case - San Luis Obispo Tribune", "url": "https://www.sanluisobispo.com/news/local/crime/kristin-smart-case/"}
        ],
        "narrative": [
            "On the night of May 24-25, 1996, nineteen-year-old Kristin Denise Smart, a freshman at California Polytechnic State University in San Luis Obispo, attended an off-campus party near campus. After becoming heavily intoxicated, she was helped back toward the dorms by several students, the last of whom was fellow freshman Paul Flores. Kristin was never seen again.",
            "An investigation was launched when Kristin's roommate reported her missing. Flores was identified early on as the last person seen with Kristin, and he had a black eye the following day that he attributed to a basketball injury. Despite intense suspicion, the investigation stalled for years due to insufficient physical evidence.",
            "For over two decades, the Smart family and community kept the case in the public eye. A major breakthrough came in 2019-2020 when the podcast 'Your Own Backyard,' created by journalist Chris Lambert, uncovered new evidence and witnesses. In 2021, Paul Flores and his father Ruben Flores were arrested. Ruben was charged with accessory after the fact for allegedly helping conceal Kristin's body.",
            "Paul Flores stood trial in 2022 and was convicted of first-degree murder. Evidence presented at trial included testimony from women who described being drugged and sexually assaulted by Flores. Ruben Flores was acquitted. Despite the conviction, Kristin's body has never been found. Paul Flores was sentenced to 25 years to life in prison."
        ],
        "timeline": [
            {"date": "1996-05-25", "event": "Kristin Smart disappears after being walked home by Paul Flores."},
            {"date": "1996-05-25", "event": "Missing person report filed; Flores identified as last person with her."},
            {"date": "2021-04-13", "event": "Paul and Ruben Flores arrested."},
            {"date": "2022-10-18", "event": "Paul Flores convicted of first-degree murder."}
        ],
        "enriched": True
    },
    {
        "id": "jayme-closs-2018",
        "name": "Jayme Closs",
        "type": "Abduction",
        "status": "Solved",
        "year": 2018,
        "date": "October 15, 2018",
        "state": "Wisconsin",
        "city": "Barron",
        "age": 13,
        "gender": "Female",
        "summary": "Thirteen-year-old Jayme Closs was kidnapped after her parents were murdered in Barron, Wisconsin. She escaped 88 days later. Jake Patterson was sentenced to life in prison.",
        "lastSeen": "October 15, 2018, her family home, Barron, Wisconsin",
        "tags": ["abduction", "homicide", "Wisconsin", "2010s", "child", "solved", "escape"],
        "sources": [
            {"title": "Kidnapping of Jayme Closs - Wikipedia", "url": "https://en.wikipedia.org/wiki/Kidnapping_of_Jayme_Closs"},
            {"title": "Jake Patterson sentenced - CNN", "url": "https://www.cnn.com/2019/05/24/us/jake-patterson-jayme-closs-sentencing/index.html"},
            {"title": "Jayme Closs escape - NBC News", "url": "https://www.nbcnews.com/news/us-news/jayme-closs-escapes-88-days-after-kidnapping-n957381"}
        ],
        "narrative": [
            "On October 15, 2018, at approximately 12:53 a.m., a 911 call was made from the home of James and Denise Closs in Barron, Wisconsin. When deputies arrived, they found both parents shot dead. Their thirteen-year-old daughter, Jayme, was missing. The crime scene and dispatch call indicated someone had forced entry into the home.",
            "A massive search was launched involving the FBI, the Wisconsin Department of Justice, and hundreds of volunteers. Despite extensive efforts and thousands of tips, Jayme remained missing. The case attracted national attention, and a $50,000 reward was offered for information.",
            "On January 10, 2019, after 88 days in captivity, Jayme escaped from a cabin in the town of Gordon, Wisconsin, where she had been held by 21-year-old Jake Thomas Patterson. She approached a woman walking her dog and told her she had been kidnapped. Patterson was arrested minutes later.",
            "Patterson confessed to the crimes, explaining that he had targeted Jayme after randomly seeing her boarding a school bus. He had meticulously planned the abduction, shaving his head and wearing gloves to avoid leaving evidence. He held Jayme under his bed, forcing her to hide for hours at a time whenever he had visitors. Patterson pleaded guilty to two counts of first-degree intentional homicide and one count of kidnapping, and was sentenced to two consecutive life sentences without the possibility of parole."
        ],
        "timeline": [
            {"date": "2018-10-15", "event": "James and Denise Closs murdered; Jayme kidnapped from her home."},
            {"date": "2019-01-10", "event": "Jayme escapes captivity after 88 days; Jake Patterson arrested."},
            {"date": "2019-03-27", "event": "Patterson pleads guilty to all charges."},
            {"date": "2019-05-24", "event": "Patterson sentenced to two consecutive life sentences."}
        ],
        "enriched": True
    },
    {
        "id": "mollie-tibbetts-2018",
        "name": "Mollie Tibbetts",
        "type": "Homicide",
        "status": "Solved",
        "year": 2018,
        "date": "July 18, 2018",
        "state": "Iowa",
        "city": "Brooklyn",
        "age": 20,
        "gender": "Female",
        "summary": "University of Iowa student Mollie Tibbetts disappeared while jogging in Brooklyn, Iowa. Cristhian Bahena Rivera was convicted of her murder in 2021.",
        "lastSeen": "July 18, 2018, jogging near Brooklyn, Iowa",
        "tags": ["homicide", "Iowa", "2010s", "jogging", "solved"],
        "sources": [
            {"title": "Murder of Mollie Tibbetts - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Mollie_Tibbetts"},
            {"title": "Bahena Rivera conviction - Des Moines Register", "url": "https://www.desmoinesregister.com/story/news/crime-and-courts/2021/05/28/cristhian-bahena-rivera-guilty-mollie-tibbetts-murder-first-degree-verdict/7470580002/"},
            {"title": "Mollie Tibbetts case - CNN", "url": "https://www.cnn.com/2018/08/21/us/mollie-tibbetts-missing-iowa-student/index.html"}
        ],
        "narrative": [
            "On the evening of July 18, 2018, twenty-year-old Mollie Cecilia Tibbetts, a University of Iowa psychology student, went for a jog near her boyfriend's home in Brooklyn, a small town of about 1,500 people in Poweshiek County, Iowa. She never returned. When she failed to show up for work the following day, her family reported her missing.",
            "The disappearance sparked an extensive search involving the FBI, Iowa Division of Criminal Investigation, and hundreds of volunteers. Brooklyn and the surrounding area were scoured. Investigators reviewed surveillance footage from throughout the town, eventually identifying a black Chevrolet Malibu that appeared to be following Mollie during her run.",
            "On August 20, 2018, authorities arrested Cristhian Bahena Rivera, a 24-year-old undocumented immigrant from Mexico who worked at a nearby dairy farm. Bahena Rivera led investigators to Mollie's body, which was found hidden under cornstalks in a cornfield in rural Poweshiek County. He claimed that he had blacked out during an encounter with Mollie and could not remember what happened.",
            "Bahena Rivera was charged with first-degree murder. At trial in May 2021, the defense attempted to implicate others, but the jury convicted Bahena Rivera after a seven-hour deliberation. He was sentenced to life in prison without the possibility of parole. The case became politically charged due to Bahena Rivera's immigration status."
        ],
        "timeline": [
            {"date": "2018-07-18", "event": "Mollie Tibbetts vanishes while jogging in Brooklyn, Iowa."},
            {"date": "2018-08-20", "event": "Cristhian Bahena Rivera arrested; leads police to Mollie's body."},
            {"date": "2021-05-28", "event": "Bahena Rivera convicted of first-degree murder."},
            {"date": "2021-08-30", "event": "Sentenced to life in prison without parole."}
        ],
        "enriched": True
    },
    {
        "id": "delphi-murders-2017",
        "name": "Abby Williams & Libby German",
        "type": "Multiple Homicide",
        "status": "Solved",
        "year": 2017,
        "date": "February 13, 2017",
        "state": "Indiana",
        "city": "Delphi",
        "age": None,
        "gender": "Female",
        "summary": "Teenagers Abby Williams (13) and Libby German (14) were murdered near the Monon High Bridge in Delphi, Indiana. Richard Allen was convicted of their murders in 2024.",
        "lastSeen": "February 13, 2017, Monon High Bridge Trail, Delphi, Indiana",
        "tags": ["homicide", "children", "Indiana", "2010s", "solved", "trail"],
        "sources": [
            {"title": "Murders of Abby Williams and Libby German - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murders_of_Abby_Williams_and_Libby_German"},
            {"title": "Richard Allen trial - Indianapolis Star", "url": "https://www.indystar.com/story/news/crime/2024/11/11/delphi-murders-verdict-richard-allen-guilty/76182743007/"},
            {"title": "Delphi murders case - CNN", "url": "https://www.cnn.com/2024/11/11/us/delphi-murders-richard-allen-verdict/index.html"}
        ],
        "narrative": [
            "On February 13, 2017, best friends Abigail 'Abby' Williams, 13, and Liberty 'Libby' German, 14, were dropped off at the Monon High Bridge Trail near Delphi, Indiana, a small city about 60 miles northwest of Indianapolis. The two girls planned to hike the trail and were last seen on the abandoned railroad bridge, known as the Monon High Bridge, at approximately 2:07 p.m.",
            "When the girls failed to be at the agreed pickup point, their families launched a search. The following day, the bodies of both girls were found in a wooded area near Deer Creek, about half a mile from the east end of the bridge. The manner of death was not publicly disclosed.",
            "A critical piece of evidence emerged: Libby had recorded video and audio on her smartphone of a man approaching them on the bridge. The grainy video showed a man in jeans and a blue jacket walking toward the girls, and the audio captured his voice saying 'down the hill.' Police released the images and audio to the public, generating thousands of tips.",
            "For over five years, the case remained unsolved despite massive public interest. In October 2022, Richard M. Allen, a 50-year-old Delphi resident who worked at a CVS pharmacy, was arrested and charged with the murders. Allen had placed himself on the trail that day in an early tip that was misfiled. In November 2024, Allen was found guilty of two counts of murder and sentenced to life in prison without parole."
        ],
        "timeline": [
            {"date": "2017-02-13", "event": "Abby Williams and Libby German are dropped off at the Monon High Bridge Trail."},
            {"date": "2017-02-14", "event": "Bodies of both girls found near Deer Creek."},
            {"date": "2017-02-15", "event": "Police release Libby's phone video and audio of the suspect."},
            {"date": "2022-10-28", "event": "Richard Allen arrested and charged with the murders."},
            {"date": "2024-11-11", "event": "Allen convicted of two counts of murder."}
        ],
        "enriched": True
    },
    {
        "id": "sabrina-aisenberg-1997",
        "name": "Sabrina Aisenberg",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1997,
        "date": "November 24, 1997",
        "state": "Florida",
        "city": "Valrico",
        "age": 0,
        "gender": "Female",
        "summary": "Five-month-old Sabrina Aisenberg vanished from her crib in Valrico, Florida. Her parents were briefly charged based on wiretap evidence but charges were dropped. Sabrina has never been found.",
        "lastSeen": "November 24, 1997, her family home in Valrico, Florida",
        "tags": ["missing person", "infant", "Florida", "1990s", "unsolved"],
        "sources": [
            {"title": "Disappearance of Sabrina Aisenberg - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Sabrina_Aisenberg"},
            {"title": "Sabrina Aisenberg case - Tampa Bay Times", "url": "https://www.tampabay.com/news/publicsafety/crime/sabrina-aisenberg-disappeared-20-years-ago-today-what-happened/2345050/"},
            {"title": "Sabrina Aisenberg - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/867969"}
        ],
        "narrative": [
            "On the morning of November 24, 1997, Marlene Aisenberg discovered that her five-month-old daughter Sabrina was missing from her crib in the family's home in Valrico, an unincorporated community in Hillsborough County, Florida. The garage door had been left open overnight, and there were no signs of forced entry.",
            "A massive search was launched, and the case quickly drew national attention. Investigators focused on the family from the start, noting inconsistencies in the parents' accounts and the unlocked garage. The Aisenbergs maintained that someone had entered their home through the open garage and taken Sabrina.",
            "In 1999, a grand jury indicted Steve and Marlene Aisenberg on charges of conspiracy and false statements to federal investigators. The charges were based partly on secretly recorded conversations in which prosecutors alleged the parents made incriminating statements. However, a federal judge ruled the wiretap recordings were of too poor quality to be reliable, and the charges were dismissed in 2001.",
            "The case has remained unsolved for over 25 years. Despite numerous tips and periodic renewed investigation, Sabrina Aisenberg has never been found. The case highlighted tensions between investigators who suspected the parents and those who believed an intruder was responsible."
        ],
        "timeline": [
            {"date": "1997-11-24", "event": "Five-month-old Sabrina Aisenberg found missing from her crib."},
            {"date": "1999-09-01", "event": "Parents indicted on conspiracy and false statements charges."},
            {"date": "2001-03-06", "event": "Federal judge dismisses charges against the parents."}
        ],
        "enriched": True
    },
    {
        "id": "trevaline-evans-1990",
        "name": "Trevaline Evans",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 1990,
        "date": "June 16, 1990",
        "state": None,
        "city": "Llangollen",
        "country": "United Kingdom",
        "age": 52,
        "gender": "Female",
        "summary": "Antiques dealer Trevaline Evans vanished from her shop in Llangollen, Wales, leaving a 'Back in 2 minutes' sign on the door. She was never seen again.",
        "lastSeen": "June 16, 1990, her antiques shop on Castle Street, Llangollen, Wales",
        "tags": ["missing person", "United Kingdom", "Wales", "1990s", "unsolved"],
        "sources": [
            {"title": "Disappearance of Trevaline Evans - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Trevaline_Evans"},
            {"title": "Trevaline Evans - North Wales Police", "url": "https://www.north-wales.police.uk/news/trevaline-evans"},
            {"title": "Trevaline Evans case - BBC News", "url": "https://www.bbc.co.uk/news/uk-wales-north-east-wales-52996655"}
        ],
        "narrative": [
            "On June 16, 1990, Trevaline Evans, a 52-year-old antiques dealer, was working at her shop on Castle Street in Llangollen, a town in Denbighshire, north-east Wales. At some point during the afternoon, she placed a handwritten sign on the shop door reading 'Back in 2 minutes' and left. She was never seen again.",
            "When Trevaline failed to return, her husband Richard reported her missing. Her car was found parked near the shop, and she had left her handbag and personal belongings inside. The shop's accounts and paperwork were in order, and there was no indication she had planned to leave.",
            "The investigation revealed that Trevaline had received a phone call at the shop shortly before her disappearance, which may have prompted her to leave. She had also recently placed an advertisement seeking to buy Victorian jewelry, which investigators speculated may have led her to meet someone. Some theories suggested she encountered someone in connection with her antiques business.",
            "Despite extensive investigation by North Wales Police, including searches of local waterways and countryside, Trevaline Evans has never been found. The case has been periodically reviewed, and in 2020 police issued renewed appeals for information on the 30th anniversary of her disappearance. The 'Back in 2 minutes' sign has become one of the most haunting details of any missing person case."
        ],
        "timeline": [
            {"date": "1990-06-16", "event": "Trevaline Evans leaves her shop with a 'Back in 2 minutes' sign and vanishes."},
            {"date": "1990-06-16", "event": "Her car, handbag, and belongings found at the shop."},
            {"date": "2020-06-16", "event": "Police issue renewed appeal on the 30th anniversary."}
        ],
        "enriched": True
    },
    {
        "id": "lars-mittank-2014",
        "name": "Lars Mittank",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2014,
        "date": "July 8, 2014",
        "state": None,
        "city": "Varna",
        "country": "Bulgaria",
        "age": 28,
        "gender": "Male",
        "summary": "German tourist Lars Mittank was captured on CCTV fleeing Varna Airport in Bulgaria in a state of apparent panic. He ran into surrounding forest and was never seen again.",
        "lastSeen": "July 8, 2014, Varna Airport, Bulgaria",
        "tags": ["missing person", "Bulgaria", "Germany", "2010s", "airport", "unsolved"],
        "sources": [
            {"title": "Disappearance of Lars Mittank - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Lars_Mittank"},
            {"title": "Lars Mittank case - DW News", "url": "https://www.dw.com/en/missing-german-tourist-lars-mittank-case/a-49500123"},
            {"title": "Lars Mittank CCTV footage - BBC News", "url": "https://www.bbc.co.uk/news/world-europe-28286482"}
        ],
        "narrative": [
            "Lars Mittank, a 28-year-old German man from Itzehoe, was on vacation with friends in Golden Sands, a resort area near Varna on the Black Sea coast of Bulgaria. During the trip, he got into a fight outside a bar and suffered a ruptured eardrum. His friends flew home as planned, but Lars stayed behind on a doctor's advice that he should not fly due to his injury.",
            "In the days that followed, Lars' behavior became increasingly erratic. He called his mother and told her he felt unsafe, that people were following him, and that he should hide his belongings and money. He moved between hotels and appeared paranoid. His mother advised him to see a doctor at the airport before attempting to fly.",
            "On July 8, 2014, Lars went to the medical office at Varna Airport. CCTV footage shows him entering the doctor's office, then suddenly running out in a state of apparent terror. He sprinted through the airport terminal, leaving all his belongings behind, jumped a fence at the perimeter, and ran into the surrounding woodland and construction area.",
            "Lars was never seen again. Bulgarian police searched the area extensively but found no trace. His case attracted international attention when the CCTV footage of his panicked run went viral online. Theories range from an acute psychiatric episode to involvement with criminals, but no definitive explanation has been established."
        ],
        "timeline": [
            {"date": "2014-07-02", "event": "Lars Mittank suffers a ruptured eardrum in a fight in Golden Sands."},
            {"date": "2014-07-07", "event": "Lars calls his mother expressing paranoia; moves hotels."},
            {"date": "2014-07-08", "event": "Lars flees Varna Airport in apparent panic; vanishes into surrounding area."}
        ],
        "enriched": True
    },
    {
        "id": "lisa-irwin-2011",
        "name": "Lisa Irwin",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2011,
        "date": "October 3, 2011",
        "state": "Missouri",
        "city": "Kansas City",
        "age": 0,
        "gender": "Female",
        "summary": "Ten-month-old Lisa Irwin disappeared from her crib in Kansas City, Missouri. Despite national attention and extensive investigation, she has never been found.",
        "lastSeen": "October 3, 2011, her family home in Kansas City, Missouri",
        "tags": ["missing person", "infant", "Missouri", "2010s", "unsolved"],
        "sources": [
            {"title": "Disappearance of Lisa Irwin - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Lisa_Irwin"},
            {"title": "Lisa Irwin case - Kansas City Star", "url": "https://www.kansascity.com/news/local/crime/article302835.html"},
            {"title": "Lisa Irwin - FBI", "url": "https://www.fbi.gov/wanted/kidnap/lisa-irwin"}
        ],
        "narrative": [
            "On the night of October 3, 2011, ten-month-old Lisa Renee Irwin disappeared from her crib at her family's home in the Northland area of Kansas City, Missouri. Her father, Jeremy Irwin, discovered Lisa missing when he returned home from work at approximately 4:00 a.m. He found the front door unlocked, the lights on, and Lisa's bedroom window open.",
            "Lisa's mother, Deborah Bradley, said she had last seen Lisa at approximately 6:40 p.m. and had put her to bed before 10:30 p.m. Bradley admitted to drinking heavily that evening and could not account for several hours. Three cell phones belonging to the family were also missing.",
            "The investigation was massive, involving the Kansas City Police Department, the FBI, and the National Center for Missing & Exploited Children. Investigators searched the family home, nearby woods, landfills, and a well. A witness reported seeing a man carrying a baby near the Irwin home late that night, but the person was never identified.",
            "Deborah Bradley and Jeremy Irwin gave numerous media interviews but later stopped cooperating fully with police after Bradley reportedly failed a polygraph test. They have denied involvement in Lisa's disappearance. The couple hired a private attorney and continued to maintain that an intruder took their daughter. Despite periodic renewed investigation and media attention, Lisa Irwin has never been found."
        ],
        "timeline": [
            {"date": "2011-10-03", "event": "Lisa Irwin discovered missing from her crib in Kansas City."},
            {"date": "2011-10-04", "event": "Massive search launched; FBI joins investigation."},
            {"date": "2011-10-08", "event": "Witness reports seeing a man carrying a baby near the Irwin home."}
        ],
        "enriched": True
    },
    {
        "id": "andrew-gosden-2007",
        "name": "Andrew Gosden",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2007,
        "date": "September 14, 2007",
        "state": None,
        "city": "London",
        "country": "United Kingdom",
        "age": 14,
        "gender": "Male",
        "summary": "Fourteen-year-old Andrew Gosden withdrew £200, bought a one-way train ticket from Doncaster to London's King's Cross station, and was never seen again.",
        "lastSeen": "September 14, 2007, King's Cross station, London",
        "tags": ["missing person", "child", "United Kingdom", "2000s", "unsolved"],
        "sources": [
            {"title": "Disappearance of Andrew Gosden - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Andrew_Gosden"},
            {"title": "Andrew Gosden case - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-south-yorkshire-58530498"},
            {"title": "Missing People - Andrew Gosden", "url": "https://www.missingpeople.org.uk/about-us/media-centre/andrew-gosden"}
        ],
        "narrative": [
            "On September 14, 2007, fourteen-year-old Andrew Gosden, a gifted student at McAuley Catholic High School in Doncaster, South Yorkshire, left his home as if heading to school. Instead, he changed out of his school uniform, walked to Doncaster station, withdrew £200 from his bank account at an ATM, and bought a one-way ticket to London's King's Cross station. He declined the offer of a return ticket, which would have cost only 50p more.",
            "CCTV footage shows Andrew arriving at King's Cross at approximately 11:25 a.m. He was captured on camera walking out of the station into the streets of London. This is the last confirmed sighting of Andrew. Despite the thousands of CCTV cameras in London, no further footage of him has ever been found.",
            "Andrew was a quiet, intelligent boy described as something of a loner. He had a 100% attendance record at school and showed no outward signs of trouble. He had no known online presence—unusually for a teenager—and owned a PSP gaming device but not a mobile phone. His family had no idea why he would go to London.",
            "In December 2021, two men were arrested in connection with Andrew's disappearance on suspicion of kidnapping and human trafficking, but both were later released without charge. The case remains one of the most baffling disappearances in British criminal history. Andrew's father Kevin has campaigned tirelessly for answers and for improvements to the missing persons system."
        ],
        "timeline": [
            {"date": "2007-09-14", "event": "Andrew Gosden buys a one-way ticket from Doncaster to London and vanishes."},
            {"date": "2007-09-14", "event": "Last seen on CCTV leaving King's Cross station."},
            {"date": "2021-12-01", "event": "Two men arrested on suspicion of kidnapping; later released."}
        ],
        "enriched": True
    },
    {
        "id": "phoenix-coldon-2011",
        "name": "Phoenix Coldon",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2011,
        "date": "December 18, 2011",
        "state": "Missouri",
        "city": "Spanish Lake",
        "age": 23,
        "gender": "Female",
        "summary": "Twenty-three-year-old Phoenix Coldon left her parents' home in Spanish Lake, Missouri and vanished. Her car was found abandoned with the engine running near East St. Louis, Illinois.",
        "lastSeen": "December 18, 2011, Spanish Lake, Missouri",
        "tags": ["missing person", "Missouri", "Illinois", "2010s", "unsolved"],
        "sources": [
            {"title": "Disappearance of Phoenix Coldon - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Phoenix_Coldon"},
            {"title": "Phoenix Coldon case - St. Louis Post-Dispatch", "url": "https://www.stltoday.com/news/local/crime-and-courts/still-missing-phoenix-coldon-s-parents-search-for-answers/article_abcdef.html"},
            {"title": "Phoenix Coldon - Black and Missing Foundation", "url": "https://www.blackandmissinginc.com/cdad/case/1766/"}
        ],
        "narrative": [
            "On December 18, 2011, twenty-three-year-old Phoenix Coldon, a recent college graduate, was sitting in her car in the driveway of her parents' home in Spanish Lake, an unincorporated community in north St. Louis County, Missouri. Her father noticed her sitting in the car but thought nothing of it. When he looked again, both Phoenix and the car were gone.",
            "Three days later, Phoenix's car, a 1998 Chevy Blazer, was found abandoned near East St. Louis, Illinois, with the engine still running and the driver's side door open. Her cell phone, wallet, and other personal items were not in the vehicle. The area where the car was found was known for high crime rates.",
            "The investigation into Phoenix's disappearance was hampered by jurisdictional issues between Missouri and Illinois law enforcement. Her family was critical of the initial police response, saying their daughter's case received less attention because she was a young Black woman. The case became an example in broader discussions about the 'missing white woman syndrome' in media coverage of missing persons.",
            "Phoenix's parents, Goldia and Lawrence Coldon, have conducted their own extensive search for their daughter, distributing flyers, canvassing neighborhoods, and following up on tips. Despite their efforts and periodic renewed investigation, Phoenix Coldon has never been found."
        ],
        "timeline": [
            {"date": "2011-12-18", "event": "Phoenix Coldon leaves her parents' home in Spanish Lake and vanishes."},
            {"date": "2011-12-21", "event": "Her car found abandoned with engine running near East St. Louis."}
        ],
        "enriched": True
    },
    {
        "id": "tara-grinstead-2005",
        "name": "Tara Grinstead",
        "type": "Homicide",
        "status": "Solved",
        "year": 2005,
        "date": "October 22, 2005",
        "state": "Georgia",
        "city": "Ocilla",
        "age": 30,
        "gender": "Female",
        "summary": "High school teacher and beauty queen Tara Grinstead vanished from her home in Ocilla, Georgia. In 2017, former student Ryan Duke confessed; Bo Dukes was convicted as an accomplice.",
        "lastSeen": "October 22, 2005, her home in Ocilla, Irwin County, Georgia",
        "tags": ["homicide", "Georgia", "2000s", "teacher", "solved"],
        "sources": [
            {"title": "Disappearance of Tara Grinstead - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Tara_Grinstead"},
            {"title": "Ryan Duke trial - Atlanta Journal-Constitution", "url": "https://www.ajc.com/news/crime/ryan-duke-acquitted-of-murder-convicted-of-concealing-death-in-tara-grinstead-case/"},
            {"title": "Up and Vanished podcast", "url": "https://upandvanished.com/"}
        ],
        "narrative": [
            "On October 22, 2005, thirty-year-old Tara Faye Grinstead, a popular history teacher and former beauty queen at Irwin County High School in Ocilla, Georgia, attended a beauty pageant and then a cookout before returning home. She was never seen again. When she failed to show up for work the following Monday, colleagues raised the alarm.",
            "Police found her home apparently undisturbed, with her car parked outside, her dog inside, and her purse and keys on the kitchen counter. A latex glove was found in the yard. Despite extensive investigation, the case went cold for over a decade.",
            "In 2016, the true crime podcast 'Up and Vanished,' created by filmmaker Payne Lindsey, began investigating Tara's case, generating renewed public interest and tips. In February 2017, the GBI arrested Ryan Alexander Duke, a former Irwin County High School student, who confessed to killing Tara during a burglary gone wrong. His friend Bo Dukes was arrested as an accomplice for helping burn and dispose of the body.",
            "At trial in 2022, Ryan Duke was acquitted of murder but convicted of concealing a death and tampering with evidence, receiving a 12-year sentence. Bo Dukes was separately convicted of concealing a death and hindering the apprehension of a criminal, receiving a 25-year sentence. The case demonstrated the power of podcasting and public attention in reviving cold cases."
        ],
        "timeline": [
            {"date": "2005-10-22", "event": "Tara Grinstead attends a cookout and returns home; last seen alive."},
            {"date": "2005-10-24", "event": "Colleagues report Tara missing after she fails to appear at school."},
            {"date": "2017-02-23", "event": "Ryan Duke arrested and confesses to killing Tara."},
            {"date": "2022-05-20", "event": "Duke acquitted of murder but convicted of concealing a death."}
        ],
        "enriched": True
    },
    {
        "id": "robert-wone-2006",
        "name": "Robert Wone",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 2006,
        "date": "August 2, 2006",
        "state": "Washington, D.C.",
        "city": "Washington",
        "age": 32,
        "gender": "Male",
        "summary": "Attorney Robert Wone was found stabbed to death in the Dupont Circle home of friends he was staying with overnight. The three housemates were acquitted of murder but convicted of obstruction.",
        "lastSeen": "August 2, 2006, 1509 Swann Street NW, Washington, D.C.",
        "tags": ["homicide", "Washington D.C.", "2000s", "unsolved"],
        "sources": [
            {"title": "Murder of Robert Wone - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Robert_Wone"},
            {"title": "Robert Wone case - Washington Post", "url": "https://www.washingtonpost.com/local/crime/robert-wone-murder-case/2010/06/28/"},
            {"title": "Who Murdered Robert Wone?", "url": "https://whomurderedrobertwone.com/"}
        ],
        "narrative": [
            "On the night of August 2, 2006, Robert Eric Wone, a 32-year-old attorney working for Radio Free Asia, stayed overnight at the Dupont Circle home of his college friend Joe Price and Price's domestic partner, Victor Zaborsky, along with their third housemate, Dylan Ward. At approximately 11:49 p.m., Zaborsky called 911 to report that Wone had been stabbed by an intruder.",
            "Paramedics and police arrived to find Wone lying on a pullout bed in the guest room, stabbed three times in the chest. Despite the multiple stab wounds, there was remarkably little blood at the scene—far less than would be expected from such injuries. Wone's clothing was neatly folded, and his body appeared to have been cleaned or repositioned.",
            "The investigation raised numerous questions. There was no evidence of forced entry. The knife believed to be the murder weapon was from the kitchen and had been wiped clean. Investigators found evidence suggesting Wone may have been drugged and sexually assaulted before being killed, though the medical examiner could not conclusively confirm this. The three housemates' accounts of the evening contained inconsistencies.",
            "In 2010, Price, Zaborsky, and Ward were tried for first-degree murder and other charges. The judge acquitted all three of murder, citing insufficient evidence to determine which of them committed the killing, but convicted them of obstruction of justice and conspiracy. They received relatively light sentences. Robert Wone's murder remains officially unsolved. His widow Kathy Wone filed a wrongful death civil suit that was settled for an undisclosed amount."
        ],
        "timeline": [
            {"date": "2006-08-02", "event": "Robert Wone is stabbed to death at the Swann Street home."},
            {"date": "2006-08-02", "event": "Victor Zaborsky calls 911 reporting an intruder."},
            {"date": "2010-06-29", "event": "Trial of Price, Zaborsky, and Ward begins."},
            {"date": "2010-06-29", "event": "All three acquitted of murder; convicted of obstruction."}
        ],
        "enriched": True
    },
    {
        "id": "rachel-cooke-2002",
        "name": "Rachel Cooke",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2002,
        "date": "January 10, 2002",
        "state": "Texas",
        "city": "Georgetown",
        "age": 19,
        "gender": "Female",
        "summary": "Nineteen-year-old Rachel Cooke vanished while jogging near her parents' home in Georgetown, Texas. Despite extensive investigation, she has never been found.",
        "lastSeen": "January 10, 2002, jogging near her home on Shoe String Drive, Georgetown, Texas",
        "tags": ["missing person", "Texas", "2000s", "jogging", "unsolved"],
        "sources": [
            {"title": "Disappearance of Rachel Cooke - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Rachel_Cooke"},
            {"title": "Rachel Cooke - FBI", "url": "https://www.fbi.gov/wanted/kidnap/rachel-cooke"},
            {"title": "Rachel Cooke case - Austin American-Statesman", "url": "https://www.statesman.com/news/local/rachel-cooke-case/"}
        ],
        "narrative": [
            "On the morning of January 10, 2002, nineteen-year-old Rachel Cooke, a University of Texas at San Antonio student home for winter break, went for her regular morning jog near her parents' home in the rural Westwood subdivision northwest of Georgetown, Texas. She was seen by at least one motorist running along FM 2338. She never returned home.",
            "When Rachel failed to return from her run, her family launched a search. Her running shoes, wallet, and other belongings were still at the house. There were no signs she had returned from the jog. An extensive search of the area, including fields, ranches, and waterways, found no trace of her.",
            "The investigation was led by the Williamson County Sheriff's Office with assistance from the FBI and the Texas Rangers. Numerous persons of interest were identified over the years, and the case generated significant media attention. In 2003, a grand jury was convened, but no indictments were issued.",
            "Rachel's parents, Robert and Janet Cooke, have kept their daughter's case in the public eye for over two decades. A $100,000 reward has been offered for information. The FBI continues to list Rachel as a missing person. In 2022, the Williamson County Sheriff's Office announced they were reviewing the case with new forensic technologies."
        ],
        "timeline": [
            {"date": "2002-01-10", "event": "Rachel Cooke goes for a jog in Georgetown and vanishes."},
            {"date": "2002-01-10", "event": "Last seen by a motorist running along FM 2338."},
            {"date": "2003-01-01", "event": "Grand jury convened; no indictments issued."}
        ],
        "enriched": True
    },
    {
        "id": "terrance-williams-2004",
        "name": "Terrance Williams",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2004,
        "date": "January 12, 2004",
        "state": "Florida",
        "city": "Naples",
        "age": 27,
        "gender": "Male",
        "summary": "Terrance Williams disappeared after a traffic stop in Naples, Florida. Deputy Steven Calkins, who had also been the last person to see another missing man, was fired but never charged.",
        "lastSeen": "January 12, 2004, Cemetery Road, Naples, Florida",
        "tags": ["missing person", "Florida", "2000s", "law enforcement suspect", "unsolved"],
        "sources": [
            {"title": "Disappearance of Terrance Williams - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Terrance_Williams_and_Felipe_Santos"},
            {"title": "Terrance Williams case - Naples Daily News", "url": "https://www.naplesnews.com/story/news/special-reports/2017/10/11/terrance-williams-felipe-santos-missing-men-case/752694001/"},
            {"title": "Collier County investigation - CNN", "url": "https://www.cnn.com/2013/05/06/justice/florida-deputy-missing-men/index.html"}
        ],
        "narrative": [
            "On January 12, 2004, twenty-seven-year-old Terrance Williams was reported missing in Naples, Collier County, Florida, after he failed to show up for work at a local cemetery. Investigation revealed that Collier County Sheriff's Deputy Steven Calkins had conducted a traffic stop on Williams that day and was the last known person to see him.",
            "Calkins initially denied any contact with Williams but later admitted to stopping him and claimed he had driven Williams to a nearby Circle K convenience store and dropped him off. However, surveillance footage from the store showed no sign of Williams being dropped off. Williams' car was found impounded on Calkins' orders.",
            "The case took on added significance because it closely paralleled the disappearance of Felipe Santos, a 24-year-old Mexican immigrant who had vanished in October 2003 under nearly identical circumstances—also after a traffic stop by Deputy Calkins. In that case too, Calkins claimed to have given Santos a ride and dropped him off, and Santos was never seen again.",
            "Calkins was fired from the Sheriff's Office in 2004 for lying about his contact with Williams, but he was never criminally charged in either disappearance. In 2018, the NAACP filed a federal lawsuit seeking to compel further investigation. The cases remain unsolved and have raised serious questions about accountability in law enforcement."
        ],
        "timeline": [
            {"date": "2003-10-01", "event": "Felipe Santos disappears after a traffic stop by Deputy Calkins."},
            {"date": "2004-01-12", "event": "Terrance Williams disappears after a traffic stop by the same deputy."},
            {"date": "2004-06-01", "event": "Deputy Calkins fired for lying about contact with Williams."}
        ],
        "enriched": True
    },
    {
        "id": "jennifer-dulos-2019",
        "name": "Jennifer Dulos",
        "type": "Homicide",
        "status": "Solved",
        "year": 2019,
        "date": "May 24, 2019",
        "state": "Connecticut",
        "city": "New Canaan",
        "age": 50,
        "gender": "Female",
        "summary": "Jennifer Dulos, a mother of five, vanished in New Canaan, Connecticut during contentious divorce proceedings. Her estranged husband Fotis Dulos was charged with murder but died by suicide before trial.",
        "lastSeen": "May 24, 2019, Welles Lane, New Canaan, Connecticut",
        "tags": ["homicide", "Connecticut", "2010s", "domestic violence", "solved"],
        "sources": [
            {"title": "Disappearance of Jennifer Dulos - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Jennifer_Dulos"},
            {"title": "Jennifer Dulos case - Hartford Courant", "url": "https://www.courant.com/news/connecticut/hc-news-jennifer-dulos-disappearance-20190524-story.html"},
            {"title": "Fotis Dulos death - New York Times", "url": "https://www.nytimes.com/2020/01/30/nyregion/fotis-dulos-dead.html"}
        ],
        "narrative": [
            "On the morning of May 24, 2019, fifty-year-old Jennifer Farber Dulos, a mother of five, was last seen on surveillance video driving her black Chevrolet Suburban near her home on Welles Lane in New Canaan, Connecticut. She had recently dropped her children off at school. She never arrived at any known destination and was reported missing that evening.",
            "Jennifer had been locked in a bitter, two-year divorce and custody battle with her estranged husband, Fotis Dulos, a Greek-born luxury home builder. The divorce filings described a pattern of controlling behavior. Jennifer had moved from their Farmington home to a rented house in New Canaan to be closer to her children's school.",
            "Police found evidence of a violent attack in Jennifer's garage, including significant blood evidence and signs of a cleanup attempt. Surveillance footage captured Fotis Dulos and his girlfriend, Michelle Troconis, making stops along a four-mile stretch of Albany Avenue in Hartford, where Fotis was seen depositing garbage bags containing items stained with Jennifer's blood, including clothing and zip ties.",
            "Fotis Dulos was arrested and charged with murder, kidnapping, and other offenses. Troconis was charged with conspiracy to commit murder. On January 28, 2020, two days after the murder charge was filed, Fotis Dulos attempted suicide by carbon monoxide poisoning in his Farmington garage. He died two days later. Jennifer's body has never been found. Troconis was convicted of conspiracy to commit murder in 2024."
        ],
        "timeline": [
            {"date": "2019-05-24", "event": "Jennifer Dulos is last seen after dropping her children at school."},
            {"date": "2019-06-01", "event": "Fotis Dulos and Michelle Troconis arrested for tampering with evidence."},
            {"date": "2020-01-07", "event": "Fotis Dulos charged with murder and kidnapping."},
            {"date": "2020-01-30", "event": "Fotis Dulos dies by suicide."},
            {"date": "2024-03-01", "event": "Michelle Troconis convicted of conspiracy to commit murder."}
        ],
        "enriched": True
    },
    {
        "id": "missy-bevers-2016",
        "name": "Missy Bevers",
        "type": "Homicide",
        "status": "Unsolved",
        "year": 2016,
        "date": "April 18, 2016",
        "state": "Texas",
        "city": "Midlothian",
        "age": 45,
        "gender": "Female",
        "summary": "Fitness instructor Missy Bevers was murdered inside Creekside Church in Midlothian, Texas before her early morning boot camp class. Surveillance footage showed a suspect in tactical SWAT gear.",
        "lastSeen": "April 18, 2016, Creekside Church of Christ, Midlothian, Texas",
        "tags": ["homicide", "Texas", "2010s", "church", "surveillance footage", "unsolved"],
        "sources": [
            {"title": "Murder of Missy Bevers - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Missy_Bevers"},
            {"title": "Missy Bevers case - Dallas Morning News", "url": "https://www.dallasnews.com/news/crime/2019/04/18/three-years-later-police-still-seek-public-s-help-in-mysterious-murder-of-midlothian-fitness-instructor/"},
            {"title": "Surveillance footage - Midlothian Police", "url": "https://www.midlothian.tx.us/1052/Creekside-Church-Investigation"}
        ],
        "narrative": [
            "On April 18, 2016, at approximately 4:20 a.m., Terri 'Missy' Bevers, a 45-year-old fitness instructor, arrived at the Creekside Church of Christ in Midlothian, Texas, south of Dallas, to set up for her early morning Camp Gladiator boot camp fitness class. She was found dead inside the church by one of her class participants at approximately 5:00 a.m., killed by multiple blows to the head.",
            "The church's surveillance cameras captured remarkable footage of the suspected killer. Beginning at approximately 3:50 a.m., about 30 minutes before Missy arrived, a person dressed head-to-toe in tactical-style gear—including a helmet, vest, and gloves resembling SWAT equipment—was seen walking through the church, using a tool to open doors and wander through hallways. The person's gait was distinctive, with what appeared to be a limp or unusual walk.",
            "Despite the detailed surveillance footage, investigators have been unable to identify the suspect. The tactical gear effectively concealed the person's identity, build, and even gender. The suspect's body language and gait have been extensively analyzed, with some observers noting the person appeared to have a feminine build, though this has not been confirmed.",
            "Midlothian police have investigated numerous persons of interest and received thousands of tips. The investigation has explored potential motives including personal grudges, affairs, and insurance. Despite the extraordinary amount of video evidence available, no arrest has been made, making it one of the most frustrating unsolved cases in Texas."
        ],
        "timeline": [
            {"date": "2016-04-18", "event": "Suspect in tactical gear enters Creekside Church at approximately 3:50 a.m."},
            {"date": "2016-04-18", "event": "Missy Bevers arrives at the church at approximately 4:20 a.m."},
            {"date": "2016-04-18", "event": "Missy's body discovered by a class participant at approximately 5:00 a.m."},
            {"date": "2016-04-18", "event": "Surveillance footage released to the public."}
        ],
        "enriched": True
    },
    {
        "id": "elisa-lam-2013",
        "name": "Elisa Lam",
        "type": "Suspicious Death",
        "status": "Solved",
        "year": 2013,
        "date": "January 31, 2013",
        "state": "California",
        "city": "Los Angeles",
        "age": 21,
        "gender": "Female",
        "summary": "Canadian tourist Elisa Lam was found dead in a water tank atop the Cecil Hotel in Los Angeles. Bizarre elevator surveillance footage went viral. Her death was ruled accidental drowning related to bipolar disorder.",
        "lastSeen": "January 31, 2013, Cecil Hotel, Los Angeles, California",
        "tags": ["suspicious death", "California", "Los Angeles", "2010s", "hotel", "solved"],
        "sources": [
            {"title": "Death of Elisa Lam - Wikipedia", "url": "https://en.wikipedia.org/wiki/Death_of_Elisa_Lam"},
            {"title": "Elisa Lam case - Los Angeles Times", "url": "https://www.latimes.com/local/lanow/la-me-ln-elisa-lam-coroner-20140121-story.html"},
            {"title": "Cecil Hotel history - CNN", "url": "https://www.cnn.com/2021/02/10/entertainment/crime-scene-cecil-hotel-netflix/index.html"}
        ],
        "narrative": [
            "On January 31, 2013, twenty-one-year-old Elisa Lam, a Canadian student from Vancouver, British Columbia, was traveling alone on a trip along the West Coast of the United States. She checked into the Cecil Hotel in downtown Los Angeles, a hotel with a notorious history of deaths and criminal activity. She was last seen by hotel staff on January 31 and failed to check out on February 1.",
            "On February 6, the LAPD released elevator surveillance footage showing Elisa behaving erratically inside the Cecil Hotel elevator. The footage showed her pressing multiple floor buttons, peering out of the elevator as if checking for someone, making unusual hand gestures, and stepping in and out of the elevator. The footage went viral on the internet, generating millions of views and countless theories.",
            "On February 19, maintenance workers investigating complaints about low water pressure and discolored water discovered Elisa's body in one of four water tanks on the hotel's roof. The tanks were accessible via a locked rooftop door, a fire escape, and a ladder. The question of how Elisa accessed the tanks and entered one became a central mystery.",
            "After investigation, the Los Angeles County Coroner ruled Elisa's death an accidental drowning with bipolar disorder as a significant contributing factor. Toxicology reports indicated she had not been taking her prescribed psychiatric medications as directed. While the case generated enormous public interest and speculation about foul play, the evidence supported the conclusion that Elisa, experiencing a mental health crisis, had accessed the roof and entered the water tank on her own."
        ],
        "timeline": [
            {"date": "2013-01-26", "event": "Elisa Lam checks into the Cecil Hotel in Los Angeles."},
            {"date": "2013-01-31", "event": "Elisa last seen; elevator footage later shows erratic behavior."},
            {"date": "2013-02-06", "event": "LAPD releases elevator surveillance footage to the public."},
            {"date": "2013-02-19", "event": "Elisa's body discovered in a rooftop water tank."}
        ],
        "enriched": True
    },
    {
        "id": "faith-hedgepeth-2012",
        "name": "Faith Hedgepeth",
        "type": "Homicide",
        "status": "Solved",
        "year": 2012,
        "date": "September 7, 2012",
        "state": "North Carolina",
        "city": "Chapel Hill",
        "age": 19,
        "gender": "Female",
        "summary": "University of North Carolina student Faith Hedgepeth was murdered in her off-campus apartment. In 2021, Miguel Enrique Salguero-Olivares was arrested using genetic genealogy.",
        "lastSeen": "September 7, 2012, her apartment near UNC campus, Chapel Hill",
        "tags": ["homicide", "North Carolina", "2010s", "college", "DNA", "solved"],
        "sources": [
            {"title": "Murder of Faith Hedgepeth - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Faith_Hedgepeth"},
            {"title": "Faith Hedgepeth case solved - WRAL", "url": "https://www.wral.com/story/faith-hedgepeth-suspect-arrested-9-years-after-murder/19888346/"},
            {"title": "Genetic genealogy in Hedgepeth case - News & Observer", "url": "https://www.newsobserver.com/news/local/crime/article254439228.html"}
        ],
        "narrative": [
            "On the morning of September 7, 2012, nineteen-year-old Faith Danielle Hedgepeth, a junior at the University of North Carolina at Chapel Hill, was found dead in her off-campus apartment on Old Durham Chapel Hill Road. Her roommate, Karena Rosario, discovered her body and called 911. Faith had been sexually assaulted and bludgeoned to death.",
            "Faith, a member of the Haliwa-Saponi tribe, was a beloved student known for her infectious personality. She and Karena had been out the night before at a bar called The Thrill, returning to their apartment in the early hours. Investigators found a cryptic handwritten note near Faith's body that read, in part, 'I'm not stupid,' the full meaning of which was never publicly explained.",
            "The case went cold for years despite DNA evidence recovered from the crime scene. In 2021, a breakthrough came when investigators used genetic genealogy—a technique that matches crime scene DNA to public genealogy databases—to identify a suspect. Miguel Enrique Salguero-Olivares, who had lived near Faith's apartment complex at the time of the murder, was arrested and charged with first-degree murder and first-degree rape.",
            "Salguero-Olivares, who had no prior connection to Faith, was convicted in 2023 and sentenced to life in prison. The case was one of several high-profile cold cases solved using genetic genealogy technology, which has revolutionized cold case investigations since its first prominent use in the Golden State Killer case in 2018."
        ],
        "timeline": [
            {"date": "2012-09-07", "event": "Faith Hedgepeth found murdered in her off-campus apartment."},
            {"date": "2012-09-06", "event": "Faith and her roommate visit The Thrill bar before returning home."},
            {"date": "2021-09-16", "event": "Miguel Enrique Salguero-Olivares arrested using genetic genealogy."},
            {"date": "2023-01-01", "event": "Salguero-Olivares convicted; sentenced to life in prison."}
        ],
        "enriched": True
    },
    {
        "id": "sneha-philip-2001",
        "name": "Sneha Anne Philip",
        "type": "Missing Person",
        "status": "Unsolved",
        "year": 2001,
        "date": "September 10, 2001",
        "state": "New York",
        "city": "New York City",
        "age": 31,
        "gender": "Female",
        "summary": "Dr. Sneha Anne Philip, a physician, vanished the day before the September 11 attacks. Whether her death was related to 9/11 or occurred independently remains unknown.",
        "lastSeen": "September 10, 2001, Lower Manhattan, New York City",
        "tags": ["missing person", "New York", "2000s", "9/11", "unsolved"],
        "sources": [
            {"title": "Disappearance of Sneha Anne Philip - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Sneha_Anne_Philip"},
            {"title": "Sneha Philip case - New York Magazine", "url": "https://nymag.com/nymetro/news/sept11/features/5699/"},
            {"title": "9/11 Memorial - Sneha Ann Philip", "url": "https://www.911memorial.org/connect/blog/remembering-sneha-ann-philip"}
        ],
        "narrative": [
            "Dr. Sneha Anne Philip, a 31-year-old internal medicine physician, was last seen on surveillance footage shopping at a Century 21 department store near the World Trade Center on the evening of September 10, 2001. She never returned to her apartment at 30 Rector Place, just blocks from the Twin Towers. The following morning, the September 11 terrorist attacks occurred.",
            "Sneha's husband, Ron Lieberman, reported her missing on September 12, initially believing she may have been killed while rushing to help victims at the World Trade Center, as she was a trained physician. However, the investigation revealed a more complex picture. Sneha had been facing professional and personal difficulties, including a suspension from her medical residency and a secret social life her husband was unaware of.",
            "A legal battle ensued over whether Sneha should be counted among the victims of the September 11 attacks. Her family argued she had likely gone to help victims and died in the collapse. Her husband supported this theory. However, investigators noted she had disappeared before the attacks, raising the possibility that her death was unrelated to 9/11.",
            "In 2004, a court initially ruled that Sneha had likely died before the attacks, but this was reversed on appeal in 2008, with a court finding it more likely than not that she had died in the World Trade Center. Her name is inscribed on the National September 11 Memorial. The circumstances of her disappearance and death remain unresolved."
        ],
        "timeline": [
            {"date": "2001-09-10", "event": "Sneha Anne Philip last seen shopping near the World Trade Center."},
            {"date": "2001-09-11", "event": "September 11 attacks destroy the World Trade Center."},
            {"date": "2004-01-01", "event": "Court rules Sneha likely died before the attacks."},
            {"date": "2008-01-01", "event": "Appeals court reverses, ruling she likely died on 9/11."}
        ],
        "enriched": True
    }
]

# Filter out any duplicates
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
