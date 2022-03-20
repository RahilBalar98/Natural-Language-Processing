def preprocess(text):
    stopwords = set(STOPWORDS)
    stopwords.update(["american", "air","airline","thank","united","us","airways","virgin","america","jetblue","youre","extremely",
                     "usairway","usairways","flight","americanair","southwestair","southwestairlines","arbitrarily","dream","crazy",
                     "southwestairway","southwestairways","virginamerica","really","will","going","thanks","thankyou","passengersdont",
                     "please","got","let","take","help","already","never","now","told","guy","new","sure","still","amp","continue",
                     "plane","tell","ye","trying","yes","guy","much","appreciate", "thx","back","ok","good","credit","aacom",
                     "flying","love","great","awesome","see","nice","alway","httptcojwl26g6lrw","dontflythem","motherinlaw","night",
                     "nogearnotraining","seriously","didnt","coudnt","cant","wont","dont","wat","buffaloniagara","hasshe","morning",
                     "woulda","people","try","youve","youd","yours","flightled","tomorrow","today","wat","jfkyou","flite","cause",
                     "flightr","flight","need","hours","nooooo","like","doesnt","right","talk","tweet","mention","pbijfk","ridiculuous",
                     "wasnt","suppose","want","understand","come","work","worse","treat","think","know","worst","paulo","staduim",
                     "wouldnt","stay","away","wont","werent","happen","sorry","havent","tonight","drive","life","thing","aa951",
                     "whats","theyre","better","thats","allow","hope","stop","cool","niece","happy","word","customercant",
                     "suck","sunday","monday","tuesday","wednesday","thursday","friday","saturday","weekend","ruin","shouldnt",
                     "miami","los angeles","new york","chicago","dallas","apparently","itover","someones","savannah","lucymay",
                     "betterother","instead","look","hopefully","yesterday","antonio","unacceptable","folks","record",'arent',
                     "miss","hang","wrong","stick","grind","tarmac","theres","forget","terrible","clothe","terrible","break",
                     "actually","frustrate","correct","ridiculous","expect","different","pathetic","bother","follow","fault",
                     "impossible","point","cover","person","ask","speak","things","earlier","mean","select","minutes",
                     "unite","horrible","country","leave","speak","apologize","faster","hop","confuse","lose","flightd","hear",
                     "literally","years","surprise","bump","fail","compensate","hand","helpful","upset","friend","excuse","claim",
                     "situation","multiple","weather","choose","company","believe","question","kick","anymore","awful","delta",
                      "dozen","medical","completely","finally", "waste","shock","annoy","maybe","strand","mess","finally",
                      "plan","place","apology","center","plan","twitter","promise","prefer","count","maybe","shock","longer","meet",
                         "important","drop"])
 
    #stopwords.update([i for i in ts])
    # stopwords.update([str(i).lower() for i in cities.City]) #removing City names in US
    r = re.compile(r'(?<=\@)(\w+)') #remove words after tags --> usually twitter account
    ra = re.compile(r'(?<=\#)(\w+)') #remove words after hashtags
    ro = re.compile(r'(flt\d*)') #remove words after flight number
    names = r.findall(text.lower())
    hashtag = ra.findall(text.lower())
    flight = ro.findall(text.lower())
    lmtzr = WordNetLemmatizer()
    def stem_tokens(tokens, lemmatize):
        lemmatized = []
        for item in tokens:
            lemmatized.append(lmtzr.lemmatize(item,'v'))
        return lemmatized
    def deEmojify(inputString):
        return inputString.encode('ascii', 'ignore').decode('ascii')

    text = deEmojify(text)
    soup = BeautifulSoup(text)
    text = soup.get_text()
    text = "".join([ch.lower() for ch in text if ch not in string.punctuation])
    tokens = nltk.word_tokenize(text)
    tokens = [ch for ch in tokens if len(ch)>4] #remove words with character length below 2
    tokens = [ch for ch in tokens if len(ch)<=15] #remove words with character length above 15 
    lemm = stem_tokens(tokens, lmtzr)
    lemstop = [i for i in lemm if i not in stopwords]
    lemstopcl = [i for i in lemstop if i not in names]
    lemstopcl = [i for i in lemstopcl if i not in hashtag]
    lemstopcl = [i for i in lemstopcl if i not in flight]
    lemstopcl = [i for i in lemstopcl if not i.isdigit()]
    return lemstopcl
