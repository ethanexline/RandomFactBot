import utility

verbs = ["got", "chuggled", "fell in love with the idea of", "slurped", "locked eyes with", "consumed", "concieved", "started a ^ revolution around the idea of", "^ly chewed on",
"won", "hired", "claimed", "started a standing ovation for", "delivered the keynote speech at a conference devoted to", "started a religion that worships", "punched the | out of",
"made a GoFundMe for", "starred in a commercial advertising", "applied ^ pressure to", "ate a ^ meal consisting exclusively of", "held ^ eye contact with", "acquired",
"created an algorithm that calculates", "fought", "sued", "smelled the ^ odor of", "rued the day that !! met", "considered purchasing", "tasted, and loved", 
"met, and was bored by", "lost & pounds by only eating", "fist-bumped", "gave a ^ talking to", "delivered a stirring speech to a crowd of people dressed like", "discovered",
"happened upon", "embraced", "lost", "entered the ring with", "spent & dollars on", "shanked", "imprisoned", "played doubles tennis with", "won a @ lookalike contest against", 
"shot a ^ look at", "took a swing at", "won an all-expenses-paid trip to", "^ly defeated", "whooshed past", "took a ^ picture of", "held a ^ conversation with",
"painted a ^ picture of", "tweeted about", "created a social media platform for", "organized a campaign for", "managed a corporate merger with the help of", "squirted out",
"founded a ^ kingdom with the help of", "^ly destroyed + while researching", "started _ in a garage owned by", "shot", "killed", "murdered", "^ly kissed", "sucked",
"wrote a ^ novel about", "learned about", "squeezed out", "gave birth to", "bought %% for", "drank an entire glass of", "wanted to slap", "^ly swallowed", "loved to hate",
"held a charity yard sale for", "^ly slit the $ of", "^ly saved", "showed real | to", "broke QQ $ because of", "punctured QQ $ with", "chewed up and spit out", "doggedly pursued",
"raised a ^ $ toward", "created the first prototype for", "envisioned a ^ future for", "proposed a toast to", "threw a ^ party to celebrate", "flew too close to", 
"engaged in $-to-$ combat with", "started a restaurant that only serves", "joked about the size of @\'s $ by referencing", "started a petition to outlaw", "held",
"was cast as @ in a TV show about", "started a Kickstarter campaign to fund the creation of", "gave an unexpected proposal to", "became", "was transformed by a magic = into",
"traveled to + with", "created a ^ sport based off the writings of", "wore a ^ dress made of", "made * out of", "contracted a ^ case of ~ from", "forced %% to relinquish",
"was served fine *, which !! paid for by pawning", "commit an armed robbery using", "began a criminal enterprise focused upon", "was marooned in + with only", 
"prepared @\'s favorite * using", "made a pilot for a show about", "climbed to the top of + using just", "climbed _\'s corporate ladder by negotiating using ",
"did groundbreaking research which discovered", "discovered that the secret to time travel is", "stole the secret recipe for * from", "built a factory to produce",
"began a club that focuses on", "conquered QQ intense fear of", "felt a pang of | while mourning the loss of", "peeled the plastic off of a fresh container of",
"threw a hissy fit over", "completely ran out of", "mulled over the idea of", "considered the consequences of endorsing", "gambled away QQ entire supply of", 
"publically denounced", "called out @ over QQ prejudice towards", 'debuted QQ new movie called \"%%CC\", starring', "did voice acting for a game where you play as",
'starred in the new sitcom \"%%CC\" alongside', "donated QQ $ to", "showed QQ | to", "made QQ world-famous * for", "wrote a ^ blog post about", "wrote a ^ song about",
'gave a resounding \"??\" to the idea of', 'said \"??\" to', 'gave a \"??\" when asked about', 'feels pretty \"??\" about', "tenderly held", "shed salty, ^ tears over", 
"mourned the loss of", "won a year's supply of", "pledged to never run out of", "developed a new paradigm around", "changed QQ outlook upon", "scraped out the last bit of a jar of",
"took a big spoonful of", "trusted the | of", "took ^ advice from", "created a new branch of philosophy based on", "couldn\'t belive the | of", "couldn\'t comprehend", 
"found a ^ passion for", "aspired to embody", "harbored a ^ | for", "thought constantly about", "was inspired by the | of", "had QQ $ stolen by", "had QQ closest brush with",
"opened a store that exclusively vends", "waxed poetic about", "choked on too big a bite of", "gave the Heimlich maneuver to", "performed CPR on", "got on QQ soapbox about"]

parties = ["a = wearing false teeth", "the President of +", "the most ^ haircut of all time", "your $ (but & inches in length)", "a =", "Flat Earth Theory",
"nuclear war", "white people", "^ people", "^ stool", "a = that " + utility.getRand(verbs) + " @", "the CFO of _", 'a new street gang called \"the ^CC VVCCs\"', '\"the ^CC VVCCs\"',
"& push-ups", "a ^, ^ bodybuilder", "a = disguised as @", "a ^ly ^ Halloween costume", "the bathroom", "^ soup", "@\'s new $s", "^ *", "a highly ^ strain of ~",
 "a ^CC =CC Champion", "the annual _ dance-off", "Dracula (but if he was from +)", "a ^ly ^ handshake", "an extra set of $s", "a * dish with = meat",
"^ly ^ *", "your ^ dentist", "@\'s accountant", "a mirror that makes you look ^ly ^", "gorgonzola cheese", "the CEO of _", "liquid *", "Obama\'s last name", "The World\'s Largest =CC",
"the entire South Pole", "a stairway to +", "the reason you were born", "a ^ly ^ almond", "a tree", "The World\'s Largest *CC", "money", 
"^, ^ *", "a war between =s and =s", "a ^ly ^ corn dog", "a = with a $ that\'s just too ^", "a = with a =", "a = with too much |", "a = with a ^ $", "The World\'s Smallest *CC",
"the element of surprise", "a slip of the $", "hard, ^ drugs", "a banana that needs to be peeled & times", "* and *", "a perfect doppelganger for @", "=s\' rights",
"the =CC President", "= enthusiasts", "attendees of a $ convention", "the stink eye", "the surface of the sun", "your VV\'s *", "@\'s *", "a =\'s $", "a =\'s *",
"_-branded swag", "_\'s holiday bash", "@", "@\'s secret $", "@\'s $", "#", "a software product for =s", "@\'s raison d\'etre", "an outbreak of ~", "The World\'s Smallest =CC",
"toast", "two =s square-knotted together", "= cruelty", "&th degree murder", "organized crime", "the NYPD", "waaay too much *", "a treasure worth & dollars",
"someone who looks vaguely like @", "*", "^ *", "a mountain of *", "^ gossip", "memes from #", "a ^ baby", "+", "animals", "plants", "dirt", "an active volcano",
"butt", "immortality", "|", "=s", "= enthusiasts", "your $", "the $ of a =", " a = with & extra $s", "^ pants", "QQ VV wearing a @ costume", "QQ VV", "a ^ case of ~",
"@\'s VV\'s favorite VV", "your VV riding a =", "^ chicken nuggets", utility.madeUpWord(False), "a ^ PR campaign", "~", "the asteroid belt", "@\'s pet =", "the sun", "the moon",
'a bar trivia team called \"the ^CC $CC\"', "\'the facilities\'", "our AI overlords", "a hypothetical *", "a hypothetical =", "the Planet of the =CCs", 'the phrase \"??\"',
"a bag of ^ =s", "a can of * that expired in #", "a ^ |", 'the hit show \"%%CC\"', 'the new movie \"%%CC\"', "Donkey Kong Country 2", "my body", "your ^ doctor", 
"a plastic surgeon specializing in $s", "a vet specializing in =s", "a $ surgeon", "mankind", "humanity", "the space-time continuum"]

begs = ["In other news,", "In light of today\'s events,", "Despite what you may have heard,", "QQ VV looked me right in the $ and said:", "After drinking & gallons of liquid *,",
"Having been born in the year #,", "Despite a lifelong battle with ~,", "Picture this in your mind for a moment:", "Fun fact:", "Did you know?", 
"| is cancelled today, due to the fact that", "Have you considered the fact that", "My favorite childhood memory is when", "What\'s ^ is that mainstream media would have you believe", 
"After eating & pounds of *,", "Once upon a time,", "When you really think about it,", "Yesterday,", "Whenever @ looks ^, it\'s because", "In the year of Our Lord #,", 
"My pitch for a hit new TV show:", "In case you haven\'t heard yet,", "Through sheer | and |,", "If you ever have a ^ day, just remember", "In an act of |,", 
"^ly, due to %%,", "If you squint and turn your head ^ly to the side, you\'ll see that", "Despite having ^ |,", "If a = or @ is attacking you, remember that", 
"Thanks to free speech,", "Wanna really get QQ attention? Lay one of these on !!!:", 'The German word \"' + utility.madeUpWord(False) + '\" describes the situation where', 
"@ has released the following statement:", "The hidden country of " + utility.madeUpWord(True) + " is where", "To strike a balance between | and |,", "To fill your life with |,", 
"To fill your $ with |,", "To impart | into @\'s $, declare that", "To fill @ with |,", "Were you aware that", "If you ever visit +, ask the locals about how", 
"It fills me with | to know that", "What if", "What !! teach in schools now is that", "An unprecendented turn of events:", "If !! got out once in a while, !!'d know that",
"Due to an outbreak of ~,", "History would never be the same after the day that", "Due to %% and QQ *,", "Before !! " + utility.getRand(verbs) + " %%,",
"I know it sounds ^, but", "%% tells me that", "All existing evidence suggests that", "We hold this truth to be self-evident, that", "Today's kids can\'t stop talking about how",
"If !! want to get kicked out of +, !! should say that", "Congress met today to discuss the issue of how", "Today's kids only worry about how",
"^ band name suggestion:", "Our AI overlords wanted me to inform you that", "We regret to inform you that", "A ^ book premiers today which will reveal the story behind how", 
"There is hope for %% as long as", "??, hope for humanity lost;", "?? -", "??;", "??,", "??...", "??!", "???", "The secret message on the back of the Constitution:",
"Hope for humanity restored:", "Because of @\'s ^ |,", "In a display of ^ |,", "Since I just contracted a ^ case of ~,"]

adjectives = ["dumb", "ugly", "brown", "campy", "proverbial", "obtuse", "arrogant", "swollen", "frightening", "hungry", "diseased", "naked", "squirming", "^---$--\'d", "surprising",
"short", "rank", "malodorous", "cold", "long", "wide", "clammy", "strong", "stirring", "classy", "high-brow", "fat", "overweight", "wooden", "verdant", "al dente", "chewy", "fudgy",
"pink", "local", "sweaty", "dry", "freeze-dried", "heroic", "suspicious", "explosive", "chunky", "*---flavored", "finely-aged", "expired", "evil", "chaotic", "black", "white", 
"chocolatey", "fast", "intimidating", "drowning", "bland", "problematic", "rootin\' tootin\'", "blessed", "savage", "room-temperature", "underwhelming", "incompetent",
"overzealoused", "slow", "burnt", "venomous", "uplifting", "beautiful", "juicy", "wet", "damp", "moist", "uncomfortable", "unhealthy", "long-winded", "unfair", "racist", 
"annoying", "pugnacious", "stabbing", "voluptuous", "candid", "quiet", "thin", "skinny", "thick", "dull", "insipid", "twisted", "knarled", "stinky", "sweet", "accidental",
"pompous", "fancy", "well-dressed", "sharp", "red", "bent", "pointed", "heavy", "tense", "intense", "lurid", "mild", "mild-mannered", "terrible", "horrible", "heinous", "passionate",
"cruel", "bumpy", "lumpy", "angry", "livid", "unnerving", "disgusting", "creamy", "woody", "peppery", "piquant", "fashionable", "prudent", "unflattering", "tricky", "more-than-^--",
"efficient", "complementary", "fortitudinous", "hard", "stiff", "tart", "sour", "acidic", "viscous", "^ly ^",  "demanding", "draining", "clever", "peanut-buttery", "verbose",
"exhausting", "well-behaved", "cute", "stunted", "bad", "good", "great", "boring", "less-than-^--", "cringeworthy", "nerdy", "racy", "new", "interesting", "useful", "good",
"elaborate", "live", "cultured", "slightly ^", "overly ^", "not-so-^--", "crispy", "crunchy", "pure", "medium-sized", "furtive", "poor", "milquetoast", "pensive", "suave",
"overwhelming", "wrong", "well-written", "happy-go-lucky", "old", "medium-sized", "extra large", "loose", "political", "particular", "thoughtful", "confusing", "mean", "useless",
"innappropriate", "quick", "fluent", "odd", "weird", "unusual", "stupid", "suspicious", "slight", "confident", "exaggerated", "unwavering", "true", "real", "emotional",
"physical", "spiritual", "virtual", "textural", "perfect", "hot", "male", "female", "broken", "stern", "whiny", "indignant", "bright", "massive", "bare", "deft", "swift",
"convenient", "functional", "chic", "united", "greedy", "brash", "proud", "unstoppable", "floppy", "flailing", "full", "positive", "negative", "dirty", "fishy", "filthy",
"candy", "iron", "bronzen", "flaxen", "golden", "rock-hard", "titanium", utility.madeUpWord(False), "moderate", "impressive", "successful", "unsuccessful", "hypothetical", "insufficient",
"frozen", "melted", "acute", "instant", "amateur", "flat", "unprecedented", "uncouth", "unbecoming", "subpar", "violent", "unattractive", "edible", "sociable", "dangerous", 
"fiscal", "invisible", "unexpected", "secret", "cool", "erect", "sexy", "appalling", "horrifying", "contagious", "profound", "colorful", "universal", "unidentifiable", "blue",
"green", "yellow", "purple", "painful", "unpleasant", "unsightly", "foul", "permanent", "desperate", "impotent", "unprofessional", "omnipresent", "soaring", "ethereal",
"exquisite", "elegant", "dark", "rude", "insane", "crazy", "vegan", "*---free", "greasy", "choice", "random", "buxom", "sad", "angry", "furious", "load-bearing", "morose", 
"gleeful", "awful", "above-average", "below-average", "inspiring", "utterly ^"]

concepts = ["gusto", "fervor", "panache", "restraint", "style", "wherewithall", "curiosity", "pride", "luck", "chastity", "charity", "joy", "wonder", "dread", "terror",
"passion", "delicacy", "peace", "understanding", "va-va-voom", "swagger", "ingenuity", "self-control", "spirit", "innovation", "clarity", "je ne sais quoi", "gumption", "||",
"love", "nerve", "hutzpah", "cacahuetes", "resolve", "verve", "boldness", "genius", "grit", "determination", "hunger", "rage", "nostalgia", "melancholy", "wistfulness",
"longing", "resilience", "wit", "faith", "honor", "candor", "serenity", "hope", "patience", "kindness", "cheer", "goodwill", "can-do attitude", "spirit", "moxie", "soul",
"joie de vivre", "virtue", "courage", "fire", "selflessness", "pride", "glamour", "$", utility.madeUpWord(False), "culture", "disdain", "apprehension", "hesitancy", "cowardice", 
"evil", "coldness", "underhandedness", "subtlety", "visibility", "sausage", "pancakes", "stupor", "~", "ambition", "fear", "shame", "desperation", "security", "dignity",
"fidelity", "humility", "honesty", "humor", "horror", "ego", "guilt", "kindness", "gentleness", "despair", "consternation", "regret", "remorse", "science", "math", "geometry",
"physics", "arithmetic", "trigenometry", "chemistry", "somatics", "logic", "ethics", "philosophy", "psychology", "sociology", "mercy", "grace", "compassion", "politics", 
"economics", "semantics", "sadness", "grief", "sorrow", "despair", "heat", "ice", "anger", "purpose", "*"]

ends = [" while @ was still president.", ", using QQ $ to chug a two-liter of liquid *.", " with the | of a ^ =.", " - how ^ is that?", ", demonstrating ^ |.",
", which, ^ly, broke the world record.", ", because that\'s what ^ | looks like.", ", cause money don\'t grow on %%.", ", showing no |.",
" - however, this angered the envoy from +, starting World War &.", ", and that\'s a fact.", " with a | that rivals @'s.", " whilst fending off ^ ladies with a ^ spatula.",
" as part of a ^ comedy routine.", ", starting a new dance craze on _\'s video-sharing hub.", ", inspiring @ to paint a ^ picture of @.", ", inspiring @ to found _.",
", landing !!! in ^ water with +.", ", which @ then made a ^ joke about on _'s new social media platform.", ", which jumpstarted @\'s | for +\'s |.", "... ??.", ", ??!",
", making @ feel like a ^ =.", ", which gave @ ~.", ", which has to be the most ^ way to lose weight.", " - thanks a lot, VV!", ". ;)", "... ??!",
", which took a lot of |.", " to prove to QQ VV that !! have ^ |.", ", in hopes that it would make @ notice QQ |.", ", which prompted @ to have !!! cancelled.", 
" - the three words I'd use to describe this would be ^, ^, and ^!", " - what a ^ time to be ^!", " - what a ^ way to have " + utility.getRand(verbs) + "!",
" by sitting and thinking very hard about %%.", " by the $ of @.", " - now that shows some ^ |!", " - now that takes some |!", " - seems a bit ^ to me...", ", which is SO not ^.", 
", giving everyone ~.", ", utilizing only %% and %%.", ", causing @ to break QQ $.", ", causing @ to instantly grow a new $.", ", after which @ got QQ $ pierced.", " - ??.",
" - in other words, " + utility.madeUpWord(False) + ".", ", permanently eradicating ~.", ", which gave @ ~.", ", curing @'s severe case of ~.", ", which is how @ and @ met.", 
", which sparked @'s interest in |.", ", which should fill you with |.", ". --@", ", which is how @ contracted ~.", " - ??!", " - ???",
", after which QQ $ fell off.", ", which is probably QQ best work.", ", which is a real slap in the $.", ' - well, "??" to you too!', " - ??, ??.", " - ??, ??!",
", which happens to be the backstory for my new character, *CCMan.", " - but what about !!!?", ", which, for !!!, was ^ly ^.", " with & sacks of * in QQ $."]

companies = ["Coca-Cola", "Monster Energy", "Frito-Lay", "Nestle", "Google", "Microsoft", "Minecraft", "JP Morgan", "Taco Bell", "Verizon", "US Cellular", "Cingular", 
"VVCC Jeans, Inc", "IBM", "Fatheads", "Fiji Water", "Vance Refrigeration", "Disney", "Fox News", "MSNBC", "Walmart", "IKEA", "Snuggie", "FlexTape", 
"Piggly Wiggly", "Purple Flurp", "Facebook", "Twitter", "Doofenshmirtz Evil, Inc", "Netflix", "Dunder Mifflin", "Apple", "WUPHF", "the Krusty Krab", "the Chum Bucket",
"Doritoes", "Target", "PETA", "Gamestop", "Dogecoin", "Youtube", "Naughty Dog", "CoolMath Games", "McDonald's", "Burger King", "Long John Silver's", 
"Nintendo", "Sony", "Gfuel", "Gamer Goo", "Dunkin Donuts", "Raid: Shadow Legends", "Pixar", "Popeye's", "Papa John's", "Tik Tok", "Buy 'n Large", "Activision", "DreamWorks",
"Starbucks", "Raid: Shadow Legends", "Blizzard", "FizzBuzz Inc", "Los Pollos Hermanos", "Amazon", "SpaceX", "Tesla", "Tumblr", "MySpace", "Reddit", "BitConnect", "The Dentist",
"Cost Cutters", "Dr. Pepper", "Pepsi", "GameStop", "|CC Inc", "$CCs-R-Us", "=CCs-R-Us", "Chuck-E-Cheese", "Candy Crush", "Angry Birds", "Staples", "OfficeMax", "PETA", "the CDC",
"Instagram", "Netflix", "Snapchat", "Spotify", "Vine", "Twitch", "Hulu", "Unilever", "Perdue Pharma", "BetterHelp", "the CIA", "the FBI", "the Department of Justice",
"the Department of Defense", "the NSA", "the FDA", "the CDC", "the US Government", utility.madeUpWord(True) + " Corp"]

celebs = ["Dolly Parton", "Robert Pattinson", "the Geico =CC", "the = from Air Bud", "Keanu Reeves", "the Car =CC", "Crisp Rat",
"Ben Shapiro", "PewDiePie", "Elvis", "Nickelback", "Guy Fieri", "Gordon Ramsay", "a =", "a ^ =", "a ^ =", "The ^CC Man", "a ^ piece of fruit", "Jennifer Lawrence",
"Michael Scott", "Ghandi", "the Pope", "Jimmy Neutron", "Carl Wheezer", "the Pillsbury Dough Boy", "Jake Paul", "Logan Paul", "you", "your VV", "Jeff Dunham", "Olivia Cockburn",
"Dane Cook", "George Washington", "Thomas Jefferson", "Abraham Lincoln", "Plato", "Aristotle", "Leonardo Da Vinci", "John Kennedy", "Isaac Newton", "Albert Einstein", 
"Will Ferrel", "Ariana Grande", "Paul Revere", "Queen Elizabeth", "Christopher Columbus", "JK Rowling", "Pablo Picasso", "Walt Disney", "Winston Churchill", 
"Elon Musk", "Bill Gates", "Jeff Bezos", "Steve Irwin", "Billy Mays", "the ^ guy from Friends", "the ^ girl from The Office", "Chester Cheeto", "Reggie Fils-Aime", "John Doe",
"Tony the =CC", "=CC Sam", "the Trix =CC", "John Mayer", "Elvis", "the Prince of |CC", "the Prince of *CC", "Mario", "Luigi", "Waluigi", "your favorite =", "Benedict Cumberbatch",
"the Duke of *CC", "Jake the =CC", "the Ice King", "Spongebob Squarepants", "QQ ^ VV", "Will Smith", "Miranda Cosgrove", "Drake and Josh", "the Burger King", "Doug",
"CatDog", "= =", "Arnold (from Hey Arnold)", "=CCMan", "The all-new Hyundai Sonata", "The ^CC $CC", "Joker (from Joker)", "Squidward", "Patrick", "Hoobastank", "Harold",
"Brendan Frasier", "Tommy Wiseau", "Kirby", "Bubsy", "Bigfoot", "Sonic the =CC", "Gurbanguly Berdimuhamedow", "Kim Jong Un", "Xi Jinping", "Moon Jae-in", "Death", "John Cena",
"Reggie Fils-Aime", "Yoshihide Suga", "Grandma", "Grandpa", "^CCMan", "Finn the =CC", "a _ employee", "Warren Buffet", "Billie Eilish", "Videogamedunkey", "Grover Cleveland", 
"Thomas Edison", "Winnie the Pooh", "QuailMan", "Jeffery Bezos", "Vermin Supreme", "Chris Hemsworth", "Chevy Chase", "Dick Van Dyke", "Andy Griffith", "Bob Hope", 
"Regis Philbin", "Dr. Phil", "Hulk Hogan", "Honey Boo-Boo", "Gordon Ramsay", "Bo Burnham", "Obamna", "Conan O'Brian", "Steve Carrell", "James Brown", "Michael Jackson",
"Steve Harvey", "Tim Apple", "The One True =CC", "Peewee Herman", '@ AKA \"the ^CC =CC\"', "me", "Rongle McDongle", "*CCMan", "George RR Martin", "George Bush",
"Charles Entertainment Cheese", "Larry the *CC", "Bob the *CC", "Gex", "Glover", "Donkey Kong", "Bowser", "Dark Souls", "@'s new lover (@)", "Ornstein and Smough",
"Lord Gwyn", "the Gaping Dragon", "Cranky Kong", "Funky Kong", "Aldia, Scholar of the First Sin", "Manus, Father of the Abyss", "Knight Artorias", "the Firekeeper",
"Martin Shkreli", "Adele", "John Krasinski", "Justin Bieber", "Brian Peppers", "Moses", "Richard Nixon", "Bill Clinton", "Ronald Reagan", "George Bush", "Andrew Jackson", 
"Andre the Giant"]

places = ["^CC Jersey", "the ^CC States", "Europe", "Russia", "Asia", "Japan", "yo VV's house", "the sock drawer", "Madagascar", "Californ-I-A", "your soul", 
"the corporate offices of _", "the ^CC House", "Yellowstone Park", "Italy", "the Pentagon", "Mount Everest", "an underground city", "the ^ dungeon", "a ^ city",
"China", "Fiji", "India", "Pyongyang", "Seoul", "one of the Koreas", "the states of ^CC and ^CC Dakota", "Hell", "^CC Virginia", "^CC Carolina", "Hell", "the year #",
"^CC York", "^CC Delhi", "Stonehenge", "VV's basement", "the Pacific Ocean", "the Statue of Liberty", utility.madeUpWord(True), "the mouth of a =", "Delfino Plaza", "the 90s",
"a ^ hill of termites", "the realm of the =CC Queen", "$CCs-R-Us", "#", "Disneyland", "Mount Rushmore", "the =CC Kingdom", "^CC Mexico", "the @ estate", "@'s house", "=CCs-R-Us",
"Tokyo", "Beijing", "Athens", "Ancient Rome", "London", "Austrialia", "^CC Zealand", "Azerbaijan", "Heaven", "the University of +", "^CCLand", "^CC-^CCLand", "Flat Earth",
"*CCLand", "=CCLand", "_'s headquarters", "Anor Londo", "Drangleic", "Londor", "the Abyss", "the ^CC Abyss", "New Londo", "Planet Namek", "the ^CC Planet", "QQ @ shrine",
"Planet ^CC's &th moon", "the Planet of the =CCs", "Firelink Shrine", "the Catacombs", "the =CC Temple", "the =CC Shrine", "@'s personal aircraft", "the |CC Dimension",
"Majula", "Kong Island", "Krem Quay", "Schitt's Creek"]

animals = ["lion", "cat", "dog", "squid", "mollusk", "clam", "zebra", "axolotl", "rhino", "tiger", "lamb", "octopus", "antelope", "fawn", "llama", "parrot", "whale", 
"geoduck", "barnacle", "snail", "slug", "squirrel", "giraffe", "dingo", "wolf", "coyote", "hyena", "ocelot", "puma", "mountain lion", "fox", "polar bear", "grizzly bear", 
"goldfish", "monkey", "spider monkey", "chimpanzee", "brown bear", "black bear", "lemur", "chihuahua", "flounder", "clownfish", "dolphin", "scallop", "sphinx", "griffin", 
"dragon", "donkey", "unicorn", "yokai", "mouse", "rat", "pig", "cow", "bull", "dove", "shrew", "armadillo", "pangolin", "anteater", "snake", "viper", "cobra", "orangutan", 
"rabbit", "bunny", "jackalope", "chimera", "cerberus", "manticore", "scorpion", "mosquito", "horsefly", "ladybug", "black widow", "brown recluse", "wolf spider", "human",
"dung beetle", "salamander", "firedrake", "wendigo", "wyvern", "sea lion", "pokemon", "goat", "cheetah", "animal", "worm", "lizard", "fish", "person", "hamster", "chick", "mushroom",
"labrador", "pit bull", "schnauzer", "beetle", "rodent", "feline", "canine", "bovine", "grandaddy long legs", "weevil", "earwig", "silverfish", "android", "cyborg", "wizard", 
"leopard", "elephant", "newt", "jellyfish", "mandrake", "sentient plant", "talking =", "panda", "lizard", "doberman", "beagle", "yorkie", "jackrabbit", "tarantula", 
"porpoise", "frog", "pit bull", "eldritch horror", "dingo", "indeterminate bug", "hedgehog", "toucan", "turtle", "lizard", "toad", "tiger", "roach", "insect", "arachnid", 
"cockroach", "butterfly", "caterpillar", "dragonfly", "behemoth", "mole", "mantis", "monster", "moth", "reptile", "amphibian", "mammal", "bird", "flamingo", "penguin", "baby",
"centipede", "devil", "demon", "angel", "eagle", "hawk", "falcon", "owl", "parrot", "peacock", "pigeon", "man", "woman", "bard", "rogue", "paladin", "necromancer", "valkyrie", 
"jester", "king", "technocrat", "oligarch", "dictator", "thief", "archer", "berserker", "viking", "spellsword", "alien", "hyena", "platypus", "badger", "komodo dragon", 
"stinko", "tortoise", "manta ray", "politician", "scientist", "astronaut", "doctor", "proletariat", "bourgeoisie", "pariah", "pope", "priest", "minion", "minstrel", "minister",
"merchant", "mermaid", "seaman", "pirate", "monk", "ninja", "nun", "rottweiler", "weimaraner", "vischla", "vampire", "terrier", "hound", "warrior", "crane", "crony", "raven",
"crow", "sparrow", "robin", "bat", "bee", "hornet", "yellowjacket", "wolverine", "wombat", "vagrant", "wabbit", "warthog", "weasel", "werewolf", "hagraven", "harpy", "hippogriff",
"hippopotamus", "spriggan", "troll", "gnome", "gargoyle", "giant", "gorgon", "griffin", "python", "water =", "lamb", "swine", "buffalo", "bison", "elk", "boar", "wild =",
"teenager", "adolescent", "elder", "puppy", "kitty", "hag", "bride", "groom", "witch"]

parts = ["ear", "eye", "nose", "earlobe", "right pinky toe", "patella", "&th eyelash from the right", "entire body", "&th nipple", "foot", "third foot", "top right incisor", 
"tooth", "teeth", "elbow", "bellybutton", "fingernail", "brain", "xiphoid process", "tooth enamel", "skin", "armpit", "foot", "bottom leg", 
"spare rib", "cheek", "butt", "no-no square", "fingie", "upper lip", "glabella", "pituitary gland", "thyroid gland", "tear duct", "epidermis", "nerve ending", "bunion", 
"amygdala", "toe", "finger", "eye", "chest", "knee", "lower back", "upper back", "ab", "diaphragm", "tongue", "epiglottis", "vocal fold", "uvula", "stomach", "peep",
"gut", "larynx", "esophagus", "pelvis", "tibia", "phalange", "skull", "head", "scapula", "spleen", "sacrum", "coccyx", "spine", "funny bone", "cerebral cortex", "brain stem", "neck",
"mouth", "inner thigh", "urethra", "pancreas", "lung", "gallbladder", "appendix", "rectum", "hand", "chest hand", "limb", "beard", "sternum", "callous", "scalp", 
"frenulum", "pie hole", "tush", "teat", "sausage", "ovary", "nostril", "eardrum", "tummy", "mind", "&th $", "*"]

disease = ["$ cancer", "diabetes", "$ swelling", "$ destruction", "$ blockage", "$ parasites", "$ failure", "$ erosion", "$ disease", "$ infection", "claustrophobia", 
"MRSA", "food poisoning", "depression", "asthma", "anxiety", "alcoholism", "impulsive shopping", "darwinism", "halitosis", "gynecomastia", "gastroenteritis", 
"anal fissures", "^ $ pain", "ugliness", "a really weird $", "= $", "pregnancy", "obesity", "sociopathy", "antidisestablishmentarianism", "pneumonoultramicroscopicsilicovolcanoconiosis",
"gastroenteritis", "PMS", "athlete's foot", "complementarianism", "extra limbs", "kidney stones", "broken $", "^-$", "hotdog finger", "count-choculitis", "no longer being alive", 
"spontaneous dental hydroplosion", "chronic ~", "swine flu", "literally every STI", "loss of $", "diminished |", "vitamin deficiency", "egalitarianism", "dwarfism", 
"|-deficiency", "=phobia", "rapidly-aging $", "a * allergy", "too much *", "^-*--", "$ pus"]

possessives = ["their", "its", "his/her", "the", "her", "his", "de", "@'s", "your", "my", "y'all's", "VV's", "our", "somebody's", "a ^", "a random", "thy", "yo VV's", "yo"]

pronounsSubject = ["they", "it", "he/she", "she", "he", "dey", "@", "you", "I", "y'all", "we", "somebody", "%%", "thou", "yo VV", "ya"]

pronounsObject = ["them", "it", "him/her", "her", "him", "dem", "@", "you", "me", "y'all", "us", "those", "%%", "thee", "yo VV", "'em"]

family = ["mom", "gramma", "grampa", "gramps", "grampie", "momma", "daddio", "g-dizzle", "brother", "sister", "mother", "dad", "stepdad", "step-sister", "step-brother", "stepmom", 
"cousin", "great-great-great VV", "uncle", "aunt", "daddy", "mommy", "gruncle", "daughter", "son", "niece", "nephew", "&th cousin, & times removed", "father", "b-pizzle",
"VV's VV's VV's great VV's great step-VV", "husband", "wife", "&th husband", "&th wife", "family", "sis", "honey", "sweetie", "baby", "teenage child", "sugar", "cousin",
"disgruntled employee", "great VV", "step-VV", "friend", "homie", "sugar momma", "sugar daddy", "baby daddy"]

foods = ["broccoli", "carrots", "cabbages", "cauliflower", "celery", "creamed corn", "cucumbers", "eggplants", "garlic", "ginger", "green beans", "kale", "lettuce", "mushrooms", "water",
"burritos", "brownies", "cake", "vegetables", "fruit", "apples", "pears", "peaches", "peppers", "pineapples", "pizza", "potatoes", "radishes", "rice", "salad", "soup", "tomatoes",
"lima beans", "spinach", "radicchio", "eggs", "yogurt", "cheese", "sour cream", "flour", "sugar", "salt", "peanuts", "butter", "honey", "bagels", "doughnuts", "cookies", "pie",
"cranberries", "strawberries", "blueberries", "raspberries", "blackberries", "grapes", "grapefruits", "kiwis", "lemons", "limes", "oranges", "plums", "pomegranates", "pumpkins", "hamburgers", 
"hot dogs", "sandwiches", "sausages", "pepperonis", "salamis", "fried chicken", "collard greens", "lettuce", "pasta", "sushi", "fish", "gravy", "pork", "beef", "bacon", "steak",
"alcohol", "lemonade", "cola", "soda", "coffee", "tea", "salsa", "refried beans", "curry", "chili", "chowder", "stew", "mashed potatoes", "tacos", "lo mein", "matcha", "almonds",
"brussels sprouts", "milk", "anchovies", "avocados", "coconuts", "coconut milk", "coconut oil", "coconut water", "custard", "dressing", "egg whites", "nuts", "pudding", "pepper",
"mustard", "ketchup", "mayonnaise", "olive oil", "pickles", "* juice", "fried =", "= oil", "= juice", "= sauce", "boiled =", "baked =", "cooked =", "pancakes", "filet mignon",
"eggs benedict", "beef wellington", "quail", "= grease", "= milk", "syrup", "= concentrate", "cream of *", "cream of =", "= eggs", "pringles", "oreos", "doritos", "mountain dew",
"chocolate", "endives", "parsley", "marjoram", "basil", "cinnamon", "coriander", "dill", "fennel", "pickled *", "pickled =", "* vinegar", "= vinegar", "* syrup", "= syrup", 
"= meat", "Dr. pepper", "fried *", "deep-fried *", "deep-fried =", "* meat", "= cheese", "* oil", "barf", "puke", "biscuits", "= soup", "= gravy", "* soup", "* gravy", "= tacos",
"* grease", "* eggs", "* sauce", "* milk", "* tea", "cumin", "anise", "paprika", "bananas", "dragonfruit", "= pie", "* pie", "vegan = meat", "vegan *", "^ cheese", "* cheese",
"* paste", "= paste", "boiled *", "arugula", "artichokes", "asparagus",  "beans", "beets", "happy meals", "= entrails", "= broth", "hummus", "chickpeas"]

interjection = ["OK", "alright", "cool", "whatever", "great", "perfect", "who\'d have thought", "yikes", "ouch", "thank goodness", "awkward", "awesome", "sheesh", "darn it all", 
"shoot", "how ^", "that's too bad", "how sad", "uh oh", "for pete\'s sake", "for crying out loud", "tough *", "how frustrating", "how embarrassing", "hmm", "what a show of |",
"never seen such |", "takes my | away", "bless QQ heart", "watch out", "preposterous", "wonderful", "for *'s sake", "tarnation", "consarnit", "^", "nice", "how dare @", 
"what |", "welp", "oh well", "gadzooks", "eureka", "aw man", "forsooth", "alas", "amen", "how could this be", "it can't be true", utility.madeUpWord(False), "golly", "yay", "!! don\'t care",
"crikey", "exclamation", "for |\'s sake", "what a =", "double drat", "so", "haha", "cringe", "don\'t get me started", "well slap my $ and call me a VV", "well, ??", "sorry",
"hallelujah", "my my", "oh my", "holy =", "holy *", "really", "oh yeah", "uh-huh"]

# ideas: quantities, occasions, colors
# less necessary but still options: sports, languages, nationalities, countries?, cities?