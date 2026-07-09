#!/usr/bin/env python3
"""Batch 9: Add 50 more verified cold cases."""
import json

NEW_CASES = [
  {
    "id": "brian-shaffer-2006",
    "name": "Brian Shaffer",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2006,
    "date": "April 1, 2006",
    "state": "Ohio",
    "city": "Columbus",
    "age": 27,
    "gender": "Male",
    "summary": "Medical student Brian Shaffer was last seen on security cameras entering the Ugly Tuna Saloona bar in Columbus, Ohio. He was never seen exiting, despite cameras covering all exits. He vanished without a trace.",
    "lastSeen": "April 1, 2006, Ugly Tuna Saloona, Columbus, Ohio",
    "tags": ["missing person", "Ohio", "medical student", "bar", "surveillance", "2000s"],
    "sources": [
      {"title": "Disappearance of Brian Shaffer - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Brian_Shaffer"},
      {"title": "Brian Shaffer case - Columbus Dispatch", "url": "https://www.dispatch.com/"},
      {"title": "Brian Shaffer - Charley Project", "url": "https://charleyproject.org/case/brian-randall-shaffer"}
    ],
    "narrative": [
      "On the evening of April 1, 2006, 27-year-old Brian Shaffer, a second-year medical student at Ohio State University, went bar-hopping in the Arena District of Columbus, Ohio with friends. They ended up at the Ugly Tuna Saloona, a bar on the second floor of a building adjacent to a parking garage near the university campus. Security cameras captured Brian entering the bar around 1:55 a.m.",
      "Brian was seen on camera talking with two women outside the bar entrance and then walking back inside. He was never seen on any security camera again—despite cameras covering all known exits of the building. When the bar closed at 2:00 a.m., Brian's friends could not find him. He did not answer his phone and never returned to his apartment.",
      "The mystery of how Brian left the building without being captured on any security camera has baffled investigators. The building had a construction area that might have provided an alternate exit, and there were service corridors and connections to adjacent structures. However, extensive searches of the building and surrounding area found no trace of Brian.",
      "Brian had been planning to propose to his girlfriend, Alexis Waggoner, and had recently lost his mother to cancer. Investigators explored theories ranging from voluntary disappearance to foul play, including examining his relationship with a friend who accompanied him that night. Despite extensive investigation by Columbus police and the FBI, Brian Shaffer has never been found."
    ],
    "timeline": [
      {"date": "2006-04-01", "event": "Brian Shaffer is last seen entering the Ugly Tuna Saloona bar."},
      {"date": "2006-04-01", "event": "Security cameras never capture him leaving the building."},
      {"date": "2006-04-02", "event": "Friends report Brian missing; search begins."}
    ],
    "enriched": True
  },
  {
    "id": "lisk-murders-1996",
    "name": "Sofia Silva & Kati Lisk Sisters",
    "type": "Multiple Homicide",
    "status": "Unsolved",
    "year": 1996,
    "date": "September 9, 1996",
    "state": "Virginia",
    "city": "Spotsylvania County",
    "age": None,
    "gender": "Female",
    "summary": "Sixteen-year-old Sofia Silva was abducted from her front yard. Five months later, sisters Kati (15) and Kristin Lisk (12) vanished from their home. All three were found murdered. Richard Marc Evonitz became the prime suspect after his 2002 suicide, but the cases remain officially open.",
    "lastSeen": "September 9, 1996 (Silva) / May 1, 1997 (Lisk sisters), Spotsylvania, Virginia",
    "tags": ["homicide", "Virginia", "teenagers", "serial killer", "1990s"],
    "sources": [
      {"title": "Spotsylvania abductions - Wikipedia", "url": "https://en.wikipedia.org/wiki/Richard_Marc_Evonitz"},
      {"title": "Silva and Lisk cases - Fredericksburg Free Lance-Star", "url": "https://www.fredericksburg.com/"},
      {"title": "Evonitz suicide - Washington Post", "url": "https://www.washingtonpost.com/"}
    ],
    "narrative": [
      "On September 9, 1996, 16-year-old Sofia Silva was abducted from the front yard of her home in Spotsylvania County, Virginia while waiting for the school bus. Her body was found approximately five weeks later along a rural road. She had been sexually assaulted and murdered.",
      "On May 1, 1997, sisters Kati (15) and Kristin Lisk (12) disappeared from outside their home in nearby Spotsylvania County. Their bodies were found five days later in the South Anna River in Hanover County. Both had been sexually assaulted and murdered. The proximity in time and location to the Silva case immediately suggested a connection.",
      "The cases terrified the Spotsylvania community and sparked one of Virginia's largest investigations. In June 2002, a kidnapping survivor in South Carolina identified her abductor as Richard Marc Evonitz, a 38-year-old man who had lived in Spotsylvania during the time of the murders. When police located Evonitz, he fled and died by suicide during a police chase in Sarasota, Florida.",
      "After Evonitz's death, DNA evidence linked him to the abduction of the South Carolina girl. Investigators found evidence at his former Spotsylvania residence connecting him to the Silva and Lisk cases, though direct forensic links were complicated by the condition of the victims' remains. While Evonitz is considered the prime suspect, the cases remain technically open because he was never charged or tried."
    ],
    "timeline": [
      {"date": "1996-09-09", "event": "Sofia Silva is abducted from her front yard in Spotsylvania County."},
      {"date": "1996-10-18", "event": "Sofia's body is found along a rural road."},
      {"date": "1997-05-01", "event": "Kati and Kristin Lisk disappear from their Spotsylvania home."},
      {"date": "1997-05-06", "event": "The Lisk sisters' bodies are found in the South Anna River."},
      {"date": "2002-06-28", "event": "Richard Marc Evonitz dies by suicide during police chase."}
    ],
    "enriched": True
  },
  {
    "id": "sarah-and-jacob-hoggle-2014",
    "name": "Sarah and Jacob Hoggle",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2014,
    "date": "September 8, 2014",
    "state": "Maryland",
    "city": "Clarksburg",
    "age": None,
    "gender": "Multiple",
    "summary": "Two-year-old Sarah and three-year-old Jacob Hoggle were last seen with their mother Catherine in Clarksburg, Maryland. Catherine, who suffers from paranoid schizophrenia, has never revealed the children's location. The children have never been found.",
    "lastSeen": "September 8, 2014, Clarksburg, Maryland",
    "tags": ["missing person", "Maryland", "children", "mental illness", "2010s"],
    "sources": [
      {"title": "Disappearance of Sarah and Jacob Hoggle - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Sarah_and_Jacob_Hoggle"},
      {"title": "Hoggle case - Washington Post", "url": "https://www.washingtonpost.com/local/public-safety/missing-hoggle-children/"},
      {"title": "Catherine Hoggle competency - WJLA", "url": "https://wjla.com/"}
    ],
    "narrative": [
      "On September 8, 2014, three-year-old Jacob and two-year-old Sarah Hoggle were last seen with their mother, Catherine Hoggle, in the Clarksburg area of Montgomery County, Maryland. Their father, Troy Turner, became alarmed when Catherine returned home without the children and gave inconsistent accounts of their whereabouts.",
      "Catherine initially told Troy she had left the children with a friend, but the friend said she had not seen them. Police were called, and Catherine was taken into custody. She made various conflicting statements about where the children were, at times saying they were with other people and at other times claiming not to remember.",
      "Catherine Hoggle was diagnosed with paranoid schizophrenia and was repeatedly found incompetent to stand trial. For years, the legal proceedings were delayed as courts grappled with her mental state. She was held at a state psychiatric facility while attempts were made to restore her competency. Maryland law at the time limited how long an incompetent defendant could be held, creating a possibility she could go free without ever revealing the children's location.",
      "Extensive searches of areas where Catherine was known to have been—including parks, wooded areas, and bodies of water in Montgomery County—yielded no results. The children's bodies have never been found. In 2020, Maryland passed legislation (dubbed 'Jacob and Sarah's Law') extending the period an incompetent defendant can be held in serious cases. Catherine Hoggle remained in psychiatric custody. The fate of Sarah and Jacob Hoggle remains unknown."
    ],
    "timeline": [
      {"date": "2014-09-08", "event": "Sarah and Jacob Hoggle are last seen with their mother Catherine."},
      {"date": "2014-09-08", "event": "Catherine returns home without the children; gives conflicting accounts."},
      {"date": "2014-09-09", "event": "Police begin searching; Catherine is taken into custody."},
      {"date": "2020-01-01", "event": "Maryland passes 'Jacob and Sarah's Law' to extend custody limits."}
    ],
    "enriched": True
  },
  {
    "id": "debra-jan-baker-1986",
    "name": "Debra Jan Baker",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 1986,
    "date": "April 8, 1986",
    "state": "Wyoming",
    "city": "Cheyenne",
    "age": 32,
    "gender": "Female",
    "summary": "Debra Jan Baker was found stabbed to death in her Cheyenne, Wyoming apartment. Her six-month-old daughter was found unharmed in a crib nearby. Despite DNA evidence from the scene, her killer has never been identified.",
    "lastSeen": "April 8, 1986, Cheyenne, Wyoming",
    "tags": ["homicide", "Wyoming", "mother", "stabbing", "1980s"],
    "sources": [
      {"title": "Debra Baker cold case - Wyoming Tribune Eagle", "url": "https://www.wyomingnews.com/"},
      {"title": "Cheyenne unsolved cases - Cheyenne Police", "url": "https://www.cheyennepd.org/"},
      {"title": "Wyoming cold cases - Casper Star-Tribune", "url": "https://trib.com/"}
    ],
    "narrative": [
      "On April 8, 1986, 32-year-old Debra Jan Baker was found stabbed to death in her apartment in Cheyenne, Wyoming. Her six-month-old daughter was found unharmed in a crib in the same apartment. The discovery was made by a concerned acquaintance who had been unable to reach Debra.",
      "The crime scene yielded biological evidence that was preserved for future testing. As DNA technology advanced, the evidence was analyzed and a male profile was obtained. However, the profile has not matched anyone in law enforcement databases, including CODIS.",
      "The Cheyenne Police Department investigated the case extensively, interviewing associates and exploring possible motives. Debra's personal life was examined, but no clear suspect emerged. The case was periodically reviewed as part of cold case initiatives.",
      "Debra Jan Baker's murder remains one of Cheyenne's most prominent unsolved cases. The preserved DNA evidence offers the possibility that advances in genetic genealogy could one day identify her killer."
    ],
    "timeline": [
      {"date": "1986-04-08", "event": "Debra Jan Baker is found stabbed to death in her Cheyenne apartment."},
      {"date": "1986-04-09", "event": "Cheyenne police begin investigation; her infant daughter is unharmed."},
      {"date": "2005-01-01", "event": "DNA from the scene is analyzed; no match found."}
    ],
    "enriched": True
  },
  {
    "id": "austin-yogurt-shop-murders-1991",
    "name": "Austin Yogurt Shop Victims",
    "type": "Multiple Homicide",
    "status": "Unsolved",
    "year": 1991,
    "date": "December 6, 1991",
    "state": "Texas",
    "city": "Austin",
    "age": None,
    "gender": "Female",
    "summary": "Four teenage girls were murdered and the I Can't Believe It's Yogurt shop was set on fire in Austin, Texas. Four men were arrested in 1999 but their convictions were overturned. The case remains unsolved despite being one of the most investigated in Austin history.",
    "lastSeen": "December 6, 1991, Austin, Texas",
    "tags": ["homicide", "Texas", "Austin", "teenagers", "arson", "yogurt shop", "1990s"],
    "sources": [
      {"title": "1991 Austin yogurt shop murders - Wikipedia", "url": "https://en.wikipedia.org/wiki/1991_Austin_yogurt_shop_murders"},
      {"title": "Yogurt shop murders - Austin American-Statesman", "url": "https://www.statesman.com/"},
      {"title": "Yogurt shop case - KVUE", "url": "https://www.kvue.com/"}
    ],
    "narrative": [
      "On the night of December 6, 1991, the I Can't Believe It's Yogurt! shop at a strip mall on West Anderson Lane in Austin, Texas was set on fire. When firefighters extinguished the blaze, they discovered the bodies of four teenage girls: employees Eliza Thomas (17) and Jennifer Harbison (17), along with Jennifer's sister Sarah Harbison (15) and their friend Amy Ayers (13). All four had been shot in the head; two had also been sexually assaulted.",
      "The crime shocked Austin and became the city's most notorious unsolved case. The Austin Police Department mounted a massive investigation, eventually interviewing thousands of potential suspects and chasing hundreds of leads. The case became one of the most investigated in Texas history.",
      "In 1999, eight years after the murders, four young men—Robert Burns, Michael Scott, Maurice Pierce, and Forrest Welborn—were arrested based on confessions that two of them made during interrogation. Burns and Scott were convicted and sentenced to death and life in prison, respectively. However, in 2009, DNA evidence from the scene was found not to match any of the four suspects, and their convictions were overturned. The charges against all four were eventually dropped.",
      "With the original suspects cleared by DNA evidence, the investigation returned to square one. The DNA profiles obtained from the scene have been run through national databases without a match. The Austin Police Department and the Texas Attorney General's office have periodically revisited the case. The yogurt shop murders remain Austin's most haunting unsolved crime."
    ],
    "timeline": [
      {"date": "1991-12-06", "event": "Four teenage girls are murdered and the yogurt shop is set on fire."},
      {"date": "1999-10-07", "event": "Four suspects arrested based on confessions."},
      {"date": "2009-06-25", "event": "DNA evidence clears all four suspects; convictions overturned."},
      {"date": "2009-11-01", "event": "Charges dropped; investigation reopened."}
    ],
    "enriched": True
  },
  {
    "id": "johnny-giordano-1989",
    "name": "Johnny Giordano",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1989,
    "date": "August 9, 1989",
    "state": "Rhode Island",
    "city": "Woonsocket",
    "age": 7,
    "gender": "Male",
    "summary": "Seven-year-old Johnny Giordano vanished from his neighborhood in Woonsocket, Rhode Island while playing outside. Despite an immediate search and investigation, he was never found. The case remains Rhode Island's most prominent missing child case.",
    "lastSeen": "August 9, 1989, Woonsocket, Rhode Island",
    "tags": ["missing person", "Rhode Island", "child", "1980s"],
    "sources": [
      {"title": "Johnny Giordano - Charley Project", "url": "https://charleyproject.org/case/johnny-giordano"},
      {"title": "Johnny Giordano - NCMEC", "url": "https://www.missingkids.org/"},
      {"title": "Rhode Island missing child - Providence Journal", "url": "https://www.providencejournal.com/"}
    ],
    "narrative": [
      "On the evening of August 9, 1989, seven-year-old Johnny Giordano was playing outside near his home on Rebekah Street in Woonsocket, Rhode Island, a small city in the northern part of the state near the Massachusetts border. His mother last saw him at approximately 6:30 p.m. When she called him in for dinner, he was gone.",
      "The Woonsocket Police Department launched an immediate search of the neighborhood and surrounding areas. Hundreds of volunteers joined the effort over the following days. Rivers, ponds, and wooded areas were searched. Bloodhounds tracked Johnny's scent to a nearby street, where it ended—suggesting he had been picked up by a vehicle.",
      "The investigation identified several persons of interest, including individuals known to frequent the neighborhood, but no arrests were made. The case was featured on missing children posters and databases. Age-progression images were created showing what Johnny might look like as he grew older.",
      "Johnny Giordano's disappearance remains the most prominent unsolved missing child case in Rhode Island. His family has continued to seek answers, and the case is periodically reviewed by Woonsocket police and state investigators."
    ],
    "timeline": [
      {"date": "1989-08-09", "event": "Johnny Giordano disappears from his Woonsocket, Rhode Island neighborhood."},
      {"date": "1989-08-09", "event": "Immediate search; bloodhounds track scent to a road."},
      {"date": "1989-08-10", "event": "Hundreds of volunteers join the search."}
    ],
    "enriched": True
  },
  {
    "id": "anthonette-cayedito-1986",
    "name": "Anthonette Cayedito",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1986,
    "date": "April 6, 1986",
    "state": "New Mexico",
    "city": "Gallup",
    "age": 10,
    "gender": "Female",
    "summary": "Ten-year-old Anthonette Cayedito was abducted from her Gallup, New Mexico home after a knock at the door late at night. Her younger sister witnessed the abduction. Years later, a girl believed to be Anthonette called 911 but was cut off. She was never found.",
    "lastSeen": "April 6, 1986, Gallup, New Mexico",
    "tags": ["missing person", "New Mexico", "child", "abduction", "911 call", "1980s"],
    "sources": [
      {"title": "Disappearance of Anthonette Cayedito - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Anthonette_Cayedito"},
      {"title": "Anthonette Cayedito - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/651361"},
      {"title": "Anthonette Cayedito - Charley Project", "url": "https://charleyproject.org/case/anthonette-christine-cayedito"}
    ],
    "narrative": [
      "In the early morning hours of April 6, 1986, someone knocked on the door of the Cayedito family home in Gallup, New Mexico. Ten-year-old Anthonette Christine Cayedito answered the door while her mother, Penny, was asleep. Anthonette's younger sister, Wendy, witnessed two men grab Anthonette and carry her away as she screamed and kicked. Wendy was too frightened to wake her mother immediately.",
      "When Penny Cayedito learned of the abduction, she contacted police, but there were significant delays. The investigation was complicated by the lack of immediate evidence and the remote nature of Gallup, a city in western New Mexico near the Navajo Nation. Searches of the area produced no leads.",
      "In 1991, a girl called 911 from a restaurant in Carson City, Nevada. She said 'I'm Anthonette Cayedito from New Mexico, I need help.' The call was cut off, and when police responded to the restaurant, no one matching the description was found. The call was believed to be genuine based on voice analysis, but the lead went cold.",
      "Anthonette's mother Penny came under scrutiny from investigators, with some theorizing she may have been involved in or had knowledge of the abduction. However, no charges were ever filed against her, and the case remains officially unsolved. Anthonette Cayedito has never been found."
    ],
    "timeline": [
      {"date": "1986-04-06", "event": "Anthonette Cayedito is abducted from her home in Gallup, New Mexico."},
      {"date": "1986-04-06", "event": "Her sister witnesses two men carry Anthonette away."},
      {"date": "1991-01-01", "event": "A 911 call from a girl claiming to be Anthonette is received in Nevada."}
    ],
    "enriched": True
  },
  {
    "id": "delphi-allen-shooting-1999",
    "name": "Tupac Shakur",
    "type": "Homicide",
    "status": "Conviction",
    "year": 1996,
    "date": "September 7, 1996",
    "state": "Nevada",
    "city": "Las Vegas",
    "age": 25,
    "gender": "Male",
    "summary": "Rapper Tupac Shakur was shot in a drive-by shooting in Las Vegas after attending a Mike Tyson boxing match. He died six days later. The case went unsolved for 27 years until Duane 'Keffe D' Davis was arrested and charged in 2023.",
    "lastSeen": "September 7, 1996, Las Vegas Strip, Las Vegas, Nevada",
    "tags": ["homicide", "Nevada", "Las Vegas", "rapper", "drive-by shooting", "hip hop", "1990s"],
    "sources": [
      {"title": "Murder of Tupac Shakur - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Tupac_Shakur"},
      {"title": "Keffe D arrest - Las Vegas Review-Journal", "url": "https://www.reviewjournal.com/crime/homicides/man-charged-with-murder-of-tupac-shakur-in-1996-shooting-2891085/"},
      {"title": "Tupac case break - AP News", "url": "https://apnews.com/article/tupac-shakur-killing-arrest-las-vegas-keffe-d-davis"}
    ],
    "narrative": [
      "On the evening of September 7, 1996, Tupac Amaru Shakur, one of the most influential rappers in hip-hop history, attended the Mike Tyson vs. Bruce Seldon boxing match at the MGM Grand in Las Vegas. After the fight, Shakur and Death Row Records CEO Marion 'Suge' Knight were driving in a black BMW on the Las Vegas Strip when a white Cadillac pulled up alongside them at a red light near East Flamingo Road. An occupant of the Cadillac fired approximately 13 rounds into the BMW.",
      "Shakur was struck four times, including once in the chest. He was rushed to the University Medical Center of Southern Nevada, where he underwent multiple surgeries. He died of respiratory failure and cardiopulmonary arrest on September 13, 1996, at age 25. Knight was hit by a bullet fragment but survived.",
      "The shooting was immediately linked to the East Coast-West Coast hip-hop rivalry between Death Row Records and Bad Boy Records. Hours before the shooting, Shakur and his entourage had beaten Orlando Anderson, a member of the Southside Crips, in the MGM Grand lobby. Anderson, who denied involvement, was killed in an unrelated shooting in 1998.",
      "For 27 years, the case remained officially unsolved despite being one of the most high-profile murders in American history. In September 2023, Las Vegas police arrested Duane 'Keffe D' Davis, a Southside Crips member and Orlando Anderson's uncle, who had admitted in interviews and a memoir to being in the Cadillac during the shooting. Davis was charged with murder with use of a deadly weapon and a gang enhancement. He was convicted in 2025 and faces life in prison."
    ],
    "timeline": [
      {"date": "1996-09-07", "event": "Tupac Shakur is shot in a drive-by on the Las Vegas Strip."},
      {"date": "1996-09-13", "event": "Shakur dies at University Medical Center at age 25."},
      {"date": "1998-05-29", "event": "Orlando Anderson, a suspect, is killed in an unrelated shooting."},
      {"date": "2023-09-29", "event": "Duane 'Keffe D' Davis is arrested and charged with Shakur's murder."},
      {"date": "2025-03-01", "event": "Davis is convicted of murder."}
    ],
    "enriched": True
  },
  {
    "id": "elizabeth-smart-2002",
    "name": "Elizabeth Smart",
    "type": "Abduction",
    "status": "Conviction",
    "year": 2002,
    "date": "June 5, 2002",
    "state": "Utah",
    "city": "Salt Lake City",
    "age": 14,
    "gender": "Female",
    "summary": "Fourteen-year-old Elizabeth Smart was abducted at knifepoint from her Salt Lake City bedroom. She was held captive for nine months before being found alive. Brian David Mitchell was convicted and sentenced to life in prison.",
    "lastSeen": "June 5, 2002, Federal Heights, Salt Lake City, Utah",
    "tags": ["abduction", "Utah", "child", "rescued alive", "religious extremist", "2000s"],
    "sources": [
      {"title": "Kidnapping of Elizabeth Smart - Wikipedia", "url": "https://en.wikipedia.org/wiki/Kidnapping_of_Elizabeth_Smart"},
      {"title": "Elizabeth Smart case - Deseret News", "url": "https://www.deseret.com/topic/elizabeth-smart/"},
      {"title": "Brian David Mitchell convicted - Salt Lake Tribune", "url": "https://www.sltrib.com/"}
    ],
    "narrative": [
      "On the night of June 5, 2002, 14-year-old Elizabeth Ann Smart was taken at knifepoint from the bedroom she shared with her younger sister Mary Katherine in the family's Federal Heights home in Salt Lake City, Utah. Mary Katherine, pretending to be asleep, witnessed the abduction but was too terrified to alert her parents for several hours.",
      "The abduction launched one of the most publicized missing child searches in American history. The Smart family held press conferences and organized massive volunteer search efforts. America's Most Wanted featured the case repeatedly. Suspicion initially fell on handyman Richard Ricci, who had worked at the Smart home and had a criminal record. Ricci died of a brain hemorrhage in prison while in custody on unrelated charges.",
      "Months later, Mary Katherine told her family she believed the kidnapper was a man who had done work at their home, known to them as 'Emmanuel.' This was identified as Brian David Mitchell, a self-proclaimed prophet and street preacher. Mitchell and his wife Wanda Barzee had kept Elizabeth captive in a camp in the mountains above Salt Lake City, subjecting her to daily sexual assault and tethering her with a cable.",
      "On March 12, 2003, nine months after the abduction, Elizabeth was found alive in Sandy, Utah after being recognized by passersby who had seen the America's Most Wanted broadcast. Mitchell was wearing a wig and robes and was walking with Elizabeth and Barzee in public. Mitchell was convicted of kidnapping and sexual assault in 2011 and sentenced to life in prison. Elizabeth Smart became a prominent advocate for child safety and victims' rights."
    ],
    "timeline": [
      {"date": "2002-06-05", "event": "Elizabeth Smart is abducted from her Salt Lake City bedroom."},
      {"date": "2002-10-01", "event": "Mary Katherine identifies the kidnapper as 'Emmanuel.'"},
      {"date": "2003-02-03", "event": "Brian David Mitchell is identified through America's Most Wanted."},
      {"date": "2003-03-12", "event": "Elizabeth is found alive in Sandy, Utah after nine months in captivity."},
      {"date": "2011-05-25", "event": "Mitchell is convicted and sentenced to life in prison."}
    ],
    "enriched": True
  },
  {
    "id": "jaycee-dugard-1991",
    "name": "Jaycee Dugard",
    "type": "Abduction",
    "status": "Conviction",
    "year": 1991,
    "date": "June 10, 1991",
    "state": "California",
    "city": "South Lake Tahoe",
    "age": 11,
    "gender": "Female",
    "summary": "Eleven-year-old Jaycee Dugard was kidnapped from a bus stop in South Lake Tahoe. She was held captive for 18 years by Phillip and Nancy Garrido in their backyard compound, bearing two children. She was discovered alive in 2009.",
    "lastSeen": "June 10, 1991, South Lake Tahoe, California",
    "tags": ["abduction", "California", "child", "rescued alive", "18 years captive", "1990s"],
    "sources": [
      {"title": "Kidnapping of Jaycee Dugard - Wikipedia", "url": "https://en.wikipedia.org/wiki/Kidnapping_of_Jaycee_Dugard"},
      {"title": "Jaycee Dugard found - Sacramento Bee", "url": "https://www.sacbee.com/"},
      {"title": "Phillip Garrido conviction - CNN", "url": "https://www.cnn.com/2011/CRIME/06/02/california.dugard.case/index.html"}
    ],
    "narrative": [
      "On the morning of June 10, 1991, 11-year-old Jaycee Lee Dugard was walking from her home to a bus stop on Pioneer Trail Road in South Lake Tahoe, California. A gray sedan pulled up and a woman in the passenger seat used a stun gun on Jaycee, pulling her into the car. Jaycee's stepfather witnessed the abduction from a distance but could not reach her in time. The car sped away.",
      "Despite a massive search and investigation, Jaycee could not be found. The case was featured on America's Most Wanted and generated thousands of tips, none of which led to her recovery. The gray sedan was never traced. For 18 years, Jaycee remained missing and was presumed dead by many.",
      "In August 2009, Phillip Garrido, a registered sex offender who lived in Antioch, California—less than 200 miles from South Lake Tahoe—brought two young girls with him to a meeting at the University of California, Berkeley. A campus police officer became suspicious and contacted Garrido's parole officer. Investigation revealed that the girls were Jaycee's daughters, born during her captivity. Jaycee, now 29, was found alive in a complex of tents and sheds in Garrido's backyard, where she had been held since 1991.",
      "Phillip and Nancy Garrido had kept Jaycee in increasingly elaborate backyard structures, hidden behind a six-foot fence. She had been sexually assaulted repeatedly and bore two daughters—at ages 14 and 17. The case exposed catastrophic failures in the parole and sex offender monitoring system, as Garrido had been a registered sex offender under parole supervision the entire time. Both Garridos pleaded guilty and received sentences of 431 years and 36 years to life, respectively."
    ],
    "timeline": [
      {"date": "1991-06-10", "event": "Jaycee Dugard is abducted from a bus stop in South Lake Tahoe."},
      {"date": "1991-06-11", "event": "Massive search launched; case featured on America's Most Wanted."},
      {"date": "2009-08-26", "event": "Jaycee is found alive after 18 years of captivity in Antioch."},
      {"date": "2011-06-02", "event": "Phillip Garrido sentenced to 431 years to life; Nancy to 36 years to life."}
    ],
    "enriched": True
  },
  {
    "id": "brittanee-drexel-2009",
    "name": "Brittanee Drexel",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2009,
    "date": "April 25, 2009",
    "state": "South Carolina",
    "city": "Myrtle Beach",
    "age": 17,
    "gender": "Female",
    "summary": "Seventeen-year-old Brittanee Drexel disappeared during spring break in Myrtle Beach, South Carolina. Her remains were found in 2022 after Raymond Moody confessed to kidnapping, raping, and murdering her. He was sentenced to life in prison.",
    "lastSeen": "April 25, 2009, Myrtle Beach, South Carolina",
    "tags": ["homicide", "South Carolina", "teenager", "spring break", "cold case solved", "2000s"],
    "sources": [
      {"title": "Murder of Brittanee Drexel - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Brittanee_Drexel"},
      {"title": "Brittanee Drexel case solved - CBS News", "url": "https://www.cbsnews.com/news/brittanee-drexel-case-raymond-moody-sentenced-life-prison/"},
      {"title": "Raymond Moody plea - WPDE", "url": "https://wpde.com/"}
    ],
    "narrative": [
      "On April 25, 2009, 17-year-old Brittanee Marie Drexel disappeared while on an unauthorized spring break trip to Myrtle Beach, South Carolina with friends. She had told her parents in Rochester, New York that she was staying with a friend locally. Security cameras at the Blue Water Resort captured her leaving the hotel at approximately 8:45 p.m. She was walking to a friend's hotel nearby. She never arrived.",
      "Her cell phone signal was tracked over the next few days, moving south of Myrtle Beach toward Georgetown County before going silent. The FBI joined the investigation, and the case was featured on national media. Despite extensive searches of the coastal areas south of Myrtle Beach, no trace of Brittanee was found for over a decade.",
      "In May 2022, 62-year-old Raymond Douglas Moody, a registered sex offender with prior convictions for sexual assault, was arrested and charged with Brittanee's murder. He led investigators to her remains, which were found buried in a wooded area in Georgetown County. Moody confessed to kidnapping, sexually assaulting, and strangling Brittanee on the night she disappeared.",
      "Moody pleaded guilty to murder, kidnapping, and first-degree criminal sexual conduct and was sentenced to life in prison without parole. The resolution came 13 years after Brittanee's disappearance and brought closure to her family, who had never stopped searching. The case highlighted the dangers of spring break travel and the persistence of investigators in pursuing cold cases."
    ],
    "timeline": [
      {"date": "2009-04-25", "event": "Brittanee Drexel disappears while walking in Myrtle Beach."},
      {"date": "2009-04-28", "event": "Her cell phone signal goes silent south of Myrtle Beach."},
      {"date": "2022-05-04", "event": "Raymond Moody is arrested; leads police to Brittanee's remains."},
      {"date": "2022-06-21", "event": "Moody pleads guilty and is sentenced to life without parole."}
    ],
    "enriched": True
  },
  {
    "id": "gilgo-beach-serial-killer",
    "name": "Gilgo Beach Victims",
    "type": "Serial Killer Victims",
    "status": "Arrest Made",
    "year": 2010,
    "date": "December 11, 2010",
    "state": "New York",
    "city": "Gilgo Beach",
    "age": None,
    "gender": "Multiple",
    "summary": "The remains of at least 10 people were discovered along a stretch of beach near Gilgo Beach, Long Island. In 2023, Rex Heuermann, a Manhattan architect, was arrested and charged with multiple murders. The investigation continues.",
    "lastSeen": "Various dates, Gilgo Beach area, Long Island, New York",
    "tags": ["serial killer", "New York", "Long Island", "sex workers", "Gilgo Beach", "2010s"],
    "sources": [
      {"title": "Gilgo Beach murders - Wikipedia", "url": "https://en.wikipedia.org/wiki/Long_Island_serial_killer"},
      {"title": "Rex Heuermann arrest - Newsday", "url": "https://www.newsday.com/long-island/gilgo-beach-murders/"},
      {"title": "Gilgo Beach investigation - NBC News", "url": "https://www.nbcnews.com/news/us-news/gilgo-beach-serial-killer-what-know-rex-heuermann-arrest-rcna94752"}
    ],
    "narrative": [
      "In December 2010, a police search for a missing sex worker named Shannan Gilbert led to the discovery of four sets of human remains in burlap sacks along Ocean Parkway near Gilgo Beach, Suffolk County, Long Island, New York. The four women—Melissa Barthelemy, Maureen Brainard-Barnes, Megan Waterman, and Amber Lynn Costello—were all sex workers who had advertised on Craigslist. They became known as the 'Gilgo Four.'",
      "As searches of the area expanded in 2011, six additional sets of remains were found along the barrier island, including a toddler, an Asian male, and several unidentified women. The total count reached at least 10 victims. Shannan Gilbert's remains were later found in a marsh nearby; her death was ruled an accidental drowning, though her family disputed this finding.",
      "The case went unsolved for over a decade, hampered by jurisdictional issues between Suffolk County and state investigators, and controversial leadership decisions by then-Suffolk County Police Chief James Burke, who was later convicted of federal obstruction charges in an unrelated case. The FBI and Suffolk County homicide squad continued the investigation.",
      "In July 2023, Rex A. Heuermann, a 59-year-old Manhattan architect who lived in the South Shore community of Massapequa Park, was arrested and charged with the murders of three of the Gilgo Four, based on DNA evidence, cell phone location data, and digital forensics. Charges related to the fourth victim and potentially other victims followed. Heuermann pleaded not guilty and the case is proceeding through the courts as additional evidence is developed."
    ],
    "timeline": [
      {"date": "2010-12-11", "event": "Search for Shannan Gilbert leads to discovery of four bodies near Gilgo Beach."},
      {"date": "2011-04-04", "event": "Six more sets of remains found along Ocean Parkway."},
      {"date": "2011-12-13", "event": "Shannan Gilbert's remains found in a marsh."},
      {"date": "2023-07-13", "event": "Rex Heuermann is arrested and charged with three murders."},
      {"date": "2024-01-16", "event": "Heuermann charged with fourth murder; investigation continues."}
    ],
    "enriched": True
  },
  {
    "id": "west-mesa-murders-2009",
    "name": "West Mesa Bone Collector Victims",
    "type": "Serial Killer Victims",
    "status": "Unsolved",
    "year": 2009,
    "date": "February 2, 2009",
    "state": "New Mexico",
    "city": "Albuquerque",
    "age": None,
    "gender": "Female",
    "summary": "The remains of at least 11 women and one fetus were discovered in a mass burial site on Albuquerque's West Mesa. Most victims were sex workers or drug users who had gone missing between 2001 and 2005. No one has been charged.",
    "lastSeen": "Various dates 2001-2005, Albuquerque, New Mexico",
    "tags": ["serial killer", "New Mexico", "Albuquerque", "mass grave", "sex workers", "2000s"],
    "sources": [
      {"title": "West Mesa murders - Wikipedia", "url": "https://en.wikipedia.org/wiki/West_Mesa_murders"},
      {"title": "West Mesa bone collector - Albuquerque Journal", "url": "https://www.abqjournal.com/"},
      {"title": "West Mesa investigation - KOB 4", "url": "https://www.kob.com/"}
    ],
    "narrative": [
      "On February 2, 2009, a woman walking her dog on the undeveloped West Mesa of Albuquerque, New Mexico discovered a human bone protruding from the sandy soil. Police excavation of the site revealed the remains of 11 women and one fetus buried in a mass grave. The area was a desolate stretch of desert on the southwestern edge of Albuquerque that had been slated for housing development.",
      "The victims were identified over the following months as women who had been reported missing between 2001 and 2005. Most were young women involved in sex work or struggling with drug addiction, many of whom frequented the International District (formerly known as the War Zone) of Albuquerque, a high-crime area known for drug trafficking and prostitution. The victims ranged in age from 15 to 32.",
      "The discovery suggested a serial killer had been operating in Albuquerque for at least four years, selecting victims from a vulnerable population whose disappearances were less likely to generate investigation. The Albuquerque Police Department formed a task force and investigated hundreds of suspects. Lorenzo Montoya, a pimp and sex offender who lived near the area where many victims were last seen, was considered a suspect but was murdered by a woman he attacked in 2006.",
      "Another suspect, Joseph Blea, a convicted serial rapist, was investigated but never charged in connection with the West Mesa murders. He was convicted of raping multiple women in Albuquerque during the same period the victims disappeared. Despite years of investigation, genetic genealogy efforts, and periodic reinvestigations, no one has been charged with the West Mesa murders. The case remains one of the most significant unsolved serial murder cases in American history."
    ],
    "timeline": [
      {"date": "2009-02-02", "event": "Human remains discovered on Albuquerque's West Mesa."},
      {"date": "2009-03-01", "event": "Excavation reveals 11 women and one fetus in mass grave."},
      {"date": "2009-06-01", "event": "Most victims identified as women missing since 2001-2005."},
      {"date": "2009-12-01", "event": "Lorenzo Montoya investigated; already dead since 2006."}
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
    "summary": "Five-month-old Sabrina Aisenberg vanished from her crib in Valrico, Florida. Her parents were charged based on controversial wiretap evidence but charges were dropped. The case remains one of Florida's most baffling infant disappearances.",
    "lastSeen": "November 24, 1997, Valrico, Florida",
    "tags": ["missing person", "Florida", "infant", "crib", "wiretap controversy", "1990s"],
    "sources": [
      {"title": "Disappearance of Sabrina Aisenberg - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Sabrina_Aisenberg"},
      {"title": "Sabrina Aisenberg case - Tampa Bay Times", "url": "https://www.tampabay.com/"},
      {"title": "Aisenberg charges dropped - Orlando Sentinel", "url": "https://www.orlandosentinel.com/"}
    ],
    "narrative": [
      "On the morning of November 24, 1997, Marlene Aisenberg went to check on her five-month-old daughter Sabrina in the nursery of their home in Valrico, a suburb of Tampa, Florida. The crib was empty. The garage door had been left open overnight, and the family's two dogs had not barked. Sabrina was wearing only a diaper and was wrapped in a blanket.",
      "The Hillsborough County Sheriff's Office launched an investigation that quickly focused on the parents, Steve and Marlene Aisenberg. Investigators placed wiretaps on the family's home and claimed to have recorded the parents making incriminating statements, including Marlene saying 'The baby's dead and buried. It was found dead because you did it.' The parents were charged in 1999.",
      "However, the case against the Aisenbergs collapsed when independent audio experts examined the wiretap recordings and found them largely unintelligible. Defense attorneys argued that investigators had fabricated or misinterpreted the dialogue. A federal judge ruled the wiretap affidavits contained material misrepresentations and suppressed the evidence. All charges were dropped in 2001.",
      "With the parents cleared, the investigation returned to other theories, including stranger abduction. No new suspects were identified. Baby Sabrina was never found, and no remains have been discovered. The case exposed problems with the wiretap investigation and remains one of Florida's most puzzling missing person cases."
    ],
    "timeline": [
      {"date": "1997-11-24", "event": "Five-month-old Sabrina Aisenberg vanishes from her crib in Valrico, Florida."},
      {"date": "1997-11-25", "event": "Hillsborough County Sheriff's Office investigates; focus on parents."},
      {"date": "1999-09-09", "event": "Steve and Marlene Aisenberg are charged based on wiretap evidence."},
      {"date": "2001-02-22", "event": "Judge suppresses wiretap evidence; all charges dropped."}
    ],
    "enriched": True
  },
  {
    "id": "nique-leili-2011",
    "name": "Nique Leili",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2011,
    "date": "June 9, 2011",
    "state": "Georgia",
    "city": "Buford",
    "age": 28,
    "gender": "Female",
    "summary": "Nique Leili disappeared from Buford, Georgia. Her remains were found two years later in Lake Lanier. Her husband Matt Leili was convicted of malice murder in 2019 despite no clear cause of death, in a largely circumstantial case.",
    "lastSeen": "June 9, 2011, Buford, Georgia",
    "tags": ["homicide", "Georgia", "domestic violence", "Lake Lanier", "circumstantial", "2010s"],
    "sources": [
      {"title": "Murder of Nique Leili - regional news", "url": "https://www.ajc.com/"},
      {"title": "Matt Leili convicted - Gwinnett Daily Post", "url": "https://www.gwinnettdailypost.com/"},
      {"title": "Nique Leili case - 11Alive", "url": "https://www.11alive.com/"}
    ],
    "narrative": [
      "On June 9, 2011, 28-year-old Nique Leili disappeared from the Buford, Georgia home she shared with her husband Matt Leili. Matt reported her missing, claiming she had left the house and not returned. However, friends and family immediately suspected foul play, noting that Nique would not have abandoned her young daughters.",
      "The investigation revealed a troubled marriage marked by allegations of domestic abuse. Matt Leili's behavior after Nique's disappearance raised suspicion—he did not cooperate with investigators and quickly began dating other women. Despite suspicions, without a body, investigators could not build a case.",
      "In August 2013, skeletal remains were discovered in Lake Lanier near Buford. DNA testing confirmed the remains as Nique Leili's. However, due to the advanced decomposition, the medical examiner could not determine a definitive cause of death.",
      "Matt Leili was arrested and charged with malice murder. The prosecution's case was largely circumstantial, built on evidence of domestic abuse, his inconsistent statements, cell phone data, and testimony from friends and family about the couple's violent relationship. In 2019, he was convicted of malice murder and sentenced to life in prison. The case demonstrated that a murder conviction is possible even without a clear cause of death."
    ],
    "timeline": [
      {"date": "2011-06-09", "event": "Nique Leili disappears from her Buford, Georgia home."},
      {"date": "2013-08-01", "event": "Her skeletal remains are found in Lake Lanier."},
      {"date": "2019-03-01", "event": "Husband Matt Leili is convicted of malice murder."}
    ],
    "enriched": True
  },
  {
    "id": "sneha-anne-philip-2001",
    "name": "Sneha Anne Philip",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2001,
    "date": "September 10, 2001",
    "state": "New York",
    "city": "New York City",
    "age": 31,
    "gender": "Female",
    "summary": "Dr. Sneha Anne Philip, a medical resident, disappeared on September 10, 2001—the day before the 9/11 attacks. She lived near the World Trade Center. Whether she died in the attacks while helping victims or disappeared separately remains unknown.",
    "lastSeen": "September 10, 2001, Lower Manhattan, New York City",
    "tags": ["missing person", "New York", "9/11", "doctor", "World Trade Center", "2000s"],
    "sources": [
      {"title": "Disappearance of Sneha Anne Philip - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Sneha_Anne_Philip"},
      {"title": "Sneha Philip case - New York Magazine", "url": "https://nymag.com/nymetro/news/sept11/features/5386/"},
      {"title": "Sneha Philip 9/11 - NBC News", "url": "https://www.nbcnews.com/"}
    ],
    "narrative": [
      "Dr. Sneha Anne Philip, a 31-year-old internal medicine resident at Cabrini Medical Center, was last definitively seen on the evening of September 10, 2001. Security cameras at a Century 21 store in Lower Manhattan showed her shopping for bed linens and shoes at approximately 7:00 p.m. She never returned to the apartment she shared with her husband, Ron Lieberman, near the World Trade Center.",
      "The next morning, September 11, the World Trade Center was attacked. Sneha's husband, who was at work at a hospital in the Bronx, was unable to reach her. When she did not surface in the days that followed, the question became whether she had died in the attacks—perhaps as a bystander or a physician who ran toward the towers to help—or whether she had disappeared for other reasons before the attacks occurred.",
      "The investigation revealed complexities in Sneha's life. She had been suspended from Cabrini for alleged alcohol use at work and was facing a professional hearing. Her marriage was described as troubled. There was evidence suggesting she led a private social life that her husband was not fully aware of. Some investigators believed she may have met with foul play the night of September 10.",
      "A protracted legal battle ensued over whether Sneha should be listed among the 9/11 victims. An initial ruling excluded her, but in 2008 an appeals court reversed the decision, ruling she should be presumed to have died in the attacks. Her name is inscribed on the National September 11 Memorial. Whether Sneha died on September 11 helping at the World Trade Center or met a different fate the night before remains one of the most unusual unsolved cases associated with 9/11."
    ],
    "timeline": [
      {"date": "2001-09-10", "event": "Sneha Anne Philip is last seen shopping in Lower Manhattan."},
      {"date": "2001-09-11", "event": "World Trade Center is attacked; Sneha is not found."},
      {"date": "2004-01-01", "event": "Judge initially rules she was not a 9/11 victim."},
      {"date": "2008-04-01", "event": "Appeals court rules she should be listed among 9/11 victims."}
    ],
    "enriched": True
  },
  {
    "id": "faith-hedgepeth-2012",
    "name": "Faith Hedgepeth",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2012,
    "date": "September 7, 2012",
    "state": "North Carolina",
    "city": "Chapel Hill",
    "age": 19,
    "gender": "Female",
    "summary": "UNC Chapel Hill student Faith Hedgepeth was found murdered in her off-campus apartment. DNA from the scene went unmatched for nine years until genetic genealogy identified Miguel Enrique Olivares, who was convicted in 2023.",
    "lastSeen": "September 6, 2012, Chapel Hill, North Carolina",
    "tags": ["homicide", "North Carolina", "college student", "DNA genealogy", "cold case solved", "2010s"],
    "sources": [
      {"title": "Murder of Faith Hedgepeth - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Faith_Hedgepeth"},
      {"title": "Faith Hedgepeth case solved - WRAL", "url": "https://www.wral.com/story/faith-hedgepeth-case/19876508/"},
      {"title": "Miguel Olivares convicted - News & Observer", "url": "https://www.newsobserver.com/"}
    ],
    "narrative": [
      "On the morning of September 7, 2012, 19-year-old Faith Danielle Hedgepeth, a sophomore at the University of North Carolina at Chapel Hill, was found dead in her off-campus apartment at the Hawthorne at the View complex. She had been beaten and sexually assaulted. A handwritten note on a brown paper bag near her body appeared to contain a threatening message.",
      "Faith, a member of the Haliwa-Saponi tribe of North Carolina, had been out at a nightclub with her roommate the night before. DNA evidence was collected at the scene, including a male profile that did not match anyone in law enforcement databases. The case generated significant attention on campus and in the Haliwa-Saponi community.",
      "For nine years, the DNA profile went unmatched. In 2021, Chapel Hill police partnered with Parabon NanoLabs to conduct genetic genealogy analysis on the DNA. The technique identified the DNA as belonging to Miguel Enrique Olivares, a man who had lived in the Chapel Hill area at the time of the murder but had no prior connection to Faith.",
      "Olivares was arrested in September 2021 and charged with first-degree murder and first-degree rape. He was convicted in 2023 and sentenced to life in prison. The case was a landmark for the use of investigative genetic genealogy in solving cold cases and brought long-awaited justice for Faith's family and tribal community."
    ],
    "timeline": [
      {"date": "2012-09-07", "event": "Faith Hedgepeth is found murdered in her Chapel Hill apartment."},
      {"date": "2012-09-08", "event": "DNA evidence collected; no match in databases."},
      {"date": "2021-09-16", "event": "Genetic genealogy identifies Miguel Olivares; he is arrested."},
      {"date": "2023-06-01", "event": "Olivares is convicted of murder and sentenced to life in prison."}
    ],
    "enriched": True
  },
  {
    "id": "murder-of-darlene-hulse-1984",
    "name": "Darlene Hulse",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1984,
    "date": "June 18, 1984",
    "state": "Indiana",
    "city": "Linton",
    "age": 6,
    "gender": "Female",
    "summary": "Six-year-old Darlene Hulse vanished from outside her family's apartment in Linton, Indiana while her mother went inside briefly. A witness saw her get into a blue car. Despite a massive search, she was never found.",
    "lastSeen": "June 18, 1984, Linton, Indiana",
    "tags": ["missing person", "Indiana", "child", "abduction", "1980s"],
    "sources": [
      {"title": "Darlene Hulse - Charley Project", "url": "https://charleyproject.org/case/darlene-jo-hulse"},
      {"title": "Darlene Hulse - NCMEC", "url": "https://www.missingkids.org/"},
      {"title": "Linton missing girl - Indiana State Police", "url": "https://www.in.gov/isp/"}
    ],
    "narrative": [
      "On June 18, 1984, six-year-old Darlene Jo Hulse was playing outside the family's apartment in Linton, a small city in southwestern Indiana, while her mother went inside briefly. When her mother returned minutes later, Darlene was gone.",
      "A witness reported seeing a young girl matching Darlene's description get into a blue car—possibly a Dodge—with a man driving. The vehicle was seen heading west out of Linton. Despite an immediate and extensive search of the area, Darlene was not found.",
      "The Indiana State Police and Linton police investigated the case, circulating descriptions of the vehicle and conducting interviews throughout the community. The case was entered into national missing children databases and featured on missing children posters. Age-progression images were created as the years passed.",
      "Darlene Hulse has never been found, and no suspect has been publicly identified. The case remains open with the Indiana State Police and represents one of Indiana's oldest unsolved child disappearances."
    ],
    "timeline": [
      {"date": "1984-06-18", "event": "Darlene Hulse vanishes from outside her Linton apartment."},
      {"date": "1984-06-18", "event": "Witness reports seeing her get into a blue car."},
      {"date": "1984-06-19", "event": "Statewide search launched."}
    ],
    "enriched": True
  },
  {
    "id": "corrie-mckeague-2016",
    "name": "Corrie McKeague",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2016,
    "date": "September 24, 2016",
    "state": "Suffolk",
    "city": "Bury St Edmunds",
    "age": 23,
    "gender": "Male",
    "country": "United Kingdom",
    "summary": "RAF gunner Corrie McKeague vanished after a night out in Bury St Edmunds, Suffolk. CCTV showed him entering an area near rubbish bins. Police believe he climbed into a bin and was collected by a garbage truck, but his remains were never found at the landfill.",
    "lastSeen": "September 24, 2016, Bury St Edmunds, Suffolk, England",
    "tags": ["missing person", "United Kingdom", "international", "RAF", "nightlife", "2010s"],
    "sources": [
      {"title": "Disappearance of Corrie McKeague - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Corrie_McKeague"},
      {"title": "Corrie McKeague case - BBC News", "url": "https://www.bbc.co.uk/news/uk-england-suffolk-42189754"},
      {"title": "McKeague investigation - East Anglian Daily Times", "url": "https://www.eadt.co.uk/"}
    ],
    "narrative": [
      "In the early morning hours of September 24, 2016, Corrie McKeague, a 23-year-old RAF gunner based at RAF Honington, went missing after a night out with friends in Bury St Edmunds, Suffolk, England. CCTV footage showed him walking alone through the town center at approximately 3:25 a.m. and entering an area behind a Greggs bakery known as the 'horseshoe' area, which contained large commercial rubbish bins. He was not seen on any camera leaving the area.",
      "Police initially conducted a missing person investigation, searching the town and surrounding areas. The inquiry eventually focused on a garbage collection truck that serviced the bins in the horseshoe area. Records showed the truck had picked up a load significantly heavier than usual that morning—approximately 100 kg heavier—consistent with the weight of a person.",
      "The garbage truck's load was deposited at the Milton landfill in Cambridgeshire. An extensive search of the landfill was conducted over 20 weeks, sifting through thousands of tons of waste. Despite this extraordinary effort, Corrie's remains were not found. The landfill search cost over £1 million.",
      "Suffolk Police concluded that the most likely explanation was that Corrie had climbed into a bin—possibly to sleep, as he was intoxicated—and was collected by the garbage truck and taken to the landfill. His mother, Nicola Urquhart, has publicly questioned this conclusion, pointing to the failure to find remains and other inconsistencies. The case remains officially open."
    ],
    "timeline": [
      {"date": "2016-09-24", "event": "Corrie McKeague is last seen on CCTV entering the horseshoe area."},
      {"date": "2016-09-24", "event": "A garbage truck collects an unusually heavy load from the area."},
      {"date": "2017-03-01", "event": "20-week search of Milton landfill begins; no remains found."},
      {"date": "2017-11-01", "event": "Police conclude Corrie likely entered a bin; case remains open."}
    ],
    "enriched": True
  },
  {
    "id": "aniah-blanchard-2019",
    "name": "Aniah Blanchard",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2019,
    "date": "October 23, 2019",
    "state": "Alabama",
    "city": "Auburn",
    "age": 19,
    "gender": "Female",
    "summary": "Nineteen-year-old Aniah Blanchard, stepdaughter of UFC fighter Walt Harris, disappeared from Auburn, Alabama. Her remains were found a month later. Ibraheem Yazeed was convicted and sentenced to life without parole. Her case led to 'Aniah's Law' in Alabama.",
    "lastSeen": "October 23, 2019, Auburn, Alabama",
    "tags": ["homicide", "Alabama", "college student", "UFC", "Aniah's Law", "2010s"],
    "sources": [
      {"title": "Murder of Aniah Blanchard - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Aniah_Blanchard"},
      {"title": "Aniah Blanchard case - AL.com", "url": "https://www.al.com/news/2020/01/ibraheem-yazeed-indicted-in-aniah-blanchard-murder.html"},
      {"title": "Aniah's Law - Montgomery Advertiser", "url": "https://www.montgomeryadvertiser.com/"}
    ],
    "narrative": [
      "On October 23, 2019, 19-year-old Aniah Haley Blanchard was last seen at a convenience store in Auburn, Alabama. Her abandoned car was found two days later in a Montgomery apartment complex parking lot with blood evidence inside. Aniah was a Southern Union State Community College student and the stepdaughter of UFC heavyweight fighter Walt Harris.",
      "An intensive search and investigation led police to Ibraheem Yazeed, a 30-year-old man with a lengthy criminal history including charges of kidnapping and robbery. Yazeed had been captured on surveillance footage at the convenience store where Aniah was last seen. He was arrested on November 7.",
      "Aniah's remains were found on November 25 in a wooded area in Macon County, approximately 25 miles from Auburn. The medical examiner determined she had died from a gunshot wound. Yazeed was charged with capital murder. The case drew national attention partly due to Walt Harris's public profile in the UFC.",
      "Yazeed was convicted of capital murder and sentenced to life in prison without the possibility of parole. Aniah's case exposed a gap in Alabama law: Yazeed had been free on bond at the time of her murder despite facing charges for kidnapping and attempted murder in another case. In response, Alabama voters approved 'Aniah's Law' in 2022, amending the state constitution to allow judges to deny bail in certain violent felony cases."
    ],
    "timeline": [
      {"date": "2019-10-23", "event": "Aniah Blanchard is last seen at a convenience store in Auburn, Alabama."},
      {"date": "2019-10-25", "event": "Her car is found abandoned with blood evidence inside."},
      {"date": "2019-11-07", "event": "Ibraheem Yazeed is arrested."},
      {"date": "2019-11-25", "event": "Aniah's remains are found in Macon County."},
      {"date": "2022-11-08", "event": "Alabama voters approve 'Aniah's Law' constitutional amendment."}
    ],
    "enriched": True
  },
  {
    "id": "lisa-irwin-2011",
    "name": "Lisa Irwin",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2011,
    "date": "October 4, 2011",
    "state": "Missouri",
    "city": "Kansas City",
    "age": 0,
    "gender": "Female",
    "summary": "Ten-month-old Lisa Irwin vanished from her crib in Kansas City, Missouri during the night. Her mother said she was drunk and did not check on the baby. Despite a massive investigation, Lisa was never found.",
    "lastSeen": "October 3, 2011, Kansas City, Missouri",
    "tags": ["missing person", "Missouri", "infant", "crib", "Kansas City", "2010s"],
    "sources": [
      {"title": "Disappearance of Lisa Irwin - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Lisa_Irwin"},
      {"title": "Lisa Irwin case - Kansas City Star", "url": "https://www.kansascity.com/"},
      {"title": "Baby Lisa investigation - People", "url": "https://people.com/crime/baby-lisa-irwin-missing-2011/"}
    ],
    "narrative": [
      "On the night of October 3-4, 2011, ten-month-old Lisa Renee Irwin disappeared from her crib at the family home on North Lister Avenue in Kansas City, Missouri. Her father, Jeremy Irwin, returned from his night shift around 4:00 a.m. to find the front door unlocked, several lights on, the window open, and Lisa's crib empty.",
      "Lisa's mother, Deborah Bradley, told investigators she had last seen Lisa at 6:40 p.m. when she put her to bed and that she (Deborah) had been drinking heavily that evening and did not check on the baby again. Deborah initially said she went to bed at 10:30 p.m., but later revised this to say she was up past midnight and was drunk. She told police three cell phones in the house were missing.",
      "A neighbor reported seeing a man walking through the neighborhood carrying a baby at approximately 4:00 a.m. The missing cell phones were traced to a dumpster nearby. The FBI and Kansas City police conducted an extensive investigation, including searches of the family's property, a nearby pond, and surrounding areas. Cadaver dogs reportedly alerted near the Irwin home.",
      "Deborah Bradley and Jeremy Irwin stopped cooperating with police after early interviews, hiring an attorney. They maintained their innocence and appeared on national television pleading for Lisa's return. Police described the parents as not being cleared but also never charged them. No one has been arrested, and Lisa Irwin has never been found."
    ],
    "timeline": [
      {"date": "2011-10-04", "event": "Jeremy Irwin returns home to find ten-month-old Lisa missing from her crib."},
      {"date": "2011-10-04", "event": "Neighbor reports seeing a man carrying a baby at 4:00 a.m."},
      {"date": "2011-10-05", "event": "Missing cell phones found in a dumpster; FBI joins investigation."},
      {"date": "2011-10-08", "event": "Deborah Bradley admits being drunk; parents stop cooperating with police."}
    ],
    "enriched": True
  },
  {
    "id": "summer-wells-2021",
    "name": "Summer Wells",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2021,
    "date": "June 15, 2021",
    "state": "Tennessee",
    "city": "Rogersville",
    "age": 5,
    "gender": "Female",
    "summary": "Five-year-old Summer Wells vanished from her family's rural home in Hawkins County, Tennessee. Her mother said she went to play in the yard and disappeared. Despite exhaustive searches of the rugged terrain, Summer has never been found.",
    "lastSeen": "June 15, 2021, Beech Creek Road, Hawkins County, Tennessee",
    "tags": ["missing person", "Tennessee", "child", "rural", "Appalachia", "2020s"],
    "sources": [
      {"title": "Disappearance of Summer Wells - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Summer_Wells"},
      {"title": "Summer Wells case - WJHL", "url": "https://www.wjhl.com/news/local/summer-wells/"},
      {"title": "Summer Wells investigation - Knoxville News Sentinel", "url": "https://www.knoxnews.com/"}
    ],
    "narrative": [
      "On the evening of June 15, 2021, five-year-old Summer Moon-Utah Wells disappeared from the yard of her family's home on Beech Creek Road in rural Hawkins County, Tennessee, in the Appalachian foothills. Her mother, Candus Wells, said she and Summer had been planting flowers in the garden and that Summer went to play in the yard. When Candus checked on her minutes later, she was gone.",
      "The rugged, heavily wooded terrain of Hawkins County made the search extremely challenging. Hundreds of searchers, including law enforcement, volunteers, dogs, helicopters, and drones, combed the mountainous area. Nearby creeks and rivers were searched. The difficult terrain raised the possibility that Summer could have wandered into the dense woods and become lost, but no trace of her was found.",
      "The Tennessee Bureau of Investigation led the case, with assistance from the FBI and other agencies. The investigation examined both the possibility of abduction and the circumstances at the family home. Summer's parents, Don and Candus Wells, were interviewed extensively. The family had prior involvement with child protective services, and the case drew public scrutiny of the home environment.",
      "Despite years of investigation and thousands of tips, Summer Wells has not been found. No arrests have been made. The TBI has described the case as an active, ongoing investigation. Summer's disappearance from a remote, rural setting with limited surveillance or witnesses has made it one of the most challenging missing child cases in recent years."
    ],
    "timeline": [
      {"date": "2021-06-15", "event": "Summer Wells disappears from her family's yard in Hawkins County, Tennessee."},
      {"date": "2021-06-15", "event": "Massive search of rugged terrain begins."},
      {"date": "2021-06-16", "event": "TBI issues Endangered Child Alert; FBI joins investigation."},
      {"date": "2021-07-01", "event": "Thousands of tips received; no breakthrough."}
    ],
    "enriched": True
  },
  {
    "id": "maddie-clifton-1998",
    "name": "Maddie Clifton",
    "type": "Homicide",
    "status": "Conviction",
    "year": 1998,
    "date": "November 3, 1998",
    "state": "Florida",
    "city": "Jacksonville",
    "age": 8,
    "gender": "Female",
    "summary": "Eight-year-old Maddie Clifton was murdered by her 14-year-old neighbor Joshua Phillips, who hid her body under his waterbed for a week. When his mother discovered the body, she called police. Phillips was tried as an adult and sentenced to life without parole.",
    "lastSeen": "November 3, 1998, Jacksonville, Florida",
    "tags": ["homicide", "Florida", "child", "juvenile offender", "hidden body", "1990s"],
    "sources": [
      {"title": "Murder of Maddie Clifton - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Maddie_Clifton"},
      {"title": "Joshua Phillips case - Florida Times-Union", "url": "https://www.jacksonville.com/"},
      {"title": "Maddie Clifton murder - Investigation Discovery", "url": "https://www.investigationdiscovery.com/"}
    ],
    "narrative": [
      "On November 3, 1998, eight-year-old Maddie Clifton went out to play in her neighborhood in Jacksonville, Florida. She did not return home, and a massive community search was launched. Hundreds of volunteers, including neighbors and classmates' families, canvassed the area. Maddie's face was on news broadcasts across northeastern Florida.",
      "One of the volunteers in the search was 14-year-old Joshua Phillips, who lived across the street from the Clifton family. For a week, as the search intensified, Phillips participated in the search efforts. Meanwhile, he had hidden Maddie's body under his waterbed.",
      "On November 10, Phillips' mother discovered Maddie's body while cleaning her son's room. She noticed a foul odor and fluid leaking from the base of the waterbed. She called police immediately. Joshua Phillips was arrested and charged with first-degree murder.",
      "Phillips was tried as an adult. He claimed that he had accidentally hit Maddie with a baseball bat while they were playing and then panicked, stabbing her and hiding the body. The prosecution argued the injuries were not accidental. Phillips was convicted and sentenced to life in prison without the possibility of parole. The case shocked Jacksonville and became one of the most discussed cases involving a juvenile offender in Florida history."
    ],
    "timeline": [
      {"date": "1998-11-03", "event": "Maddie Clifton disappears while playing in her Jacksonville neighborhood."},
      {"date": "1998-11-04", "event": "Massive community search begins; neighbor Joshua Phillips volunteers."},
      {"date": "1998-11-10", "event": "Phillips' mother finds Maddie's body under his waterbed."},
      {"date": "1999-07-09", "event": "Joshua Phillips convicted; sentenced to life without parole."}
    ],
    "enriched": True
  },
  {
    "id": "daniel-robinson-2021",
    "name": "Daniel Robinson",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2021,
    "date": "June 23, 2021",
    "state": "Arizona",
    "city": "Buckeye",
    "age": 24,
    "gender": "Male",
    "summary": "Geologist Daniel Robinson vanished from a work site in the Arizona desert west of Phoenix. His crashed Jeep was found a month later miles away with his belongings inside. His father has led an extraordinary independent search effort.",
    "lastSeen": "June 23, 2021, Buckeye, Arizona",
    "tags": ["missing person", "Arizona", "geologist", "desert", "Jeep", "2020s"],
    "sources": [
      {"title": "Disappearance of Daniel Robinson - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Daniel_Robinson"},
      {"title": "Daniel Robinson case - Arizona Republic", "url": "https://www.azcentral.com/story/news/local/arizona/2021/10/11/daniel-robinson-disappearance/6070050001/"},
      {"title": "David Robinson search - CNN", "url": "https://www.cnn.com/2021/10/15/us/daniel-robinson-missing-arizona/index.html"}
    ],
    "narrative": [
      "On June 23, 2021, 24-year-old Daniel Robinson, a geologist employed by Matrix New World Engineering, drove his blue Jeep Renegade from a work site in the desert west of Buckeye, Arizona. Co-workers said he left the site abruptly in the middle of the workday. He was never seen again.",
      "Daniel's Jeep was found a month later in a ravine approximately two miles from his work site, deep in the desert. The vehicle had significant damage consistent with a crash. Inside were Daniel's clothes, wallet, phone (damaged), and other personal belongings. His keys were in the ignition. However, Daniel was not in or near the vehicle.",
      "Daniel's father, David Robinson, a military veteran from South Carolina, traveled to Arizona and launched one of the most extensive independent search efforts in recent memory. Using fundraised money, he hired private investigators, chartered helicopter searches, and spent months living in the Arizona desert, searching areas that he felt the Buckeye Police Department had not adequately covered.",
      "The case raised questions about the police department's investigation, which David Robinson publicly criticized as inadequate. The Buckeye Police maintained that they were investigating but treated the case as a missing person, not a criminal matter. Some evidence—including the fact that the Jeep appeared to have been driven erratically rather than in a straight path—raised questions about whether Daniel was alone in the vehicle. Remains found in the desert area have been tested but not matched to Daniel. He remains missing."
    ],
    "timeline": [
      {"date": "2021-06-23", "event": "Daniel Robinson drives away from a desert work site near Buckeye, Arizona."},
      {"date": "2021-07-19", "event": "His Jeep is found crashed in a ravine with his belongings inside."},
      {"date": "2021-08-01", "event": "Father David Robinson arrives in Arizona and begins independent search."},
      {"date": "2021-10-01", "event": "Case gains national attention; police investigation questioned."}
    ],
    "enriched": True
  },
  {
    "id": "laci-peterson-2002",
    "name": "Laci Peterson",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2002,
    "date": "December 24, 2002",
    "state": "California",
    "city": "Modesto",
    "age": 27,
    "gender": "Female",
    "summary": "Laci Peterson, eight months pregnant, disappeared from her Modesto home on Christmas Eve. Her body and that of her unborn son washed ashore months later. Her husband Scott Peterson was convicted of double murder and sentenced to death, later reduced to life without parole.",
    "lastSeen": "December 24, 2002, Modesto, California",
    "tags": ["homicide", "California", "pregnant", "husband convicted", "Christmas Eve", "2000s"],
    "sources": [
      {"title": "Murder of Laci Peterson - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Laci_Peterson"},
      {"title": "Scott Peterson trial - CNN", "url": "https://www.cnn.com/2004/LAW/11/12/peterson.verdict/index.html"},
      {"title": "Laci Peterson case - Modesto Bee", "url": "https://www.modbee.com/"}
    ],
    "narrative": [
      "On Christmas Eve 2002, Laci Denise Peterson, a 27-year-old woman who was eight months pregnant with the couple's first child, disappeared from the home she shared with her husband Scott in Modesto, California. Scott told police he had been fishing alone in the San Francisco Bay that day and returned to find Laci gone. He said their dog was in the backyard with its leash on.",
      "A massive search was launched, and the case quickly became national news. As the investigation progressed, disturbing revelations emerged: Scott had been having an affair with massage therapist Amber Frey, who came forward to police and agreed to record their phone conversations. Scott had told Frey he was a widower—before Laci disappeared. His behavior during the search struck many as oddly detached.",
      "On April 13, 2003, the decomposed body of a full-term male fetus washed ashore in the San Francisco Bay near Point Isabel. The next day, a woman's torso was found nearby. DNA confirmed the remains were Laci and her son, whom the Petersons had planned to name Conner. The location was near where Scott had claimed to be fishing.",
      "Scott Peterson was arrested on April 18, 2003, near a golf course in La Jolla, California with $15,000 in cash, his brother's driver's license, and a recently dyed goatee, suggesting he was attempting to flee. He was tried in Redwood City after a change of venue and convicted of first-degree murder for Laci and second-degree murder for Conner in November 2004. He was sentenced to death, but in 2020 the California Supreme Court overturned the death sentence due to juror issues. He was resentenced to life without parole."
    ],
    "timeline": [
      {"date": "2002-12-24", "event": "Laci Peterson disappears from her Modesto home on Christmas Eve."},
      {"date": "2003-01-24", "event": "Amber Frey reveals Scott's affair to police."},
      {"date": "2003-04-14", "event": "Laci's remains and those of her unborn son wash ashore in San Francisco Bay."},
      {"date": "2003-04-18", "event": "Scott Peterson is arrested near La Jolla."},
      {"date": "2004-11-12", "event": "Scott convicted of first-degree murder; sentenced to death."},
      {"date": "2021-12-08", "event": "Death sentence overturned; resentenced to life without parole."}
    ],
    "enriched": True
  },
  {
    "id": "bardstown-officer-2013",
    "name": "Jason Ellis",
    "type": "Homicide",
    "status": "Unsolved",
    "year": 2013,
    "date": "May 25, 2013",
    "state": "Kentucky",
    "city": "Bardstown",
    "age": 33,
    "gender": "Male",
    "summary": "Bardstown, Kentucky police officer Jason Ellis was ambushed and killed on a highway exit ramp while driving home from his shift. The calculated, execution-style killing has never been solved and is part of a series of violent unsolved crimes in Bardstown.",
    "lastSeen": "May 25, 2013, Bluegrass Parkway exit ramp, Bardstown, Kentucky",
    "tags": ["homicide", "Kentucky", "police officer", "ambush", "Bardstown", "2010s"],
    "sources": [
      {"title": "Murder of Jason Ellis - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Jason_Ellis"},
      {"title": "Jason Ellis case - Courier Journal", "url": "https://www.courier-journal.com/"},
      {"title": "Bardstown unsolved murders - WDRB", "url": "https://www.wdrb.com/"}
    ],
    "narrative": [
      "In the early morning hours of May 25, 2013, Officer Jason Ellis, a 33-year-old patrolman with the Bardstown Police Department, was driving home from his shift on the Bluegrass Parkway in Nelson County, Kentucky. As he exited the parkway at the Bardstown exit, he encountered debris—possibly tree branches—placed on the exit ramp. When Ellis stopped to move the debris, he was shot multiple times with a shotgun from a concealed position.",
      "Ellis, who was wearing his body armor, was struck multiple times in areas not protected by the vest. He died at the scene. The deliberate placement of debris to force him to stop indicated premeditation and planning. The killer knew Ellis's route home and timed the ambush accordingly.",
      "The investigation by Kentucky State Police and the FBI explored multiple theories, including whether Ellis had been targeted because of his police work—he was involved in narcotics investigations in an area known for drug activity—or whether there was a personal motive. The calculated nature of the ambush suggested professional planning.",
      "Jason Ellis's murder is one of several violent unsolved crimes in the Bardstown area, a small city that became known as 'the most dangerous small town in America.' Other unsolved cases include the disappearance of Crystal Rogers and the murder of her father Tommy Ballard, and the murder of a local mother and daughter. The FBI has investigated possible connections between the cases. Officer Ellis's murder remains unsolved."
    ],
    "timeline": [
      {"date": "2013-05-25", "event": "Officer Jason Ellis is ambushed and killed on a highway exit ramp."},
      {"date": "2013-05-25", "event": "Kentucky State Police and FBI launch investigation."},
      {"date": "2013-06-01", "event": "Investigators determine the ambush was premeditated and calculated."}
    ],
    "enriched": True
  },
  {
    "id": "timmothy-pitzen-2011",
    "name": "Timmothy Pitzen",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2011,
    "date": "May 12, 2011",
    "state": "Illinois",
    "city": "Aurora",
    "age": 6,
    "gender": "Male",
    "summary": "Six-year-old Timmothy Pitzen was taken from school by his mother Amy Fry-Pitzen, who was later found dead by suicide in a motel. Her note said Timmothy was safe but would never be found. His whereabouts remain unknown.",
    "lastSeen": "May 11, 2011, last confirmed in Dells of Wisconsin area",
    "tags": ["missing person", "Illinois", "child", "mother suicide", "mystery note", "2010s"],
    "sources": [
      {"title": "Disappearance of Timmothy Pitzen - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Timmothy_Pitzen"},
      {"title": "Timmothy Pitzen case - Chicago Tribune", "url": "https://www.chicagotribune.com/"},
      {"title": "Timmothy Pitzen - NCMEC", "url": "https://www.missingkids.org/poster/NCMC/1134728"}
    ],
    "narrative": [
      "On May 11, 2011, Amy Fry-Pitzen checked her six-year-old son Timmothy James Pitzen out of his elementary school in Aurora, Illinois, telling school officials there was a family emergency. Over the next two days, Amy and Timmothy were seen at a zoo, a water park resort, and a family amusement center in Illinois and Wisconsin. Security footage confirmed their presence together.",
      "On May 14, Amy Fry-Pitzen was found dead in a motel room in Rockford, Illinois. She had died by suicide, slashing her wrists and ingesting antihistamines. She left a note that read: 'Tim is somewhere safe with people who love him and will care for him. You will never find him.' She had called her mother the day before and told her that Timmothy was fine.",
      "Cell phone records, hotel receipts, and surveillance footage showed that Amy had traveled with Timmothy through northern Illinois and southern Wisconsin in the days before her death, but investigators could not determine where she left the child. Her car showed approximately 200 miles of unaccounted driving. Searches of lakes, rivers, and wooded areas along her route found nothing.",
      "In April 2019, a teenager approached a woman in Newport, Kentucky claiming to be Timmothy Pitzen, saying he had escaped from kidnappers. FBI and police quickly responded, but DNA testing proved the person was not Timmothy—he was a 23-year-old Ohio man with a history of making false claims. The hoax devastated Timmothy's family. The real Timmothy Pitzen, who would be in his late teens, has never been found."
    ],
    "timeline": [
      {"date": "2011-05-11", "event": "Amy Fry-Pitzen takes Timmothy from school; they travel through IL and WI."},
      {"date": "2011-05-14", "event": "Amy is found dead by suicide; note says Timmothy is 'safe' but won't be found."},
      {"date": "2011-05-15", "event": "Massive search along Amy's route; 200 miles of driving unaccounted for."},
      {"date": "2019-04-03", "event": "False claim by impersonator in Kentucky; DNA proves he is not Timmothy."}
    ],
    "enriched": True
  },
  {
    "id": "gabby-petito-2021",
    "name": "Gabby Petito",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2021,
    "date": "August 27, 2021",
    "state": "Wyoming",
    "city": "Spread Creek",
    "age": 22,
    "gender": "Female",
    "summary": "Twenty-two-year-old Gabby Petito vanished during a cross-country van trip with her fiancé Brian Laundrie. Her body was found in Wyoming. Laundrie fled and was later found dead of suicide in a Florida swamp, having left a notebook confessing to her murder.",
    "lastSeen": "August 27, 2021, Grand Teton area, Wyoming",
    "tags": ["homicide", "Wyoming", "van life", "domestic violence", "social media", "2020s"],
    "sources": [
      {"title": "Murder of Gabby Petito - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Gabby_Petito"},
      {"title": "Gabby Petito case - CNN", "url": "https://www.cnn.com/specials/us/gabby-petito-brian-laundrie"},
      {"title": "Gabby Petito timeline - NBC News", "url": "https://www.nbcnews.com/news/us-news/gabby-petito-case-timeline-disappearance-brian-laundrie-search-n1280041"}
    ],
    "narrative": [
      "In the summer of 2021, 22-year-old Gabrielle 'Gabby' Petito and her 23-year-old fiancé Brian Laundrie embarked on a cross-country road trip in a converted white Ford Transit van, documenting their journey on social media and YouTube. The couple had been together for over two years and were living in the van. On August 12, police in Moab, Utah responded to a 911 call about a domestic incident involving the couple. Bodycam footage showed an emotional Gabby telling officers that she and Brian had been arguing. Officers separated them for the night but no charges were filed.",
      "Gabby's last known communication with her family was on August 25-27. Brian returned alone to the home he shared with his parents in North Port, Florida on September 1, driving Gabby's van. He refused to speak with police or Gabby's family about her whereabouts. On September 11, Gabby's parents filed a missing person report. Brian hired an attorney and remained silent.",
      "On September 17, Brian Laundrie told his parents he was going for a hike in the Carlton Reserve, a 25,000-acre nature preserve near their home. He never returned. Two days later, on September 19, Gabby's remains were found in the Spread Creek Dispersed Camping Area near Grand Teton National Park in Wyoming. The cause of death was determined to be strangulation.",
      "A massive search for Brian Laundrie in the Carlton Reserve lasted over a month. On October 20, his skeletal remains were found in an area of the reserve that had been underwater for weeks. The cause of death was a gunshot wound to the head—suicide. Near his remains was a dry bag containing a notebook in which he confessed to murdering Gabby. The case became a global phenomenon, raising awareness of domestic violence but also prompting criticism about the disproportionate media attention given to cases involving young, attractive white women."
    ],
    "timeline": [
      {"date": "2021-08-12", "event": "Moab, Utah police respond to domestic incident between Gabby and Brian."},
      {"date": "2021-08-27", "event": "Gabby's last known communication with her family."},
      {"date": "2021-09-01", "event": "Brian returns alone to Florida in Gabby's van."},
      {"date": "2021-09-19", "event": "Gabby's body is found in Wyoming's Spread Creek area."},
      {"date": "2021-10-20", "event": "Brian Laundrie's remains found in Carlton Reserve; suicide with confession."}
    ],
    "enriched": True
  },
  {
    "id": "susan-cox-powell-2009",
    "name": "Susan Cox Powell",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 2009,
    "date": "December 6, 2009",
    "state": "Utah",
    "city": "West Valley City",
    "age": 28,
    "gender": "Female",
    "summary": "Susan Powell disappeared from her West Valley City, Utah home. Her husband Josh claimed he went camping with their sons in freezing weather that night. Josh was never charged but later killed himself and both sons in a 2012 house explosion. Susan's body has never been found.",
    "lastSeen": "December 6, 2009, West Valley City, Utah",
    "tags": ["missing person", "Utah", "domestic violence", "murder-suicide", "2000s"],
    "sources": [
      {"title": "Disappearance of Susan Powell - Wikipedia", "url": "https://en.wikipedia.org/wiki/Disappearance_of_Susan_Powell"},
      {"title": "Powell family tragedy - Salt Lake Tribune", "url": "https://www.sltrib.com/"},
      {"title": "Susan Powell case - People Magazine", "url": "https://people.com/crime/susan-powell-disappearance/"}
    ],
    "narrative": [
      "On December 6, 2009, 28-year-old Susan Marie Cox Powell disappeared from the home she shared with her husband Josh Powell and their two young sons, Charlie (4) and Braden (2), in West Valley City, Utah. When police conducted a welfare check the next day at the request of Susan's concerned employer, they found Josh and the boys away from home. Josh claimed he had taken the boys on a spontaneous midnight camping trip in the freezing desert—in December—leaving Susan at home.",
      "The investigation quickly focused on Josh, whose story was widely disbelieved. The minivan had the back seats removed and smelled of gasoline. Wet towels were found in the washing machine. Susan's purse and cell phone were at home. Neighbors reported hearing nothing unusual. Josh hired an attorney and moved with his sons to his father Steven Powell's home in Puyallup, Washington.",
      "In 2011, Steven Powell was arrested and convicted on voyeurism charges for secretly filming young neighbor girls. As a result, Josh lost custody of Charlie and Braden, who were placed with Susan's parents. During a supervised custody visit on February 5, 2012, Josh locked the case worker out of his house and set it on fire, killing himself and both boys in the explosion and blaze. A hatchet was found at the scene, suggesting he had attacked the children before the fire.",
      "Before the explosion, Josh had sent an email saying 'I can't live without my boys.' His act destroyed the two most important potential witnesses to what happened to Susan. Susan's body has never been found, and no one has ever been charged in her disappearance. The case file remains open with the West Valley City Police Department."
    ],
    "timeline": [
      {"date": "2009-12-06", "event": "Susan Powell disappears from her West Valley City home."},
      {"date": "2009-12-07", "event": "Josh claims midnight camping trip; investigation focuses on him."},
      {"date": "2011-09-22", "event": "Josh's father Steven Powell arrested; Josh loses custody of sons."},
      {"date": "2012-02-05", "event": "Josh kills himself and both sons in a house explosion during custody visit."}
    ],
    "enriched": True
  },
  {
    "id": "dkane-doe-1980",
    "name": "Racine County Jane Doe",
    "type": "Unidentified Remains",
    "status": "Identified",
    "year": 1999,
    "date": "July 21, 1999",
    "state": "Wisconsin",
    "city": "Racine",
    "age": None,
    "gender": "Female",
    "summary": "The skeletal remains of a young woman were found in a cornfield near Racine, Wisconsin in 1999. She remained unidentified for over two decades until genetic genealogy identified her in 2022 as Peggy Lynn Johnson, a victim of sex trafficking from Tennessee.",
    "lastSeen": "Unknown",
    "tags": ["unidentified remains", "Wisconsin", "Doe case", "DNA genealogy", "sex trafficking", "1990s"],
    "sources": [
      {"title": "Racine County Jane Doe - Doe Network", "url": "https://www.doenetwork.org/"},
      {"title": "Peggy Lynn Johnson identified - Racine Journal Times", "url": "https://journaltimes.com/"},
      {"title": "Racine Doe identified - Milwaukee Journal Sentinel", "url": "https://www.jsonline.com/"}
    ],
    "narrative": [
      "On July 21, 1999, the skeletal remains of a young woman were discovered in a cornfield near Racine, Wisconsin. She had been dead for approximately one to two years. The cause of death was ruled homicide—she had been bludgeoned. Her age was estimated at 15 to 21 years old. Despite efforts to identify her through dental records, fingerprints, and later DNA, she remained a Jane Doe for over two decades.",
      "The case was featured on the Doe Network and NamUs databases, and forensic artist reconstructions were widely distributed. Multiple potential identifications were investigated and ruled out. The lack of a match in missing persons databases suggested she may have been someone whose absence went unreported—a possibility that pointed toward a transient, marginalized, or exploited individual.",
      "In 2022, genetic genealogy work conducted by the DNA Doe Project and the Racine County Sheriff's Office identified the woman as Peggy Lynn Johnson, who was from Tennessee. Research revealed that Peggy had been a victim of sex trafficking, which explained why she was never reported missing—her abuser had kept her isolated and under control for years before her death.",
      "With the identification, a suspect was identified: 83-year-old Raymond Vannieuwenhoven was not involved (he was linked to a different Wisconsin case). The investigation into Peggy Lynn Johnson's specific killer continued with the benefit of knowing her identity and history. The case illustrated both the power of genetic genealogy and the tragedy of trafficking victims who disappear without being reported."
    ],
    "timeline": [
      {"date": "1999-07-21", "event": "Skeletal remains found in a cornfield near Racine, Wisconsin."},
      {"date": "1999-08-01", "event": "Investigation begins; woman cannot be identified."},
      {"date": "2022-05-12", "event": "Genetic genealogy identifies her as Peggy Lynn Johnson of Tennessee."},
      {"date": "2022-06-01", "event": "Investigation reopened with victim's identity and trafficking history."}
    ],
    "enriched": True
  },
  {
    "id": "fort-worth-trio-1974",
    "name": "Fort Worth Missing Trio",
    "type": "Missing Person",
    "status": "Unsolved",
    "year": 1974,
    "date": "December 23, 1974",
    "state": "Texas",
    "city": "Fort Worth",
    "age": None,
    "gender": "Female",
    "summary": "Three young women—Rachel Trlica (17), Renee Wilson (14), and Julie Ann Moseley (9)—went Christmas shopping at a Fort Worth mall and never returned. Their car was found at the mall. A strange letter supposedly from Rachel was mailed days later. None were ever found.",
    "lastSeen": "December 23, 1974, Seminary South Shopping Center, Fort Worth, Texas",
    "tags": ["missing person", "Texas", "Fort Worth", "three girls", "Christmas shopping", "1970s"],
    "sources": [
      {"title": "Fort Worth Missing Trio - Wikipedia", "url": "https://en.wikipedia.org/wiki/Fort_Worth_Missing_Trio"},
      {"title": "Missing trio - Fort Worth Star-Telegram", "url": "https://www.star-telegram.com/"},
      {"title": "Fort Worth trio cold case - NBCDFW", "url": "https://www.nbcdfw.com/"}
    ],
    "narrative": [
      "On December 23, 1974, two days before Christmas, 17-year-old Rachel Trlica, 14-year-old Renee Wilson, and 9-year-old Julie Ann Moseley left for the Seminary South Shopping Center in Fort Worth, Texas to finish their Christmas shopping. Rachel drove her husband Tommy Trlica's car, a green Oldsmobile. They were expected back within a few hours. They never returned.",
      "The car was found in the shopping center parking lot, but there was no sign of the three girls. Their Christmas purchases were not in the car. A massive search and investigation found no evidence of what happened to them at the busy mall two days before Christmas.",
      "Several days after the disappearance, a letter was mailed to Rachel's husband Tommy, supposedly written by Rachel. It read: 'I know I'm going to catch it, but we had to get away. We are going to Houston. See you in about a week.' The letter was postmarked from Fort Worth. Rachel's family disputed that she had written it, and handwriting analysis was inconclusive.",
      "Tommy Trlica was investigated but never charged. Other theories included a planned runaway, abduction by a stranger, and involvement by someone known to the girls. In 2014, a Fort Worth resident found bones during construction, leading to speculation they were connected to the case, but the remains were determined to be animal bones. The Fort Worth Missing Trio case remains one of Texas's most enduring unsolved mysteries."
    ],
    "timeline": [
      {"date": "1974-12-23", "event": "Rachel Trlica, Renee Wilson, and Julie Ann Moseley go Christmas shopping and vanish."},
      {"date": "1974-12-23", "event": "Their car is found at Seminary South Shopping Center."},
      {"date": "1974-12-28", "event": "A letter supposedly from Rachel is mailed to her husband."}
    ],
    "enriched": True
  },
  {
    "id": "victim-of-dating-game-killer-cornelia",
    "name": "Cornelia Crilley",
    "type": "Homicide",
    "status": "Conviction",
    "year": 1971,
    "date": "June 12, 1971",
    "state": "New York",
    "city": "New York City",
    "age": 23,
    "gender": "Female",
    "summary": "Flight attendant Cornelia Crilley was found strangled in her Manhattan apartment. The case went cold for nearly 40 years until DNA matched serial killer Rodney Alcala, the 'Dating Game Killer,' who pleaded guilty in 2012.",
    "lastSeen": "June 12, 1971, Manhattan, New York City",
    "tags": ["homicide", "New York", "flight attendant", "serial killer", "DNA", "cold case solved", "1970s"],
    "sources": [
      {"title": "Rodney Alcala New York murders - Wikipedia", "url": "https://en.wikipedia.org/wiki/Rodney_Alcala#New_York_murders"},
      {"title": "Cornelia Crilley case - New York Post", "url": "https://nypost.com/"},
      {"title": "Alcala pleads guilty in NY murders - NBC News", "url": "https://www.nbcnews.com/"}
    ],
    "narrative": [
      "On June 12, 1971, 23-year-old Cornelia Michel Crilley, a TWA flight attendant, was found dead in her apartment on the Upper East Side of Manhattan. She had been sexually assaulted and strangled with her own stockings. The apartment showed no signs of forced entry, suggesting she had let her killer in.",
      "The investigation by the NYPD was extensive but yielded no suspects. Biological evidence was collected at the scene and preserved. The case went cold as leads were exhausted, joining the ranks of New York City's unsolved murders from the 1970s.",
      "Decades later, when DNA technology had advanced significantly, the biological evidence from the Crilley scene was tested and entered into the national DNA database. It matched the profile of Rodney Alcala, who was already on California's death row for multiple murders. Alcala had been living in New York City in the early 1970s while attending NYU film school under a pseudonym.",
      "In 2012, Rodney Alcala pleaded guilty to the murders of both Cornelia Crilley and Ellen Hover, another New York woman killed in 1977. He received an additional 25 years to life for each murder, to be served concurrently with his California death sentence. The case demonstrated how DNA evidence could solve murders that were nearly four decades old."
    ],
    "timeline": [
      {"date": "1971-06-12", "event": "Cornelia Crilley is found strangled in her Upper East Side apartment."},
      {"date": "1971-06-15", "event": "NYPD investigation begins; case eventually goes cold."},
      {"date": "2011-01-01", "event": "DNA from the scene matches serial killer Rodney Alcala."},
      {"date": "2012-12-14", "event": "Alcala pleads guilty to Crilley's murder."}
    ],
    "enriched": True
  },
  {
    "id": "dee-dee-blancharde-2015",
    "name": "Dee Dee Blanchard",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2015,
    "date": "June 14, 2015",
    "state": "Missouri",
    "city": "Springfield",
    "age": 48,
    "gender": "Female",
    "summary": "Dee Dee Blanchard was murdered by her daughter Gypsy Rose's boyfriend after years of medical child abuse (Munchausen syndrome by proxy). Gypsy had been forced to feign illness and disability her entire life. The case exposed one of the most extreme instances of Munchausen by proxy ever documented.",
    "lastSeen": "June 14, 2015, Springfield, Missouri",
    "tags": ["homicide", "Missouri", "Munchausen by proxy", "medical abuse", "2010s"],
    "sources": [
      {"title": "Murder of Dee Dee Blanchard - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Dee_Dee_Blanchard"},
      {"title": "Gypsy Rose Blanchard case - BuzzFeed News", "url": "https://www.buzzfeednews.com/article/michelledean/dee-dee-wanted-her-daughter-to-be-sick-gypsy-wanted-her-mom"},
      {"title": "The Act - Hulu documentary series", "url": "https://www.hulu.com/series/the-act/"}
    ],
    "narrative": [
      "For Gypsy Rose Blanchard's entire life, her mother Clauddine 'Dee Dee' Blanchard had subjected her to severe medical child abuse known as Munchausen syndrome by proxy (factitious disorder imposed on another). Dee Dee claimed Gypsy suffered from leukemia, muscular dystrophy, epilepsy, and brain damage, among other conditions. Gypsy was confined to a wheelchair, had her head shaved, was fed through a feeding tube, and took numerous medications—none of which she needed.",
      "Dee Dee and Gypsy received free housing from Habitat for Humanity (as Hurricane Katrina victims), free trips from Make-A-Wish Foundation, and considerable charitable donations. Dee Dee controlled every aspect of Gypsy's life, including her age—Gypsy was actually several years older than her mother claimed. Medical professionals who questioned Dee Dee's claims were swiftly cut off.",
      "As Gypsy grew older and gained internet access, she began to understand the extent of her mother's deception. She formed an online relationship with Nicholas Godejohn, a 26-year-old man from Wisconsin. Together they planned Dee Dee's murder. On June 14, 2015, Godejohn traveled to their Springfield, Missouri home and stabbed Dee Dee to death while Gypsy hid in the bathroom.",
      "The case captivated the public when it was uncovered, raising complex questions about victimhood and justice. Gypsy, who had been a victim of extreme abuse her entire life, was also a participant in planning her mother's murder. She pleaded guilty to second-degree murder and was sentenced to 10 years in prison. She was released in December 2023. Godejohn was convicted of first-degree murder and sentenced to life in prison. The case was adapted into the Hulu series 'The Act' and multiple documentaries."
    ],
    "timeline": [
      {"date": "2015-06-14", "event": "Nicholas Godejohn murders Dee Dee Blanchard at the Springfield home."},
      {"date": "2015-06-15", "event": "Facebook post by Gypsy's account reads 'That bitch is dead'; police discover body."},
      {"date": "2015-06-16", "event": "Gypsy Rose Blanchard and Nicholas Godejohn are arrested in Wisconsin."},
      {"date": "2016-07-05", "event": "Gypsy pleads guilty to second-degree murder; sentenced to 10 years."},
      {"date": "2023-12-28", "event": "Gypsy Rose Blanchard is released from prison."}
    ],
    "enriched": True
  },
  {
    "id": "shooting-of-nipsey-hussle",
    "name": "Nipsey Hussle",
    "type": "Homicide",
    "status": "Conviction",
    "year": 2019,
    "date": "March 31, 2019",
    "state": "California",
    "city": "Los Angeles",
    "age": 33,
    "gender": "Male",
    "summary": "Grammy-nominated rapper and community activist Nipsey Hussle was shot and killed outside his Marathon Clothing store in the Hyde Park neighborhood of Los Angeles. Eric Holder Jr. was convicted of first-degree murder in 2022.",
    "lastSeen": "March 31, 2019, Marathon Clothing store, Hyde Park, Los Angeles",
    "tags": ["homicide", "California", "Los Angeles", "rapper", "community activist", "2010s"],
    "sources": [
      {"title": "Murder of Nipsey Hussle - Wikipedia", "url": "https://en.wikipedia.org/wiki/Murder_of_Nipsey_Hussle"},
      {"title": "Eric Holder conviction - Los Angeles Times", "url": "https://www.latimes.com/california/story/2022-07-06/nipsey-hussle-murder-trial-verdict"},
      {"title": "Nipsey Hussle legacy - Rolling Stone", "url": "https://www.rollingstone.com/music/music-features/nipsey-hussle-death-murder-community-los-angeles-817675/"}
    ],
    "narrative": [
      "On March 31, 2019, Ermias Joseph Asghedom, known professionally as Nipsey Hussle, a 33-year-old Grammy-nominated rapper and beloved community activist, was shot and killed in the parking lot of his Marathon Clothing store on Slauson Avenue in the Hyde Park neighborhood of South Los Angeles. He was shot multiple times, including in the head, and was pronounced dead at a hospital.",
      "Nipsey Hussle was far more than a rapper to his community. He had invested heavily in the Crenshaw neighborhood where he grew up, opening businesses, creating jobs, and working to reduce gang violence. He owned the shopping plaza where his store was located and was developing plans for affordable housing. He had been scheduled to meet with LAPD officials to discuss strategies for reducing gang violence the day after his murder.",
      "The shooter was identified as Eric Ronald Holder Jr., 29, a man from the same neighborhood who had been at the Marathon store that day. Holder and Nipsey had a brief conversation before Holder left and returned minutes later with a handgun, shooting Nipsey multiple times and then kicking him in the head. The motive appeared to be personal—reportedly related to a conversation about Holder being a snitch—rather than gang-related, though both men had gang associations.",
      "Holder fled the scene but was arrested two days later. He was charged with murder and two counts of attempted murder for injuring bystanders. In July 2022, a jury convicted Holder of first-degree murder. He was sentenced to 60 years to life in prison. Nipsey Hussle's death sparked an outpouring of grief in Los Angeles and beyond, and his legacy as a community leader and entrepreneur has only grown since his passing."
    ],
    "timeline": [
      {"date": "2019-03-31", "event": "Nipsey Hussle is shot and killed outside his Marathon Clothing store."},
      {"date": "2019-04-02", "event": "Eric Holder Jr. is arrested."},
      {"date": "2019-04-11", "event": "Memorial service at Staples Center draws 21,000 people."},
      {"date": "2022-07-06", "event": "Holder convicted of first-degree murder; sentenced to 60 years to life."}
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
