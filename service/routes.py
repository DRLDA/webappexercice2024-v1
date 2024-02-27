#create web app "explore countries"
#import flask and json
import flask
import json

from flask import request, redirect, url_for

from service import app

#app = flask.Flask(__name__, static_url_path='/static')
json_file_path_short = 'D:\Code\Flask\Debug\webappexercice2024\countryshortlistvf.json'
country_list_json_file_path = 'D:\Code\Flask\Debug\webappexercice2024\countryfactsheetDBvf.json'
  #json_file_path_short = '/Users/Darell/workspace/ExtensionSchool/python/20.Webapp/countryshortlistvf.json'

#function to read data from my json file
def read_json(): ##Suppression du paramètre
    #print("read_json")
    with open(json_file_path_short, mode='r') as file:
        content = file.read()
    if content: 
        data = json.loads(content)
        return data
    else:
        return None
    
def write_to_json(new_data):
    # Lire le contenu actuel du fichier JSON
    with open(json_file_path_short, mode='r') as file:
        content = file.read()
    
    # Convertir le contenu en une structure de données Python
    if content:
        data = json.loads(content)
    else:
        data = {"country_details": []}

    # Ajouter de nouvelles données au tableau country_details
    data["country_details"].append(new_data)

    # Écrire la nouvelle structure de données dans le fichier JSON
    with open(json_file_path_short, mode='w') as file:
        json.dump(data, file, indent=2)

#read the Json data from the file   
data = read_json()

#first variable to get first html page
def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

#to get-read country recorded in country short list
def get_country():
    with open("countryshortlistvf.json") as countryshortlist:
        data = json.load(countryshortlist) 
        return data

#APP ROUTES
@app.route("/")
def homepage(): 
    return flask.render_template('./index.html')

@app.route("/get_json_data", methods=["GET"])
def get_json_data():
    return flask.jsonify(data)        

@app.route("/search", methods=["GET"])
def search():
    try:
        search_input = flask.request.args.get('searchInput')
        found_country = next((country for country in data['country_details'] if country['Country'].lower() == search_input.lower()), None)
        found_countrys = "fred"

        if found_country:
            return flask.jsonify({"data": found_country,"success":True})
            return flask.render_template('countryfactsheet.html', countryss=found_countrys)
        else:
            return flask.jsonify({"data": {},"success":False})
            #return "Country not found. Please add it using the Add functionality."
    except Exception as e:
        print("Error processing search request:", e)
        return flask.jsonify({"data": e,"success":False})
        #return "An error occurred while processing the search request."

#@app.route("/countryfactsheet/<country_name>")
#def country_factsheet(country_name):
#    country_data = next((country for country in csv_data if country['Country'].lower() == country_name.lower()), None)
#    print("Country Data:", country_data)
#    return flask.render_template('countryfactsheet.html', country=country_data)

@app.route("/countryfactsheet/<country_name>")
def country_factsheet(country_name):
    try:
        country_data = next((country for country in data if country['Country'].lower() == country_name.lower()), None)
        print("Country Data:", country_data)
        if country_data:
            return flask.render_template('countryfactsheet.html', country=country_data)
        else:
            return "Country not found. Please add it using the Add functionality."
    except Exception as e:
        print("Error processing request:", e)
        return "An error occurred while processing the request."
    

@app.route("/addcountry", methods= ["POST"])
def add_country():
    country_name =  request.json['countryName']
    try:
        new_data = {
            "Country": country_name,
            "Density": 109,
            "Birth_Rate": 9.7,
            "Capital": "Lol",
            "GDP": "446,314,739,528",
            "Life_expectancy": 81.6,
            "Official_language": "Lol",
            "Unemployment_rate": 4.67,
            "Urban_population": "5,194,416",
            "Latitude": 47.516231,
            "Longitude": 14.550072
        }
        write_to_json(new_data)
        return flask.jsonify({"data": new_data,"success":True})
    except Exception as e:
        print("Error processing request:", e)
        return "An error occurred while processing the request."

# Redirection passant par un chemin intermédiaire pour lister les pays
@app.route("/allcountryfactredirect")
def redirection():
    return redirect(url_for('allcountrysheet'))

@app.route('/allcountrysheet')
def allcountrysheet():
    liste  = []
    with open(country_list_json_file_path, mode='r') as file:
        content = file.read()
    if content: 
        #chargement des données json à partir du fichier 
        data = json.loads(content)
        # for line in file:
            # liste.append(line)
        # return data
        # focntion flask.jsonify renvoie une response data
        # country =  flask.jsonify({"data": data,"success":True})
        # liste =  flask.jsonify({"data": data,"success":True})

        return flask.render_template("allcountryfactsheets.html", liste = data)

    
    else:
        return flask.render_template("allcountryfactsheets.html", liste = None)


    

    # return flask.render_template("allcountryfactsheets.html", liste=liste)
    return flask.render_template("allcountryfactsheets.html" )

# Redirectection pasant par un chemin intermédiaire pour afficher le resultat d'une recherche d'un pays
@app.route('/searchspecificcountryredirect')
def redirectionPays():
    return redirect(url_for('showcountry'))

@app.route('/showcountry')
def showcountry():
    return flask.render_template('showcountry.html')
