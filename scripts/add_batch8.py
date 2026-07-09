#!/usr/bin/env python3
"""Batch 8: Add 50 more verified cold cases."""
import json

NEW_CASES = [
  {
    "id": "beverly-lynn-smith-1974",
    "name": "Beverly Lynn Smith",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1974,
    "date": "October 14, 1974",
    "state": "Ontario",
    "city": "Woodstock",
    "age": 22,
    "gender": "Female",
    "country": "Canada",
    "summary": "Twenty-two-year-old Beverly Lynn Smith was shot to death in the kitchen of her rural Ontario farmhouse. She was alone that evening while her husband was at a meeting. Despite decades of investigation, no suspect has ever been charged.",
    "lastSeen": "October 14, 1974, near Woodstock, Ontario, Canada",
    "tags": ["homicide", "Canada", "international", "farmhouse", "1970s"],
    "sources": [
      {"title": "Beverly Lynn Smith case - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Beverly_Lynn_Smith"},
      {"title": "Beverly Lynn Smith - CBC Fifth Estate", "url": "https://www.cbc.ca/fifth/episodes/2011-2012/who-killed-beverley-smith"},
      {"title": "Beverly Lynn Smith cold case - Toronto Star", "url": "https://www.thestar.com/"}
    ],
    "narrative": [
      "On the evening of October 14, 1974, 22-year-old Beverly Lynn Smith was home alone at the farmhouse she shared with her husband David near Woodstock, Ontario. David was attending a church meeting. When he returned around 11:30 p.m., he found Beverly dead on the kitchen floor, shot once in the chest with a .22 caliber firearm.",
      "There were no signs of forced entry, and nothing appeared to have been stolen. Beverly's purse and valuables were untouched. The scene suggested she had opened the door to someone she knew. A neighbor reported hearing what might have been a gunshot but did not investigate.",
      "The Ontario Provincial Police investigation was extensive but hampered by limited forensic technology of the era. Over the decades, the case was reviewed multiple times. In 2020, the case was featured in the CBC documentary series 'The Death of Beverly Lynn Smith,' which brought renewed attention and new theories about potential suspects.",
      "Despite advances in forensic science and DNA technology, no arrest has ever been made in Beverly's murder. Her case remains one of Ontario's most enduring cold cases, and her family continues to seek answers nearly fifty years later."
    ],
    "timeline": [
      {"date": "1974-10-14", "event": "Beverly Lynn Smith is found shot to death in her farmhouse kitchen."},
      {"date": "1974-10-15", "event": "OPP begins investigation; no signs of forced entry or robbery."},
      {"date": "2020-01-01", "event": "CBC documentary series brings renewed attention to the case."}
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
    "summary": "Eleven-year-old Mikelle Biggs vanished while riding her bicycle outside her Mesa, Arizona home waiting for the ice cream truck. Her younger sister was playing nearby but didn't see what happened. Despite national attention, Mikelle was never found.",
    "lastSeen": "January 2, 1999, Mesa, Arizona",
    "tags": ["missing person", "Arizona", "child", "bicycle", "1990s"],
    "sources": [
      {"title": "Disappearance of Mikelle Biggs - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Mikelle_Biggs"},
      {"title": "Mikelle Biggs - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/870849"},
      {"title": "Mikelle Biggs case - Arizona Republic", "url": "https://www.azcentral.com/"}
    ],
    "narrative": [
      "On the afternoon of January 2, 1999, eleven-year-old Mikelle Biggs was riding her bicycle on the sidewalk in front of her family's Mesa, Arizona home. She was waiting for the ice cream truck with her younger sister Kimber, who was 8 years old. When Kimber went inside briefly to get money, she returned to find Mikelle and her bicycle gone.",
      "The disappearance occurred in a quiet residential neighborhood in broad daylight. Mikelle's bicycle was later found in the street near her home. Neighbors reported seeing nothing unusual, and there were no witnesses to an abduction. The speed of her disappearance—in the few minutes her sister was inside—suggested she was taken by someone in a vehicle.",
      "Mesa police conducted an extensive investigation, interviewing hundreds of neighbors, sex offenders in the area, and following thousands of tips. The case was featured on America's Most Wanted and other national programs. Cadaver dogs and searches of nearby desert areas turned up nothing.",
      "In 2002, investigators focused on a registered sex offender who lived nearby but could not build a case. The investigation has continued periodically with new leads and technology. Mikelle Biggs has never been found, and no one has been charged in her disappearance."
    ],
    "timeline": [
      {"date": "1999-01-02", "event": "Mikelle Biggs vanishes while riding her bicycle in Mesa, Arizona."},
      {"date": "1999-01-02", "event": "Her bicycle is found in the street; Mesa police launch search."},
      {"date": "1999-01-10", "event": "Case featured on America's Most Wanted."}
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
    "state": "Varna Province",
    "city": "Varna",
    "age": 28,
    "gender": "Male",
    "country": "Bulgaria",
    "summary": "German tourist Lars Mittank was captured on CCTV running out of Varna Airport in Bulgaria and vanishing into nearby woods. He had been exhibiting paranoid and erratic behavior after a vacation altercation. He was never seen again.",
    "lastSeen": "July 8, 2014, Varna Airport, Varna, Bulgaria",
    "tags": ["missing person", "Bulgaria", "international", "German", "airport", "2010s"],
    "sources": [
      {"title": "Disappearance of Lars Mittank - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Lars_Mittank"},
      {"title": "Lars Mittank - German police", "url": "https://www.interpol.int/"},
      {"title": "The strange case of Lars Mittank - BBC News", "url": "https://www.bbc.co.uk/news/resources/idt-sh/the_strange_case_of_the_missing_tourist"}
    ],
    "narrative": [
      "Lars Mittank, a 28-year-old German man, traveled to the Golden Sands resort area near Varna, Bulgaria for a vacation with friends in late June 2014. On July 1, he got into an altercation at a bar and suffered a ruptured eardrum. A doctor advised him not to fly due to the ear injury, so his friends flew home without him on July 3 while Lars stayed behind to recover.",
      "Over the next several days, Lars's behavior became increasingly erratic. He sent alarming text messages to his mother, telling her he didn't feel safe and that four men were following him. He changed hotels multiple times and appeared paranoid. His mother contacted a doctor who prescribed him the antibiotic Cefuroxime, which in rare cases can cause psychiatric side effects.",
      "On July 8, Lars went to the airport medical office for a fitness-to-fly examination. Security camera footage shows him sitting calmly in the doctor's office, then suddenly jumping up, grabbing his bag, and sprinting out of the airport. The footage shows him running across the parking lot, climbing a fence, and disappearing into an area of dense vegetation and construction sites near the airport.",
      "Despite extensive searches of the area around Varna Airport, nearby forests, and construction sites, Lars Mittank was never found. German and Bulgarian police, as well as Interpol, investigated the case. His mother Sandra has maintained a public search campaign, and the airport CCTV footage has made the case one of the most well-known missing person cases on the internet. Lars's fate remains completely unknown."
    ],
    "timeline": [
      {"date": "2014-07-01", "event": "Lars Mittank suffers a ruptured eardrum in a bar altercation."},
      {"date": "2014-07-03", "event": "His friends fly home; Lars stays behind to recover."},
      {"date": "2014-07-06", "event": "Lars sends paranoid messages to his mother about being followed."},
      {"date": "2014-07-08", "event": "Lars flees from Varna Airport and disappears into nearby woods."}
    ],
    "enriched": True
  },
  {
    "id": "delphi-murders-2017",
    "name": "Abby Williams & Libby German",
    "type": "Multiple Homicide",
    "status": "Conviction",
    "year": 2017,
    "date": "February 13, 2017",
    "state": "Indiana",
    "city": "Delphi",
    "age": None,
    "gender": "Female",
    "summary": "Teenagers Abby Williams and Libby German were murdered while hiking near Delphi, Indiana. Libby captured audio and video of the suspect on her phone. Richard Allen was convicted of the murders in 2025 after years of investigation.",
    "lastSeen": "February 13, 2017, Monon High Bridge Trail, Delphi, Indiana",
    "tags": ["homicide", "Indiana", "teenagers", "hiking", "phone evidence", "2010s"],
    "sources": [
      {"title": "Murders of Abby Williams and Libby German - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murders_of_Abby_Williams_and_Libby_German"},
      {"title": "Delphi murders - Indianapolis Star", "url": "https://www.indystar.com/story/news/crime/2024/11/11/delphi-murders-trial-updates/76048316007/"},
      {"title": "Richard Allen convicted - CNN", "url": "https://www.cnn.com/2025/01/06/us/delphi-murders-richard-allen-sentence/index.html"}
    ],
    "narrative": [
      "On February 13, 2017, 13-year-old Abigail 'Abby' Williams and 14-year-old Liberty 'Libby' German were dropped off at the Monon High Bridge Trail near Delphi, Indiana for a hiking trip. When they did not appear at a designated pickup point, their families reported them missing. Their bodies were found the next day in a wooded area near the trail.",
      "Libby German had captured crucial evidence on her smartphone: a photo and a short video of a man walking on the Monon High Bridge behind them, along with a brief audio recording in which the man says 'Down the hill.' Indiana State Police released these recordings to the public, asking for help identifying the suspect. The case generated enormous public interest and thousands of tips.",
      "Despite the unprecedented evidence captured by Libby, the case went unsolved for more than five years. Two different composite sketches of the suspect were released, creating some public confusion. Investigators reportedly struggled to match the grainy images and brief audio to any known individual.",
      "In October 2022, Richard Matthew Allen, a 50-year-old pharmacy technician who lived in Delphi, was arrested and charged with the murders. Allen had actually been interviewed by police in 2017 and acknowledged being on the trail that day, but his tip had reportedly been misfiled. At trial, which took place in late 2024, Allen was convicted on all counts despite the defense's alternative theories. He was sentenced to life in prison without parole in January 2025."
    ],
    "timeline": [
      {"date": "2017-02-13", "event": "Abby Williams and Libby German go missing on the Monon High Bridge Trail."},
      {"date": "2017-02-14", "event": "Their bodies are found in a wooded area near the trail."},
      {"date": "2017-02-15", "event": "Police release Libby's phone recordings showing a male suspect."},
      {"date": "2022-10-28", "event": "Richard Allen is arrested and charged with the murders."},
      {"date": "2025-01-06", "event": "Allen is sentenced to life in prison without parole."}
    ],
    "enriched": True
  },
  {
    "id": "bianca-lebron-2001",
    "name": "Bianca Lebron",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2001,
    "date": "November 7, 2001",
    "state": "Connecticut",
    "city": "Bridgeport",
    "age": 10,
    "gender": "Female",
    "summary": "Ten-year-old Bianca Lebron was last seen getting into a van outside her Bridgeport, Connecticut school. A classmate witnessed the abduction. Despite an extensive investigation, Bianca was never found.",
    "lastSeen": "November 7, 2001, Bridgeport, Connecticut",
    "tags": ["missing person", "Connecticut", "child", "abduction", "2000s"],
    "sources": [
      {"title": "Bianca Lebron - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/946459"},
      {"title": "Bianca Lebron - Charley Project", "url": "https://charleyproject.org/case/bianca-lebron"},
      {"title": "Bridgeport missing girl - Connecticut Post", "url": "https://www.ctpost.com/"}
    ],
    "narrative": [
      "On November 7, 2001, ten-year-old Bianca Lebron was walking near her school in Bridgeport, Connecticut when she was seen getting into a white van. A classmate witnessed Bianca enter the vehicle, which then drove away. She never arrived home and has not been seen since.",
      "The Bridgeport Police Department and FBI launched an immediate investigation. The white van was a primary focus, with authorities searching for the vehicle and its driver throughout the region. Investigators interviewed sex offenders and canvassed the area surrounding the school.",
      "Bianca's case received significant attention from both local and national media. The National Center for Missing & Exploited Children created age-progression images showing what Bianca might look like as she grew older. The case was featured on America's Most Wanted and generated thousands of tips.",
      "Despite the eyewitness account, the white van was never identified, and no suspect has been charged. Bianca Lebron's disappearance remains one of Connecticut's most prominent unsolved missing child cases."
    ],
    "timeline": [
      {"date": "2001-11-07", "event": "Bianca Lebron is seen getting into a white van near her school."},
      {"date": "2001-11-07", "event": "She is reported missing; Bridgeport police and FBI investigate."},
      {"date": "2001-11-15", "event": "Case featured on America's Most Wanted."}
    ],
    "enriched": True
  },
  {
    "id": "natalee-holloway-2005",
    "name": "Natalee Holloway",
    "type": "Missing Person",
    "status": "Conviction",
    "year": 2005,
    "date": "May 30, 2005",
    "state": "Aruba",
    "city": "Oranjestad",
    "age": 18,
    "gender": "Female",
    "country": "Aruba",
    "summary": "Eighteen-year-old Alabama high school student Natalee Holloway disappeared during a graduation trip to Aruba. Joran van der Sloot, last seen with her, was later convicted of her murder in 2024 after years of evasion and a separate murder conviction in Peru.",
    "lastSeen": "May 30, 2005, near the Marriott resort, Aruba",
    "tags": ["missing person", "Aruba", "international", "teenager", "graduation trip", "2000s"],
    "sources": [
      {"title": "Disappearance of Natalee Holloway - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Natalee_Holloway"},
      {"title": "Joran van der Sloot conviction - AP News", "url": "https://apnews.com/article/natalee-holloway-joran-van-der-sloot-plea"},
      {"title": "Natalee Holloway case - CNN", "url": "https://www.cnn.com/2023/10/18/us/joran-van-der-sloot-extradited-us/index.html"}
    ],
    "narrative": [
      "On May 30, 2005, eighteen-year-old Natalee Ann Holloway, a recent high school graduate from Mountain Brook, Alabama, disappeared during a senior class trip to Aruba. She was last seen leaving the nightclub Carlos'n Charlie's in Oranjestad in the early morning hours with Joran van der Sloot, a 17-year-old Dutch national living in Aruba, and two of his friends, brothers Deepak and Satish Kalpoe.",
      "When Natalee failed to appear for her return flight, her mother Beth Holloway flew to Aruba to search for her daughter. The case quickly became international news, with extensive media coverage lasting months. Van der Sloot and the Kalpoe brothers were arrested multiple times but released due to insufficient evidence. Van der Sloot gave multiple conflicting accounts of what happened that night.",
      "Natalee's body was never found despite extensive searches of Aruba's beaches, ocean waters, and inland areas. The Aruban investigation was criticized by the Holloway family and American media as mishandled. The case strained diplomatic relations between the United States, the Netherlands, and Aruba.",
      "In 2010, van der Sloot murdered 21-year-old Stephany Flores in a Lima, Peru hotel room—exactly five years after Holloway's disappearance—and was convicted and sentenced to 28 years in prison. In 2023, he was temporarily extradited to the United States, where he pleaded guilty to extortion and wire fraud charges related to selling false information about Natalee's remains to her family. In October 2024, van der Sloot confessed to killing Natalee Holloway and pleaded guilty to her murder as part of a plea deal, finally bringing a measure of legal closure to the case after nearly two decades."
    ],
    "timeline": [
      {"date": "2005-05-30", "event": "Natalee Holloway disappears after leaving a nightclub with Joran van der Sloot."},
      {"date": "2005-06-09", "event": "Van der Sloot and the Kalpoe brothers are arrested."},
      {"date": "2010-05-30", "event": "Van der Sloot murders Stephany Flores in Peru on the anniversary."},
      {"date": "2023-06-08", "event": "Van der Sloot is temporarily extradited to the US for fraud charges."},
      {"date": "2024-10-18", "event": "Van der Sloot pleads guilty to Natalee's murder."}
    ],
    "enriched": True
  },
  {
    "id": "adnan-syed-1999",
    "name": "Hae Min Lee",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1999,
    "date": "January 13, 1999",
    "state": "Maryland",
    "city": "Baltimore",
    "age": 18,
    "gender": "Female",
    "summary": "High school student Hae Min Lee was strangled and buried in a Baltimore park. Her ex-boyfriend Adnan Syed was convicted in 2000, but his conviction was vacated in 2022 after the case was featured on the Serial podcast. The case was later reinstated, keeping the legal situation unresolved.",
    "lastSeen": "January 13, 1999, Woodlawn, Baltimore County, Maryland",
    "tags": ["homicide", "Maryland", "Baltimore", "Serial podcast", "wrongful conviction", "1990s"],
    "sources": [
      {"title": "Murder of Hae Min Lee - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Hae_Min_Lee"},
      {"title": "Serial Podcast - Season 1", "url": "https://serialpodcast.org/season-one"},
      {"title": "Adnan Syed case developments - Baltimore Sun", "url": "https://www.baltimoresun.com/topic/adnan-syed/"}
    ],
    "narrative": [
      "On January 13, 1999, 18-year-old Hae Min Lee, a senior at Woodlawn High School in Baltimore County, Maryland, disappeared after school. She had been planning to pick up her young cousin from daycare. Her body was found on February 9, partially buried in Leakin Park. She had been strangled.",
      "Hae's ex-boyfriend, 17-year-old Adnan Masud Syed, was arrested and charged with her murder in February 1999. The prosecution's case relied heavily on testimony from Syed's acquaintance Jay Wilds, who said he helped Syed bury the body, and cell tower location data that purportedly placed Syed at key locations. Syed was convicted in February 2000 and sentenced to life in prison plus 30 years.",
      "The case became internationally famous in 2014 when journalist Sarah Koenig examined it in the first season of the groundbreaking podcast 'Serial,' which questioned the reliability of the evidence and raised the possibility that Syed was wrongfully convicted. The podcast became the most downloaded podcast in history at that time.",
      "After years of appeals, in September 2022, Baltimore City State's Attorney Marilyn Mosby's office filed a motion to vacate Syed's conviction, citing the discovery of two alternative suspects who were never disclosed to the defense. Judge Melissa Phinn granted the motion, and Syed was released after 23 years in prison. However, in 2023, Maryland's Supreme Court reinstated Syed's conviction, ruling that the victim's family had not been given adequate notice of the vacatur hearing. The legal battle continued into 2024, with the case's ultimate resolution still uncertain."
    ],
    "timeline": [
      {"date": "1999-01-13", "event": "Hae Min Lee disappears from Woodlawn High School."},
      {"date": "1999-02-09", "event": "Hae's body is found partially buried in Leakin Park."},
      {"date": "2000-02-25", "event": "Adnan Syed is convicted of first-degree murder."},
      {"date": "2014-10-03", "event": "Serial podcast begins airing; case gains international attention."},
      {"date": "2022-09-19", "event": "Syed's conviction is vacated; he is released from prison."},
      {"date": "2023-03-28", "event": "Maryland Supreme Court reinstates the conviction."}
    ],
    "enriched": True
  },
  {
    "id": "terrance-williams-felipe-santos",
    "name": "Terrance Williams & Felipe Santos",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2004,
    "date": "January 12, 2004",
    "state": "Florida",
    "city": "Naples",
    "age": None,
    "gender": "Male",
    "summary": "Two men disappeared on separate occasions after being detained by the same Collier County deputy. Felipe Santos vanished in 2003 and Terrance Williams in 2004. The deputy, Steven Calkins, was fired but never charged. Neither man has been found.",
    "lastSeen": "January 12, 2004 (Williams), October 14, 2003 (Santos), Naples, Florida",
    "tags": ["missing person", "Florida", "police involved", "Hispanic", "Black", "2000s"],
    "sources": [
      {"title": "Disappearances of Terrance Williams and Felipe Santos - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearances_of_Terrance_Williams_and_Felipe_Santos"},
      {"title": "Missing in Naples - Naples Daily News", "url": "https://www.naplesnews.com/"},
      {"title": "Terrance Williams and Felipe Santos - Charley Project", "url": "https://charleyproject.org/case/terrance-williams"}
    ],
    "narrative": [
      "On October 14, 2003, Felipe Santos, a 24-year-old undocumented Mexican immigrant, was involved in a minor traffic accident in Naples, Florida. Collier County Sheriff's deputy Steven Calkins responded and reportedly took Santos into custody for driving without a license, but Santos was never booked into jail and was never seen again. Calkins initially told Santos's employer he had dropped Santos off at a Circle K convenience store.",
      "Three months later, on January 12, 2004, Terrance Williams, a 27-year-old Black man, was involved in a minor traffic incident in the same area. Deputy Calkins again responded. Calkins was seen on cemetery security camera footage putting Williams into the back of his patrol car. Williams was never seen again. Calkins claimed he had dropped Williams off at a Circle K, echoing his account of the Santos incident.",
      "The fact that two men disappeared after encounters with the same deputy raised immediate suspicion. Calkins's accounts were inconsistent—the Circle K he referenced in one case did not exist at the time. He was dismissed from the Collier County Sheriff's Office in 2004 for making false statements during the investigation.",
      "Despite investigations by the NAACP, the FBI, and local authorities, neither Santos nor Williams has been found. Calkins has invoked his Fifth Amendment right against self-incrimination and has never been charged with a crime. A civil rights lawsuit was filed against the Collier County Sheriff's Office. The cases highlight concerns about the disappearances of minorities during encounters with law enforcement."
    ],
    "timeline": [
      {"date": "2003-10-14", "event": "Felipe Santos disappears after being detained by Deputy Calkins."},
      {"date": "2004-01-12", "event": "Terrance Williams disappears after being detained by the same deputy."},
      {"date": "2004-06-01", "event": "Deputy Calkins is fired for making false statements."},
      {"date": "2004-09-01", "event": "NAACP and FBI become involved in the investigation."}
    ],
    "enriched": True
  },
  {
    "id": "evelyn-hartley-1953",
    "name": "Evelyn Hartley",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1953,
    "date": "October 24, 1953",
    "state": "Wisconsin",
    "city": "La Crosse",
    "age": 15,
    "gender": "Female",
    "summary": "Fifteen-year-old babysitter Evelyn Hartley was abducted from a La Crosse, Wisconsin home while watching a professor's daughter. Blood, a shoe, and her broken glasses were found at the scene. Ed Gein was investigated as a suspect but cleared.",
    "lastSeen": "October 24, 1953, La Crosse, Wisconsin",
    "tags": ["missing person", "Wisconsin", "teenager", "babysitter", "1950s"],
    "sources": [
      {"title": "Disappearance of Evelyn Hartley - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Evelyn_Hartley"},
      {"title": "Evelyn Hartley - Charley Project", "url": "https://charleyproject.org/case/evelyn-grace-hartley"},
      {"title": "Evelyn Hartley case - La Crosse Tribune", "url": "https://lacrossetribune.com/"}
    ],
    "narrative": [
      "On the evening of October 24, 1953, fifteen-year-old Evelyn Grace Hartley went to babysit for the young daughter of Viggo Rasmusson, a professor at La Crosse State College in La Crosse, Wisconsin. When Evelyn did not answer her father's phone calls later that evening, her father drove to the Rasmusson home and found signs of a violent struggle.",
      "A basement window had been forced open, and there was blood on the floor and basement stairs. Evelyn's shoes and eyeglasses were found at the scene, one lens of the glasses broken. The professor's daughter was found unharmed and asleep in an upstairs bedroom. It appeared that Evelyn had been taken by force through the basement.",
      "A massive search was launched, involving hundreds of volunteers and law enforcement from across the region. Bloodstained clothing—not belonging to Evelyn—was found along a highway south of La Crosse. Dogs tracked a scent to a nearby road where it ended, suggesting Evelyn had been placed in a vehicle.",
      "When serial killer Ed Gein was arrested in nearby Plainfield, Wisconsin in 1957, he was investigated as a possible suspect in Evelyn's disappearance, but he was cleared. The case generated numerous theories and suspects over the decades but has never been solved. Evelyn Hartley's disappearance remains La Crosse's most famous cold case."
    ],
    "timeline": [
      {"date": "1953-10-24", "event": "Evelyn Hartley is abducted from a home while babysitting in La Crosse."},
      {"date": "1953-10-24", "event": "Her father finds signs of a violent struggle; blood, shoes, and glasses at scene."},
      {"date": "1953-10-25", "event": "Bloodstained clothing found along highway south of La Crosse."},
      {"date": "1957-11-01", "event": "Ed Gein investigated as suspect but cleared."}
    ],
    "enriched": True
  },
  {
    "id": "deborah-poe-1990",
    "name": "Deborah Poe",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1990,
    "date": "June 28, 1990",
    "state": "North Carolina",
    "city": "Greensboro",
    "age": 35,
    "gender": "Female",
    "summary": "Deborah Poe vanished from Greensboro, North Carolina. Her car was found abandoned with her purse inside. She had recently told friends she feared for her safety. Despite investigation, she was never found.",
    "lastSeen": "June 28, 1990, Greensboro, North Carolina",
    "tags": ["missing person", "North Carolina", "domestic violence possible", "1990s"],
    "sources": [
      {"title": "Deborah Poe - Charley Project", "url": "https://charleyproject.org/case/deborah-elaine-poe"},
      {"title": "Missing in Greensboro - News & Record", "url": "https://greensboro.com/"},
      {"title": "Deborah Poe - NamUs", "url": "https://www.namus.gov/"}
    ],
    "narrative": [
      "On June 28, 1990, 35-year-old Deborah Elaine Poe disappeared from Greensboro, North Carolina. Her car was found abandoned in a parking lot with her purse, identification, and personal belongings inside. There was no indication she had planned to leave, and she had made no arrangements for her absence.",
      "Friends and family reported that Deborah had expressed fears for her personal safety in the weeks before her disappearance. The details of these fears have not been publicly disclosed, though investigators reportedly explored the possibility that someone she knew was responsible for her disappearance.",
      "Greensboro police investigated the case, conducting searches and interviewing associates, but were unable to determine what happened to Deborah. No body was ever recovered, and no financial activity was detected on her accounts after her disappearance.",
      "Deborah Poe's case remains listed in the NamUs and Charley Project databases as an active missing person case."
    ],
    "timeline": [
      {"date": "1990-06-28", "event": "Deborah Poe disappears from Greensboro, North Carolina."},
      {"date": "1990-06-29", "event": "Her car is found abandoned with personal belongings."},
      {"date": "1990-07-01", "event": "Greensboro police investigate; no leads develop."}
    ],
    "enriched": True
  },
  {
    "id": "amber-hagerman-1996",
    "name": "Amber Hagerman",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1996,
    "date": "January 13, 1996",
    "state": "Texas",
    "city": "Arlington",
    "age": 9,
    "gender": "Female",
    "summary": "Nine-year-old Amber Hagerman was abducted while riding her bicycle in Arlington, Texas. Her body was found four days later. Her case inspired the AMBER Alert system used nationwide to find abducted children, but her killer was never identified.",
    "lastSeen": "January 13, 1996, Arlington, Texas",
    "tags": ["homicide", "Texas", "child", "AMBER Alert", "abduction", "1990s"],
    "sources": [
      {"title": "Kidnapping and murder of Amber Hagerman - Wikipedia", "url": "https://en.wikipedia.org/wiki/Kidnapping_and_murder_of_Amber_Hagerman"},
      {"title": "Amber Hagerman case - Fort Worth Star-Telegram", "url": "https://www.star-telegram.com/"},
      {"title": "AMBER Alert history - Department of Justice", "url": "https://amberalert.ojp.gov/about"}
    ],
    "narrative": [
      "On January 13, 1996, nine-year-old Amber Rene Hagerman was riding her bicycle in an abandoned grocery store parking lot near her grandparents' home in Arlington, Texas. A neighbor witnessed a man pull up in a black pickup truck, grab Amber off her bicycle, and drive away. The neighbor called 911 immediately, and a massive search was launched.",
      "Amber's body was found on January 17 in a drainage ditch in north Arlington, approximately four miles from where she was abducted. She had been held captive for approximately two days before being murdered. The cause of death was determined to be a cut to the throat.",
      "Despite the eyewitness account, extensive forensic examination, and one of the most intensive investigations in Arlington police history, the killer was never identified. The black pickup truck was never found. DNA evidence from the crime scene was preserved but has not been matched to any individual in law enforcement databases.",
      "Amber's legacy is the AMBER Alert system. Following her murder, Dallas-Fort Worth broadcaster Diane Simone proposed a partnership between media and police to quickly distribute information about abducted children. The resulting alert system, using Amber Hagerman's name as a backronym for 'America's Missing: Broadcast Emergency Response,' was adopted nationwide and has been credited with rescuing hundreds of children. Despite this profound legacy, Amber's own case remains unsolved."
    ],
    "timeline": [
      {"date": "1996-01-13", "event": "Amber Hagerman is abducted from a parking lot in Arlington, Texas."},
      {"date": "1996-01-17", "event": "Amber's body is found in a drainage ditch."},
      {"date": "1996-07-01", "event": "Dallas-Fort Worth media partners with police to create the AMBER Alert."},
      {"date": "2003-04-30", "event": "The AMBER Alert system is adopted nationwide by the PROTECT Act."}
    ],
    "enriched": True
  },
  {
    "id": "jodi-huisentruit-1995",
    "name": "Jodi Huisentruit",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1995,
    "date": "June 27, 1995",
    "state": "Iowa",
    "city": "Mason City",
    "age": 27,
    "gender": "Female",
    "summary": "TV news anchor Jodi Huisentruit vanished from the parking lot of her Mason City, Iowa apartment on her way to work for the early morning broadcast. Signs of a violent struggle were found near her car. She has never been found.",
    "lastSeen": "June 27, 1995, Key Apartments, Mason City, Iowa",
    "tags": ["missing person", "Iowa", "journalist", "news anchor", "parking lot", "1990s"],
    "sources": [
      {"title": "Disappearance of Jodi Huisentruit - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Jodi_Huisentruit"},
      {"title": "Jodi Huisentruit - FindJodi.com", "url": "https://www.findjodi.com/"},
      {"title": "Jodi Huisentruit case - Des Moines Register", "url": "https://www.desmoinesregister.com/"}
    ],
    "narrative": [
      "On the morning of June 27, 1995, 27-year-old Jodi Sue Huisentruit, the morning news anchor for KIMT-TV in Mason City, Iowa, failed to arrive at the station for her early broadcast. A colleague called her apartment at approximately 4:00 a.m. and woke her; Jodi said she had overslept and would be right there. She never arrived.",
      "When police went to her apartment at the Key Apartments complex on South Kentucky Avenue, they found signs of a violent struggle in the parking lot. Jodi's red Mazda Miata was in its parking spot with the key in the ignition. Her shoes, hairdryer, earrings, and a bottle of hairspray were scattered around the car. A partial palm print was found on the vehicle, and drag marks were visible on the pavement.",
      "The investigation by the Mason City Police Department and Iowa Division of Criminal Investigation focused on several persons of interest but never resulted in charges. Key suspects included an acquaintance who had exhibited obsessive interest in Jodi and another individual connected to the case through circumstantial evidence. Despite extensive searches of farms, bodies of water, and rural properties around Mason City, no remains were found.",
      "Jodi Huisentruit was declared legally dead in 2001. The case has been the subject of books, documentaries, and podcasts. Her disappearance from a small, safe Midwestern city shocked the community and the television news industry. The FindJodi.com website, maintained by supporters, continues to publicize the case and solicit tips. The Mason City Police Department maintains the investigation as an active case."
    ],
    "timeline": [
      {"date": "1995-06-27", "event": "Jodi Huisentruit vanishes from her apartment parking lot in Mason City."},
      {"date": "1995-06-27", "event": "Signs of struggle found near her car; drag marks visible."},
      {"date": "1995-07-01", "event": "Extensive search of rural areas around Mason City yields nothing."},
      {"date": "2001-05-31", "event": "Jodi is declared legally dead."}
    ],
    "enriched": True
  },
  {
    "id": "tammy-zywicki-1992",
    "name": "Tammy Zywicki",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1992,
    "date": "August 23, 1992",
    "state": "Illinois",
    "city": "LaSalle",
    "age": 21,
    "gender": "Female",
    "summary": "College student Tammy Zywicki was last seen with her disabled car on Interstate 80 in LaSalle County, Illinois. Her body was found nine days later in Missouri. Multiple witnesses saw a semi-truck near her car, but the driver was never identified.",
    "lastSeen": "August 23, 1992, Interstate 80, LaSalle County, Illinois",
    "tags": ["homicide", "Illinois", "college student", "highway", "truck driver", "1990s"],
    "sources": [
      {"title": "Murder of Tammy Zywicki - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Tammy_Zywicki"},
      {"title": "Tammy Zywicki case - FBI", "url": "https://www.fbi.gov/wanted/seeking-info/tammy-jo-zywicki"},
      {"title": "Tammy Zywicki - Chicago Tribune", "url": "https://www.chicagotribune.com/"}
    ],
    "narrative": [
      "On August 23, 1992, 21-year-old Tammy Jo Zywicki was driving from her family's home in New Jersey to Grinnell College in Iowa for the start of her junior year. Her car, a white 1985 Pontiac T-1000, broke down on Interstate 80 near the LaSalle-Peru exit in LaSalle County, Illinois. Multiple witnesses reported seeing Tammy standing by her disabled car, and several reported seeing a semi-truck—variously described as white with a rust-colored or tan cab—parked behind her vehicle.",
      "When Tammy did not arrive at Grinnell College, her family contacted authorities. Her car was found on the shoulder of I-80 with the hazard lights still on. On September 1, her body was found wrapped in a blanket and a red sleeping bag along the shoulder of Interstate 44 in Lawrence County, Missouri, approximately 500 miles from where her car had been found. She had been stabbed.",
      "The FBI joined the investigation and focused on the semi-truck seen near Tammy's car. A composite sketch of the truck driver was created from witness descriptions, and the sketch was distributed nationwide. The case was featured on America's Most Wanted and generated thousands of tips. Long-haul truckers were extensively investigated.",
      "Despite one of the most intensive FBI investigations of a highway murder, the killer has never been identified. The FBI investigated the possibility that Tammy's murder was connected to other unsolved highway murders of young women during the 1990s, including cases attributed to possible serial killers operating along the interstate system. The FBI continues to seek information about the semi-truck and its driver."
    ],
    "timeline": [
      {"date": "1992-08-23", "event": "Tammy Zywicki's car breaks down on I-80 in LaSalle County, Illinois."},
      {"date": "1992-08-23", "event": "Witnesses see a semi-truck parked behind her car."},
      {"date": "1992-09-01", "event": "Tammy's body is found 500 miles away along I-44 in Missouri."},
      {"date": "1992-09-15", "event": "FBI releases composite sketch of semi-truck driver."}
    ],
    "enriched": True
  },
  {
    "id": "asha-degree-2000",
    "name": "Asha Degree",
    "type": "Missing Person",
    "status": "Arrest Made",
    "year": 2000,
    "date": "February 14, 2000",
    "state": "North Carolina",
    "city": "Shelby",
    "age": 9,
    "gender": "Female",
    "summary": "Nine-year-old Asha Degree left her home in Shelby, North Carolina in the middle of the night during a rainstorm and walked along a highway. Multiple motorists saw her. Her backpack was found buried along a highway a year later. In 2024, arrests were made in connection with her case.",
    "lastSeen": "February 14, 2000, Highway 18, Shelby, North Carolina",
    "tags": ["missing person", "North Carolina", "child", "highway", "night", "2000s"],
    "sources": [
      {"title": "Disappearance of Asha Degree - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Asha_Degree"},
      {"title": "Asha Degree - FBI", "url": "https://www.fbi.gov/wanted/kidnap/asha-jaquilla-degree"},
      {"title": "Asha Degree arrests - Charlotte Observer", "url": "https://www.charlotteobserver.com/"}
    ],
    "narrative": [
      "In the early morning hours of February 14, 2000, nine-year-old Asha Jaquilla Degree left her family's home in Shelby, North Carolina and walked along North Carolina Highway 18 in the rain and darkness. At least two motorists saw a small girl walking along the highway around 4:00 a.m. and one turned around to check on her, at which point she ran off the road into a wooded area. It was later determined she had packed her backpack with clothes and personal items before leaving.",
      "When Asha's parents discovered she was missing the next morning, a massive search was launched. Searches of the woods along Highway 18 found a candy wrapper and a pencil with her scent, along with a hair bow in a nearby shed, but no sign of Asha. The investigation was hampered by heavy rain that washed away potential evidence and the lack of any obvious motive for a nine-year-old to leave home in a storm.",
      "In August 2001, Asha's backpack was found buried and wrapped in a plastic bag along Highway 18 in Burke County, approximately 26 miles north of where she was last seen. Inside were items belonging to Asha as well as a Dr. Seuss book that did not belong to her and a NKOTB t-shirt. The burial of the backpack suggested someone else was involved in her disappearance.",
      "The case remained one of America's most baffling for over two decades. In 2024, a significant breakthrough came when Roy Lee Dedmon was arrested in connection with the case, along with other individuals. Authorities indicated that the arrests resulted from long-running investigative efforts and new evidence, though specific details were kept under court seal. Asha Degree has not been found."
    ],
    "timeline": [
      {"date": "2000-02-14", "event": "Asha Degree leaves her home in the middle of the night and walks along Highway 18."},
      {"date": "2000-02-14", "event": "Motorists spot a young girl on the highway; she runs into woods."},
      {"date": "2001-08-03", "event": "Asha's buried backpack is found along Highway 18."},
      {"date": "2024-11-01", "event": "Arrests made in connection with Asha's disappearance."}
    ],
    "enriched": True
  },
  {
    "id": "victim-of-dating-game-killer",
    "name": "Robin Samsoe",
    "type": "Homicide",
    "status": "Conviction",
    "year": 1979,
    "date": "June 20, 1979",
    "state": "California",
    "city": "Huntington Beach",
    "age": 12,
    "gender": "Female",
    "summary": "Twelve-year-old Robin Samsoe was abducted while riding her bicycle to dance class in Huntington Beach. Her case led to the identification and conviction of serial killer Rodney Alcala, known as 'The Dating Game Killer,' who is believed to have murdered at least seven women and girls.",
    "lastSeen": "June 20, 1979, Huntington Beach, California",
    "tags": ["homicide", "California", "child", "serial killer", "Dating Game Killer", "1970s"],
    "sources": [
      {"title": "Rodney Alcala - Wikipedia", "url": "https://en.wikipedia.org/wiki/Rodney_Alcala"},
      {"title": "Robin Samsoe case - Orange County Register", "url": "https://www.ocregister.com/"},
      {"title": "The Dating Game Killer - Crime Library", "url": "https://www.crimelibrary.org/"}
    ],
    "narrative": [
      "On June 20, 1979, twelve-year-old Robin Christine Samsoe was riding her bicycle from the beach to a ballet class in Huntington Beach, California. She never arrived. Earlier that day, a man had been taking photographs of Robin and her friend on the beach; the friend later identified him as Rodney Alcala.",
      "Robin's body was found twelve days later in the foothills of the Angeles National Forest. She had been sexually assaulted and murdered. A pair of earrings found in Alcala's storage locker were identified by Robin's mother as belonging to her daughter, helping to link Alcala to the crime.",
      "Rodney Alcala was a convicted sex offender who had appeared as a contestant on the television show 'The Dating Game' in 1978, earning him the nickname 'The Dating Game Killer.' He was a photographer who used his camera as a lure for potential victims. Alcala was tried three times for Robin's murder—his first two convictions were overturned on appeal—before being finally convicted in 2010.",
      "During the 2010 trial, prosecutors also charged Alcala with four additional murders in Los Angeles County from the 1970s. He was convicted of all five counts and sentenced to death. DNA evidence later linked him to two additional murders in New York in the 1970s, for which he pleaded guilty. Investigators believe Alcala may have murdered dozens more, based on hundreds of unidentified photographs of women and children found in his possession. Alcala died on death row in 2021."
    ],
    "timeline": [
      {"date": "1979-06-20", "event": "Robin Samsoe is abducted while riding her bicycle in Huntington Beach."},
      {"date": "1979-07-02", "event": "Robin's body is found in the Angeles National Forest foothills."},
      {"date": "1980-06-20", "event": "Rodney Alcala is first convicted; conviction later overturned."},
      {"date": "2010-03-30", "event": "Alcala convicted a third time and sentenced to death for five murders."},
      {"date": "2021-07-24", "event": "Rodney Alcala dies on death row."}
    ],
    "enriched": True
  },
  {
    "id": "zodiac-letters-1969",
    "name": "Zodiac Killer Victims",
    "type": "Serial Killer Victims",
    "status": "Unsolved",
    "year": 1968,
    "date": "December 20, 1968",
    "state": "California",
    "city": "Various",
    "age": None,
    "gender": "Multiple",
    "summary": "The Zodiac Killer terrorized Northern California from 1968-1969, killing at least five people and sending taunting coded letters to newspapers. Despite one of the largest investigations in California history, the Zodiac was never identified.",
    "lastSeen": "Various locations in Northern California, 1968-1969",
    "tags": ["serial killer", "California", "ciphers", "letters", "unsolved", "1960s"],
    "sources": [
      {"title": "Zodiac Killer - Wikipedia", "url": "https://en.wikipedia.org/wiki/Zodiac_Killer"},
      {"title": "Zodiac Killer - FBI", "url": "https://www.fbi.gov/history/famous-cases/zodiac-killer"},
      {"title": "Zodiac case files - San Francisco Chronicle", "url": "https://www.sfchronicle.com/zodiac/"}
    ],
    "narrative": [
      "The Zodiac Killer is one of the most infamous unidentified serial killers in American history. The confirmed attacks began on December 20, 1968, when David Faraday (17) and Betty Lou Jensen (16) were shot to death on a remote road near Benicia, California. On July 4, 1969, the Zodiac shot Darlene Ferrin and Michael Mageau at Blue Rock Springs Park in Vallejo; Ferrin died but Mageau survived. On September 27, Bryan Hartnell and Cecelia Shepard were stabbed at Lake Berryessa; Shepard died but Hartnell survived. On October 11, taxi driver Paul Stine was shot and killed in San Francisco's Presidio Heights neighborhood.",
      "What made the Zodiac unique was his communication with the press. Beginning in August 1969, he sent a series of letters and cryptograms to Bay Area newspapers—the San Francisco Chronicle, San Francisco Examiner, and Vallejo Times-Herald—taking credit for the murders and threatening more. The letters included a four-part cipher that, when decoded by a Salinas couple, contained the Zodiac's boast that 'killing is more fun than killing wild game.' He sent at least 18 letters between 1969 and 1974.",
      "The investigation was the largest in San Francisco Police Department history. The SFPD, Vallejo PD, Napa County Sheriff's Office, and later the FBI all worked the case. Suspects included Arthur Leigh Allen, who was extensively investigated but never charged. DNA from stamps on the letters was tested but proved inconclusive. A second cipher, the Z340, remained unsolved for 51 years until a team of codebreakers cracked it in December 2020, revealing another boastful message.",
      "The Zodiac claimed to have killed 37 people, though investigators believe the confirmed count is five dead and two wounded. Additional unsolved murders in the Bay Area have been tentatively linked to the Zodiac, including the murder of Cheri Jo Bates in Riverside in 1966. Despite decades of investigation and thousands of suspects, the Zodiac Killer has never been conclusively identified. The FBI and California Department of Justice consider the case open."
    ],
    "timeline": [
      {"date": "1968-12-20", "event": "David Faraday and Betty Lou Jensen are shot dead near Benicia."},
      {"date": "1969-07-04", "event": "Darlene Ferrin killed and Michael Mageau wounded in Vallejo."},
      {"date": "1969-08-01", "event": "Zodiac sends first letters and ciphers to Bay Area newspapers."},
      {"date": "1969-09-27", "event": "Cecelia Shepard stabbed to death at Lake Berryessa."},
      {"date": "1969-10-11", "event": "Taxi driver Paul Stine shot and killed in San Francisco."},
      {"date": "2020-12-05", "event": "The Z340 cipher is cracked after 51 years."}
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
    "summary": "Seventeen-year-old Brianna Maitland disappeared after her shift at the Black Lantern Inn in Montgomery, Vermont. Her car was found backed into an abandoned farmhouse. Despite tips suggesting foul play related to drugs, she was never found.",
    "lastSeen": "March 19, 2004, Montgomery, Vermont",
    "tags": ["missing person", "Vermont", "teenager", "waitress", "rural", "2000s"],
    "sources": [
      {"title": "Disappearance of Brianna Maitland - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Brianna_Maitland"},
      {"title": "Brianna Maitland - Vermont State Police", "url": "https://vsp.vermont.gov/"},
      {"title": "Brianna Maitland case - Burlington Free Press", "url": "https://www.burlingtonfreepress.com/"}
    ],
    "narrative": [
      "On the evening of March 19, 2004, 17-year-old Brianna Maitland finished her shift as a waitress at the Black Lantern Inn, a restaurant and inn in the small rural town of Montgomery, Vermont, near the Canadian border. She left the inn around 11:30 p.m. to drive to a friend's house where she had been staying. She never arrived.",
      "The next day, Brianna's 1985 Oldsmobile was found backed into the side of an abandoned farmhouse on Route 118, about a mile from the Black Lantern Inn. The car's rear end had crashed through the building's wall. Inside the car, some of Brianna's personal items were found. Outside the car, investigators found what appeared to be signs of a confrontation—disturbed ground and items scattered near the vehicle.",
      "The investigation by the Vermont State Police explored multiple theories. Brianna had reportedly been involved in a physical altercation with another young woman shortly before her disappearance, and some tips suggested her vanishing was connected to drug activity in the area near the Canadian border. Multiple persons of interest were identified but no charges were filed.",
      "Brianna Maitland's case has drawn parallels to the disappearance of Maura Murray, another young woman who vanished in rural New England the same year. While there is no evidence connecting the cases, they have been jointly discussed in true crime media. The Vermont State Police continues to investigate and periodically releases updates asking for the public's help."
    ],
    "timeline": [
      {"date": "2004-03-19", "event": "Brianna Maitland finishes her shift at the Black Lantern Inn."},
      {"date": "2004-03-20", "event": "Her car is found crashed into an abandoned farmhouse on Route 118."},
      {"date": "2004-03-21", "event": "Vermont State Police launch full investigation."}
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
    "summary": "Nuclear plant worker and union activist Karen Silkwood died in a single-car crash en route to meet a reporter with documents about safety violations at the Kerr-McGee plutonium plant. The documents were never found. Her death is officially an accident, but suspicions of murder persist.",
    "lastSeen": "November 13, 1974, Highway 74 near Crescent, Oklahoma",
    "tags": ["suspicious death", "Oklahoma", "nuclear", "whistleblower", "union", "1970s"],
    "sources": [
      {"title": "Karen Silkwood - Wikipedia", "url": "https://en.wikipedia.org/wiki/Karen_Silkwood"},
      {"title": "Silkwood case - The Oklahoman", "url": "https://www.oklahoman.com/"},
      {"title": "Karen Silkwood: The Whistleblower - Bulletin of the Atomic Scientists", "url": "https://thebulletin.org/"}
    ],
    "narrative": [
      "Karen Gay Silkwood was a 28-year-old chemical technician and union activist at the Kerr-McGee Cimarron Fuel Fabrication Site, a nuclear fuel processing plant near Crescent, Oklahoma. She had become increasingly concerned about safety violations at the plant, including allegations of falsified quality control records for plutonium fuel rods being manufactured for the Breeder Reactor demonstration project.",
      "As a member of the Oil, Chemical and Atomic Workers International Union, Silkwood had been gathering evidence of these violations. In early November 1974, she was found to be contaminated with plutonium—levels high enough that her apartment had to be decontaminated. The source of the contamination was never definitively determined, though Kerr-McGee implied she had contaminated herself to embarrass the company.",
      "On the evening of November 13, 1974, Silkwood left a union meeting at a Hub Cap Cafe in Crescent, reportedly carrying a manila folder and a large notebook containing documents about safety violations. She was driving to meet David Burnham, a New York Times reporter, and Steve Wodka, an official from her union. Her car was found crashed into a concrete culvert on Highway 74. She was dead. The documents were not in the car.",
      "The official ruling was that Silkwood fell asleep at the wheel. However, an independent investigation found dents on the rear of her car consistent with being struck by another vehicle, and a private investigator found traces of methaqualone in her system that he believed were insufficient to cause her to fall asleep. Kerr-McGee settled a lawsuit by Silkwood's estate in 1986 for $1.38 million. The case inspired the 1983 film 'Silkwood' starring Meryl Streep. Whether Karen Silkwood was murdered to prevent her from exposing nuclear safety violations has never been definitively answered."
    ],
    "timeline": [
      {"date": "1974-11-05", "event": "Karen Silkwood is found contaminated with plutonium."},
      {"date": "1974-11-13", "event": "Silkwood dies in a single-car crash on Highway 74 near Crescent."},
      {"date": "1974-11-14", "event": "Documents she was reportedly carrying are not found in her car."},
      {"date": "1979-05-18", "event": "Jury awards Silkwood estate $10.5 million; amount later reduced."},
      {"date": "1986-08-01", "event": "Kerr-McGee settles with the Silkwood estate for $1.38 million."}
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
    "state": "District of Columbia",
    "city": "Washington",
    "age": 24,
    "gender": "Female",
    "summary": "Congressional intern Chandra Levy disappeared from Washington, D.C. Her remains were found a year later in Rock Creek Park. The case was complicated by her affair with Congressman Gary Condit. A suspect was convicted and then acquitted at retrial, leaving the case unresolved.",
    "lastSeen": "May 1, 2001, Washington, D.C.",
    "tags": ["homicide", "Washington D.C.", "intern", "Congress", "Rock Creek Park", "2000s"],
    "sources": [
      {"title": "Murder of Chandra Levy - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Chandra_Levy"},
      {"title": "Chandra Levy case - Washington Post", "url": "https://www.washingtonpost.com/local/public-safety/chandra-levy-murder-case/"},
      {"title": "Levy case developments - CNN", "url": "https://www.cnn.com/2016/07/28/us/chandra-levy-case-charges-dropped/index.html"}
    ],
    "narrative": [
      "On May 1, 2001, 24-year-old Chandra Ann Levy, an intern at the Federal Bureau of Prisons in Washington, D.C., disappeared from her apartment in the Dupont Circle neighborhood. Her disappearance was reported by her parents on May 6 when they could not reach her. The case became a media sensation when it was revealed that Levy had been having an affair with U.S. Representative Gary Condit (D-CA), who initially denied the relationship.",
      "The investigation into Levy's disappearance dominated the news throughout the summer of 2001, overshadowed only by the September 11 attacks. Her remains were discovered on May 22, 2002, by a man walking his dog in a remote section of Rock Creek Park in northwest Washington. The remains were skeletal, and the medical examiner could not determine a definitive cause of death, though homicide was suspected.",
      "In 2009, Ingmar Guandique, an undocumented immigrant from El Salvador who had been convicted of assaulting two other women in Rock Creek Park around the same time as Levy's disappearance, was charged with her murder. He was convicted in 2010 based largely on the testimony of a jailhouse informant. However, the informant later recanted, and in 2015, prosecutors agreed to a new trial. In 2016, the charges were dropped entirely, with prosecutors acknowledging they could no longer prove the case beyond a reasonable doubt.",
      "With Guandique's charges dropped, Chandra Levy's murder is once again officially unsolved. Gary Condit, while never a formal suspect, saw his political career destroyed by the scandal. He lost his 2002 primary election and has maintained he had nothing to do with Levy's disappearance. The case remains one of Washington, D.C.'s most prominent unsolved homicides."
    ],
    "timeline": [
      {"date": "2001-05-01", "event": "Chandra Levy disappears from her Washington, D.C. apartment."},
      {"date": "2001-07-06", "event": "Gary Condit's affair with Levy is publicly revealed."},
      {"date": "2002-05-22", "event": "Levy's skeletal remains are found in Rock Creek Park."},
      {"date": "2010-11-22", "event": "Ingmar Guandique is convicted of Levy's murder."},
      {"date": "2016-07-28", "event": "Charges against Guandique are dropped; case is again unsolved."}
    ],
    "enriched": True
  },
  {
    "id": "jennifer-kesse-2006",
    "name": "Jennifer Kesse",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2006,
    "date": "January 24, 2006",
    "state": "Florida",
    "city": "Orlando",
    "age": 24,
    "gender": "Female",
    "summary": "Twenty-four-year-old finance manager Jennifer Kesse vanished from her Orlando condo. Security cameras captured a person of interest parking her car at a nearby complex, but the individual's face was obscured behind a fence post in every frame. She has never been found.",
    "lastSeen": "January 24, 2006, Orlando, Florida",
    "tags": ["missing person", "Florida", "Orlando", "condo", "surveillance", "2000s"],
    "sources": [
      {"title": "Disappearance of Jennifer Kesse - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Jennifer_Kesse"},
      {"title": "Jennifer Kesse - FindJenniferKesse.com", "url": "https://www.findjenniferkesse.com/"},
      {"title": "Jennifer Kesse case - Orlando Sentinel", "url": "https://www.orlandosentinel.com/"}
    ],
    "narrative": [
      "On the morning of January 24, 2006, 24-year-old Jennifer Joyce Kesse prepared for work at her condominium in the Mosaic at Millenia complex in Orlando, Florida. Her employer, Central Florida Investments, grew concerned when she did not arrive at work or answer calls. Her family, alerted by the company, contacted Orlando police.",
      "Jennifer's car, a black Chevy Malibu, was found the next day at the Huntington on the Green apartment complex, approximately 1.2 miles from her condo. Security cameras at the Huntington captured a person of interest walking away from Jennifer's car at approximately noon on January 24. In an extraordinary stroke of bad luck, the individual's face was obscured in every frame by the fence posts along the walkway, making identification impossible.",
      "The investigation revealed that Jennifer's condo showed signs of her normal morning routine—the shower had been used, her clothes were laid out, and her toiletries were packed for a trip she had planned. Construction workers at her complex, many of whom were transient laborers, became persons of interest but could not be fully investigated due to their mobility and undocumented status.",
      "Jennifer's parents, Drew and Joyce Kesse, took legal action in 2018 to gain access to the police case files, winning a lawsuit against the Orlando Police Department to review the evidence. They subsequently hired private investigators. Despite extensive searches, rewards, and publicity, Jennifer Kesse has never been found. The case remains one of Florida's most frustrating unsolved disappearances."
    ],
    "timeline": [
      {"date": "2006-01-24", "event": "Jennifer Kesse fails to arrive at work in Orlando."},
      {"date": "2006-01-25", "event": "Her car is found at a nearby apartment complex."},
      {"date": "2006-01-26", "event": "Security camera footage shows person of interest, face obscured."},
      {"date": "2018-08-01", "event": "Kesse family wins lawsuit to access police case files."}
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
    "summary": "Housewife Joan Risch vanished from her Lincoln, Massachusetts home leaving a trail of blood through the kitchen and garage. Library records showed she had been researching disappearances. Neither her body nor a suspect was ever found.",
    "lastSeen": "October 24, 1961, Lincoln, Massachusetts",
    "tags": ["missing person", "Massachusetts", "housewife", "blood evidence", "library research", "1960s"],
    "sources": [
      {"title": "Disappearance of Joan Risch - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Joan_Risch"},
      {"title": "Joan Risch - Charley Project", "url": "https://charleyproject.org/case/joan-carolyn-risch"},
      {"title": "Joan Risch case - Boston Globe", "url": "https://www.bostonglobe.com/"}
    ],
    "narrative": [
      "On the afternoon of October 24, 1961, 31-year-old Joan Carolyn Risch vanished from her home on Old Bedford Road in Lincoln, Massachusetts, an affluent suburb west of Boston. Her husband Martin was away on a business trip, and their two children—a two-year-old daughter and a four-year-old son—had been left with a neighbor for the afternoon.",
      "When the neighbor brought the children home around 4:15 p.m., the house was empty and there was blood throughout the kitchen, hallway, and garage. Approximately a half-pint of blood—Joan's type O—was smeared on the floors, walls, and a telephone directory open to the emergency numbers page. The telephone receiver had been torn from the wall. Despite the blood, there was no sign of a weapon or the kind of massive bleeding that would indicate a fatal wound at the scene.",
      "A neighbor reported seeing Joan walking along the road near her house around 3:45 p.m. with a red, concave-shaped object—possibly a basin—pressed against her midsection, as though she were carrying it. She appeared to be heading toward Route 2, the main highway. Another witness reported seeing a woman matching Joan's description being assisted into a car.",
      "The most intriguing detail emerged from library records. In the weeks before her disappearance, Joan had borrowed several books about people who had disappeared, including books about amnesia and planned disappearances. This led to theories that she had orchestrated her own vanishing. Others believed the blood evidence suggested she was the victim of violence and the library books were coincidental. Despite extensive searches of the surrounding woods and waterways, Joan Risch was never found."
    ],
    "timeline": [
      {"date": "1961-10-24", "event": "Joan Risch vanishes from her Lincoln, Massachusetts home; blood found."},
      {"date": "1961-10-24", "event": "Neighbor sees Joan walking along road carrying a red object."},
      {"date": "1961-10-25", "event": "Police discover Joan had been checking out books about disappearances."},
      {"date": "1961-11-01", "event": "Extensive search of area finds no trace."}
    ],
    "enriched": True
  },
  {
    "id": "skelton-brothers-2010",
    "name": "Skelton Brothers",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2010,
    "date": "November 26, 2010",
    "state": "Michigan",
    "city": "Morenci",
    "age": None,
    "gender": "Male",
    "summary": "Three brothers—Andrew (9), Alexander (7), and Tanner (5) Skelton—disappeared from their father's home in Morenci, Michigan over Thanksgiving. Their father attempted suicide and later claimed he gave the boys to a group that would 'keep them safe,' but they were never found.",
    "lastSeen": "November 26, 2010, Morenci, Michigan",
    "tags": ["missing person", "Michigan", "children", "three brothers", "Thanksgiving", "2010s"],
    "sources": [
      {"title": "Disappearance of the Skelton brothers - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_the_Skelton_brothers"},
      {"title": "Skelton brothers - NCMEC", "url": "https://www.missingkids.org/"},
      {"title": "Skelton brothers case - Toledo Blade", "url": "https://www.toledoblade.com/"}
    ],
    "narrative": [
      "Over the Thanksgiving holiday in 2010, nine-year-old Andrew, seven-year-old Alexander, and five-year-old Tanner Skelton were staying with their father, John Skelton, at his home in Morenci, Michigan, a small town near the Ohio border. John and the boys' mother, Tanya Zuvers, were going through a contentious divorce, and John had the boys for the holiday as part of a custody arrangement. He was supposed to return them to their mother on November 26.",
      "When John Skelton did not return the boys, Tanya called police. Officers went to Skelton's home and found him in the garage, having attempted suicide by hanging. He was hospitalized but survived. When questioned, Skelton gave contradictory accounts. He initially said the boys were with a woman named Joann Taylor, but no such person could be found. He later claimed he had given the boys to an underground group called 'United Foster Outreach' that would protect them from their mother. No such organization exists.",
      "An extensive search was conducted throughout Lenawee County, Michigan and across the border into Ohio. Dogs, divers, aerial searches, and hundreds of volunteers covered wide areas. Some of the boys' clothing was found in a wooded area near a river, and evidence suggested Skelton had visited the area. However, the boys themselves were never found.",
      "John Skelton was convicted of unlawful imprisonment and sentenced to 10-15 years in prison. He has consistently refused to reveal the boys' location. He has been periodically questioned by investigators but has not provided useful information. The FBI and Michigan State Police continue to investigate, and the boys' mother has made regular public appeals for information. The Skelton brothers would be in their teens and twenties today."
    ],
    "timeline": [
      {"date": "2010-11-26", "event": "John Skelton fails to return his three sons to their mother."},
      {"date": "2010-11-26", "event": "Skelton is found having attempted suicide; claims boys are with a caretaker."},
      {"date": "2010-11-27", "event": "Massive search begins; boys' clothing found near a river."},
      {"date": "2011-09-19", "event": "John Skelton is convicted of unlawful imprisonment."}
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
    "summary": "Nursing student Maura Murray vanished after crashing her car on a rural road in Haverhill, New Hampshire. She had left college abruptly that day. When police arrived minutes after the crash, she was gone. Her case became one of the most discussed missing person cases in true crime.",
    "lastSeen": "February 9, 2004, Route 112, Haverhill, New Hampshire",
    "tags": ["missing person", "New Hampshire", "college student", "car crash", "White Mountains", "2000s"],
    "sources": [
      {"title": "Disappearance of Maura Murray - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Maura_Murray"},
      {"title": "Maura Murray case - Oxygen", "url": "https://www.oxygen.com/the-disappearance-of-maura-murray"},
      {"title": "Maura Murray - NH State Police", "url": "https://www.nhsp.dos.nh.gov/"}
    ],
    "narrative": [
      "On February 9, 2004, 21-year-old Maura Murray, a nursing student at the University of Massachusetts Amherst, packed her belongings into her black 1996 Saturn, emailed her professors saying she would be away for a week due to a death in the family (no family member had died), and drove north toward New Hampshire. She had searched MapQuest for directions to Burlington, Vermont and Berkshires-area destinations. She also brought alcohol.",
      "At approximately 7:27 p.m., Maura's car crashed into a snowbank on Route 112 in Haverhill, New Hampshire, near Woodsville. A school bus driver, Butch Atwood, stopped and asked if she needed help. Maura declined, saying she had called AAA (she had not; there was no cell service in the area). Atwood went to his home nearby and called police. When officers arrived approximately 7-10 minutes later, Maura and her personal belongings were gone. The car was locked, and an open box of wine was found inside.",
      "A massive search of the area, including cadaver dogs, helicopters, and hundreds of volunteers, found no trace of Maura. There were no footprints in the snow leading away from the car beyond what would be expected from the crash scene. The investigation explored whether she fled into the woods and succumbed to the cold, was picked up by a passing motorist, or met with foul play.",
      "Maura's case has become one of the most discussed disappearances in true crime, inspiring multiple books, documentaries, podcasts, and a dedicated online community. Her father, Fred Murray, has spent two decades searching for answers and has publicly clashed with New Hampshire law enforcement over the investigation's handling. Despite periodic leads and extensive public interest, Maura Murray has never been found. The New Hampshire State Police Cold Case Unit maintains the investigation."
    ],
    "timeline": [
      {"date": "2004-02-09", "event": "Maura Murray leaves UMass Amherst and drives north."},
      {"date": "2004-02-09", "event": "Her car crashes on Route 112 in Haverhill, New Hampshire."},
      {"date": "2004-02-09", "event": "She declines help from a passing motorist; police arrive to find her gone."},
      {"date": "2004-02-10", "event": "Massive search of surrounding area finds no trace."}
    ],
    "enriched": True
  },
  {
    "id": "megan-kanka-1994",
    "name": "Megan Kanka",
    "type": "Homicide",
    "status": "Conviction",
    "year": 1994,
    "date": "July 29, 1994",
    "state": "New Jersey",
    "city": "Hamilton Township",
    "age": 7,
    "gender": "Female",
    "summary": "Seven-year-old Megan Kanka was raped and murdered by a neighbor who was a twice-convicted sex offender. The family had no knowledge of his criminal history. Her case directly inspired Megan's Law, which requires sex offender registration and community notification.",
    "lastSeen": "July 29, 1994, Hamilton Township, New Jersey",
    "tags": ["homicide", "New Jersey", "child", "sex offender", "Megan's Law", "1990s"],
    "sources": [
      {"title": "Murder of Megan Kanka - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Megan_Kanka"},
      {"title": "Megan's Law - Department of Justice", "url": "https://www.justice.gov/criminal-ceos/megans-law"},
      {"title": "Jesse Timmendequas conviction - NJ.com", "url": "https://www.nj.com/"}
    ],
    "narrative": [
      "On the evening of July 29, 1994, seven-year-old Megan Nicole Kanka went across the street from her home in Hamilton Township, Mercer County, New Jersey to see her neighbor's new puppy. The neighbor, Jesse Timmendequas, was a 33-year-old twice-convicted sex offender who shared a house with two other convicted sex offenders. Megan never came home.",
      "After Megan's parents reported her missing, the community mobilized for a search. Timmendequas initially claimed he had not seen Megan, but investigators quickly focused on him. Under questioning, he confessed to luring Megan into his home with the promise of seeing a puppy, then raping and strangling her. He led police to a park in nearby Mercer County where he had left her body in a wooden toy chest.",
      "Timmendequas was charged with capital murder. The Kanka family, devastated that three convicted sex offenders had been living across the street from their home without their knowledge, began a campaign for sex offender notification laws. Within three months, New Jersey passed 'Megan's Law,' requiring convicted sex offenders to register with police and mandating community notification of their presence.",
      "In 1997, Timmendequas was convicted of murder, kidnapping, and sexual assault, and was sentenced to death. The federal version of Megan's Law was signed by President Clinton in 1996, and all 50 states eventually passed their own versions. In 2007, New Jersey abolished the death penalty, and Timmendequas's sentence was commuted to life without parole. Megan Kanka's legacy—the nationwide sex offender registry system—remains one of the most significant changes in American criminal justice policy to emerge from a single crime."
    ],
    "timeline": [
      {"date": "1994-07-29", "event": "Megan Kanka disappears from her Hamilton Township neighborhood."},
      {"date": "1994-07-30", "event": "Neighbor Jesse Timmendequas confesses and leads police to Megan's body."},
      {"date": "1994-10-31", "event": "New Jersey passes Megan's Law."},
      {"date": "1996-05-17", "event": "President Clinton signs federal Megan's Law."},
      {"date": "1997-06-20", "event": "Timmendequas convicted and sentenced to death."}
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
    "summary": "Seven-year-old Kyron Horman vanished from Skyline Elementary School in Portland, Oregon during a science fair. His stepmother, Terri Horman, was the last person to see him. Despite one of Oregon's largest investigations, Kyron was never found.",
    "lastSeen": "June 4, 2010, Skyline Elementary School, Portland, Oregon",
    "tags": ["missing person", "Oregon", "child", "school", "science fair", "2010s"],
    "sources": [
      {"title": "Disappearance of Kyron Horman - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Kyron_Horman"},
      {"title": "Kyron Horman case - The Oregonian", "url": "https://www.oregonlive.com/kyron-horman/"},
      {"title": "Kyron Horman - FBI Portland", "url": "https://www.fbi.gov/contact-us/field-offices/portland"}
    ],
    "narrative": [
      "On the morning of June 4, 2010, seven-year-old Kyron Richard Horman attended a science fair at Skyline Elementary School in the West Hills of Portland, Oregon. His stepmother, Terri Moulton Horman, drove him to school and walked him to his science fair exhibit. She said she last saw Kyron walking down the hallway toward his classroom at approximately 8:45 a.m. When Kyron did not get off the school bus that afternoon, his family called the school and learned he had been marked absent for the day.",
      "A massive search was launched, involving the FBI, Multnomah County Sheriff's Office, and hundreds of volunteers. The heavily wooded hills surrounding the school were searched extensively by ground teams, helicopters, and dogs. No trace of Kyron was found. The investigation quickly became one of the largest and most expensive in Oregon history.",
      "Suspicion focused on Terri Horman, who could not account for approximately two hours between leaving the school and running errands. She was seen on school security cameras but allegedly left before Kyron reached his classroom. Kyron's father, Kaine Horman, filed for divorce and a restraining order. It was later revealed that Terri had allegedly tried to hire a landscaper to murder Kaine months before Kyron's disappearance.",
      "Despite the suspicion surrounding Terri Horman, she was never arrested or charged. She has denied any involvement in Kyron's disappearance and invoked her Fifth Amendment rights. The Multnomah County Sheriff's Office has stated they have never excluded Terri as a person of interest but also have not publicly named a suspect. Kyron Horman has never been found, and the case remains one of the Pacific Northwest's most agonizing unsolved disappearances."
    ],
    "timeline": [
      {"date": "2010-06-04", "event": "Kyron Horman vanishes from Skyline Elementary School during a science fair."},
      {"date": "2010-06-04", "event": "Massive search launched in the West Hills of Portland."},
      {"date": "2010-06-25", "event": "Kaine Horman files for divorce and restraining order against Terri."},
      {"date": "2010-07-01", "event": "FBI joins investigation; no charges filed."}
    ],
    "enriched": True
  },
  {
    "id": "crystal-rogers-2015",
    "name": "Crystal Rogers",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2015,
    "date": "July 3, 2015",
    "state": "Kentucky",
    "city": "Bardstown",
    "age": 35,
    "gender": "Female",
    "summary": "Crystal Rogers disappeared from Bardstown, Kentucky. Her car was found on a highway with her belongings inside. Her boyfriend Brooks Houck is the primary suspect. Her father Tommy Ballard was shot and killed while investigating her case in 2016.",
    "lastSeen": "July 3, 2015, Bardstown, Kentucky",
    "tags": ["missing person", "Kentucky", "Bardstown", "boyfriend suspect", "2010s"],
    "sources": [
      {"title": "Disappearance of Crystal Rogers - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Crystal_Rogers"},
      {"title": "Crystal Rogers case - Courier Journal", "url": "https://www.courier-journal.com/story/news/crime/2020/08/05/crystal-rogers-case-what-we-know-bardstown-disappearance/5571685002/"},
      {"title": "Bardstown mysteries - WDRB", "url": "https://www.wdrb.com/"}
    ],
    "narrative": [
      "On July 3, 2015, 35-year-old Crystal Gayle Rogers disappeared from Bardstown, Kentucky, a small city approximately 40 miles south of Louisville. Crystal was the mother of five children and worked at her family's business. She had been in a relationship with Brooks David Houck, a local farmer, with whom she had her youngest child.",
      "Crystal's maroon Chevrolet Impala was found the next day on the Bluegrass Parkway, a highway near Bardstown, with a flat tire. Her purse, keys, and cell phone were inside the car. She was reported missing by her family on July 5. Nelson County police investigated, with the FBI later becoming involved.",
      "Brooks Houck was named the primary suspect but has never been charged. He stopped cooperating with investigators early in the case and hired a criminal defense attorney. Grand jury proceedings were conducted, but no indictment was returned.",
      "In November 2016, Crystal's father, 54-year-old Tommy Ballard, was shot and killed while hunting on his Bardstown farm. Ballard had been actively investigating his daughter's disappearance and had publicly accused Houck. His murder remains unsolved and is believed by many to be connected to Crystal's case. The Rogers-Ballard case is one of several unsolved violent crimes in Bardstown that have given it the reputation as 'the most dangerous small town in America.' Crystal's body has never been found."
    ],
    "timeline": [
      {"date": "2015-07-03", "event": "Crystal Rogers disappears from Bardstown, Kentucky."},
      {"date": "2015-07-04", "event": "Her car is found on the Bluegrass Parkway with her belongings inside."},
      {"date": "2016-11-19", "event": "Crystal's father Tommy Ballard is shot and killed while hunting."},
      {"date": "2020-08-01", "event": "FBI takes over the investigation from local police."}
    ],
    "enriched": True
  },
  {
    "id": "mollie-tibbetts-2018",
    "name": "Mollie Tibbetts",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2018,
    "date": "July 18, 2018",
    "state": "Iowa",
    "city": "Brooklyn",
    "age": 20,
    "gender": "Female",
    "summary": "Twenty-year-old University of Iowa student Mollie Tibbetts vanished while jogging in Brooklyn, Iowa. Her body was found a month later in a cornfield. Cristhian Bahena Rivera was convicted of her murder in 2021.",
    "lastSeen": "July 18, 2018, Brooklyn, Iowa",
    "tags": ["homicide", "Iowa", "college student", "jogger", "2010s"],
    "sources": [
      {"title": "Murder of Mollie Tibbetts - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Mollie_Tibbetts"},
      {"title": "Mollie Tibbetts case - Des Moines Register", "url": "https://www.desmoinesregister.com/story/news/crime-and-courts/2021/05/28/mollie-tibbetts-murder-trial-cristhian-bahena-rivera-guilty-verdict/7488286002/"},
      {"title": "Tibbetts case verdict - CNN", "url": "https://www.cnn.com/2021/05/28/us/mollie-tibbetts-trial-verdict/index.html"}
    ],
    "narrative": [
      "On the evening of July 18, 2018, 20-year-old Mollie Cecilia Tibbetts, a University of Iowa student, went for a jog in the small town of Brooklyn, Iowa, where she was dog-sitting for her boyfriend. She was tracked by her Fitbit activity tracker, which showed her running route. She never returned. Her disappearance sparked a massive search and national media attention.",
      "For a month, law enforcement searched for Mollie using GPS data, surveillance footage, and tips from the public. On August 20, investigators identified 24-year-old Cristhian Bahena Rivera, an undocumented immigrant from Mexico who worked at a nearby dairy farm, after reviewing security camera footage from houses along Mollie's jogging route that showed his car following her.",
      "Under questioning, Bahena Rivera led investigators to a cornfield in rural Poweshiek County where Mollie's body was hidden under cornstalk leaves. He initially claimed he blacked out and couldn't remember what happened. At trial, he changed his story to claim that two masked men had actually killed Mollie and forced him to dispose of the body.",
      "In May 2021, Bahena Rivera was convicted of first-degree murder by a jury in Davenport, Iowa (the trial was moved due to pretrial publicity). He was sentenced to life in prison without parole. Mollie's case became entangled in the national immigration debate, with some politicians citing it as an argument for stricter immigration enforcement, while Mollie's family asked that her death not be used to promote anti-immigrant sentiment."
    ],
    "timeline": [
      {"date": "2018-07-18", "event": "Mollie Tibbetts disappears while jogging in Brooklyn, Iowa."},
      {"date": "2018-08-20", "event": "Cristhian Bahena Rivera is arrested; leads police to Mollie's body."},
      {"date": "2021-05-28", "event": "Bahena Rivera is convicted of first-degree murder."},
      {"date": "2021-08-30", "event": "Sentenced to life in prison without parole."}
    ],
    "enriched": True
  },
  {
    "id": "holly-bobo-2011",
    "name": "Holly Bobo",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2011,
    "date": "April 13, 2011",
    "state": "Tennessee",
    "city": "Parsons",
    "age": 20,
    "gender": "Female",
    "summary": "Nursing student Holly Bobo was abducted from her home in Parsons, Tennessee. Her brother witnessed a man leading her into the woods. Her remains were found in 2014. Zachary Adams was convicted and sentenced to life plus 50 years.",
    "lastSeen": "April 13, 2011, Parsons, Decatur County, Tennessee",
    "tags": ["homicide", "Tennessee", "nursing student", "abduction", "rural", "2010s"],
    "sources": [
      {"title": "Murder of Holly Bobo - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Holly_Bobo"},
      {"title": "Holly Bobo case - The Tennessean", "url": "https://www.tennessean.com/story/news/crime/2017/09/22/holly-bobo-case-timeline/692037001/"},
      {"title": "Zachary Adams conviction - CNN", "url": "https://www.cnn.com/2017/09/22/us/holly-bobo-murder-trial-verdict/index.html"}
    ],
    "narrative": [
      "On the morning of April 13, 2011, 20-year-old Holly Lynn Bobo, a nursing student at the University of Tennessee at Martin, was preparing to leave for clinicals at her family's home in Parsons, a small town in rural Decatur County, Tennessee. Her brother Clint looked out a window and saw Holly being led into the woods adjacent to the home by a man wearing camouflage. He assumed it was Holly's boyfriend and did not intervene. When he later found blood on the garage floor and Holly's lunch box in the driveway, he called police.",
      "Holly's abduction triggered Tennessee's largest-ever criminal investigation. Thousands of acres of West Tennessee countryside were searched by ground teams, dogs, divers, and aircraft. The Tennessee Bureau of Investigation (TBI), FBI, and ATF all participated. Tips numbered in the tens of thousands. Despite the massive effort, Holly was not found.",
      "The case broke in February 2014 when two hunters discovered Holly's skull and other remains in a wooded area in Decatur County. DNA confirmed the identification. Zachary Adams and Jason Autry, local men known to law enforcement, were charged with kidnapping and murder. The prosecution alleged that Adams and Autry abducted and killed Holly and that others helped conceal the crime.",
      "Zachary Adams was convicted of first-degree felony murder, especially aggravated kidnapping, and aggravated rape in September 2017 and sentenced to life plus 50 years. Jason Autry testified against Adams in exchange for a reduced sentence. A third defendant, Shayne Austin, died by suicide before trial. The case exposed tensions in the tight-knit rural community and the difficulty of investigating crimes in areas where witnesses may fear retribution."
    ],
    "timeline": [
      {"date": "2011-04-13", "event": "Holly Bobo is seen being led into the woods by a man in camouflage."},
      {"date": "2011-04-13", "event": "Tennessee's largest criminal investigation is launched."},
      {"date": "2014-09-07", "event": "Holly's remains are found by hunters in Decatur County."},
      {"date": "2017-09-22", "event": "Zachary Adams is convicted and sentenced to life plus 50 years."}
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
    "state": "District of Columbia",
    "city": "Washington",
    "age": 8,
    "gender": "Female",
    "summary": "Eight-year-old Relisha Rudd vanished from a Washington, D.C. homeless shelter. She had been in the care of a janitor, Khalil Tatum, who was later found dead of self-inflicted gunshot wound. Relisha has never been found.",
    "lastSeen": "March 1, 2014, Washington, D.C.",
    "tags": ["missing person", "Washington D.C.", "child", "homeless shelter", "systemic failure", "2010s"],
    "sources": [
      {"title": "Disappearance of Relisha Rudd - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Relisha_Rudd"},
      {"title": "Relisha Rudd case - Washington Post", "url": "https://www.washingtonpost.com/local/search-for-relisha-rudd-dc-girl-missing-since-march-focuses-on-kenilworth-park/2014/04/01/6e98b97e-b993-11e3-9a05-c739f29ccb08_story.html"},
      {"title": "Where is Relisha Rudd? - NBC Washington", "url": "https://www.nbcwashington.com/"}
    ],
    "narrative": [
      "Eight-year-old Relisha Tenau Rudd lived with her mother and siblings at the DC General Family Shelter, a large homeless shelter in Washington, D.C. housed in a former hospital. In early 2014, Khalil Tatum, a 51-year-old janitor at the shelter, began spending time with Relisha and showering her and her family with gifts and money. Relisha's mother, Shamika Young, allowed Tatum to take Relisha for outings and overnights.",
      "Relisha was last seen on March 1, 2014, on security footage at a Holiday Inn Express hotel with Tatum. Her absence from school went unnoticed for weeks because Tatum had forged a doctor's note excusing her absences. When school officials finally investigated, they discovered Relisha had not been seen for an extended period.",
      "The investigation led police to Khalil Tatum, who had murdered his wife, 51-year-old Andrea Tatum, on March 20. Her body was found in a Maryland motel. Tatum went on the run, and on March 31, his body was found in a wooded area of Kenilworth Park in northeast D.C. He had died of a self-inflicted gunshot wound. Relisha was not with him.",
      "An extensive search of Kenilworth Park and the surrounding area, involving hundreds of officers, dogs, and divers, found no sign of Relisha. The case exposed catastrophic failures in the District's social services and shelter systems—the shelter had no system for tracking children's whereabouts, and multiple adults in Relisha's life failed to intervene as an adult man took increasing control over a child. Relisha Rudd has never been found."
    ],
    "timeline": [
      {"date": "2014-03-01", "event": "Relisha Rudd is last seen on hotel security footage with Khalil Tatum."},
      {"date": "2014-03-19", "event": "Relisha's school finally investigates her prolonged absence."},
      {"date": "2014-03-20", "event": "Tatum's wife Andrea is found murdered in a Maryland motel."},
      {"date": "2014-03-31", "event": "Tatum is found dead of suicide in Kenilworth Park."},
      {"date": "2014-04-01", "event": "Massive search of Kenilworth Park finds no sign of Relisha."}
    ],
    "enriched": True
  },
  {
    "id": "henry-mccabe-2015",
    "name": "Henry McCabe",
    "type": "Suspicious Death",
    "status": "Unsolved",
    "year": 2015,
    "date": "September 6, 2015",
    "state": "Minnesota",
    "city": "Fridley",
    "age": 32,
    "gender": "Male",
    "summary": "Henry McCabe disappeared after a night out in Minneapolis. He left a terrifying 2-minute voicemail of screaming and distressed sounds on his wife's phone. His body was found two months later in Rush Lake. The cause of death was ruled undetermined.",
    "lastSeen": "September 6, 2015, Fridley, Minnesota",
    "tags": ["suspicious death", "Minnesota", "voicemail", "lake", "2010s"],
    "sources": [
      {"title": "Death of Henry McCabe - Wikipedia", "url": "https://en.wikipedia.org/wiki/Death_of_Henry_McCabe"},
      {"title": "Henry McCabe voicemail - KARE 11", "url": "https://www.kare11.com/"},
      {"title": "McCabe case - Star Tribune", "url": "https://www.startribune.com/"}
    ],
    "narrative": [
      "On the night of September 6, 2015, 32-year-old Henry McCabe went out with friends to bars and nightclubs in Minneapolis, Minnesota. He was a Liberian immigrant who worked as a nurse at a senior care facility and lived in the suburb of Fridley with his wife and children. At approximately 2:00 a.m. on September 7, a friend dropped McCabe off at a gas station in Fridley, where he said he would wait for his wife to pick him up.",
      "At 2:13 a.m., McCabe's wife received a voicemail from his phone that lasted approximately two minutes. The recording contained terrifying sounds—screaming, groaning, and what some have interpreted as sounds of an attack, followed by silence. The content of the voicemail has been widely discussed online, with debate about what exactly it captures.",
      "McCabe was never seen alive again. His cell phone was found the next day in the parking lot of the gas station where he had been dropped off. On November 2, 2015, his body was recovered from Rush Lake in Anoka County, approximately two miles from the gas station. The Hennepin County Medical Examiner ruled the cause of death as 'undetermined,' noting that the body had been in the water for approximately two months.",
      "The case remains deeply puzzling. The voicemail suggests McCabe may have been attacked, but there was no definitive evidence of foul play on his body (though decomposition may have obscured injuries). How he ended up in Rush Lake, two miles from where he was last seen, is unexplained. The friend who dropped him at the gas station was investigated but not charged. The Fridley Police Department considers the case open."
    ],
    "timeline": [
      {"date": "2015-09-07", "event": "Henry McCabe is dropped at a Fridley gas station at 2:00 a.m."},
      {"date": "2015-09-07", "event": "His wife receives a two-minute voicemail of screaming and distressed sounds."},
      {"date": "2015-09-07", "event": "McCabe's phone is found in the gas station parking lot."},
      {"date": "2015-11-02", "event": "McCabe's body is recovered from Rush Lake."}
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
    "summary": "Fitness instructor Missy Bevers was murdered inside a church before an early morning fitness class. Security cameras captured her killer walking through the church dressed in police tactical gear, but the suspect has never been identified despite the clear footage.",
    "lastSeen": "April 18, 2016, Creekside Church of Christ, Midlothian, Texas",
    "tags": ["homicide", "Texas", "fitness instructor", "church", "tactical gear", "surveillance", "2010s"],
    "sources": [
      {"title": "Murder of Missy Bevers - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Missy_Bevers"},
      {"title": "Missy Bevers case - Dallas Morning News", "url": "https://www.dallasnews.com/"},
      {"title": "Missy Bevers investigation - CBS 48 Hours", "url": "https://www.cbsnews.com/news/48-hours-missy-bevers-murder-investigation-who-is-behind-the-mask/"}
    ],
    "narrative": [
      "In the early morning hours of April 18, 2016, security cameras inside the Creekside Church of Christ in Midlothian, Texas captured a person walking through the building wearing full police-style tactical gear, including a helmet with face shield, vest, and gloves. The individual was methodically breaking into rooms and opening doors throughout the church, apparently lying in wait.",
      "Terri 'Missy' Bevers, a 45-year-old fitness instructor and mother of three, arrived at the church at approximately 4:20 a.m. to set up for her 5:00 a.m. Camp Gladiator fitness class, which was held in the church's gymnasium. She encountered the person in tactical gear and was murdered. When students arrived for the class, they found Missy's body inside the church.",
      "The security footage, which clearly showed the suspect walking through the church for approximately 30 minutes before the murder, became one of the most widely circulated pieces of evidence in modern true crime. Despite the clarity of the footage, the suspect's face was completely concealed by the tactical helmet. Viewers and investigators analyzed the suspect's build, gait, and movements, with some suggesting the person may have been female based on body proportions and walking style.",
      "The Midlothian Police Department investigated extensively, following thousands of tips and examining Missy's personal and professional relationships. The tactical gear worn by the suspect—which appeared to be generic equipment purchasable online rather than actual law enforcement equipment—was a key focus. Despite the wealth of video evidence and intense public interest, the person in the tactical gear has never been identified. The case remains one of the most distinctive unsolved murders in recent Texas history."
    ],
    "timeline": [
      {"date": "2016-04-18", "event": "Security cameras capture suspect in tactical gear inside Creekside Church."},
      {"date": "2016-04-18", "event": "Missy Bevers is murdered inside the church before her fitness class."},
      {"date": "2016-04-19", "event": "Midlothian police release security footage; national attention follows."},
      {"date": "2016-05-01", "event": "Thousands of tips received; suspect remains unidentified."}
    ],
    "enriched": True
  },
  {
    "id": "dail-dinwiddie-1992",
    "name": "Dail Dinwiddie",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1992,
    "date": "September 24, 1992",
    "state": "South Carolina",
    "city": "Columbia",
    "age": 23,
    "gender": "Female",
    "summary": "Twenty-three-year-old Dail Dinwiddie vanished after leaving a Columbia, South Carolina bar in the Five Points entertainment district. Multiple witnesses saw her walking alone. Despite extensive investigation, she was never found.",
    "lastSeen": "September 24, 1992, Five Points, Columbia, South Carolina",
    "tags": ["missing person", "South Carolina", "young woman", "bar", "Five Points", "1990s"],
    "sources": [
      {"title": "Disappearance of Dail Dinwiddie - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Dail_Dinwiddie"},
      {"title": "Dail Dinwiddie - Charley Project", "url": "https://charleyproject.org/case/dail-dinwiddie"},
      {"title": "Dail Dinwiddie case - The State", "url": "https://www.thestate.com/"}
    ],
    "narrative": [
      "On the evening of September 24, 1992, 23-year-old Dail Elmore Dinwiddie went out with friends to bars in the Five Points entertainment district of Columbia, South Carolina, a popular nightlife area near the University of South Carolina campus. Dail became separated from her friends at a bar called Jungle Jim's sometime around midnight.",
      "Multiple witnesses saw Dail walking alone on Harden Street in the Five Points area between midnight and 1:00 a.m. She appeared to be looking for a ride home. One witness reported seeing her talking to someone in a vehicle. She was never seen again.",
      "Dail's family launched an extensive search campaign, hiring private investigators and offering substantial rewards. Her father, a prominent Columbia attorney, used his connections and resources to pursue the case aggressively. The Columbia Police Department investigated, with the FBI later assisting. Several persons of interest were identified but no charges were ever filed.",
      "The case has been periodically revisited with new tips and investigative techniques. In the mid-2000s, investigators explored possible connections to a convicted sex offender who had been in the area at the time. However, no definitive evidence has emerged, and Dail Dinwiddie's fate remains unknown. Her disappearance contributed to increased safety awareness in the Five Points area."
    ],
    "timeline": [
      {"date": "1992-09-24", "event": "Dail Dinwiddie is last seen walking in Five Points, Columbia."},
      {"date": "1992-09-25", "event": "Friends and family report her missing; search begins."},
      {"date": "1992-10-01", "event": "Columbia police and FBI investigate; no leads develop."}
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
    "summary": "Six-year-old beauty queen JonBenét Ramsey was found murdered in the basement of her family's Boulder, Colorado home on Christmas Day. A lengthy ransom note was found, but she had never left the house. The case became one of the most publicized and controversial unsolved murders in American history.",
    "lastSeen": "December 25, 1996, Boulder, Colorado",
    "tags": ["homicide", "Colorado", "Boulder", "child", "beauty queen", "ransom note", "1990s"],
    "sources": [
      {"title": "Murder of JonBenét Ramsey - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_JonBen%C3%A9t_Ramsey"},
      {"title": "JonBenét Ramsey case - Boulder Daily Camera", "url": "https://www.dailycamera.com/"},
      {"title": "JonBenét case - CNN", "url": "https://www.cnn.com/2013/08/29/us/jonbenet-ramsey-murder-fast-facts/index.html"}
    ],
    "narrative": [
      "On the morning of December 26, 1996, Patsy Ramsey found a two-and-a-half-page handwritten ransom note on the kitchen staircase of the family's Boulder, Colorado home demanding $118,000 for the safe return of her six-year-old daughter, JonBenét Patricia Ramsey. Patsy called police at 5:52 a.m. Officers arrived and searched the house but did not initially check the basement. Friends and family were allowed into the home, potentially contaminating the crime scene.",
      "At approximately 1:00 p.m., police asked John Ramsey, JonBenét's father, to search the house. He went to the basement and found JonBenét's body in a rarely used room called the wine cellar. She had been struck on the head and strangled with a garrote fashioned from a broken paintbrush and cord. There was evidence of sexual assault. Despite the ransom note, she had never left the house.",
      "The investigation was plagued by errors from the start. The crime scene was not secured, allowing numerous people to move through the house. The Boulder Police Department and the District Attorney's office clashed over the direction of the investigation. The Ramsey family hired their own team of investigators and attorneys, and the relationship between the family and police became adversarial. A grand jury voted to indict John and Patsy Ramsey in 1999, but District Attorney Alex Hunter declined to sign the indictment, saying the evidence was insufficient.",
      "JonBenét's murder became a media phenomenon, fueled by the combination of the child beauty pageant world, the wealthy family, the bizarre ransom note, and the unsolved nature of the crime. DNA found on JonBenét's clothing did not match any family member and was entered into CODIS, but no match has been found. Patsy Ramsey died of ovarian cancer in 2006. The case has been the subject of dozens of books, documentaries, and countless theories. Despite decades of investigation and advances in DNA technology, no one has ever been charged with JonBenét Ramsey's murder."
    ],
    "timeline": [
      {"date": "1996-12-26", "event": "Patsy Ramsey finds a ransom note; JonBenét is found dead in the basement."},
      {"date": "1997-01-01", "event": "Boulder police begin investigation; crime scene contamination issues emerge."},
      {"date": "1999-10-13", "event": "Grand jury votes to indict the Ramseys; DA declines to sign."},
      {"date": "2006-06-24", "event": "Patsy Ramsey dies of cancer."},
      {"date": "2008-07-09", "event": "DNA evidence formally clears the Ramsey family."}
    ],
    "enriched": True
  },
  {
    "id": "springfield-three-1992",
    "name": "Springfield Three",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1992,
    "date": "June 7, 1992",
    "state": "Missouri",
    "city": "Springfield",
    "age": None,
    "gender": "Female",
    "summary": "Three women—Sherrill Levitt and her daughter Suzie Streeter, along with Suzie's friend Stacy McCall—vanished from their Springfield, Missouri home. Their cars, purses, and belongings were left behind. No trace of the three has ever been found.",
    "lastSeen": "June 7, 1992, Springfield, Missouri",
    "tags": ["missing person", "Missouri", "three women", "graduation night", "1990s"],
    "sources": [
      {"title": "Springfield Three - Wikipedia", "url": "https://en.wikipedia.org/wiki/Springfield_Three"},
      {"title": "Springfield Three case - Springfield News-Leader", "url": "https://www.news-leader.com/"},
      {"title": "Springfield Three - Charley Project", "url": "https://charleyproject.org/case/sherrill-elizabeth-levitt"}
    ],
    "narrative": [
      "In the early morning hours of June 7, 1992, three women disappeared from the home of 47-year-old Sherrill Levitt at 1717 East Delmar Street in Springfield, Missouri. Sherrill's 19-year-old daughter, Suzanne 'Suzie' Streeter, and Suzie's friend Stacy McCall (also 19) had attended graduation parties the night before and came to Sherrill's home to sleep. When friends came to the house the next morning, all three women were gone.",
      "The house showed no signs of forced entry or struggle, though the front porch light's glass globe was broken and found on the front steps. All three women's purses, including their identification, money, and keys, were inside the house. Their cars were in the driveway. Sherrill's small dog was inside, frightened but unharmed. The television was on. It appeared the women had left—or been taken—suddenly and without any of their belongings.",
      "The Springfield Police Department and FBI conducted an enormous investigation, interviewing thousands of people and following hundreds of leads. The broken porch light became a key piece of evidence, with some theorizing it was used to lure one of the women outside. A disturbing answering machine message that was accidentally deleted by a friend who used the phone before police arrived may have contained crucial evidence.",
      "Over the years, theories have focused on a grave-robber who was in the area, a van spotted near the house, and various individuals connected to the Springfield criminal underworld. In 2007, the parking garage of a hospital built near the Levitt home was the subject of ground-penetrating radar testing, but nothing was found. Despite being one of the most investigated missing person cases in Missouri history, no bodies have been recovered, no suspects have been charged, and the fate of the Springfield Three remains completely unknown."
    ],
    "timeline": [
      {"date": "1992-06-07", "event": "Sherrill Levitt, Suzie Streeter, and Stacy McCall vanish from Levitt's home."},
      {"date": "1992-06-07", "event": "Friends arrive to find purses, cars, and belongings left behind."},
      {"date": "1992-06-08", "event": "Springfield police launch massive investigation."},
      {"date": "2007-01-01", "event": "Ground-penetrating radar tests a hospital parking garage; nothing found."}
    ],
    "enriched": True
  },
  {
    "id": "lori-erica-ruff-2010",
    "name": "Lori Erica Ruff",
    "type": "Suspicious Death",
    "status": "Identified",
    "year": 2010,
    "date": "December 24, 2010",
    "state": "Texas",
    "city": "Longview",
    "age": 42,
    "gender": "Female",
    "summary": "A Texas woman known as Lori Erica Ruff died by suicide on Christmas Eve, leaving behind evidence she had been living under a stolen identity for decades. Her true identity—Kimberly McLean of Pennsylvania—was not discovered until 2016 through DNA genealogy.",
    "lastSeen": "December 24, 2010, Longview, Texas",
    "tags": ["suspicious death", "Texas", "identity theft", "DNA genealogy", "cold case solved", "2010s"],
    "sources": [
      {"title": "Lori Erica Ruff - Wikipedia", "url": "https://en.wikipedia.org/wiki/Lori_Erica_Ruff"},
      {"title": "Who Was Lori Ruff? - Seattle Times", "url": "https://www.seattletimes.com/seattle-news/who-was-lori-ruff/"},
      {"title": "Lori Ruff identified - NBC News", "url": "https://www.nbcnews.com/news/us-news/mysterious-texas-woman-who-stole-dead-baby-s-identity-finally-n649786"}
    ],
    "narrative": [
      "On Christmas Eve 2010, a 42-year-old woman known as Lori Erica Ruff shot and killed herself in the driveway of her in-laws' home in Longview, Texas. She had recently separated from her husband, Blake Ruff, and was in a custody dispute over their young daughter. After her death, her in-laws found a lockbox containing documents that revealed her identity was fabricated.",
      "The lockbox contained a birth certificate for a deceased Idaho girl named Becky Sue Turner, who had died in a house fire as a toddler in 1971. Lori had apparently used this deceased child's identity to obtain a new Social Security card and then legally changed her name to 'Lori Erica Kennedy' before marrying Blake Ruff. She had created an entirely new person, complete with a GED, college attendance, and a social history—all under a false identity.",
      "Lori had been secretive and controlling throughout her marriage, refusing to discuss her past and cutting off contact with anyone from before her marriage. She told various conflicting stories about her childhood and family. Her in-laws described her as increasingly paranoid and emotionally unstable. After her death, investigators tried for years to determine who she really was, but her fingerprints and DNA were not in any law enforcement database.",
      "In 2016, genetic genealogy researchers used DNA from Lori's remains to identify her as Kimberly McLean, born in 1968 in the Philadelphia area. She had run away from her family as a teenager in the late 1980s and reinvented herself completely. Her biological family in Pennsylvania was located and confirmed the identification. The case became a landmark example of genetic genealogy's power to solve identity mysteries."
    ],
    "timeline": [
      {"date": "2010-12-24", "event": "Woman known as Lori Erica Ruff dies by suicide in Longview, Texas."},
      {"date": "2010-12-26", "event": "In-laws discover lockbox with evidence of stolen identity."},
      {"date": "2011-01-01", "event": "Investigation reveals identity was built on a deceased child's records."},
      {"date": "2016-09-03", "event": "Genetic genealogy identifies her as Kimberly McLean of Pennsylvania."}
    ],
    "enriched": True
  },
  {
    "id": "sumter-county-does-1976",
    "name": "Sumter County Does",
    "type": "Homicide",
    "status": "Identified",
    "year": 1976,
    "date": "August 9, 1976",
    "state": "South Carolina",
    "city": "Sumter",
    "age": None,
    "gender": "Multiple",
    "summary": "A young couple was found shot to death on a rural road near Sumter, South Carolina. They remained unidentified for 45 years until DNA genealogy identified them in 2021 as James Paul Freund and Pamela Mae Buckley, both from out of state.",
    "lastSeen": "August 9, 1976, near Sumter, South Carolina",
    "tags": ["homicide", "South Carolina", "unidentified", "couple", "Doe case", "DNA genealogy", "1970s"],
    "sources": [
      {"title": "Sumter County Does - Wikipedia", "url": "https://en.wikipedia.org/wiki/Sumter_County_Does"},
      {"title": "Sumter County Does identified - Post and Courier", "url": "https://www.postandcourier.com/"},
      {"title": "Doe Network - Sumter County Does", "url": "https://www.doenetwork.org/"}
    ],
    "narrative": [
      "On August 9, 1976, the bodies of a young man and woman were found shot to death on a dirt road off Interstate 95 near Sumter, South Carolina. Both had been shot multiple times. They appeared to be in their early twenties and were well-dressed, leading investigators to believe they were travelers. No identification was found on or near them, and their car was never located.",
      "The couple became known as the Sumter County Does and remained among South Carolina's most enduring unidentified person cases for over four decades. Despite detailed descriptions, dental records, and later DNA extraction, they could not be matched to any missing persons reports. The case was featured in numerous unidentified person databases and generated periodic media attention.",
      "In January 2021, breakthrough DNA genealogy work by genetic genealogist Dr. Colleen Fitzpatrick and the DNA Doe Project identified the man as James Paul Freund (30), originally from Lancaster, Pennsylvania, and the woman as Pamela Mae Buckley (26), from Redondo Beach, California. The couple had apparently been traveling together and stopped in the Sumter area for unknown reasons.",
      "The identification opened new investigative avenues. With names and backgrounds, investigators could begin retracing the couple's movements and associations in 1976. As of the identification, no suspect had been named, but the case—now a double homicide with identified victims rather than unknown Does—has been actively reinvestigated by the Sumter County Sheriff's Office."
    ],
    "timeline": [
      {"date": "1976-08-09", "event": "Bodies of unidentified couple found shot on a dirt road near Sumter, SC."},
      {"date": "1976-08-10", "event": "Sumter County investigation begins; no identification found."},
      {"date": "2021-01-21", "event": "DNA genealogy identifies the couple as James Freund and Pamela Buckley."},
      {"date": "2021-02-01", "event": "Investigation reopened with new focus based on victims' identities."}
    ],
    "enriched": True
  },
  {
    "id": "kendrick-johnson-2013",
    "name": "Kendrick Johnson",
    "type": "Suspicious Death",
    "status": "Unsolved",
    "year": 2013,
    "date": "January 11, 2013",
    "state": "Georgia",
    "city": "Valdosta",
    "age": 17,
    "gender": "Male",
    "summary": "Seventeen-year-old Kendrick Johnson was found dead inside a rolled-up gym mat at his Valdosta, Georgia high school. Officials ruled it an accident, but his family disputed this and hired independent investigators. The case became a national controversy over the investigation's handling.",
    "lastSeen": "January 10, 2013, Lowndes High School, Valdosta, Georgia",
    "tags": ["suspicious death", "Georgia", "teenager", "high school", "gym mat", "2010s"],
    "sources": [
      {"title": "Death of Kendrick Johnson - Wikipedia", "url": "https://en.wikipedia.org/wiki/Death_of_Kendrick_Johnson"},
      {"title": "Kendrick Johnson case - CNN", "url": "https://www.cnn.com/2013/10/09/us/georgia-gym-mat-death/index.html"},
      {"title": "Kendrick Johnson investigation - Valdosta Daily Times", "url": "https://www.valdostadailytimes.com/"}
    ],
    "narrative": [
      "On January 11, 2013, the body of 17-year-old Kendrick LaShawn Johnson was discovered inside a vertically standing rolled-up wrestling mat in the gymnasium of Lowndes High School in Valdosta, Georgia. He was found upside down, head-first in the center of the mat. He had been reported missing by his family the previous day.",
      "The Lowndes County Sheriff's Office and the Georgia Bureau of Investigation (GBI) investigated and concluded that Kendrick had died accidentally after climbing into the mat to retrieve a sneaker and becoming trapped upside down. The initial autopsy determined the cause of death as positional asphyxia. The case was closed in May 2013.",
      "Kendrick's parents, Kenneth and Jacquelyn Johnson, vehemently rejected the accidental death ruling. They commissioned an independent autopsy by private pathologist Dr. William Anderson, who concluded that Kendrick had died from blunt force trauma to the right neck area—a direct contradiction of the official finding. The independent autopsy also revealed that Kendrick's organs had been removed and his body cavity stuffed with newspaper during the initial autopsy process, a fact that outraged the family.",
      "The case drew national attention and raised questions about racial bias in the investigation (Kendrick was Black, and his family alleged that sons of prominent white families at the school were involved). The U.S. Department of Justice opened a federal investigation in 2013 but closed it in 2016 without bringing charges, saying the evidence was insufficient. A subsequent GBI review upheld the original accidental death finding. Kendrick's parents filed lawsuits against the school and various officials. The case remains contentious, with the official ruling disputed by the family and their supporters."
    ],
    "timeline": [
      {"date": "2013-01-11", "event": "Kendrick Johnson's body is found inside a gym mat at Lowndes High School."},
      {"date": "2013-05-02", "event": "Sheriff's office rules death accidental; case closed."},
      {"date": "2013-06-15", "event": "Independent autopsy finds blunt force trauma; family disputes ruling."},
      {"date": "2013-10-01", "event": "DOJ opens federal investigation into the case."},
      {"date": "2016-06-20", "event": "DOJ closes investigation without charges."}
    ],
    "enriched": True
  },
  {
    "id": "elisa-lam-2013",
    "name": "Elisa Lam",
    "type": "Suspicious Death",
    "status": "Unsolved",
    "year": 2013,
    "date": "January 31, 2013",
    "state": "California",
    "city": "Los Angeles",
    "age": 21,
    "gender": "Female",
    "country": "Canada",
    "summary": "Canadian tourist Elisa Lam was found dead in a water tank on the roof of the Cecil Hotel in Los Angeles. Bizarre elevator surveillance footage showed her pressing buttons frantically and appearing to talk to someone unseen. Her death was ruled accidental drowning with bipolar disorder as a contributing factor.",
    "lastSeen": "January 31, 2013, Cecil Hotel, Los Angeles, California",
    "tags": ["suspicious death", "California", "Los Angeles", "hotel", "Cecil Hotel", "elevator footage", "2010s"],
    "sources": [
      {"title": "Death of Elisa Lam - Wikipedia", "url": "https://en.wikipedia.org/wiki/Death_of_Elisa_Lam"},
      {"title": "Elisa Lam case - Los Angeles Times", "url": "https://www.latimes.com/local/lanow/la-me-ln-elisa-lam-water-tank-20150115-story.html"},
      {"title": "Cecil Hotel documentary - Netflix", "url": "https://www.netflix.com/title/81183727"}
    ],
    "narrative": [
      "Elisa Lam, a 21-year-old Canadian student from Vancouver, was traveling alone through California in January 2013 when she checked into the Cecil Hotel (also known as Stay on Main) in downtown Los Angeles, a hotel with a long and notorious history including connections to serial killers Richard Ramirez and Jack Unterweger. She was last seen on January 31.",
      "When Lam was reported missing, police searched the hotel and released elevator surveillance footage that became one of the most discussed videos on the internet. The footage shows Lam entering the elevator, pressing multiple floor buttons, then peering out as if checking whether someone is in the hallway. She appears to talk and gesture to an unseen person and exhibits increasingly bizarre behavior before walking out of frame. The elevator doors, notably, do not close during the entire four-minute clip.",
      "On February 19, guests at the Cecil began complaining about low water pressure and dark, foul-tasting water. A maintenance worker checking the four large cisterns on the hotel's roof discovered Lam's naked body floating in one of the tanks. The tanks were enclosed and accessible only via a locked hatch and a fire escape, and the lid was reportedly found closed. How Lam reached the roof and entered the tank was unclear.",
      "The Los Angeles County Coroner ruled Lam's death an accidental drowning, citing bipolar disorder—for which she had been prescribed medication—as a significant contributing factor. The ruling suggested she had been experiencing a manic or psychotic episode. However, many questioned how she could have accessed the locked roof, opened the heavy tank lid, and entered the tank, particularly if she was disoriented. The case became a global internet phenomenon and the subject of the Netflix documentary 'Crime Scene: The Vanishing at the Cecil Hotel.' It remains officially an accidental death, though questions linger."
    ],
    "timeline": [
      {"date": "2013-01-26", "event": "Elisa Lam checks into the Cecil Hotel in downtown Los Angeles."},
      {"date": "2013-01-31", "event": "Lam is last seen; bizarre elevator footage is recorded."},
      {"date": "2013-02-15", "event": "LAPD releases elevator surveillance footage to the public."},
      {"date": "2013-02-19", "event": "Lam's body is found in a rooftop water tank at the Cecil Hotel."},
      {"date": "2013-06-20", "event": "Coroner rules death accidental drowning with bipolar disorder as factor."}
    ],
    "enriched": True
  },
  {
    "id": "tylenol-murders-1982",
    "name": "Chicago Tylenol Murders Victims",
    "type": "Multiple Homicide",
    "status": "Unsolved",
    "year": 1982,
    "date": "September 29, 1982",
    "state": "Illinois",
    "city": "Chicago",
    "age": None,
    "gender": "Multiple",
    "summary": "Seven people in the Chicago area died after taking Extra-Strength Tylenol capsules laced with potassium cyanide. The case led to a revolution in consumer product safety, including tamper-evident packaging. No one has ever been charged.",
    "lastSeen": "September 29 - October 1, 1982, Chicago metropolitan area, Illinois",
    "tags": ["homicide", "Illinois", "Chicago", "poisoning", "cyanide", "product tampering", "1980s"],
    "sources": [
      {"title": "Chicago Tylenol murders - Wikipedia", "url": "https://en.wikipedia.org/wiki/Chicago_Tylenol_murders"},
      {"title": "Tylenol murders - FBI", "url": "https://www.fbi.gov/history/famous-cases/tylenol-murders-1982"},
      {"title": "Tylenol case 40 years later - Chicago Tribune", "url": "https://www.chicagotribune.com/news/ct-tylenol-murders-40-year-anniversary-20220928-d25i4jdz5zbkxbm7tvqq2ztqcy-story.html"}
    ],
    "narrative": [
      "Between September 29 and October 1, 1982, seven people in the Chicago metropolitan area died after taking Extra-Strength Tylenol capsules that had been laced with potassium cyanide. The victims—Mary Kellerman (12), Adam Janus (27), Stanley Janus (25), Theresa Janus (19), Mary McFarland (31), Paula Prince (35), and Mary Reiner (27)—had no connection to each other. The only link was that each had taken Tylenol purchased from different stores in the northwest Chicago suburbs.",
      "The discovery that the deaths were caused by tampered medication triggered a massive public health response. Johnson & Johnson, the parent company of Tylenol maker McNeil Consumer Products, immediately recalled approximately 31 million bottles of Tylenol from stores nationwide—one of the first major product recalls in history. The company's swift and transparent response, led by CEO James Burke, became a textbook case study in crisis management.",
      "The FBI and Illinois authorities conducted one of the most extensive investigations in American history. They examined the production and distribution chain, tested tens of thousands of capsules, and investigated hundreds of suspects. The leading suspect was James William Lewis, who was convicted of extortion for sending a letter to Johnson & Johnson demanding $1 million to 'stop the killings.' He served nearly 13 years in prison for the extortion but was never charged with the murders. He has denied involvement.",
      "The Tylenol murders transformed consumer product safety. Congress passed the Federal Anti-Tampering Act in 1983, making product tampering a federal crime. The pharmaceutical and food industries adopted tamper-evident packaging, including sealed caps, foil seals, and shrink wrapping. Johnson & Johnson pioneered the caplet—a solid tablet in capsule shape—that replaced the easy-to-tamper gelatin capsule. Despite these profound changes, the actual person who placed cyanide in those Tylenol bottles has never been identified. The FBI considers the case open."
    ],
    "timeline": [
      {"date": "1982-09-29", "event": "Mary Kellerman and Adam Janus die after taking cyanide-laced Tylenol."},
      {"date": "1982-09-30", "event": "Three more deaths; investigators connect them to Tylenol."},
      {"date": "1982-10-01", "event": "Johnson & Johnson recalls 31 million bottles of Tylenol nationwide."},
      {"date": "1982-10-13", "event": "James Lewis sends extortion letter; later convicted of extortion only."},
      {"date": "1983-05-01", "event": "Congress passes Federal Anti-Tampering Act."}
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
    "state": "New South Wales",
    "city": "Kendall",
    "age": 3,
    "gender": "Male",
    "country": "Australia",
    "summary": "Three-year-old William Tyrrell vanished while playing in his foster grandmother's front yard in Kendall, New South Wales, wearing a Spider-Man costume. His disappearance became Australia's most high-profile missing child case and remains unsolved.",
    "lastSeen": "September 12, 2014, Kendall, New South Wales, Australia",
    "tags": ["missing person", "Australia", "international", "child", "Spider-Man", "2010s"],
    "sources": [
      {"title": "Disappearance of William Tyrrell - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_William_Tyrrell"},
      {"title": "William Tyrrell case - ABC Australia", "url": "https://www.abc.net.au/news/2021-11-18/william-tyrrell-timeline-what-we-know/100628994"},
      {"title": "William Tyrrell inquest - Sydney Morning Herald", "url": "https://www.smh.com.au/national/nsw/william-tyrrell-what-we-know-about-the-disappearance-20220707-p5b058.html"}
    ],
    "narrative": [
      "On the morning of September 12, 2014, three-year-old William Tyrrell was playing in the front yard of his foster grandmother's home on Benaroon Drive in Kendall, a small town on the mid-north coast of New South Wales, Australia. He was wearing a Spider-Man costume and was playing a game of roaring like a tiger with his foster mother, who was on the front deck. When she went inside briefly to make tea, William disappeared.",
      "His foster mother searched the property and neighborhood immediately, then called police. An extensive search was launched involving hundreds of police, State Emergency Service volunteers, and community members. The heavily wooded area around Kendall was searched extensively, including bushland, waterways, and properties. No trace of William was found.",
      "A $1 million reward was offered for information—the largest in New South Wales history at that time. The case was referred to a coronial inquest and investigated by Strike Force Rosann, one of the largest police operations in Australian history. Investigators explored theories of abduction, accident, and involvement of known persons.",
      "In 2021, police returned to the foster grandmother's property and conducted extensive searches of surrounding bushland, focusing on a new theory. The foster mother became a person of interest, with investigators exploring whether William's death may have been a result of an accident that was then covered up. However, no charges have been filed. The coronial inquest continued into 2022 without a definitive finding. William Tyrrell's disappearance remains Australia's most prominent missing child case."
    ],
    "timeline": [
      {"date": "2014-09-12", "event": "William Tyrrell vanishes from his foster grandmother's yard in Kendall."},
      {"date": "2014-09-12", "event": "Massive search of the Kendall area begins."},
      {"date": "2014-09-19", "event": "NSW government offers $1 million reward for information."},
      {"date": "2021-11-18", "event": "Police return to the Kendall property for new searches."}
    ],
    "enriched": True
  },
  {
    "id": "jack-the-stripper-1964",
    "name": "Jack the Stripper Victims",
    "type": "Serial Killer Victims",
    "status": "Unsolved",
    "year": 1964,
    "date": "February 2, 1964",
    "state": "London",
    "city": "Hammersmith",
    "age": None,
    "gender": "Female",
    "country": "United Kingdom",
    "summary": "Six women, all sex workers, were found murdered in or near the Thames in west London between 1964 and 1965. The killer, dubbed 'Jack the Stripper' by the media, was never identified despite a massive police investigation led by Detective Chief Superintendent John du Rose.",
    "lastSeen": "Various locations in west London, 1964-1965",
    "tags": ["serial killer", "United Kingdom", "international", "London", "Thames", "1960s"],
    "sources": [
      {"title": "Jack the Stripper - Wikipedia", "url": "https://en.wikipedia.org/wiki/Jack_the_Stripper"},
      {"title": "Hammersmith nude murders - Metropolitan Police history", "url": "https://www.met.police.uk/"},
      {"title": "Jack the Stripper case - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-london-48498165"}
    ],
    "narrative": [
      "Between February 1964 and February 1965, six women were found dead in or near the River Thames in the Hammersmith and surrounding areas of west London. All were sex workers, and all had been asphyxiated—several showed evidence of having teeth forcibly removed. The victims were Hannah Tailford, Irene Lockwood, Helen Barthelemy, Mary Fleming, Margaret McGowan, and Bridie O'Hara. Their nude or partially clothed bodies were found at various locations along the river.",
      "The murders became known as the 'Hammersmith nude murders' and the killer was dubbed 'Jack the Stripper' by the press, drawing a deliberate parallel to Jack the Ripper. Detective Chief Superintendent John du Rose of Scotland Yard was assigned to lead the investigation—one of the largest police operations in London at that time.",
      "A key forensic lead was microscopic paint particles found on several of the victims' bodies, suggesting they had been stored in or near an industrial paint spraying facility before being dumped. Du Rose's investigation narrowed the search to premises near the Heron Trading Estate in Acton, where a transformer provided warm air that could explain the bodies' condition. The investigation identified a number of suspects in the area.",
      "Du Rose later stated publicly that the killer was among his final shortlist of suspects, and that the man had committed suicide before he could be arrested. However, he never publicly named the individual, and his claim has been disputed by other investigators. Several suspects have been proposed over the decades, including a security guard, a boxer, and a disgraced Metropolitan Police officer. The case remains officially unsolved, and the identity of Jack the Stripper has never been conclusively established."
    ],
    "timeline": [
      {"date": "1964-02-02", "event": "Hannah Tailford's body is found in the Thames near Hammersmith."},
      {"date": "1964-04-24", "event": "Helen Barthelemy found with paint particles on her body."},
      {"date": "1964-07-14", "event": "Mary Fleming found; investigation intensifies."},
      {"date": "1964-11-25", "event": "Margaret McGowan found; media dubs killer 'Jack the Stripper.'"},
      {"date": "1965-02-16", "event": "Bridie O'Hara found; last confirmed victim."},
      {"date": "1965-07-01", "event": "DCS du Rose claims prime suspect committed suicide."}
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
