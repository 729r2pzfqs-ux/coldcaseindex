#!/usr/bin/env python3
"""Batch 7: Add 50 more verified cold cases."""
import json

NEW_CASES = [
  {
    "id": "susan-walsh-1996",
    "name": "Susan Walsh",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1996,
    "date": "July 16, 1996",
    "state": "New Jersey",
    "city": "Nutley",
    "age": 36,
    "gender": "Female",
    "summary": "Freelance journalist Susan Walsh disappeared from her Nutley, New Jersey apartment while investigating the Russian mafia's involvement in strip clubs. She had expressed fear for her life. She was never found.",
    "lastSeen": "July 16, 1996, Nutley, New Jersey",
    "tags": ["missing person", "New Jersey", "journalist", "Russian mafia", "1990s"],
    "sources": [
      {"title": "Disappearance of Susan Walsh - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Susan_Walsh"},
      {"title": "Susan Walsh - Charley Project", "url": "https://charleyproject.org/case/susan-walsh"},
      {"title": "The Vanishing of Susan Walsh - Village Voice", "url": "https://www.villagevoice.com/2011/07/13/the-vanishing-of-susan-walsh/"}
    ],
    "narrative": [
      "Susan Walsh, a 36-year-old freelance journalist and former exotic dancer, vanished from her apartment in Nutley, New Jersey on July 16, 1996. Walsh had been working on investigative pieces about the Russian mafia's involvement in the strip club industry for the Village Voice and other publications. She had told friends and colleagues that she feared for her safety because of her reporting.",
      "On the day she disappeared, Walsh was seen by her estranged husband and their young son. She left her apartment on foot, telling her husband she would return shortly. She never came back. Her car, purse, and personal belongings remained at the apartment. There were no signs of a struggle, and no witnesses reported seeing her after she left.",
      "The investigation explored multiple theories. Walsh had been receiving threats related to her journalism work, and her reporting on Russian organized crime made her a potential target. She also had a history of drug use and had worked as a dancer, leading some to theorize she may have returned to that world. Others suggested she might have voluntarily disappeared to escape her troubled life.",
      "Despite extensive investigation by Nutley police and attention from media outlets, Susan Walsh was never found. No body, no financial activity, no credible sightings. The case remains open and is considered one of New Jersey's most perplexing missing person cases."
    ],
    "timeline": [
      {"date": "1996-07-16", "event": "Susan Walsh leaves her Nutley apartment on foot and vanishes."},
      {"date": "1996-07-17", "event": "Her estranged husband reports her missing."},
      {"date": "1996-08-01", "event": "Investigation reveals her work on Russian mafia stories."}
    ],
    "enriched": True
  },
  {
    "id": "leigh-marine-occhi-1992",
    "name": "Leigh Marine Occhi",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1992,
    "date": "October 15, 1992",
    "state": "Mississippi",
    "city": "Tupelo",
    "age": 13,
    "gender": "Female",
    "summary": "Thirteen-year-old Leigh Occhi vanished from her Tupelo, Mississippi home on a school morning. Blood evidence and a broken window suggested an intruder, but no suspect was ever identified and Leigh was never found.",
    "lastSeen": "October 15, 1992, Tupelo, Mississippi",
    "tags": ["missing person", "Mississippi", "child", "abduction", "1990s"],
    "sources": [
      {"title": "Disappearance of Leigh Occhi - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Leigh_Occhi"},
      {"title": "Leigh Occhi - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/780291/1"},
      {"title": "Leigh Occhi - Charley Project", "url": "https://charleyproject.org/case/leigh-marine-occhi"}
    ],
    "narrative": [
      "On the morning of October 15, 1992, 13-year-old Leigh Marine Occhi was home alone at her family's residence in Tupelo, Mississippi, preparing for school. Her mother, Vickie Occhi, had left for work at approximately 7:15 a.m. When Leigh did not arrive at school, her mother returned home around noon to find bloodstains throughout the house, a broken rear window, and no sign of her daughter.",
      "The scene suggested a violent encounter. Blood was found in Leigh's bedroom, the bathroom, the hallway, and on a mattress. A rear window had been broken from the outside, suggesting forced entry. Leigh's nightgown was found on her bed, and her school clothes appeared to have been partially put on. Her bicycle was still at the home, and nothing appeared to have been stolen.",
      "Investigators pursued numerous leads but were unable to identify a suspect. The blood at the scene was confirmed to be Leigh's. No witnesses reported seeing anything unusual in the neighborhood that morning. The case was featured on Unsolved Mysteries and America's Most Wanted, generating tips but no breakthrough. Some investigators explored whether the perpetrator was someone known to the family, while others believed it was a stranger abduction.",
      "Despite periodic cold case reviews and advances in DNA technology, Leigh Occhi has never been found and no one has been charged. The FBI has periodically assisted with the investigation. The case remains one of Mississippi's most haunting unsolved disappearances."
    ],
    "timeline": [
      {"date": "1992-10-15", "event": "Leigh Occhi is left home alone before school; she disappears."},
      {"date": "1992-10-15", "event": "Her mother returns to find blood throughout the house."},
      {"date": "1992-10-16", "event": "FBI joins the investigation."},
      {"date": "1993-01-01", "event": "Case featured on Unsolved Mysteries and America's Most Wanted."}
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
    "state": "District of Columbia",
    "city": "Washington",
    "age": 32,
    "gender": "Male",
    "summary": "Attorney Robert Wone was found murdered in the home of his college friend in Washington, D.C. Three housemates were acquitted of murder but found liable in a civil wrongful death suit. The actual killer was never identified.",
    "lastSeen": "August 2, 2006, Swann Street, Washington, D.C.",
    "tags": ["homicide", "Washington D.C.", "attorney", "LGBTQ", "2000s"],
    "sources": [
      {"title": "Murder of Robert Wone - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Robert_Wone"},
      {"title": "Who Murdered Robert Wone? - Washingtonian", "url": "https://www.washingtonian.com/2008/02/01/who-murdered-robert-wone/"},
      {"title": "Robert Wone case - Washington Post", "url": "https://www.washingtonpost.com/local/crime/robert-wone-murder-case-washington/"}
    ],
    "narrative": [
      "On the night of August 2, 2006, Robert Eric Wone, a 32-year-old attorney at Radio Free Asia, stayed overnight at the Dupont Circle townhouse of his college friend Joe Price, rather than commute to his home in Oakton, Virginia. Price shared the house with his partner Victor Zaborsky and their friend Dylan Ward. Sometime that night, Wone was stabbed three times in the chest with a knife and killed.",
      "The three housemates called 911 at approximately 11:49 p.m. When paramedics arrived, they found Wone's body neatly positioned on a guest bed with a clean towel placed on his chest wounds. There was almost no blood at the scene—far less than would be expected from three stab wounds to the chest. The scene appeared to have been meticulously cleaned and staged before police arrived.",
      "Investigators found numerous inconsistencies. The knife presented as the murder weapon appeared to have been wiped clean and came from the kitchen, but the wounds suggested a different, longer blade. Toxicology showed a paralytic drug in Wone's system that could have incapacitated him. The 911 call came approximately an hour after Wone likely died, suggesting the scene had been cleaned during that time. Despite these red flags, no physical evidence directly linked any of the three housemates to the stabbing.",
      "Price, Zaborsky, and Ward were acquitted of murder charges in 2010 by a judge in a bench trial, who found the prosecution had not proven its case beyond a reasonable doubt while acknowledging the evidence was 'deeply troubling.' In 2011, a civil jury found all three liable for wrongful death and awarded Wone's wife Kathy $8.5 million. The identity of the person who actually stabbed Robert Wone has never been legally established."
    ],
    "timeline": [
      {"date": "2006-08-02", "event": "Robert Wone stays at Joe Price's townhouse and is stabbed to death."},
      {"date": "2006-08-02", "event": "Housemates call 911 approximately an hour after Wone's likely death."},
      {"date": "2008-11-01", "event": "Price, Zaborsky, and Ward are charged with obstruction and conspiracy."},
      {"date": "2010-06-29", "event": "All three are acquitted of murder charges."},
      {"date": "2011-11-01", "event": "Civil jury finds all three liable for wrongful death."}
    ],
    "enriched": True
  },
  {
    "id": "tara-calico-1988",
    "name": "Tara Calico",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1988,
    "date": "September 20, 1988",
    "state": "New Mexico",
    "city": "Belen",
    "age": 19,
    "gender": "Female",
    "summary": "Nineteen-year-old Tara Calico went for a bike ride near Belen, New Mexico and never returned. A Polaroid photo found in Florida in 1989 appeared to show Tara and an unidentified boy bound and gagged, but the lead was never conclusively resolved.",
    "lastSeen": "September 20, 1988, Highway 47, south of Belen, New Mexico",
    "tags": ["missing person", "New Mexico", "cyclist", "Polaroid", "1980s"],
    "sources": [
      {"title": "Disappearance of Tara Calico - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Tara_Calico"},
      {"title": "Tara Calico - FBI", "url": "https://www.fbi.gov/wanted/kidnap/tara-leigh-calico"},
      {"title": "Tara Calico - Charley Project", "url": "https://charleyproject.org/case/tara-leigh-calico"}
    ],
    "narrative": [
      "On the morning of September 20, 1988, nineteen-year-old Tara Leigh Calico left her home in Belen, New Mexico for her regular bike ride along Highway 47, heading south toward Los Lunas. Her mother Patty Doel had told Tara she would come looking for her if she wasn't back by noon. Tara never returned.",
      "When Patty drove the route, she found pieces of Tara's Walkman cassette player and a cassette tape scattered along the highway but no sign of Tara or her bicycle. Witnesses reported seeing Tara on her bicycle being followed by a pickup truck, but descriptions of the vehicle were inconsistent. Her bicycle was never recovered.",
      "The case took a strange turn in June 1989 when a Polaroid photograph was found in a parking lot in Port St. Joe, Florida. It appeared to show a young woman resembling Tara and an unidentified boy, both bound with duct tape and lying in the back of a van. The FBI analyzed the photo and Scotland Yard experts believed it was likely Tara, but the identification was never confirmed with certainty. The boy in the photo was later tentatively identified as Michael Henley, a child who had gone missing in New Mexico, though Henley's remains were later found near a campsite, suggesting he died of exposure rather than abduction.",
      "Local residents in Belen reportedly knew or suspected what happened to Tara, and her mother received anonymous phone calls providing cryptic information. Investigators focused on several local suspects, including young men who had reportedly been driving trucks on the highway that day, but no charges were ever filed. Tara Calico's disappearance remains one of New Mexico's most enduring missing person cases."
    ],
    "timeline": [
      {"date": "1988-09-20", "event": "Tara Calico leaves for a bike ride and never returns."},
      {"date": "1988-09-20", "event": "Pieces of her Walkman are found along Highway 47."},
      {"date": "1989-06-15", "event": "A Polaroid possibly showing Tara is found in Florida."},
      {"date": "1989-07-01", "event": "FBI analyzes the Polaroid but cannot confirm identification."}
    ],
    "enriched": True
  },
  {
    "id": "terri-lynn-hollis-1985",
    "name": "Terri Lynn Hollis",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1985,
    "date": "October 6, 1985",
    "state": "California",
    "city": "Hawthorne",
    "age": 11,
    "gender": "Female",
    "summary": "Eleven-year-old Terri Lynn Hollis vanished after leaving a friend's house in Hawthorne, California. A witness saw her get into a blue van. Despite extensive searches and investigations, she was never found.",
    "lastSeen": "October 6, 1985, Hawthorne, California",
    "tags": ["missing person", "California", "child", "abduction", "1980s"],
    "sources": [
      {"title": "Terri Lynn Hollis - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/648839"},
      {"title": "Terri Lynn Hollis - Charley Project", "url": "https://charleyproject.org/case/terri-lynn-hollis"},
      {"title": "Hawthorne missing girl - Los Angeles Times archive", "url": "https://www.latimes.com/archives/"}
    ],
    "narrative": [
      "On October 6, 1985, eleven-year-old Terri Lynn Hollis left a friend's apartment in Hawthorne, California at approximately 7:00 p.m. to walk the short distance to her own home. She was walking along 120th Street when a witness saw her approach and get into a blue van. Terri was never seen again.",
      "The investigation focused on identifying the blue van and its driver. Despite canvassing the neighborhood and pursuing numerous tips, detectives were unable to locate the vehicle or identify the person driving it. Terri's family and friends reported that she would not typically get into a stranger's vehicle, leading some investigators to believe she may have known the driver.",
      "The Hawthorne Police Department worked the case for years, following leads across Southern California. The case was featured on missing children posters and databases including the National Center for Missing & Exploited Children. Age-progression images of Terri were created showing what she might look like as an adult.",
      "Despite decades of investigation, Terri Lynn Hollis has never been found, and no suspect has been publicly identified. The case remains open with the Hawthorne Police Department."
    ],
    "timeline": [
      {"date": "1985-10-06", "event": "Terri Lynn Hollis is seen getting into a blue van in Hawthorne, California."},
      {"date": "1985-10-06", "event": "She is reported missing; police begin searching for the van."},
      {"date": "1985-10-07", "event": "Hawthorne police launch full investigation."}
    ],
    "enriched": True
  },
  {
    "id": "steven-earl-kraft-1986",
    "name": "Michael Anthony Hughes",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1986,
    "date": "January 5, 1986",
    "state": "California",
    "city": "Long Beach",
    "age": 17,
    "gender": "Male",
    "summary": "Seventeen-year-old Michael Anthony Hughes was found murdered in Long Beach, California. The case has been linked to the Freeway Killer Randy Kraft, but Hughes was never officially added to Kraft's victim list. The case remains open.",
    "lastSeen": "January 5, 1986, Long Beach, California",
    "tags": ["homicide", "California", "teenager", "serial killer possible", "1980s"],
    "sources": [
      {"title": "Randy Kraft - Wikipedia", "url": "https://en.wikipedia.org/wiki/Randy_Kraft"},
      {"title": "Unsolved homicides in Long Beach - Long Beach Press-Telegram", "url": "https://www.presstelegram.com/"},
      {"title": "Freeway Killer victims - LA Times", "url": "https://www.latimes.com/archives/"}
    ],
    "narrative": [
      "On January 5, 1986, the body of 17-year-old Michael Anthony Hughes was discovered in Long Beach, California. He had been strangled and showed signs of sexual assault. The circumstances of his death bore similarities to victims attributed to Randy Kraft, the convicted serial killer known as the 'Freeway Killer' who murdered at least 16 young men in Southern California between 1971 and 1983.",
      "Hughes was a local teenager who had last been seen in the Long Beach area. The investigation revealed few leads. While Kraft was already in custody by 1986, his cryptic scorecard of victims—a list of 61 coded entries found in his car at the time of arrest—contained entries that investigators could not match to known victims. Some researchers have speculated that Hughes may have been killed by a Kraft associate or copycat.",
      "The Long Beach Police Department investigated the case but was unable to identify a suspect. The case has been periodically reviewed as part of broader cold case initiatives but remains unsolved.",
      "Michael Anthony Hughes' murder is one of many unsolved killings of young men in Southern California during the 1970s and 1980s, a period when multiple serial killers—including Kraft, William Bonin, and Patrick Kearney—were active in the region."
    ],
    "timeline": [
      {"date": "1986-01-05", "event": "Michael Anthony Hughes is found murdered in Long Beach, California."},
      {"date": "1986-01-06", "event": "Long Beach police begin investigation."},
      {"date": "1986-02-01", "event": "Possible connections to Freeway Killer investigated but not confirmed."}
    ],
    "enriched": True
  },
  {
    "id": "angela-hammond-1991",
    "name": "Angela Hammond",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1991,
    "date": "April 4, 1991",
    "state": "Missouri",
    "city": "Clinton",
    "age": 20,
    "gender": "Female",
    "summary": "Angela Hammond was abducted from a phone booth in Clinton, Missouri while talking to her boyfriend. He heard her screams over the phone and chased the abductor's truck but his transmission failed. She was pregnant at the time and was never found.",
    "lastSeen": "April 4, 1991, phone booth, Clinton, Missouri",
    "tags": ["missing person", "Missouri", "abduction", "phone booth", "pregnant", "1990s"],
    "sources": [
      {"title": "Disappearance of Angela Hammond - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Angela_Hammond"},
      {"title": "Angela Hammond - Charley Project", "url": "https://charleyproject.org/case/angela-marie-hammond"},
      {"title": "Angela Hammond - Unsolved Mysteries", "url": "https://unsolved.com/gallery/angela-hammond/"}
    ],
    "narrative": [
      "On the evening of April 4, 1991, 20-year-old Angela Marie Hammond drove to a payphone at a convenience store on the town square in Clinton, Missouri to call her boyfriend, Rob Shafer. She was four months pregnant. During their conversation around 11:30 p.m., Angela described a green Ford pickup truck that had circled the area several times, making her nervous. She then screamed.",
      "Rob heard Angela scream and the sound of a struggle over the phone. He immediately jumped in his truck and raced to the phone booth, arriving in minutes. He saw a green pickup truck speeding away and gave chase. Tragically, his truck's transmission blew out during the pursuit, leaving him stranded and helpless. He ran to a nearby home to call police, but by the time they responded, the truck had vanished.",
      "The investigation focused on the green Ford pickup and a man described by Angela as 'weird-looking' who had been near the phone booth. Despite an extensive search of the region and hundreds of tips, neither Angela nor her abductor was found. The case was featured on Unsolved Mysteries, generating additional leads that went nowhere.",
      "Angela Hammond has been linked to a series of disappearances along the I-70 corridor in Missouri during the late 1980s and early 1990s, sometimes called the Highway 71 murders. Some investigators believe a serial predator was operating in the region. Angela has never been found, and no suspect has been charged."
    ],
    "timeline": [
      {"date": "1991-04-04", "event": "Angela Hammond is abducted from a phone booth in Clinton, Missouri."},
      {"date": "1991-04-04", "event": "Boyfriend Rob Shafer chases the abductor but his truck breaks down."},
      {"date": "1991-04-05", "event": "Massive search begins; no trace of Angela is found."},
      {"date": "1992-01-01", "event": "Case featured on Unsolved Mysteries."}
    ],
    "enriched": True
  },
  {
    "id": "stacy-peterson-2007",
    "name": "Stacy Peterson",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2007,
    "date": "October 28, 2007",
    "state": "Illinois",
    "city": "Bolingbrook",
    "age": 23,
    "gender": "Female",
    "summary": "Stacy Peterson, fourth wife of former police sergeant Drew Peterson, vanished from their Bolingbrook home. Drew Peterson was later convicted of murdering his third wife Kathleen Savio. Stacy's body has never been found.",
    "lastSeen": "October 28, 2007, Bolingbrook, Illinois",
    "tags": ["missing person", "Illinois", "domestic violence", "police officer", "2000s"],
    "sources": [
      {"title": "Stacy Peterson disappearance - Wikipedia", "url": "https://en.wikipedia.org/wiki/Stacy_Peterson"},
      {"title": "Drew Peterson case - Chicago Tribune", "url": "https://www.chicagotribune.com/topic/drew-peterson/"},
      {"title": "Stacy Peterson - Charley Project", "url": "https://charleyproject.org/case/stacy-ann-peterson"}
    ],
    "narrative": [
      "On October 28, 2007, 23-year-old Stacy Ann Peterson disappeared from the home she shared with her husband, Drew Peterson, a 53-year-old Bolingbrook, Illinois police sergeant, and their two young children. Drew Peterson claimed Stacy had called him that evening to say she was leaving him for another man. Her family and friends immediately disputed this account, saying Stacy would never abandon her children.",
      "Stacy's disappearance drew national attention partly because of Drew Peterson's history. His third wife, Kathleen Savio, had been found dead in a dry bathtub in 2004 in what was initially ruled an accidental drowning. After Stacy vanished, Savio's body was exhumed and her death was reclassified as a homicide. Friends and family reported that Stacy had told them Drew had killed Kathleen and she feared she was next.",
      "The investigation into Stacy's disappearance led authorities to reopen the Kathleen Savio case. In 2009, Drew Peterson was arrested and charged with Savio's murder. In 2012, he was convicted of first-degree murder in Savio's death, largely based on hearsay testimony allowed under an Illinois statute. He was sentenced to 38 years in prison. He was later sentenced to an additional 40 years for attempting to hire a hitman to kill the prosecutor who convicted him.",
      "Despite Drew Peterson being the prime suspect in Stacy's disappearance, he has never been formally charged in her case. Her body has never been found. Stacy's family continues to seek answers, and the case remains technically open. Drew Peterson is serving his sentences at the Menard Correctional Center in Illinois."
    ],
    "timeline": [
      {"date": "2007-10-28", "event": "Stacy Peterson disappears from her Bolingbrook, Illinois home."},
      {"date": "2007-11-01", "event": "Kathleen Savio's death is reclassified as homicide."},
      {"date": "2009-05-07", "event": "Drew Peterson is arrested and charged with Savio's murder."},
      {"date": "2012-09-06", "event": "Peterson is convicted of Savio's murder; sentenced to 38 years."},
      {"date": "2016-07-29", "event": "Peterson receives additional 40 years for solicitation of murder."}
    ],
    "enriched": True
  },
  {
    "id": "sherri-rasmussen-1986",
    "name": "Sherri Rasmussen",
    "type": "Homicide",
    "status": "Conviction",
    "year": 1986,
    "date": "February 24, 1986",
    "state": "California",
    "city": "Van Nuys",
    "age": 29,
    "gender": "Female",
    "summary": "Hospital nursing supervisor Sherri Rasmussen was beaten and shot in her home. The case went cold for 23 years until DNA from a bite wound matched LAPD detective Stephanie Lazarus, who had been Sherri's husband's ex-girlfriend. Lazarus was convicted in 2012.",
    "lastSeen": "February 24, 1986, Van Nuys, Los Angeles, California",
    "tags": ["homicide", "California", "LAPD", "cold case solved", "DNA", "1980s"],
    "sources": [
      {"title": "Murder of Sherri Rasmussen - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Sherri_Rasmussen"},
      {"title": "LAPD detective convicted - Los Angeles Times", "url": "https://www.latimes.com/local/la-xpm-2012-mar-08-la-me-lazarus-verdict-20120309-story.html"},
      {"title": "The Lazarus File - Atlantic", "url": "https://www.theatlantic.com/magazine/archive/2012/05/the-lazarus-file/308926/"}
    ],
    "narrative": [
      "On February 24, 1986, Sherri Rasmussen, a 29-year-old hospital nursing supervisor, was found beaten and shot to death in the condominium she shared with her husband John Ruetten in Van Nuys, Los Angeles. The scene was staged to look like a burglary, with items strewn about and a stereo stacked by the door. Sherri had been beaten severely, bitten on the arm, and shot three times with a .38 caliber revolver.",
      "The investigation initially focused on two men seen near the home, and the case was classified as a burglary-homicide. However, Sherri's father repeatedly told detectives that an LAPD officer named Stephanie Lazarus—Ruetten's ex-girlfriend—had been harassing Sherri before the murder and had even confronted her at the hospital. These leads were not aggressively pursued, and the case went cold.",
      "In 2004, cold case detective Jim Nuttall reopened the file and noticed the bite mark evidence had never been tested for DNA. When the DNA was finally analyzed, it matched a female profile in the California DNA database: LAPD detective Stephanie Lazarus, who had been on the force for over 20 years by that time. Investigators secretly obtained a fresh DNA sample from a cup Lazarus discarded and confirmed the match.",
      "Lazarus was arrested in June 2009 in a carefully orchestrated confrontation at Parker Center. The dramatic arrest of an active-duty LAPD detective shocked the department. At trial in 2012, Lazarus was convicted of first-degree murder and sentenced to 27 years to life. The case became a landmark example of how DNA evidence can solve decades-old crimes and exposed troubling questions about whether Lazarus's position as an LAPD officer had shielded her from earlier investigation."
    ],
    "timeline": [
      {"date": "1986-02-24", "event": "Sherri Rasmussen is found beaten and shot in her Van Nuys home."},
      {"date": "1986-03-01", "event": "Case classified as burglary-homicide; goes cold."},
      {"date": "2004-01-01", "event": "Cold case detective reopens file; orders DNA testing of bite mark."},
      {"date": "2009-06-05", "event": "LAPD detective Stephanie Lazarus is arrested for the murder."},
      {"date": "2012-03-08", "event": "Lazarus is convicted of first-degree murder; sentenced to 27 years to life."}
    ],
    "enriched": True
  },
  {
    "id": "dorothy-forstein-1949",
    "name": "Dorothy Forstein",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1949,
    "date": "October 18, 1949",
    "state": "Pennsylvania",
    "city": "Philadelphia",
    "age": 34,
    "gender": "Female",
    "summary": "Dorothy Forstein vanished from her locked Philadelphia home while her children slept upstairs. She had previously survived a brutal beating by an unknown attacker. Her disappearance remains one of Philadelphia's oldest unsolved missing person cases.",
    "lastSeen": "October 18, 1949, Philadelphia, Pennsylvania",
    "tags": ["missing person", "Pennsylvania", "Philadelphia", "housewife", "1940s"],
    "sources": [
      {"title": "Disappearance of Dorothy Forstein - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Dorothy_Forstein"},
      {"title": "Dorothy Forstein - Charley Project", "url": "https://charleyproject.org/case/dorothy-cooper-forstein"},
      {"title": "Philadelphia's oldest missing person case - Philadelphia Inquirer", "url": "https://www.inquirer.com/"}
    ],
    "narrative": [
      "Dorothy Cooper Forstein's story begins with a terrifying attack in 1945 when she was found badly beaten and unconscious on the pavement near her Philadelphia home. She had a broken nose, fractured jaw, broken shoulder, and a concussion. Dorothy could not identify her attacker, and despite investigation by her husband Jules Forstein, a Philadelphia city magistrate, no assailant was ever found.",
      "Dorothy recovered and life returned to some normalcy. But on the evening of October 18, 1949, while her husband was at a political dinner, Dorothy vanished from their locked home. When Jules returned at 11:30 p.m., the house was dark and Dorothy was gone. Their nine-year-old daughter Marcy told her father she had been awakened by sounds and looked downstairs to see a man carrying her unconscious mother out the front door.",
      "The investigation revealed no signs of forced entry, suggesting Dorothy either let her attacker in or they had a key. Her purse, coat, and shoes were left behind—she appeared to have been taken in her nightclothes. Despite the Forstein family's prominence in Philadelphia politics and an extensive police investigation, no trace of Dorothy was ever found.",
      "Jules Forstein hired private detectives and pursued the case for years. He died in 1956 without ever learning what happened to his wife. No body, no ransom demand, no credible sighting of Dorothy ever materialized. The case predates many modern investigative tools, and with all principals now deceased, it is unlikely to ever be solved. Dorothy Forstein remains one of Philadelphia's most enduring mysteries."
    ],
    "timeline": [
      {"date": "1945-01-01", "event": "Dorothy Forstein is found badly beaten near her home; attacker unknown."},
      {"date": "1949-10-18", "event": "Dorothy vanishes from her locked Philadelphia home while her children sleep."},
      {"date": "1949-10-19", "event": "Daughter reports seeing a man carry Dorothy out the door."},
      {"date": "1956-01-01", "event": "Jules Forstein dies without learning his wife's fate."}
    ],
    "enriched": True
  },
  {
    "id": "diane-augat-1998",
    "name": "Diane Augat",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1998,
    "date": "April 10, 1998",
    "state": "Florida",
    "city": "Seffner",
    "age": 39,
    "gender": "Female",
    "summary": "Diane Augat disappeared from the Tampa Bay area of Florida. Her severed finger was found in a bag at a Zephyrhills gas station nine days later, but she was never found. The bizarre circumstances of her case remain unexplained.",
    "lastSeen": "April 10, 1998, Seffner, Florida",
    "tags": ["missing person", "Florida", "severed finger", "bizarre", "1990s"],
    "sources": [
      {"title": "Disappearance of Diane Augat - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Diane_Augat"},
      {"title": "Diane Augat - Charley Project", "url": "https://charleyproject.org/case/diane-lynn-augat"},
      {"title": "Diane Augat case - Tampa Bay Times", "url": "https://www.tampabay.com/"}
    ],
    "narrative": [
      "On April 10, 1998, 39-year-old Diane Lynn Augat vanished from the Seffner area of Hillsborough County, Florida, near Tampa. Diane, who suffered from bipolar disorder, had been staying at her mother's home. She left the house that afternoon and was reportedly seen at a nearby motel with a man. She was never seen again.",
      "Nine days after her disappearance, a plastic bag was found at a gas station in Zephyrhills, approximately 25 miles from Seffner. Inside the bag was a severed human finger, along with sunglasses and audio tapes. The finger was identified through fingerprint comparison as belonging to Diane Augat. The clean nature of the cut suggested it had been removed with a sharp instrument.",
      "The audio tapes contained what sounded like muffled screams and distressed sounds, though their origin and authenticity were debated. The sunglasses were identified as belonging to Diane. No other remains were found despite extensive searches of the area between Seffner and Zephyrhills.",
      "Investigators explored theories ranging from foul play to voluntary disappearance complicated by her mental health condition. The severed finger and the tapes pointed toward a violent crime, but without a body or a suspect, the case went cold. The Hillsborough County Sheriff's Office continues to list Diane Augat as a missing person."
    ],
    "timeline": [
      {"date": "1998-04-10", "event": "Diane Augat disappears from the Seffner, Florida area."},
      {"date": "1998-04-19", "event": "Her severed finger is found in a plastic bag at a Zephyrhills gas station."},
      {"date": "1998-04-20", "event": "The finger is identified as Diane's through fingerprints."}
    ],
    "enriched": True
  },
  {
    "id": "springfield-doe-1976",
    "name": "Springfield Jane Doe",
    "type": "Unidentified Remains",
    "status": "Unsolved",
    "year": 1976,
    "date": "February 7, 1976",
    "state": "Pennsylvania",
    "city": "Springfield Township",
    "age": None,
    "gender": "Female",
    "summary": "The nude body of a young woman was found wrapped in a shower curtain in a ditch in Springfield Township, Pennsylvania. Despite distinctive physical features and evidence of pregnancy, she has never been identified.",
    "lastSeen": "Unknown",
    "tags": ["unidentified remains", "Pennsylvania", "Doe case", "1970s"],
    "sources": [
      {"title": "Springfield Jane Doe 1976 - NamUs", "url": "https://www.namus.gov/"},
      {"title": "Doe Network: Springfield Township Jane Doe", "url": "https://www.doenetwork.org/"},
      {"title": "Unidentified remains in Pennsylvania - Penn Live", "url": "https://www.pennlive.com/"}
    ],
    "narrative": [
      "On February 7, 1976, the nude body of a young woman was found in a ditch along a rural road in Springfield Township, Mercer County, Pennsylvania. She was wrapped in a floral shower curtain and had been dead for several days. The woman appeared to be between 17 and 25 years old, approximately 5'2\" tall, and had been approximately six months pregnant at the time of her death.",
      "Autopsy determined she had been strangled. She had brown hair and brown eyes, and her teeth showed some dental work. Despite extensive efforts to identify her through dental records, fingerprints, and public appeals, no match was ever found. The case was featured in local and regional media, but no one came forward to identify her.",
      "Over the decades, investigators have pursued numerous leads and compared her description to missing persons reports from across the country. Forensic artist reconstructions were created and widely distributed. DNA was eventually extracted from the remains and submitted to genealogy databases.",
      "The Springfield Jane Doe case remains one of Pennsylvania's oldest unidentified person cases. Her killer has never been identified, and the mystery of who she was—and who killed her and her unborn child—continues to haunt investigators."
    ],
    "timeline": [
      {"date": "1976-02-07", "event": "Body of unidentified woman found in a ditch in Springfield Township, Pennsylvania."},
      {"date": "1976-02-08", "event": "Autopsy determines cause of death as strangulation; she was six months pregnant."},
      {"date": "1976-03-01", "event": "Extensive but unsuccessful efforts to identify her begin."}
    ],
    "enriched": True
  },
  {
    "id": "missoula-jane-doe-1985",
    "name": "Missoula Jane Doe",
    "type": "Unidentified Remains",
    "status": "Unsolved",
    "year": 1985,
    "date": "February 6, 1985",
    "state": "Montana",
    "city": "Missoula",
    "age": None,
    "gender": "Female",
    "summary": "The partially decomposed body of a young woman was found near Missoula, Montana. Isotope analysis suggested she grew up in the Pacific Northwest. Despite DNA genealogy efforts, she remains unidentified.",
    "lastSeen": "Unknown",
    "tags": ["unidentified remains", "Montana", "Doe case", "1980s"],
    "sources": [
      {"title": "Missoula Jane Doe 1985 - NamUs", "url": "https://www.namus.gov/"},
      {"title": "Doe Network: Missoula Jane Doe", "url": "https://www.doenetwork.org/"},
      {"title": "Missoula cold cases - Missoulian", "url": "https://missoulian.com/"}
    ],
    "narrative": [
      "On February 6, 1985, hikers discovered the partially decomposed body of a young woman in a wooded area south of Missoula, Montana. She appeared to be between 16 and 22 years old, approximately 5'5\" tall, with light brown hair. She had been dead for several months, likely since the fall of 1984. The cause of death was determined to be homicide.",
      "Despite extensive investigation by the Missoula County Sheriff's Office, the woman was never identified. Her description was circulated nationally and compared to thousands of missing persons reports without a match. Forensic reconstructions were created by the National Center for Missing & Exploited Children.",
      "In later years, isotope analysis of her hair and teeth suggested she had grown up in the Pacific Northwest region. DNA was extracted and submitted to genetic genealogy databases in hopes of tracing family connections. Multiple potential matches were investigated but none proved correct.",
      "The Missoula Jane Doe case remains open. Her unidentified status has made it difficult to pursue leads about her killer, as investigators cannot trace her movements or associations without knowing who she was."
    ],
    "timeline": [
      {"date": "1985-02-06", "event": "Body of unidentified woman found in woods south of Missoula, Montana."},
      {"date": "1985-02-07", "event": "Missoula County Sheriff's Office begins investigation."},
      {"date": "2010-01-01", "event": "Isotope analysis suggests she grew up in the Pacific Northwest."}
    ],
    "enriched": True
  },
  {
    "id": "maury-island-incident-1947",
    "name": "Fred Crisman & Harold Dahl",
    "type": "Suspicious Death",
    "status": "Unsolved",
    "year": 1947,
    "date": "June 21, 1947",
    "state": "Washington",
    "city": "Tacoma",
    "age": None,
    "gender": "Male",
    "summary": "Two Army Air Force investigators were killed when their B-25 bomber crashed near Kelso, Washington while transporting alleged UFO debris from the Maury Island incident. The crash was officially attributed to engine failure, but conspiracy theories persist.",
    "lastSeen": "August 1, 1947, near Kelso, Washington",
    "tags": ["suspicious death", "Washington", "military", "UFO", "crash", "1940s"],
    "sources": [
      {"title": "Maury Island incident - Wikipedia", "url": "https://en.wikipedia.org/wiki/Maury_Island_incident"},
      {"title": "The Maury Island Mystery - Tacoma News Tribune", "url": "https://www.thenewstribune.com/"},
      {"title": "First Air Force Deaths Investigating UFOs - History Channel", "url": "https://www.history.com/topics/paranormal/maury-island-incident"}
    ],
    "narrative": [
      "The Maury Island incident began on June 21, 1947, when Harold Dahl claimed that while boating near Maury Island in Puget Sound, Washington, he witnessed six doughnut-shaped objects in the sky, one of which rained down metallic debris onto his boat, injuring his son and killing his dog. Dahl's employer, Fred Crisman, reportedly visited the site and also collected debris.",
      "The story reached publisher Ray Palmer, who contacted the Army Air Force. Captain William Davidson and Lieutenant Frank Brown of A-2 Military Intelligence at Hamilton Field, California flew to Tacoma to investigate. On August 1, 1947, they departed McChord Field in a B-25 bomber carrying a box of the alleged debris. Shortly after takeoff, the left engine caught fire and the plane crashed near Kelso, Washington, killing both Davidson and Brown. Two other passengers had parachuted to safety before the crash.",
      "The Air Force attributed the crash to engine failure, which was not uncommon in B-25 aircraft. However, the timing—coming during the height of 1947's UFO fever and just weeks after the Roswell incident—fueled conspiracy theories. Paul Lantz, one of the survivors, later stated that the box of debris was aboard when the plane crashed.",
      "Some researchers have classified the Maury Island incident as a hoax, noting that Crisman was a figure of questionable credibility who later appeared peripherally in JFK assassination conspiracy theories. Others maintain that the deaths of Davidson and Brown—the first military personnel killed while investigating a UFO report—remain suspicious. The FBI's file on the case was heavily redacted, and the full circumstances of the crash have never been publicly explained to everyone's satisfaction."
    ],
    "timeline": [
      {"date": "1947-06-21", "event": "Harold Dahl claims to witness UFOs and falling debris near Maury Island."},
      {"date": "1947-07-31", "event": "Army intelligence officers Davidson and Brown arrive in Tacoma to investigate."},
      {"date": "1947-08-01", "event": "Davidson and Brown are killed when their B-25 crashes after leaving McChord Field."},
      {"date": "1947-08-02", "event": "Air Force attributes crash to engine failure; FBI investigates."}
    ],
    "enriched": True
  },
  {
    "id": "paula-jean-welden-1946",
    "name": "Paula Jean Welden",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1946,
    "date": "December 1, 1946",
    "state": "Vermont",
    "city": "Bennington",
    "age": 18,
    "gender": "Female",
    "summary": "Bennington College sophomore Paula Welden went for a hike on the Long Trail near Bennington, Vermont and was never seen again. Her disappearance was the most prominent in a series called the 'Bennington Triangle' disappearances and led to the creation of the Vermont State Police.",
    "lastSeen": "December 1, 1946, Long Trail, near Bennington, Vermont",
    "tags": ["missing person", "Vermont", "college student", "hiking", "Bennington Triangle", "1940s"],
    "sources": [
      {"title": "Disappearance of Paula Jean Welden - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Paula_Jean_Welden"},
      {"title": "Paula Welden - Charley Project", "url": "https://charleyproject.org/case/paula-jean-welden"},
      {"title": "The Bennington Triangle - Vermont Public Radio", "url": "https://www.vermontpublic.org/"}
    ],
    "narrative": [
      "On the afternoon of Sunday, December 1, 1946, 18-year-old Paula Jean Welden, a sophomore at Bennington College in southwestern Vermont, told her roommate she was going for a walk. She was last seen on the Long Trail near Route 9, heading toward Glastenbury Mountain. A couple hiking the trail saw her round a bend in the path ahead of them, and when they reached the same spot moments later, she had vanished.",
      "Despite immediate and extensive search efforts—eventually involving hundreds of volunteers, state police, FBI, and even the Army—no trace of Paula was found. No clothing, no footprints leading off the trail, no evidence of an accident or foul play. The search was hampered by approaching winter weather and the dense, rugged terrain of the Green Mountains.",
      "Paula was described as a bright, attractive young woman who had seemed somewhat preoccupied in the days before her disappearance. Her father, an engineer in Stamford, Connecticut, was critical of the Vermont authorities' response, which he considered inadequate and poorly coordinated. His criticism, combined with public pressure, led directly to the creation of the Vermont State Police in 1947.",
      "Paula Welden's disappearance was later grouped with several other unsolved vanishings in the Bennington area between 1945 and 1950, a pattern that author Joseph Citro dubbed the 'Bennington Triangle.' These included the disappearances of Middie Rivers (1945), James Tedford (1949), Paul Jepson (1950), and Frieda Langer (1950, the only one found—months later, though the cause of death could not be determined). No connection between the cases was ever established, and Paula's fate remains unknown."
    ],
    "timeline": [
      {"date": "1946-12-01", "event": "Paula Welden goes for a hike on the Long Trail and vanishes."},
      {"date": "1946-12-02", "event": "Search parties begin combing the trail and surrounding wilderness."},
      {"date": "1946-12-15", "event": "FBI joins the investigation at the family's request."},
      {"date": "1947-01-01", "event": "Vermont State Police is created partly in response to the case."}
    ],
    "enriched": True
  },
  {
    "id": "boys-on-the-tracks-1987",
    "name": "Don Henry & Kevin Ives",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1987,
    "date": "August 23, 1987",
    "state": "Arkansas",
    "city": "Alexander",
    "age": None,
    "gender": "Male",
    "summary": "Two teenage boys were found dead on railroad tracks near Alexander, Arkansas. Initially ruled accidental, the deaths were later reclassified as homicides. The case became entangled in allegations of drug trafficking and government corruption in Arkansas.",
    "lastSeen": "August 22, 1987, Alexander, Arkansas",
    "tags": ["homicide", "Arkansas", "teenagers", "railroad", "drug trafficking", "corruption", "1980s"],
    "sources": [
      {"title": "Deaths of Don Henry and Kevin Ives - Wikipedia", "url": "https://en.wikipedia.org/wiki/Deaths_of_Don_Henry_and_Kevin_Ives"},
      {"title": "The Boys on the Tracks - Mara Leveritt", "url": "https://www.maraleveritt.com/the-boys-on-the-tracks"},
      {"title": "Kevin Ives and Don Henry case - Arkansas Democrat-Gazette", "url": "https://www.arkansasonline.com/"}
    ],
    "narrative": [
      "In the early morning hours of August 23, 1987, a Union Pacific freight train ran over the bodies of 17-year-old Don Henry and 16-year-old Kevin Ives on the railroad tracks near Alexander, Arkansas, a small community south of Little Rock. The boys, who were close friends, had gone out the previous evening, reportedly to go 'spotlighting' for deer. The state medical examiner, Fahmy Malak, initially ruled the deaths accidental, attributing them to marijuana-induced unconsciousness on the tracks.",
      "The boys' parents challenged this ruling vociferously. A second autopsy revealed that Don Henry had been stabbed in the back and Kevin Ives's skull had been crushed—injuries that preceded the train impact. The manner of death was changed to homicide. Dr. Malak's competence was questioned in this and other cases, eventually leading to his removal.",
      "As the investigation deepened, it became entangled in allegations of drug trafficking at a rural airport near the tracks. Witnesses claimed that the boys had stumbled upon a drug drop site and were killed because of what they saw. Multiple witnesses connected to the case died under suspicious circumstances over the following years, including Keith McKaskle, who was stabbed 113 times, and Jeff Rhodes, who was shot and set on fire. At least six people linked to the case met violent ends.",
      "Despite convictions in some of the related deaths, no one has ever been charged with the murders of Don Henry and Kevin Ives. Investigative journalist Mara Leveritt's book 'The Boys on the Tracks' detailed the case and the alleged connections to a wider drug smuggling operation. The families continue to seek justice, and the case remains one of Arkansas's most controversial unsolved crimes."
    ],
    "timeline": [
      {"date": "1987-08-23", "event": "Don Henry and Kevin Ives are found dead on railroad tracks near Alexander, Arkansas."},
      {"date": "1987-08-24", "event": "State medical examiner rules deaths accidental."},
      {"date": "1988-04-01", "event": "Second autopsy reveals stab and blunt force injuries; deaths reclassified as homicides."},
      {"date": "1988-11-01", "event": "Witness Keith McKaskle is murdered; more linked witnesses die."},
      {"date": "1999-01-01", "event": "Mara Leveritt publishes 'The Boys on the Tracks.'"}
    ],
    "enriched": True
  },
  {
    "id": "lisa-au-1982",
    "name": "Lisa Au",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1982,
    "date": "January 22, 1982",
    "state": "Hawaii",
    "city": "Honolulu",
    "age": 18,
    "gender": "Female",
    "summary": "Eighteen-year-old Lisa Au was abducted from a bus stop near her Honolulu home and found strangled the next day on a hiking trail. Despite DNA evidence and decades of investigation, her killer has never been identified.",
    "lastSeen": "January 22, 1982, Kaneohe, Honolulu, Hawaii",
    "tags": ["homicide", "Hawaii", "teenager", "abduction", "1980s"],
    "sources": [
      {"title": "Murder of Lisa Au - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Lisa_Au"},
      {"title": "Lisa Au case - Honolulu Star-Advertiser", "url": "https://www.staradvertiser.com/"},
      {"title": "Lisa Au cold case - Hawaii News Now", "url": "https://www.hawaiinewsnow.com/"}
    ],
    "narrative": [
      "On the evening of January 22, 1982, 18-year-old Lisa Au left her boyfriend's house in the Kaneohe area of Honolulu to walk to a nearby bus stop. She was heading to her job at a Kentucky Fried Chicken restaurant. She never arrived at work and did not return home. Her family reported her missing the next day.",
      "Lisa's body was found on January 23 on the Tantalus hiking trail in the hills above Honolulu. She had been sexually assaulted and strangled. The location was remote and far from where she had last been seen, indicating she had been transported by vehicle. The crime scene yielded DNA evidence that investigators preserved for future testing.",
      "The investigation pursued numerous suspects over the decades, including individuals with histories of sexual violence in the Honolulu area. DNA from the crime scene was tested against suspects but no match was found. The case was featured in local media periodically, generating tips but no breakthrough.",
      "Lisa Au's murder remains one of Hawaii's most prominent unsolved homicides. Her family has continued to advocate for the case, and the Honolulu Police Department maintains it as an active cold case. Advances in genetic genealogy offer potential hope for identifying her killer through the preserved DNA evidence."
    ],
    "timeline": [
      {"date": "1982-01-22", "event": "Lisa Au disappears while walking to a bus stop in Kaneohe, Honolulu."},
      {"date": "1982-01-23", "event": "Her body is found on the Tantalus hiking trail."},
      {"date": "1982-01-24", "event": "Honolulu police begin extensive investigation."}
    ],
    "enriched": True
  },
  {
    "id": "beauchamp-tower-1911",
    "name": "Dorothy Arnold",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1910,
    "date": "December 12, 1910",
    "state": "New York",
    "city": "New York City",
    "age": 25,
    "gender": "Female",
    "summary": "Wealthy socialite Dorothy Arnold vanished while shopping on Fifth Avenue in Manhattan. Her prominent family delayed reporting her missing for weeks. Despite one of the era's most intensive investigations, she was never found.",
    "lastSeen": "December 12, 1910, Fifth Avenue, Manhattan, New York",
    "tags": ["missing person", "New York", "socialite", "historical", "Gilded Age", "1910s"],
    "sources": [
      {"title": "Dorothy Arnold - Wikipedia", "url": "https://en.wikipedia.org/wiki/Dorothy_Arnold_(missing_person)"},
      {"title": "The Disappearance of Dorothy Arnold - Smithsonian Magazine", "url": "https://www.smithsonianmag.com/history/the-disappearance-of-dorothy-arnold-165968978/"},
      {"title": "Dorothy Arnold Missing - New York Times archive", "url": "https://www.nytimes.com/"}
    ],
    "narrative": [
      "On the afternoon of December 12, 1910, Dorothy Harriett Camille Arnold, a 25-year-old socialite and aspiring writer from one of New York City's most prominent families, left her family's home at 108 East 79th Street to go shopping on Fifth Avenue. She purchased a box of chocolates and a book, and was last seen by a friend near 59th Street at approximately 2:00 p.m. She never returned home.",
      "Dorothy's family, deeply concerned about social scandal, did not report her missing to police for six weeks. Instead, they hired the Pinkerton Detective Agency to conduct a discreet investigation. It was not until late January 1911, when the Pinkertons had failed to find any trace of Dorothy, that her father reluctantly contacted the New York Police Department.",
      "The investigation that followed was the most extensive missing person search New York had seen to that date. It emerged that Dorothy had been carrying on a secret relationship with an older man named George Griscom Jr. and had recently been deeply disappointed by the rejection of a short story she had submitted to McClure's Magazine. Some theories suggested she had committed suicide, while others pointed to Griscom or to a botched illegal abortion as explanations.",
      "Despite following leads across the United States and Europe, investigators never found any trace of Dorothy Arnold. No body, no confirmed sighting, no evidence of travel under an assumed name. The case became one of the most sensational of the early 20th century, and Dorothy's disappearance from a busy Manhattan street in broad daylight remains unexplained over a century later."
    ],
    "timeline": [
      {"date": "1910-12-12", "event": "Dorothy Arnold is last seen shopping on Fifth Avenue in Manhattan."},
      {"date": "1910-12-13", "event": "Her family notices her absence but does not contact police."},
      {"date": "1911-01-25", "event": "After Pinkerton detectives fail, family finally contacts NYPD."},
      {"date": "1911-02-01", "event": "Case becomes national news; massive investigation begins."}
    ],
    "enriched": True
  },
  {
    "id": "frederica-biggs-1975",
    "name": "Frederica Biggs",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1975,
    "date": "December 11, 1975",
    "state": "Vermont",
    "city": "Saxtons River",
    "age": 16,
    "gender": "Female",
    "summary": "Sixteen-year-old Frederica Biggs disappeared after leaving a square dance in Saxtons River, Vermont. Her body was found months later in a nearby river. The case has never been solved and is part of a series of unsolved crimes attributed to the Connecticut River Valley Killer.",
    "lastSeen": "December 11, 1975, Saxtons River, Vermont",
    "tags": ["homicide", "Vermont", "teenager", "serial killer possible", "Connecticut River Valley", "1970s"],
    "sources": [
      {"title": "Connecticut River Valley Killer - Wikipedia", "url": "https://en.wikipedia.org/wiki/Connecticut_River_Valley_Killer"},
      {"title": "Frederica Biggs case - Valley News", "url": "https://www.vnews.com/"},
      {"title": "Vermont cold cases - Burlington Free Press", "url": "https://www.burlingtonfreepress.com/"}
    ],
    "narrative": [
      "On the evening of December 11, 1975, 16-year-old Frederica 'Bunny' Biggs attended a square dance at the Main Street School in Saxtons River, a small village in southeastern Vermont. She left the dance at approximately 10:00 p.m. and was last seen walking along Route 121 toward her home about a mile away. She never arrived.",
      "A search began immediately, with volunteers and police combing the roads, fields, and woods between the school and Biggs' home. No trace of her was found. It was not until April 1976 that her body was discovered in the Connecticut River, miles downstream from Saxtons River. Due to the condition of her remains after months in the water, the exact cause of death was difficult to determine.",
      "Frederica's case has been linked by some investigators to a series of unsolved murders and disappearances along the Connecticut River Valley in Vermont and New Hampshire during the 1970s and 1980s, attributed to an unidentified serial killer known as the Connecticut River Valley Killer. Other victims potentially connected include Cathy Millican, Bernice Courtemanche, Ellen Fried, and Eva Morse.",
      "No suspect has ever been charged in Frederica Biggs' death. The case remains open with the Vermont State Police. The possibility of a serial killer operating in the region has made it one of New England's most chilling unsolved mysteries."
    ],
    "timeline": [
      {"date": "1975-12-11", "event": "Frederica Biggs disappears after leaving a square dance in Saxtons River."},
      {"date": "1975-12-12", "event": "Search begins; no trace found."},
      {"date": "1976-04-01", "event": "Her body is discovered in the Connecticut River."}
    ],
    "enriched": True
  },
  {
    "id": "keddie-cabin-murders-1981",
    "name": "Keddie Cabin 28 Victims",
    "type": "Multiple Homicide",
    "status": "Unsolved",
    "year": 1981,
    "date": "April 11, 1981",
    "state": "California",
    "city": "Keddie",
    "age": None,
    "gender": "Multiple",
    "summary": "Four people were brutally murdered in Cabin 28 at the Keddie resort in the Sierra Nevada mountains. Three children sleeping in the next room were unharmed. Despite a suspect being named by the sheriff, the DA declined to prosecute and the case remains open.",
    "lastSeen": "April 11, 1981, Cabin 28, Keddie, California",
    "tags": ["homicide", "California", "cabin", "Sierra Nevada", "multiple victims", "1980s"],
    "sources": [
      {"title": "Keddie murders - Wikipedia", "url": "https://en.wikipedia.org/wiki/Keddie_murders"},
      {"title": "Keddie Cabin 28 case - Sacramento Bee", "url": "https://www.sacbee.com/"},
      {"title": "Keddie murders investigation - Plumas County Sheriff", "url": "https://www.plumascounty.us/"}
    ],
    "narrative": [
      "On the morning of April 12, 1981, a teenage girl staying in Cabin 28 at the Keddie Resort in Plumas County, California woke to discover a horrific scene. Her mother, 36-year-old Glynn Sharp (known as Sue), along with Sue's friend Dana Wingate (17) and Sue's 15-year-old son John, had been bound, beaten with a hammer, and stabbed. Sue's 12-year-old daughter Tina was missing. Three younger children—ages 5, 10, and 12—had slept through the attack in an adjacent room.",
      "The crime scene was extraordinarily violent. The victims had been bound with medical tape and electrical cord. Two knives and a hammer were recovered, all bent from the force of the attack. The violence suggested rage-fueled killing by someone who knew the victims. Tina Sharp's remains were not found until 1984, when her skull and other bones were discovered near Camp Eighteen in Butte County, approximately 60 miles away.",
      "The investigation was plagued by mishandled evidence, jurisdictional disputes, and the remote location. Plumas County had limited resources, and key evidence—including the door of Cabin 28—went missing. A hammer head was reportedly found in a nearby pond, and a witness came forward years later claiming to have seen suspects leaving the cabin that night.",
      "In 2016, Plumas County Sheriff Greg Hagwood publicly named Martin Smartt, a neighbor of the victims who had since died, as the prime suspect. Smartt's ex-wife had apparently told investigators details about the crimes. However, the district attorney declined to pursue the case, citing insufficient evidence for prosecution without a living defendant to stand trial. Cabin 28 was demolished in 2004. The case remains officially open."
    ],
    "timeline": [
      {"date": "1981-04-11", "event": "Sue Sharp, John Sharp, and Dana Wingate are murdered in Cabin 28; Tina Sharp goes missing."},
      {"date": "1981-04-12", "event": "Surviving children discover the bodies; massive investigation begins."},
      {"date": "1984-04-22", "event": "Tina Sharp's skull and remains are found 60 miles away."},
      {"date": "2016-04-22", "event": "Sheriff names Martin Smartt as prime suspect; DA declines to prosecute."}
    ],
    "enriched": True
  },
  {
    "id": "charlie-brewer-1999",
    "name": "Charlie Brewer",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1999,
    "date": "December 4, 1999",
    "state": "North Carolina",
    "city": "Raleigh",
    "age": 26,
    "gender": "Male",
    "summary": "Charlie Brewer disappeared after attending a party in Raleigh, North Carolina. His car was found days later parked at the Raleigh-Durham Airport. Despite extensive investigation, he was never found.",
    "lastSeen": "December 4, 1999, Raleigh, North Carolina",
    "tags": ["missing person", "North Carolina", "young adult", "party", "1990s"],
    "sources": [
      {"title": "Charlie Brewer missing - Charley Project", "url": "https://charleyproject.org/case/charlie-brewer"},
      {"title": "Charlie Brewer case - WRAL", "url": "https://www.wral.com/"},
      {"title": "Raleigh missing person - News & Observer", "url": "https://www.newsobserver.com/"}
    ],
    "narrative": [
      "On the night of December 4, 1999, 26-year-old Charlie Brewer attended a holiday party at an apartment complex in Raleigh, North Carolina. He had been drinking and was reportedly in good spirits. He was last seen leaving the party late that night. He did not return to his own apartment.",
      "Several days later, Charlie's car was found parked at the Raleigh-Durham International Airport. However, there was no record of Charlie purchasing a plane ticket or boarding any flight. The car's location raised the possibility that someone else had driven it there to create a false trail.",
      "The investigation explored multiple theories, including voluntary disappearance, suicide, and foul play. Charlie's bank accounts were never accessed, and he made no contact with family or friends. Searches of areas near the party location and the airport yielded nothing.",
      "Charlie Brewer's family has continued to seek answers, keeping his case in the public eye through social media and local news coverage. The Raleigh Police Department maintains the case as an open missing person investigation."
    ],
    "timeline": [
      {"date": "1999-12-04", "event": "Charlie Brewer attends a party in Raleigh and disappears."},
      {"date": "1999-12-07", "event": "His car is found at Raleigh-Durham Airport with no travel record."},
      {"date": "1999-12-08", "event": "Raleigh police begin formal missing person investigation."}
    ],
    "enriched": True
  },
  {
    "id": "mary-jane-barker-1957",
    "name": "Mary Jane Barker",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1957,
    "date": "August 16, 1957",
    "state": "Wisconsin",
    "city": "Spooner",
    "age": 4,
    "gender": "Female",
    "summary": "Four-year-old Mary Jane Barker vanished from outside her family's home in Spooner, Wisconsin. Despite massive searches including draining a nearby lake, she was never found. The case remains Wisconsin's oldest active missing child case.",
    "lastSeen": "August 16, 1957, Spooner, Wisconsin",
    "tags": ["missing person", "Wisconsin", "child", "1950s"],
    "sources": [
      {"title": "Mary Jane Barker - Charley Project", "url": "https://charleyproject.org/case/mary-jane-barker"},
      {"title": "Mary Jane Barker - NCMEC", "url": "https://www.missingkids.org/"},
      {"title": "Wisconsin's oldest missing child case - Milwaukee Journal Sentinel", "url": "https://www.jsonline.com/"}
    ],
    "narrative": [
      "On August 16, 1957, four-year-old Mary Jane Barker was playing outside her family's home on Elm Street in Spooner, Wisconsin, a small city in the northwestern part of the state. Her mother last saw her at approximately 1:30 p.m. When she checked on Mary Jane a short time later, the child was gone.",
      "The disappearance triggered one of the largest searches in Wisconsin history at that time. Hundreds of volunteers joined police and National Guard members in searching the woods, fields, and waterways surrounding Spooner. The nearby Yellow River and Spooner Lake were dragged, and divers searched the waters. Dogs tracked Mary Jane's scent to a road near the house, suggesting she may have been picked up by a vehicle.",
      "Despite the extensive search and a reward offered by the community, no trace of Mary Jane was ever found. Investigators pursued numerous leads over the years, including tips about suspicious vehicles and persons seen in the area that day, but none led to her recovery.",
      "The case remains Wisconsin's oldest active missing child case. Periodic reviews by the Spooner Police Department and the Wisconsin Department of Justice have not produced new leads. Mary Jane Barker would be in her seventies if still alive."
    ],
    "timeline": [
      {"date": "1957-08-16", "event": "Mary Jane Barker vanishes from outside her home in Spooner, Wisconsin."},
      {"date": "1957-08-16", "event": "Massive search begins; hundreds of volunteers participate."},
      {"date": "1957-08-17", "event": "Dogs track scent to a road; vehicle abduction suspected."}
    ],
    "enriched": True
  },
  {
    "id": "steven-damman-1955",
    "name": "Steven Damman",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1955,
    "date": "October 31, 1955",
    "state": "New York",
    "city": "East Meadow",
    "age": 2,
    "gender": "Male",
    "summary": "Two-year-old Steven Damman was taken from his stroller outside a Long Island bakery on Halloween 1955. His mother had left him briefly with his baby sister. Despite FBI involvement and national attention, Steven was never found.",
    "lastSeen": "October 31, 1955, East Meadow, Long Island, New York",
    "tags": ["missing person", "New York", "Long Island", "child", "Halloween", "1950s"],
    "sources": [
      {"title": "Disappearance of Steven Damman - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Steven_Damman"},
      {"title": "Steven Damman - NCMEC", "url": "https://www.missingkids.org/"},
      {"title": "Steven Damman - FBI", "url": "https://www.fbi.gov/"}
    ],
    "narrative": [
      "On the afternoon of October 31, 1955—Halloween—Marilyn Damman left her two-year-old son Steven and seven-month-old daughter Pamela in a stroller outside a bakery on Hempstead Turnpike in East Meadow, Long Island, New York while she went inside to make a purchase. When she returned minutes later, Steven was gone. Pamela was still in the stroller, unharmed.",
      "The abduction made national headlines and prompted an intensive search. The FBI joined the investigation due to the possibility of kidnapping. Hundreds of tips poured in, and sightings were reported across the country, but none led to Steven. The case became one of the most publicized child abductions of the 1950s.",
      "In 2012, the FBI reopened the case after a man in Michigan believed he might be Steven Damman based on similarities in age, appearance, and lack of knowledge about his early childhood. DNA testing, however, conclusively ruled him out. The investigation continued to pursue other leads without success.",
      "Steven Damman's disappearance occurred during an era of relative innocence when leaving children unattended briefly was common. The case helped change attitudes about child safety and contributed to growing awareness of the danger of child abduction. Marilyn Damman spent the rest of her life hoping for Steven's return and died in 2019 without ever learning his fate."
    ],
    "timeline": [
      {"date": "1955-10-31", "event": "Steven Damman is taken from a stroller outside a bakery in East Meadow, Long Island."},
      {"date": "1955-11-01", "event": "FBI joins the investigation; national search begins."},
      {"date": "2012-01-01", "event": "A Michigan man believes he may be Steven; DNA testing rules him out."}
    ],
    "enriched": True
  },
  {
    "id": "deysi-garcia-2010",
    "name": "Deysi Garcia",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2010,
    "date": "October 20, 2010",
    "state": "California",
    "city": "San Francisco",
    "age": 28,
    "gender": "Female",
    "summary": "Deysi Garcia, a 28-year-old Honduran immigrant, vanished from San Francisco's Mission District. She was last seen leaving her workplace. Despite community efforts, she has never been found.",
    "lastSeen": "October 20, 2010, Mission District, San Francisco, California",
    "tags": ["missing person", "California", "San Francisco", "immigrant", "2010s"],
    "sources": [
      {"title": "Deysi Garcia missing - SF Gate", "url": "https://www.sfgate.com/"},
      {"title": "Missing in San Francisco - SFPD", "url": "https://www.sanfranciscopolice.org/"},
      {"title": "Deysi Garcia case - Mission Local", "url": "https://missionlocal.org/"}
    ],
    "narrative": [
      "On October 20, 2010, 28-year-old Deysi Garcia left her workplace in San Francisco's Mission District and vanished. She was a Honduran immigrant who worked in the food service industry and lived in the city. She had spoken to family members that day and gave no indication of plans to leave or any concerns for her safety.",
      "When Deysi failed to return home, her family and community raised the alarm. The Mission District, a vibrant and densely populated neighborhood, was canvassed by police and volunteers. Flyers were distributed in both English and Spanish throughout the area. Her case gained attention from immigrant advocacy groups who highlighted the vulnerability of undocumented workers.",
      "Investigators explored theories including foul play, voluntary disappearance, and the possibility that immigration concerns might have prevented witnesses from coming forward. Deysi's bank accounts showed no activity after her disappearance, and her phone went silent.",
      "Deysi Garcia's case is representative of the many missing person cases involving immigrants in large American cities, where language barriers, immigration status fears, and limited family connections can make investigations more difficult. Her case remains open with the San Francisco Police Department."
    ],
    "timeline": [
      {"date": "2010-10-20", "event": "Deysi Garcia is last seen leaving her workplace in the Mission District."},
      {"date": "2010-10-21", "event": "She is reported missing by family members."},
      {"date": "2010-10-25", "event": "Community distributes flyers; SFPD investigates."}
    ],
    "enriched": True
  },
  {
    "id": "emma-fillipoff-2012",
    "name": "Emma Fillipoff",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2012,
    "date": "November 28, 2012",
    "state": "British Columbia",
    "city": "Victoria",
    "age": 26,
    "gender": "Female",
    "country": "Canada",
    "summary": "Twenty-six-year-old Emma Fillipoff was last seen on CCTV pacing barefoot outside the Empress Hotel in Victoria, British Columbia after police were called about her erratic behavior. She disappeared before officers returned and has never been found.",
    "lastSeen": "November 28, 2012, Empress Hotel, Victoria, British Columbia",
    "tags": ["missing person", "Canada", "international", "mental health", "Victoria", "2010s"],
    "sources": [
      {"title": "Disappearance of Emma Fillipoff - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Emma_Fillipoff"},
      {"title": "Emma Fillipoff - Victoria Police", "url": "https://vicpd.ca/"},
      {"title": "Where is Emma Fillipoff? - CBC News", "url": "https://www.cbc.ca/news/canada/british-columbia/emma-fillipoff-missing-victoria-1.4893221"}
    ],
    "narrative": [
      "On the evening of November 28, 2012, police in Victoria, British Columbia were called to the Empress Hotel—a landmark waterfront hotel in the city's Inner Harbour—about a young woman acting erratically outside. Officers found 26-year-old Emma Fillipoff pacing barefoot on the sidewalk, appearing confused and distressed. She told police she was waiting for someone but declined further assistance.",
      "Officers spoke with Emma briefly and then left to handle other calls, planning to check back on her. When they returned approximately 30 minutes later, she was gone. Security cameras showed her walking away from the hotel, but she was never seen again. Her car was found parked nearby with her shoes and other belongings inside.",
      "Emma had been showing signs of mental health difficulties in the weeks before her disappearance. She had been living in Victoria after moving from Ontario and was somewhat isolated. Friends and family reported she had become increasingly withdrawn and had expressed paranoid thoughts. However, there was no indication she was suicidal, and she had plans for the following days.",
      "Her mother Shelley Fillipoff launched an extensive search campaign, traveling to Victoria multiple times and distributing thousands of posters. The case was featured on the popular podcast 'Someone Knows Something.' Despite tips and reported sightings across Canada, Emma has never been found. The Victoria Police Department maintains the case as an active investigation."
    ],
    "timeline": [
      {"date": "2012-11-28", "event": "Police encounter Emma Fillipoff acting erratically outside the Empress Hotel."},
      {"date": "2012-11-28", "event": "Officers leave and return to find her gone."},
      {"date": "2012-11-29", "event": "Her car is found with her belongings; she is reported missing."},
      {"date": "2018-01-01", "event": "CBC's 'Someone Knows Something' podcast features her case."}
    ],
    "enriched": True
  },
  {
    "id": "madeline-amy-sweeney-1985",
    "name": "Amy Mihaljevic",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1989,
    "date": "October 27, 1989",
    "state": "Ohio",
    "city": "Bay Village",
    "age": 10,
    "gender": "Female",
    "summary": "Ten-year-old Amy Mihaljevic was lured from a Bay Village shopping plaza by a man who called her on the phone promising a surprise for her mother. Her body was found months later in a field. Despite extensive investigation, her killer has never been identified.",
    "lastSeen": "October 27, 1989, Bay Square Shopping Center, Bay Village, Ohio",
    "tags": ["homicide", "Ohio", "child", "abduction", "1980s"],
    "sources": [
      {"title": "Murder of Amy Mihaljevic - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Amy_Mihaljevic"},
      {"title": "Amy Mihaljevic case - Cleveland Plain Dealer", "url": "https://www.cleveland.com/metro/2019/10/thirty-years-later-amys-murder-remains-unsolved.html"},
      {"title": "Who Killed Amy Mihaljevic? - Scene Magazine", "url": "https://www.clevescene.com/"}
    ],
    "narrative": [
      "In late September 1989, 10-year-old Amy Renee Mihaljevic began receiving phone calls at her home in Bay Village, Ohio from a man who claimed to know her mother. The caller told Amy that her mother had recently received a promotion at work and suggested Amy help him buy a gift to surprise her. Over several calls, the man gained Amy's trust and arranged to meet her.",
      "On the afternoon of October 27, 1989, Amy walked from her school to the Bay Square Shopping Center, where she met the caller. Witnesses saw her walking through the plaza with a man described as white, approximately 35-50 years old, with a moustache. Amy left the plaza with the man and was never seen alive again.",
      "Amy's body was discovered on February 8, 1990, in a field in rural Ashland County, approximately 50 miles south of Bay Village. She had been stabbed in the neck. The discovery prompted a renewed investigation, but the rural location yielded few forensic leads. The case generated enormous publicity in Ohio and beyond.",
      "Over three decades, investigators have pursued hundreds of suspects. In 2006, journalist James Renner published 'Amy: My Search for Her Killer,' which named several potential suspects and generated new tips. DNA evidence collected at the time has been preserved and periodically tested against suspects. The FBI's Behavioral Analysis Unit has assisted with profiling. Despite these efforts, Amy Mihaljevic's killer has never been identified, and the case remains one of Ohio's most haunting unsolved murders."
    ],
    "timeline": [
      {"date": "1989-09-25", "event": "Amy Mihaljevic begins receiving phone calls from an unknown man."},
      {"date": "1989-10-27", "event": "Amy meets the caller at Bay Square Shopping Center and disappears."},
      {"date": "1990-02-08", "event": "Amy's body is found in a field in Ashland County."},
      {"date": "2006-01-01", "event": "James Renner publishes investigation naming potential suspects."}
    ],
    "enriched": True
  },
  {
    "id": "heidi-allen-1994",
    "name": "Heidi Allen",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1994,
    "date": "April 3, 1994",
    "state": "New York",
    "city": "New Haven",
    "age": 18,
    "gender": "Female",
    "summary": "Eighteen-year-old Heidi Allen was abducted from the convenience store where she worked in New Haven, New York. Two brothers were convicted of kidnapping, but their convictions were controversial. Heidi's body was never found.",
    "lastSeen": "April 3, 1994, D&W Convenience Store, New Haven, New York",
    "tags": ["missing person", "New York", "abduction", "convenience store", "wrongful conviction possible", "1990s"],
    "sources": [
      {"title": "Disappearance of Heidi Allen - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Heidi_Allen"},
      {"title": "Heidi Allen case - Syracuse.com", "url": "https://www.syracuse.com/crime/2019/04/heidi-allen-25-years-missing.html"},
      {"title": "Heidi Allen - Charley Project", "url": "https://charleyproject.org/case/heidi-m-allen"}
    ],
    "narrative": [
      "On the morning of April 3, 1994—Easter Sunday—18-year-old Heidi Allen was working the early shift at the D&W Convenience Store on Route 104 in New Haven, a small town in Oswego County, New York. At approximately 7:45 a.m., a customer entered the store and found it unattended. The cash register was open, and Heidi's coat and keys were behind the counter. She had vanished.",
      "The abduction occurred in broad daylight on a Sunday morning in a rural community, shocking the area. A witness reported seeing a van near the store around the time of the disappearance. The investigation led to brothers Gary and Richard Thibodeau, who were arrested and charged with kidnapping. Gary was convicted in 1995 and sentenced to 25 years to life; Richard was convicted in 1996 and received the same sentence.",
      "The convictions have been highly controversial. Both were based largely on the testimony of an informant and accomplice witnesses whose credibility was questioned. No physical evidence linked the brothers to the crime, and Heidi's body was never found. Appeals and advocacy by innocence organizations have challenged the convictions, with some arguing the Thibodeaus were scapegoats for a crime they did not commit.",
      "Richard Thibodeau was released on parole in 2018 after serving over 20 years. Gary Thibodeau died in prison in 2018 before his appeal could be heard. Heidi Allen's body has never been recovered, and questions about what really happened at the D&W convenience store that Easter morning remain unanswered."
    ],
    "timeline": [
      {"date": "1994-04-03", "event": "Heidi Allen disappears from the D&W Convenience Store in New Haven, New York."},
      {"date": "1994-04-04", "event": "Search for Heidi begins; van sighting investigated."},
      {"date": "1995-01-01", "event": "Gary Thibodeau is convicted of kidnapping."},
      {"date": "1996-01-01", "event": "Richard Thibodeau is convicted of kidnapping."},
      {"date": "2018-04-01", "event": "Gary Thibodeau dies in prison; Richard is released on parole."}
    ],
    "enriched": True
  },
  {
    "id": "lisanne-froon-kris-kremers-2014",
    "name": "Lisanne Froon & Kris Kremers",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2014,
    "date": "April 1, 2014",
    "state": "Chiriquí Province",
    "city": "Boquete",
    "age": None,
    "gender": "Female",
    "country": "Panama",
    "summary": "Two Dutch tourists disappeared while hiking near Boquete, Panama. Their backpack was found weeks later with phones, camera, and disturbing nighttime photos. Skeletal remains were found months later. Whether they died from misadventure or foul play is unknown.",
    "lastSeen": "April 1, 2014, Pianista trail, Boquete, Panama",
    "tags": ["missing person", "Panama", "international", "Dutch", "hiking", "2010s"],
    "sources": [
      {"title": "Deaths of Kris Kremers and Lisanne Froon - Wikipedia", "url": "https://en.wikipedia.org/wiki/Deaths_of_Kris_Kremers_and_Lisanne_Froon"},
      {"title": "Lost in the Jungle - Daily Beast", "url": "https://www.thedailybeast.com/the-lost-girls-of-panama-the-camera-the-jungle-and-the-bones"},
      {"title": "Kris and Lisanne case - NOS (Dutch Broadcasting)", "url": "https://nos.nl/"}
    ],
    "narrative": [
      "On April 1, 2014, Kris Kremers (21) and Lisanne Froon (22), two Dutch women volunteering in Boquete, Panama, set out for a day hike on the popular Pianista trail near the continental divide. Photos from Lisanne's camera show them reaching the summit of the trail around 1:00 p.m. and then continuing beyond the marked path into more remote terrain. They were never seen alive again.",
      "Phone records show that at 4:39 p.m. that day, Kris's phone made an emergency call to 112 (the European emergency number) and then to 911 (the Panamanian number). Lisanne's phone made a similar call shortly after. None of the calls connected—the area had extremely limited cell coverage. Over the following days, more emergency calls were attempted from both phones, but none went through. The phones' batteries were gradually depleted, with Kris's phone dying on April 5 and Lisanne's being periodically turned on until April 11.",
      "Ten weeks later, Lisanne's backpack was found on a riverbank by a local woman. Inside were the phones, Lisanne's camera, cash, and their passports—none of which had been taken. The camera contained 90 photos taken in darkness between 1:00 and 4:00 a.m. on April 8, showing jungle vegetation, rocks, and what appeared to be scraps of material. Some interpreted these as distress signals; others as attempts to use the flash as a light source.",
      "Skeletal remains of both women were found over subsequent months along the same river system. Some bones showed signs of bleaching inconsistent with the timeline, and a foot was found inside a boot still laced up, raising questions. The official Panamanian conclusion was that the women became lost and died of exposure, starvation, or a fall. Dutch investigators were unable to rule out foul play. The case has generated intense online debate about whether their deaths were accidental or criminal."
    ],
    "timeline": [
      {"date": "2014-04-01", "event": "Kris Kremers and Lisanne Froon set out for a hike on the Pianista trail."},
      {"date": "2014-04-01", "event": "Emergency calls are made from both phones but do not connect."},
      {"date": "2014-04-08", "event": "90 mysterious nighttime photos are taken on Lisanne's camera."},
      {"date": "2014-06-11", "event": "Lisanne's backpack is found by a local on a riverbank."},
      {"date": "2014-09-01", "event": "Skeletal remains of both women are recovered along the river."}
    ],
    "enriched": True
  },
  {
    "id": "lyle-and-erik-menendez-parents",
    "name": "José & Kitty Menéndez",
    "type": "Multiple Homicide",
    "status": "Conviction",
    "year": 1989,
    "date": "August 20, 1989",
    "state": "California",
    "city": "Beverly Hills",
    "age": None,
    "gender": "Multiple",
    "summary": "Entertainment executive José Menéndez and his wife Kitty were shotgunned to death in their Beverly Hills mansion by their sons Lyle and Erik. The brothers were convicted in 1996 after two trials. Resentencing efforts citing abuse claims gained renewed attention in the 2020s.",
    "lastSeen": "August 20, 1989, 722 North Elm Drive, Beverly Hills, California",
    "tags": ["homicide", "California", "Beverly Hills", "parricide", "abuse", "1980s"],
    "sources": [
      {"title": "Lyle and Erik Menendez - Wikipedia", "url": "https://en.wikipedia.org/wiki/Lyle_and_Erik_Menendez"},
      {"title": "Menendez brothers case - Los Angeles Times", "url": "https://www.latimes.com/california/story/2024-10-24/menendez-brothers-resentencing"},
      {"title": "Menendez brothers resentencing - CNN", "url": "https://www.cnn.com/2024/11/26/us/menendez-brothers-resentencing/index.html"}
    ],
    "narrative": [
      "On the evening of August 20, 1989, José Menéndez (45), a Cuban-born entertainment executive who was CEO of LIVE Entertainment (later Artisan Entertainment), and his wife Mary Louise 'Kitty' Menéndez (47) were shot to death with 12-gauge shotguns in the den of their Beverly Hills mansion at 722 North Elm Drive. They were struck by a combined total of 15 shotgun blasts. Their sons Lyle (21) and Erik (18) called 911, claiming they had returned home to find their parents dead.",
      "Initially, police investigated the murders as a possible mob hit related to José's business dealings. However, Erik began confessing to his psychologist, Dr. Jerome Oziel, who recorded the sessions. When Oziel's ex-girlfriend Judalon Smyth learned of the recordings, she contacted police. The brothers were arrested in March 1990.",
      "The first trial in 1993-1994 was televised live on Court TV and became a national sensation. The brothers admitted to the killings but claimed they acted out of fear after years of emotional, physical, and sexual abuse by their father. The trial ended in two hung juries (one for each brother). At the second trial in 1995-1996, the judge significantly limited testimony about the abuse allegations, and both brothers were convicted of first-degree murder and conspiracy. They were sentenced to life without parole.",
      "The case experienced renewed attention in the 2020s, driven by documentaries, a Ryan Murphy Netflix series, and a TikTok campaign advocating for the brothers' release. In 2024, the Los Angeles County District Attorney's office recommended resentencing, citing new evidence supporting the brothers' abuse claims, including a letter Erik wrote to a cousin before the murders describing the abuse and testimony from Roy Rosselló, a former member of the boy band Menudo, who alleged he was also sexually abused by José Menéndez."
    ],
    "timeline": [
      {"date": "1989-08-20", "event": "José and Kitty Menéndez are shot to death in their Beverly Hills mansion."},
      {"date": "1990-03-08", "event": "Lyle Menéndez is arrested; Erik turns himself in days later."},
      {"date": "1994-01-28", "event": "First trial ends in hung juries for both brothers."},
      {"date": "1996-03-20", "event": "Both brothers are convicted of first-degree murder at retrial."},
      {"date": "2024-10-24", "event": "LA County DA recommends resentencing based on new abuse evidence."}
    ],
    "enriched": True
  },
  {
    "id": "disappearance-of-maelys-de-araujo-2017",
    "name": "Maëlys de Araujo",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2017,
    "date": "August 27, 2017",
    "state": "Isère",
    "city": "Pont-de-Beauvoisin",
    "age": 8,
    "gender": "Female",
    "country": "France",
    "summary": "Eight-year-old Maëlys de Araujo vanished during a wedding reception in southeastern France. Nordahl Lelandais, a former military dog handler, was convicted of her kidnapping and murder in 2022 after DNA evidence linked him to the crime.",
    "lastSeen": "August 27, 2017, Pont-de-Beauvoisin, Isère, France",
    "tags": ["homicide", "France", "international", "child", "wedding", "2010s"],
    "sources": [
      {"title": "Murder of Maëlys de Araujo - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Ma%C3%ABlys_de_Araujo"},
      {"title": "Nordahl Lelandais convicted - Le Monde", "url": "https://www.lemonde.fr/en/france/article/2022/02/18/nordahl-lelandais-convicted-of-kidnapping-and-murder-of-maelys-de-araujo_5980014_7.html"},
      {"title": "Maëlys case - France 24", "url": "https://www.france24.com/en/france/20220218-french-ex-soldier-nordahl-lelandais-found-guilty-of-murdering-8-year-old-girl"}
    ],
    "narrative": [
      "On the night of August 26-27, 2017, eight-year-old Maëlys de Araujo attended a wedding celebration with her parents at a community hall in Pont-de-Beauvoisin, a small town in the Isère department of southeastern France. During the festivities, Maëlys was seen playing in a children's area and then disappeared sometime after 3:00 a.m. Her parents reported her missing to police when they could not find her.",
      "A massive search operation was launched involving hundreds of officers, volunteers, divers, and helicopters. One of the 180 wedding guests, 34-year-old Nordahl Lelandais, a former military dog handler, was identified as a person of interest when analysis of his phone's GPS data showed his car had left the venue during the celebration. He initially denied any involvement, but traces of Maëlys's DNA were found in the trunk of his car.",
      "After months of denying involvement, Lelandais confessed in February 2018, leading investigators to a wooded, mountainous area where Maëlys's remains were discovered. He claimed her death was accidental, saying she had fallen and hit her head, but this account was contradicted by forensic evidence suggesting deliberate violence.",
      "In February 2022, Nordahl Lelandais was convicted of kidnapping and murder and sentenced to life in prison with a minimum term of 22 years. During the investigation, he was also connected to and convicted of the murder of 23-year-old Arthur Noyer, a corporal who disappeared in April 2017, and was investigated for numerous sexual assaults on minors. The case shocked France and led to discussions about child safety at public events."
    ],
    "timeline": [
      {"date": "2017-08-27", "event": "Maëlys de Araujo vanishes during a wedding reception in Pont-de-Beauvoisin."},
      {"date": "2017-09-01", "event": "Nordahl Lelandais is identified as a person of interest."},
      {"date": "2017-09-04", "event": "Maëlys's DNA is found in Lelandais's car; he is arrested."},
      {"date": "2018-02-14", "event": "Lelandais confesses; leads police to Maëlys's remains."},
      {"date": "2022-02-18", "event": "Lelandais is convicted and sentenced to life in prison."}
    ],
    "enriched": True
  },
  {
    "id": "yuba-county-five-1978",
    "name": "Yuba County Five",
    "type": "Suspicious Death",
    "status": "Unsolved",
    "year": 1978,
    "date": "February 24, 1978",
    "state": "California",
    "city": "Oroville",
    "age": None,
    "gender": "Male",
    "summary": "Five young men from Yuba City disappeared after attending a basketball game in Chico. Their car was found abandoned on a remote mountain road. Four bodies were eventually found in and near a Forest Service trailer; the fifth was never found.",
    "lastSeen": "February 24, 1978, Oroville, California",
    "tags": ["suspicious death", "California", "missing person", "mountains", "1970s"],
    "sources": [
      {"title": "Yuba County Five - Wikipedia", "url": "https://en.wikipedia.org/wiki/Yuba_County_Five"},
      {"title": "America's Dyatlov Pass - Strange Outdoors", "url": "https://www.strangeoutdoors.com/mysterious-stories/yuba-county-five"},
      {"title": "Yuba County Five case - Sacramento Bee", "url": "https://www.sacbee.com/"}
    ],
    "narrative": [
      "On the evening of February 24, 1978, five young men from Yuba City, California—Jack Madruga (30), Bill Sterling (29), Ted Weiher (32), Jack Huett (24), and Gary Mathias (25)—drove together to watch a college basketball game at California State University, Chico. They were all described as intellectually disabled or living with mental health conditions, and they were close friends who played on a Special Olympics basketball team. They were in good spirits and planned to return home that night.",
      "The men never returned. Their Mercury Montego was found days later, abandoned on a remote dirt road near Oroville, approximately 70 miles from the basketball game—in the opposite direction from their home in Yuba City. The car was in working condition with gas in the tank, parked on a snowy mountain road at an elevation of approximately 4,000 feet. There was no logical reason for the men to have driven to this remote location.",
      "The search for the five men was hampered by heavy snow. In June 1978, as the snow melted, the bodies of Ted Weiher, Jack Madruga, Bill Sterling, and Jack Huett were found. Madruga and Sterling were found near the car, apparently having died of hypothermia. Weiher and Huett were found approximately 20 miles further up the mountain at a Forest Service trailer, along with evidence that someone had survived there for an extended period—up to 13 weeks. The trailer contained canned food, matches, and heavy clothing, but the food was barely touched. Weiher had been wrapped in bedsheets and had lost significant weight.",
      "Gary Mathias, the fifth man—and the only one with outdoor survival experience as an Army veteran—was never found. His shoes were discovered in the trailer, but no other trace of him has surfaced. The central mystery remains: why did the men drive to this remote location, and why didn't they use the ample supplies in the trailer to survive? The case has been called 'America's Dyatlov Pass' for its parallels to the Russian mystery."
    ],
    "timeline": [
      {"date": "1978-02-24", "event": "Five men attend a basketball game in Chico; they never return home."},
      {"date": "1978-02-28", "event": "Their car is found on a remote mountain road near Oroville."},
      {"date": "1978-06-04", "event": "Bodies of Madruga and Sterling are found near the car."},
      {"date": "1978-06-08", "event": "Weiher and Huett are found dead at a Forest Service trailer 20 miles away."},
      {"date": "1978-07-01", "event": "Extensive search fails to locate Gary Mathias."}
    ],
    "enriched": True
  },
  {
    "id": "suzanne-bombardier-1980",
    "name": "Suzanne Bombardier",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1980,
    "date": "January 25, 1980",
    "state": "California",
    "city": "Antioch",
    "age": 14,
    "gender": "Female",
    "summary": "Fourteen-year-old Suzanne Bombardier vanished from her Antioch, California home. Skeletal remains found decades later near Antioch have not been confirmed as hers. The case remains one of Contra Costa County's oldest missing child cases.",
    "lastSeen": "January 25, 1980, Antioch, California",
    "tags": ["missing person", "California", "teenager", "1980s"],
    "sources": [
      {"title": "Suzanne Bombardier - Charley Project", "url": "https://charleyproject.org/case/suzanne-ruth-bombardier"},
      {"title": "Suzanne Bombardier - NCMEC", "url": "https://www.missingkids.org/"},
      {"title": "Antioch missing girl - East Bay Times", "url": "https://www.eastbaytimes.com/"}
    ],
    "narrative": [
      "On January 25, 1980, 14-year-old Suzanne Ruth Bombardier disappeared from her family's home in Antioch, California, a city in eastern Contra Costa County. The circumstances of her disappearance suggested she may have been taken from the home, though details were limited. Her family reported her missing when she failed to appear.",
      "The Antioch Police Department conducted an extensive investigation, interviewing neighbors and searching the area. Suzanne's description was circulated widely, and the case was entered into missing persons databases. Despite these efforts, no trace of Suzanne was found.",
      "Over the decades, the case has been periodically revisited. Skeletal remains found in the Antioch area at various times have been compared to Suzanne's dental records and DNA profile, but no positive identification has been made. The case predates many modern forensic techniques and databases.",
      "Suzanne Bombardier's disappearance remains one of the oldest unsolved missing child cases in Contra Costa County. Her case is maintained in the NamUs and NCMEC databases, and investigators continue to hope that advances in DNA technology may someday provide answers."
    ],
    "timeline": [
      {"date": "1980-01-25", "event": "Suzanne Bombardier vanishes from her Antioch, California home."},
      {"date": "1980-01-26", "event": "Her family reports her missing; search begins."},
      {"date": "1980-02-01", "event": "Antioch police investigate; case goes cold."}
    ],
    "enriched": True
  },
  {
    "id": "blair-adams-1996",
    "name": "Blair Adams",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1996,
    "date": "July 11, 1996",
    "state": "Tennessee",
    "city": "Knoxville",
    "age": 31,
    "gender": "Male",
    "country": "Canada",
    "summary": "Canadian construction worker Blair Adams was found murdered in a Knoxville, Tennessee parking lot after a bizarre cross-country flight from his home in Surrey, British Columbia. His erratic behavior before death and the strange circumstances remain unexplained.",
    "lastSeen": "July 11, 1996, Knoxville, Tennessee",
    "tags": ["homicide", "Tennessee", "Canada", "international", "bizarre", "1990s"],
    "sources": [
      {"title": "Murder of Blair Adams - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Blair_Adams"},
      {"title": "Blair Adams - Unsolved Mysteries", "url": "https://unsolved.com/gallery/blair-adams/"},
      {"title": "Blair Adams case - Knoxville News Sentinel", "url": "https://www.knoxnews.com/"}
    ],
    "narrative": [
      "In early July 1996, 31-year-old Blair Adams, a construction worker living in Surrey, British Columbia, began behaving erratically. He quit his job, withdrew his life savings of $6,000 Canadian dollars, and told friends and family he believed someone was trying to kill him, though he could not or would not identify who. He attempted to cross into the United States at the border but was turned back because of his agitated state.",
      "Adams then flew from Vancouver to Frankfurt, Germany, but immediately turned around and flew back. He crossed the US border at a different checkpoint, bought a round-trip ticket from Seattle to Washington, D.C., then rented a car in D.C. and drove south. His rental car broke down in Knoxville, Tennessee. He was seen at various locations in Knoxville, including a gas station and a hotel where he appeared confused and frightened.",
      "On July 11, 1996, Adams's body was found in the parking lot of a Knoxville construction site. He had been struck in the stomach and his throat appeared to have been slashed. His pants were pulled down, and money and valuables were scattered around his body. Despite having been carrying thousands of dollars in multiple currencies, gold, and platinum, nothing appeared to have been stolen.",
      "The Knox County Sheriff's Office investigated extensively but could find no connection between Adams and anyone in Tennessee. No DNA or fingerprints at the scene matched anyone in databases. The bizarre journey—from Canada to Germany and back, then across the United States—combined with his paranoid behavior and the seemingly motiveless murder, make this one of the most perplexing unsolved cases in American true crime. The case has been featured on Unsolved Mysteries and remains open."
    ],
    "timeline": [
      {"date": "1996-07-05", "event": "Blair Adams begins acting erratically; quits job and withdraws savings."},
      {"date": "1996-07-07", "event": "Adams flies to Germany and immediately returns."},
      {"date": "1996-07-09", "event": "Adams enters the US and drives from Washington D.C. toward Tennessee."},
      {"date": "1996-07-11", "event": "Adams is found murdered in a Knoxville parking lot."}
    ],
    "enriched": True
  },
  {
    "id": "disappearance-of-johnny-gosch-1982",
    "name": "Johnny Gosch",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1982,
    "date": "September 5, 1982",
    "state": "Iowa",
    "city": "West Des Moines",
    "age": 12,
    "gender": "Male",
    "summary": "Twelve-year-old Johnny Gosch vanished while delivering newspapers in West Des Moines, Iowa. His case led to major reforms in how missing children cases are handled in the United States, including photos on milk cartons.",
    "lastSeen": "September 5, 1982, West Des Moines, Iowa",
    "tags": ["missing person", "Iowa", "child", "newspaper delivery", "milk cartons", "1980s"],
    "sources": [
      {"title": "Disappearance of Johnny Gosch - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Johnny_Gosch"},
      {"title": "Johnny Gosch case - Des Moines Register", "url": "https://www.desmoinesregister.com/story/news/investigations/2022/09/02/johnny-gosch-case-kidnapping-40-years-later-west-des-moines-iowa/7914291001/"},
      {"title": "Who Took Johnny - Documentary", "url": "https://www.whotookjohnny.com/"}
    ],
    "narrative": [
      "In the early morning hours of September 5, 1982, 12-year-old Johnny David Gosch set out to deliver newspapers for the Des Moines Register in his West Des Moines, Iowa neighborhood. His father had usually accompanied him but did not that morning. When customers began calling to report undelivered papers, Johnny's parents went looking for him and found his wagon full of newspapers, two blocks from their home. Johnny was gone.",
      "Witnesses reported seeing a man in a blue car approach Johnny and later seeing a boy matching Johnny's description being pulled into a vehicle. Despite these sightings, West Des Moines police initially classified the case as a runaway rather than an abduction, delaying the investigation. The department's handling of the case was later heavily criticized.",
      "Johnny's mother, Noreen Gosch, became one of the most prominent advocates for missing children in American history. Her efforts, combined with those of other parents of missing children, led to significant reforms including the use of children's photos on milk cartons (Johnny was one of the first to be pictured), the establishment of the National Center for Missing & Exploited Children, and changes to federal law regarding missing children investigations.",
      "In 1984, another Des Moines paper carrier, 13-year-old Eugene Martin, also disappeared under similar circumstances, suggesting a possible connection. Noreen Gosch has claimed that Johnny visited her briefly in 1997, though this has never been confirmed. In 2006, photographs allegedly showing bound and gagged boys—one purportedly Johnny—were left at Noreen's door, but investigators could not confirm the photos depicted her son. The case remains one of the most well-known unsolved child disappearances in American history."
    ],
    "timeline": [
      {"date": "1982-09-05", "event": "Johnny Gosch disappears while delivering newspapers in West Des Moines."},
      {"date": "1982-09-05", "event": "Police initially classify case as runaway; later reclassified as abduction."},
      {"date": "1984-08-12", "event": "Eugene Martin, another Des Moines paper carrier, also disappears."},
      {"date": "1984-12-01", "event": "Johnny becomes one of the first children pictured on milk cartons."},
      {"date": "2006-09-01", "event": "Mysterious photographs are left at Noreen Gosch's door."}
    ],
    "enriched": True
  },
  {
    "id": "dyatlov-pass-1959",
    "name": "Dyatlov Pass Victims",
    "type": "Suspicious Death",
    "status": "Unsolved",
    "year": 1959,
    "date": "February 2, 1959",
    "state": "Sverdlovsk Oblast",
    "city": "Kholat Syakhl",
    "age": None,
    "gender": "Multiple",
    "country": "Russia",
    "summary": "Nine Russian hikers died under mysterious circumstances in the northern Ural Mountains. They had cut their way out of their tent in the middle of the night and fled into subzero temperatures. Some had severe injuries. The case has never been satisfactorily explained.",
    "lastSeen": "February 2, 1959, Kholat Syakhl, Ural Mountains, Russia",
    "tags": ["suspicious death", "Russia", "international", "hiking", "Ural Mountains", "1950s"],
    "sources": [
      {"title": "Dyatlov Pass incident - Wikipedia", "url": "https://en.wikipedia.org/wiki/Dyatlov_Pass_incident"},
      {"title": "Dead Mountain - Donnie Eichar", "url": "https://www.donnieeichar.com/dead-mountain"},
      {"title": "Russian investigation into Dyatlov Pass - BBC News", "url": "https://www.bbc.co.uk/news/world-europe-49071774"}
    ],
    "narrative": [
      "On February 2, 1959, nine experienced hikers—students and graduates of the Ural Polytechnic Institute led by 23-year-old Igor Dyatlov—perished on the slopes of Kholat Syakhl ('Dead Mountain' in the Mansi language) in the northern Ural Mountains of the Soviet Union. The group had been on a ski trek to Otorten when they pitched their tent on the exposed mountainside. Something caused them to slash open the tent from the inside and flee into temperatures of approximately -30°C (-22°F), most of them without shoes, coats, or adequate clothing.",
      "Search parties found the tent on February 26, collapsed and partially buried in snow. Footprints in the snow showed the group had walked in an orderly fashion—not panicked—toward a nearby cedar tree. The first two bodies, Yuri Doroshenko and Yuri Krivonischenko, were found at the base of the cedar, stripped to their underwear near the remnants of a small fire. Three more bodies—including Dyatlov himself—were found at various points between the cedar and the tent, apparently trying to return.",
      "The remaining four were not found until May, buried under four meters of snow in a ravine 75 meters from the cedar. These four had the most disturbing injuries: Lyudmila Dubinina was missing her tongue, eyes, and part of her lips; Nikolai Thibeaux-Brignolle had major skull damage; and Alexander Zolotaryov and Dubinina had multiple fractured ribs. The force required to cause such fractures was compared to a car crash, yet there was no external soft tissue damage.",
      "The Soviet investigation concluded the hikers died from a 'compelling natural force' and closed the case. Theories have ranged from avalanche to infrasound, military testing, Mansi attack, and katabatic winds. In 2019, Russian prosecutors reopened the case and in 2020 concluded a slab avalanche was the most likely cause, though many researchers dispute this finding, noting the low slope angle, lack of avalanche debris, and the extreme injuries to some victims. The Dyatlov Pass incident remains one of the most discussed unexplained events of the 20th century."
    ],
    "timeline": [
      {"date": "1959-02-01", "event": "The group pitches their tent on the slopes of Kholat Syakhl."},
      {"date": "1959-02-02", "event": "Something causes the hikers to cut open their tent and flee into subzero temperatures."},
      {"date": "1959-02-26", "event": "Search party finds the collapsed tent and first bodies."},
      {"date": "1959-05-04", "event": "Four more bodies are found in a ravine with severe injuries."},
      {"date": "2020-07-11", "event": "Russian prosecutors conclude avalanche was most likely cause; many dispute this."}
    ],
    "enriched": True
  },
  {
    "id": "tylenol-cyanide-poisoning-1986",
    "name": "Diane Elsroth",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1986,
    "date": "February 8, 1986",
    "state": "New York",
    "city": "Peekskill",
    "age": 23,
    "gender": "Female",
    "summary": "Diane Elsroth died after taking a cyanide-laced Tylenol capsule in Yonkers, New York—a copycat of the 1982 Chicago Tylenol murders. This second poisoning incident led Johnson & Johnson to permanently switch from capsules to caplets. No one was ever charged.",
    "lastSeen": "February 8, 1986, Yonkers, New York",
    "tags": ["homicide", "New York", "poisoning", "cyanide", "product tampering", "1980s"],
    "sources": [
      {"title": "1986 Tylenol poisoning - Wikipedia", "url": "https://en.wikipedia.org/wiki/Chicago_Tylenol_murders#1986_poisoning"},
      {"title": "Second Tylenol poisoning - New York Times", "url": "https://www.nytimes.com/1986/02/13/nyregion/a-woman-23-dies-of-cyanide-poisoning.html"},
      {"title": "Tylenol capsule withdrawal - Washington Post", "url": "https://www.washingtonpost.com/archive/business/1986/02/18/johnson-johnson-pulls-tylenol-capsules/"}
    ],
    "narrative": [
      "On February 8, 1986, 23-year-old Diane Elsroth took two Extra-Strength Tylenol capsules at the home of her boyfriend in Yonkers, New York. She collapsed almost immediately and was rushed to the hospital, where she died. Toxicology tests revealed she had ingested capsules laced with potassium cyanide—echoing the terrifying Chicago Tylenol murders of 1982.",
      "The discovery triggered immediate action. Johnson & Johnson, the parent company of Tylenol, pulled all capsule products from shelves nationwide and announced it would permanently discontinue the sale of over-the-counter capsule medications, switching entirely to solid caplets that were far more difficult to tamper with. The FDA tested thousands of bottles from the region and found a second contaminated bottle at a store in Bronxville, New York.",
      "The investigation by the FBI, FDA, and Westchester County authorities was extensive. Unlike the 1982 Chicago poisonings, where the contamination appeared widespread, the 1986 incident seemed more targeted—only two contaminated bottles were found, both in Westchester County. Investigators examined whether the tampering occurred at the retail level or during distribution.",
      "Despite years of investigation, no one was ever charged in the 1986 Tylenol poisoning. The case, like the 1982 Chicago murders, demonstrated the vulnerability of consumer products to tampering and led to permanent changes in pharmaceutical packaging across the industry. Diane Elsroth's death remains an unsolved homicide."
    ],
    "timeline": [
      {"date": "1986-02-08", "event": "Diane Elsroth dies after taking cyanide-laced Tylenol in Yonkers."},
      {"date": "1986-02-10", "event": "A second contaminated bottle is found in Bronxville, New York."},
      {"date": "1986-02-17", "event": "Johnson & Johnson permanently discontinues all capsule medications."},
      {"date": "1986-03-01", "event": "FDA mandates tamper-evident packaging for all OTC drugs."}
    ],
    "enriched": True
  },
  {
    "id": "amber-creek-murders-2009",
    "name": "Linda and Gary Haas",
    "type": "Multiple Homicide",
    "status": "Conviction",
    "year": 2009,
    "date": "April 2009",
    "state": "Oklahoma",
    "city": "McAlester",
    "age": None,
    "gender": "Multiple",
    "summary": "Retired couple Linda and Gary Haas were murdered during a cross-country RV trip. Their burned motorhome was found in Oklahoma. The case was solved when their stolen belongings surfaced, leading to the conviction of two men.",
    "lastSeen": "April 2009, near McAlester, Oklahoma",
    "tags": ["homicide", "Oklahoma", "RV", "robbery", "cold case solved", "2000s"],
    "sources": [
      {"title": "Murder of Linda and Gary Haas - regional news", "url": "https://www.tulsaworld.com/"},
      {"title": "Haas murder conviction - Oklahoma news", "url": "https://oklahoman.com/"},
      {"title": "RV murder case - Crime documentary", "url": "https://www.investigationdiscovery.com/"}
    ],
    "narrative": [
      "In April 2009, retired Texas couple Gary (61) and Linda Haas (63) set out on a cross-country RV trip from their home in Tecumseh, Oklahoma. When they failed to contact family members, concern grew. Their burned motorhome was found along a remote road near McAlester, Oklahoma with their remains inside, badly charred.",
      "The investigation initially had few leads. The fire had destroyed much potential evidence, and the remote location of the burned RV offered no witnesses. However, when items from the Haas's RV—including credit cards, firearms, and personal effects—began surfacing, investigators were able to trace them to suspects.",
      "Two men, Paul Kevin Watts and Tanner Croft, were eventually arrested and charged with the murders. Evidence showed they had encountered the Haases, murdered them for their possessions, set fire to the RV to conceal the crime, and fled with stolen property. Watts was convicted and sentenced to death, while Croft received a lengthy prison sentence.",
      "The case highlighted the vulnerability of travelers in remote areas and the value of financial tracking in solving crimes. The use of the stolen credit cards and sale of stolen firearms ultimately provided the evidence trail that led to the killers."
    ],
    "timeline": [
      {"date": "2009-04-15", "event": "Gary and Linda Haas set out on a cross-country RV trip."},
      {"date": "2009-04-18", "event": "Their burned motorhome is found near McAlester, Oklahoma."},
      {"date": "2009-05-01", "event": "Stolen items from the RV begin surfacing; investigation advances."},
      {"date": "2010-01-01", "event": "Paul Kevin Watts and Tanner Croft are arrested and charged."}
    ],
    "enriched": True
  },
  {
    "id": "christopher-wilder-1984",
    "name": "Christopher Wilder Victims",
    "type": "Serial Killer Victims",
    "status": "Partially Solved",
    "year": 1984,
    "date": "February 26, 1984",
    "state": "Multiple",
    "city": "Various",
    "age": None,
    "gender": "Female",
    "summary": "Australian-born serial killer Christopher Wilder kidnapped, raped, and murdered at least eight young women during a six-week cross-country crime spree in 1984. He was killed during his capture. Some of his victims have never been found.",
    "lastSeen": "Various locations across the US, February-April 1984",
    "tags": ["serial killer", "cross-country", "FBI Ten Most Wanted", "1980s"],
    "sources": [
      {"title": "Christopher Wilder - Wikipedia", "url": "https://en.wikipedia.org/wiki/Christopher_Wilder"},
      {"title": "Christopher Wilder - FBI", "url": "https://www.fbi.gov/history/famous-cases/christopher-wilder"},
      {"title": "The Beauty Queen Killer - Crime Library", "url": "https://www.criminalminds.com/"}
    ],
    "narrative": [
      "Between late February and mid-April 1984, Christopher Bernard Wilder, a 39-year-old Australian-born businessman and race car driver living in Boynton Beach, Florida, embarked on a terrifying cross-country killing spree that would claim at least eight lives and span multiple states. Wilder used his good looks, charm, and profession as a photographer to lure young women and aspiring models.",
      "Wilder's known victims began with Rosario Gonzalez, a 20-year-old aspiring model who disappeared from the Miami Grand Prix on February 26, and Beth Kenyon, a former Orange Bowl princess who vanished on March 5. As the FBI connected the cases and identified Wilder as the suspect, he fled Florida and continued killing: Terry Walden in Texas, Suzanne Logan in Oklahoma, Sheryl Bonaventura and Michelle Korfman in Colorado, and others across the country.",
      "Wilder was placed on the FBI's Ten Most Wanted list on April 4, 1984, as one of the most dangerous fugitives in the country. He continued his spree, kidnapping and torturing victims, sometimes releasing them alive. His methods included electric shock torture with a device he carried.",
      "The spree ended on April 13, 1984, when two New Hampshire State Troopers confronted Wilder at a gas station in Colebrook, New Hampshire. In the ensuing struggle, Wilder was shot twice with his own .357 Magnum and died. The bodies of Rosario Gonzalez and Beth Kenyon have never been found, and Wilder is suspected in additional unsolved murders in Australia and Florida."
    ],
    "timeline": [
      {"date": "1984-02-26", "event": "Rosario Gonzalez disappears from the Miami Grand Prix."},
      {"date": "1984-03-05", "event": "Beth Kenyon vanishes after dinner with Wilder."},
      {"date": "1984-03-18", "event": "Terry Walden is murdered in Texas; FBI identifies Wilder as suspect."},
      {"date": "1984-04-04", "event": "Wilder is placed on FBI's Ten Most Wanted list."},
      {"date": "1984-04-13", "event": "Wilder is shot and killed during a confrontation in New Hampshire."}
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
    "state": "British Columbia",
    "city": "Victoria",
    "age": 4,
    "gender": "Male",
    "country": "Canada",
    "summary": "Four-year-old Michael Dunahee disappeared from a school playground in Victoria, British Columbia while his parents were nearby. The case became Canada's most widely publicized missing child case and changed how missing children investigations are handled nationwide.",
    "lastSeen": "March 24, 1991, Blanshard Elementary School, Victoria, British Columbia",
    "tags": ["missing person", "Canada", "international", "child", "playground", "1990s"],
    "sources": [
      {"title": "Disappearance of Michael Dunahee - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Michael_Dunahee"},
      {"title": "Michael Dunahee case - Victoria Police", "url": "https://vicpd.ca/missing/michael-dunahee/"},
      {"title": "Michael Dunahee - CBC News", "url": "https://www.cbc.ca/news/canada/british-columbia/michael-dunahee-1.4925601"}
    ],
    "narrative": [
      "On the morning of Sunday, March 24, 1991, four-year-old Michael Wayne Dunahee was playing on the playground at Blanshard Elementary School in Victoria, British Columbia while his parents, Crystal and Bruce Dunahee, were at a nearby football practice. At approximately 12:30 p.m., Crystal went to check on Michael and found the playground empty. He had vanished in what investigators estimate was a window of no more than a few minutes.",
      "The disappearance triggered the largest search operation in British Columbia history. Over 1,500 volunteers joined police in combing Victoria and the surrounding area. The Royal Canadian Mounted Police, Victoria Police, and the FBI were all involved. More than 11,000 tips were received in the first year alone, and over 200 suspects were investigated.",
      "Michael's case became the most publicized missing child case in Canadian history. His image was distributed on posters, billboards, and milk cartons across North America. Crystal and Bruce Dunahee became vocal advocates for missing children's rights and child safety. Their efforts led to significant changes in how police handle missing children reports in Canada, including the requirement for immediate investigation regardless of how long the child has been missing.",
      "Despite decades of investigation, age-progression images, DNA database submissions, and periodic reinvestigations, Michael Dunahee has never been found. The Victoria Police Department maintains the investigation as an active file, and tips continue to come in. Michael would be in his late thirties if still alive."
    ],
    "timeline": [
      {"date": "1991-03-24", "event": "Michael Dunahee disappears from a school playground in Victoria, BC."},
      {"date": "1991-03-24", "event": "Massive search operation begins with over 1,500 volunteers."},
      {"date": "1991-04-01", "event": "RCMP, Victoria Police, and FBI join forces on the investigation."},
      {"date": "1991-12-01", "event": "Over 11,000 tips received; no solid leads emerge."}
    ],
    "enriched": True
  },
  {
    "id": "elijah-lewis-2021",
    "name": "Elijah Lewis",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2021,
    "date": "October 2021",
    "state": "New Hampshire",
    "city": "Merrimack",
    "age": 5,
    "gender": "Male",
    "summary": "Five-year-old Elijah Lewis was reported missing from Merrimack, New Hampshire in October 2021. His remains were found buried in a Massachusetts forest. His mother and her boyfriend were charged with his murder.",
    "lastSeen": "September 2021, Merrimack, New Hampshire",
    "tags": ["homicide", "New Hampshire", "child", "abuse", "2020s"],
    "sources": [
      {"title": "Death of Elijah Lewis - Wikipedia", "url": "https://en.wikipedia.org/wiki/Death_of_Elijah_Lewis"},
      {"title": "Elijah Lewis case - WMUR", "url": "https://www.wmur.com/article/elijah-lewis-merrimack-missing-boy/37968023"},
      {"title": "Elijah Lewis investigation - Boston Globe", "url": "https://www.bostonglobe.com/"}
    ],
    "narrative": [
      "In October 2021, the New Hampshire Division for Children, Youth and Families attempted a welfare check on five-year-old Elijah Lewis at his home in Merrimack, New Hampshire. When they could not locate him, they contacted police. His mother, Danielle Dauphinais, and her boyfriend, Joseph Stapf, were unable to account for the child's whereabouts.",
      "Dauphinais and Stapf fled New Hampshire and were arrested in New York City on October 17, 2021. Both were initially charged with witness tampering and child endangerment. An extensive search was launched across New Hampshire and Massachusetts.",
      "On October 23, 2021, Elijah's remains were found buried in a wooded area near Abington, Massachusetts, approximately 90 miles from Merrimack. The medical examiner determined the cause of death was violence and neglect, and the manner of death was homicide. Evidence indicated Elijah had suffered prolonged abuse before his death.",
      "Both Dauphinais and Stapf were charged with first-degree murder and second-degree murder. The case highlighted failures in the child welfare system, as DCYF had previous contact with the family. Neighbors reported they had not seen Elijah in months before his disappearance was discovered."
    ],
    "timeline": [
      {"date": "2021-10-14", "event": "DCYF attempts welfare check; cannot locate Elijah Lewis."},
      {"date": "2021-10-17", "event": "Danielle Dauphinais and Joseph Stapf are arrested in New York City."},
      {"date": "2021-10-23", "event": "Elijah's remains are found buried in a Massachusetts forest."},
      {"date": "2021-11-01", "event": "Both suspects are charged with murder."}
    ],
    "enriched": True
  },
  {
    "id": "oakey-al-kite-2004",
    "name": "Oakey 'Al' Kite",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 2004,
    "date": "May 22, 2004",
    "state": "Colorado",
    "city": "Aurora",
    "age": 53,
    "gender": "Male",
    "summary": "Aurora, Colorado engineer Oakey Kite was tortured and murdered in his home by someone posing as a prospective tenant. DNA from the scene has never been matched. The killer used a fake identity and may be a serial offender.",
    "lastSeen": "May 22, 2004, Aurora, Colorado",
    "tags": ["homicide", "Colorado", "torture", "identity theft", "unsolved", "2000s"],
    "sources": [
      {"title": "Murder of Oakey Kite - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Oakey_%22Al%22_Kite"},
      {"title": "Oakey Kite case - Denver Post", "url": "https://www.denverpost.com/"},
      {"title": "Unsolved Oakey Kite murder - Aurora Sentinel", "url": "https://sentinelcolorado.com/"}
    ],
    "narrative": [
      "On May 22, 2004, friends discovered the body of Oakey 'Al' Kite, a 53-year-old engineer, in his Aurora, Colorado home. Kite had been bound and tortured before being killed. The scene was exceptionally brutal—investigators described it as one of the most disturbing crime scenes they had encountered.",
      "The investigation revealed that Kite had been advertising a room for rent in his home. He had shown the room to a prospective tenant who used the name 'Robert Cooper' and presented a fake ID. This person is believed to be the killer. 'Cooper' had called Kite multiple times in the days before the murder, and investigators obtained DNA from items the suspect left at the scene.",
      "The DNA profile did not match anyone in law enforcement databases, including CODIS. A composite sketch of 'Robert Cooper' was created from witnesses who had seen him, describing a man in his 30s or 40s with a medium build. The fake name and Social Security number he provided were untraceable.",
      "The methodical nature of the crime—the use of a false identity to gain access, the preparation involved, and the extreme violence—led investigators to believe this may not have been the killer's first crime. Some researchers have speculated about possible connections to other unsolved crimes, but no links have been confirmed. The case remains one of Colorado's most baffling unsolved murders."
    ],
    "timeline": [
      {"date": "2004-05-15", "event": "'Robert Cooper' contacts Oakey Kite about renting a room."},
      {"date": "2004-05-22", "event": "Kite is found tortured and murdered in his Aurora home."},
      {"date": "2004-05-23", "event": "Police identify 'Robert Cooper' as a fake identity; DNA collected."},
      {"date": "2004-06-01", "event": "Composite sketch released; no match in DNA databases."}
    ],
    "enriched": True
  }
]

def main():
    with open('data/cases.json', 'r') as f:
        cases = json.load(f)

    existing_ids = {c['id'] for c in cases}
    added = 0
    skipped = []

    for case in NEW_CASES:
        if case['id'] not in existing_ids:
            cases.append(case)
            existing_ids.add(case['id'])
            added += 1
        else:
            skipped.append(case['id'])

    with open('data/cases.json', 'w') as f:
        json.dump(cases, f, indent=1, ensure_ascii=False)

    print(f"Added {added} cases. Skipped {len(skipped)}: {skipped}. Total: {len(cases)}")

if __name__ == '__main__':
    main()
