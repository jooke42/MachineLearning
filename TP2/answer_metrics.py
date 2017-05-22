import re
class answer_metrics():
    """
     Calcul de tout un tas de métriques associées à un texte. 
     'av_words' : nombre moyen de mots par phrase
     'code' :  code contenu dans le texte
     'extract_code' : métode pour extraire le code
     'html' :  texte initial
     'len_html' : longueur du html
     'nb_allcaps' : nombre de mots en majuscules
     'nb_codelines' : nombre de lignes de code
     'nb_imgs' : nombre d'images
     'nb_lines' : nombre de lignes
     'nb_links' : nombre de liens
     'nb_paragraphs' : nombre de paragraphes
     'nb_pretty' : nombre de mises en forme gras, italique, souligné,  
     'nb_words' : nombre de mots
     'strip_code' : méthode pour retirer le code
     'striphtml' : méthode pour retirer le texte html
     'text' : le texte sans html
     =================================================
     auteur: jfb mars 2015
    
    """
    import re
    def __init__(self,text=None):
        if text is None: 
            print("You  need to feed the object with a text")
        else:    
            self.html=text
            self.code=self.extract_code()
            self.text=self.striphtml(self.strip_code())
        
    def __call__(self,text=None):
        if text is None: 
            print("You  must feed the object with a text")
        else:    
            self.html=text
            self.code=self.extract_code()
            self.text=self.striphtml(self.strip_code())                    

    def striphtml(self,text):
        return re.sub('<[^<]+?>', '', text)
    
    def len_html(self):
        return len(self.html) 
    
    def extract_code(self):
        out=re.findall('<pre><code>([\s\S]*?)</code></pre>', self.html)
        return out
    
    def nb_paragraphs(self):
        nb_p=len(re.findall("<p>",self.html))
        return nb_p
    
    def strip_code(self):
        out=re.sub('<pre><code>([\s\S]*?)</code></pre>', '',self.html)
        return out

    def nb_codelines(self):
        Lcode=0
        for code in self.code:
            Lcode=Lcode+len(code.split('\n'))-1 #not perfect. Fails on expression involving \n
        return Lcode

    def nb_lines(self):
        Llines=len(self.text.split('\n'))
        return Llines

    def nb_allcaps(self):
        allcaps=re.findall('\\b[A-Z]{2,}\\b',self.text)
        Lallcaps=len(allcaps)
        return Lallcaps

    def nb_words(self):
        Nbwords=len(self.text.split())
        return Nbwords

    def av_words(self):
        sentences=re.split("\\w[\.!?]",self.text)
        nb_sentences=len(sentences)
        nb_words=0
        for sentence in sentences: nb_words+=len(sentence.split())
        return nb_words, nb_words/nb_sentences    
    
    def nb_pretty(self):
        return len(re.findall('<strong>',self.html))+\
                len(re.findall('<li>',self.html))+\
                len(re.findall('<em>',self.html))

    def nb_links(self):
        links=re.findall('<a href="http://.*?".*?>(.*?)</a>',self.html)
        nb_links=len(links)
        return nb_links

    def nb_imgs(self):
        imgs=re.findall('<img(.*?)/>',self.html)
        nb_imgs=len(imgs)
        return nb_imgs    

#a=answer_metrics (tst_texte)       