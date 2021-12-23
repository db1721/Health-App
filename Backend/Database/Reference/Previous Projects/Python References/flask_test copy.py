from flask import Flask, request, redirect
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
    index += popParagraph(popLink("http://localhost:5000/Form",
                                  "Go to a picking your favorite media form"))
    index += popImage("static/home.jpg", "This is the home page image")
    index += popDateTime(formattedTime, formattedDate)
    index += popEnd()
    return index

@app.route('/MakeRecipe')
def recipeIndex():
    index = popHead("The Best Recipe!!");
    index += popH1('This is the best recipe for Keto Chocolate Mouse')
    index += popReturn()
    index += popImage("static/mousse.jpg", "Keto mousse")
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
    index = popHead("The Best Place to Store Personal Media")
    index += popH1('The Best Place to Store Personal Media')
    index += popImage("static/plex1.png", "Plex logo")
    index += popH2('PLEX organizes:')
    index += popReturn()
    index += popH3(popUnorderList("<li>Movies</li>"
                                  "<li>TV Shows</li>"
                                  "<li>Pictures</li>"
                                  "<li>Music Videos</li>"
                                  "<li>Home Videos</li>"))
    index += plexTableBuild()
    index += popParagraph(popLink("https://www.plex.tv/",
                                  "PLEX"))
    index += popImage("static/plex.jpg", "Plex screenshot")
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
    index += popImage("static/guitar.jpg", "Guitar")
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

@app.route('/Form')
def formIndex():
    index = plexBuildForm()
    return index

@app.route('/Submitted', methods = ['POST'])
def submitted():
    favMedia1 = request.form['med']
    favMedia2 = request.form['med2']
    favEx = request.form['explain']
    print(favMedia1 + favMedia2 + favEx)
    f= open("Favorite Media.txt","w+")
    f.write("Your favorite media is " + favMedia1 + " and " + favMedia2 + 
            " because " + favEx)
    return redirect('/home')

#function shortcuts for all HTML code
@app.route('/moreHTML')
def plexBuildForm():  
    
    #Begin build
    bLabel = "<!DOCTYPE html>"
    bLabel += "<head>"
    bLabel += "<form action='/Submitted' method='post'>"
    bLabel += "<div>"
    bLabel += "<label>"
    bLabel += "Your favorite "
    bLabel += "<input id='mediachoice' list='media'>"
    bLabel += "</label>"
    bLabel += "</div>"
    
    #textbox for input
    bLabel += "<label for='mediaSelection'>are: </label>"
    bLabel += "<input type='text' name='med' id='mediaSelection'></input>"
    
    #textbox for input2
    bLabel += "<label for='mediaSelection'>and </label>"
    bLabel += "<input type='text' name='med2' id='mediaSelection2'></input>"
    
    #textbox
    bLabel += "<br/>"
    bLabel += "<label for='exlpain' style='display: block;'>"
    bLabel += "Why are theses your favorite?.</label>"
    bLabel += "<textarea name='explain' rows='10' cols='60'>"
    bLabel += "Enter explanation here"
    bLabel += "</textarea>"
    
    #post button
    bLabel += "<br/>"
    bLabel += "<input type='submit' class='submit' value='Post'></input>"
    bLabel += "<input type='reset' value='Clear Form'>"
    bLabel += "</form>"

    #dropdown list
    bLabel += "<datalist id='media'>"
    bLabel += "<label>"
    bLabel += "select from a list:"
    bLabel += "<select name='mediaoption'>"
    bLabel += "<option value=''>"
    bLabel += "<option>Movies"
    bLabel += "<option>TV Shows"
    bLabel += "</select>"
    bLabel += "</label>"
    
    #End build
    bLabel += "</body>"
    bLabel += "</html>"
    
    return bLabel
    
def plexTableBuild():
    table = "<table border='4' style='width:60%;'>"
    table += "<caption>Favorites of Plex</caption>"
    table += "<tr>"
    table += "<th width='15%'>Media</th>"
    table += "<th width='30%'>Favorite Title</th>"
    table += "<th width='15%'>Times Watched</th>"
    table += "</tr>"
    table += "<tr>"
    table += "<td>Movie</td>"
    table += "<td>The Grinch</td>"
    table += "<td>20</td>"
    table += "</tr>"
    table += "<tr>"
    table += "<td>Movie</td>"
    table += "<td>The Princess Bride</td>"
    table += "<td>15</td>"
    table += "</tr>"
    table += "<tr>"
    table += "<td>TV Show</td>"
    table += "<td>The Office</td>"
    table += "<td>500</td>"
    table += "</tr>"
    table += "<tr>"
    table += "<td>TV Show</td>"
    table += "<td>The Big Bang Theory</td>"
    table += "<td>10</td>"
    table += "</tr>"
    table += "</table>"
    return table
    
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

def popImage(imageSource, altText):
    image = "<img src=" + imageSource + " alt=" + altText + ">"
    return image

def popEnd():
    endData = "</body>"
    endData += "</html>"
    return endData

def popLink(link, words):
    link = "<a href=" + link + ">" + words + "</a>"
    return link

if __name__ == '__main__':
    app.run(debug=True)