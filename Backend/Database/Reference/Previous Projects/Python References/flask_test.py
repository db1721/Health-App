from flask import Flask
import datetime
import pytz

fmt = '%H:%M:%S'
date = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
formattedDate = date.strftime('%B %d, %Y')

time = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
formattedTime = time.strftime(fmt)

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    index = popHead("Getting Started");
    index += popParagraph(popLink("http://localhost:5000/MakeRecipe",
                                  "Go to the best mouse recipe"))
    index += popParagraph(popLink("http://localhost:5000/StoreMedia",
                                  "Go to the best media streaming service"))
    index += popParagraph(popLink("http://localhost:5000/LearnGuitar",
                                  "Go to a playlist to learn guitar"))
    index += popDateTime(formattedTime, formattedDate)
    index += popEnd()
    return index

@app.route('/MakeRecipe')
def recipeIndex():
    index = popHead("The Best Recipe!!");
    index += popH1('This is the best recipe for Keto Chocolate Mouse')
    index += popReturn()
    index += popH2(popUnorderList("<li>2 ripe avocados</li>"
                                  "<li>3/4 c. heavy cream</li>"
                                  "<li>1/2 c. keto-approved chocolate chips "
                                  "(we love Lily's), melted</li>"
                                  "<li>1/4 c. honey or your favorite keto "
                                  "sweetener</li>"
                                  "<li>3 tbsp. unsweetened cocoa powder</li>"
                                  "<li>1 tsp. vanilla</li>"
                                  "<li>1/2 tsp. kosher salt</li>"
                                  "<li>chocolate curls, for garnish "
                                  "(optional)</li>"))
    index += popH3(popOrderList("<li>In a food processor or blender, blend "
                                "all ingredients except chocolate curls until"
                                " smooth.</li>"
                                "<li>Transfer to serving glasses and "
                                "refrigerate 30 minutes and up to 1 hour. "
                                "Garnish with chocolate curls if "
                                "using.</li>"))
    index += popParagraph(popLink("https://www.delish.com/cooking/recipe-"
                                  "ideas/recipes/a57631/paleo-chocolate-"
                                  "mousse-recipe/","Keto Chocolate Mouse"))
    index += popDateTime(formattedTime, formattedDate)
    index += popEnd()
    return index

@app.route('/StoreMedia')
def mediaIndex():
    index = popHead("The Best Place to Store Personal Media");
    index += popH1('The Best Place to Store Personal Media')
    index += popH2('PLEX organizes:')
    index += popReturn()
    index += popH3(popUnorderList("<li>Movies</li>"
                                  "<li>TV Shows</li>"
                                  "<li>Pictures</li>"
                                  "<li>Music Videos</li>"
                                  "<li>Home Videos</li>"))
    index += popParagraph(popLink("https://www.plex.tv/",
                                  "PLEX"))
    index += popDateTime(formattedTime, formattedDate)
    index += popEnd()
    return index

@app.route('/LearnGuitar')
def guitarIndex():
    index = popHead("A great start to learning guitar");
    index += popH1("A great start to " +  
                   popLink("https://www.chordbuddy.com/guitar-learning-system"
                           "-for-everyone/how-to-play-the-guitar-for-"
                           "beginners/", "learning guitar"))
    index += popComment('Really not that great...')
    index += popReturn()
    index += popParagraph("Whether you’re young or old, there’s no better "
                          "feeling than learning to play an instrument. While"
                          "many attempt to learn the guitar, it is "
                          "unfortunately very common for beginners to give up"
                           "after only a couple of months. Guitar lessons "
                           "with an instructor can be expensive and it can be"
                           " frustrating if you’re not seeing progress "
                           "immediately. In this article, you’ll learn about "
                           "choosing a guitar, how to play guitar chords, "
                           "how to tune a guitar, and how to hold a guitar. "
                           "You can also find out more about the ChordBuddy "
                           "guitar learning system which has shown great "
                           "success among beginner guitar players of every "
                           "age")
    index += popDateTime(formattedTime, formattedDate)
    index += popEnd()
    return index

#function shortcuts for all HTML code
@app.route('/moreHTML')
def popDateTime(time, day):
    foot = day + " ---- " + time
    final = popFooter(foot)
    return final

def popFooter(content):
    footer = "<footer>" + content + "</footer>"
    return footer
    
def popComment(comment):
    comm = "<!--" + comment + "-->"
    return comm
    
def popHead(headTitle):
    headData = "<!DOCTYPE html> "
    headData +="<head> "
    headData +="<title>" + headTitle + "</title>"
    headData +="</head>"
    headData +="<body>"
    return headData

def popReturn():
    returnSpace = "<p></p>"
    return returnSpace

def popParagraph(paragraph):
    returnPara = "<p>" + paragraph + "</p>"
    return returnPara

def popOrderList(myOrList):
    ol = "<ol style='list-style-type: decimal;'>" + myOrList + "</ol>"
    return ol

def popUnorderList(myUnorList):
    ol = "<ul style='list-style-type: circle'>" + myUnorList + "</ul>"
    return ol

def popH1(myString):
    newString = '<H1>' + myString + '</H1>'
    return newString

def popH2(myString):
    newString = '<H2>' + myString + '</H2>'
    return newString

def popH3(myString):
    newString = '<H3>' + myString + '</H3>'
    return newString

def popEnd():
    endData = "</body>"
    endData += "</html>"
    return endData

def popLink(link, words):
    link = "<a href=" + link + ">" + words + "</a>"
    return link

if __name__ == '__main__':
    app.run(debug=True)