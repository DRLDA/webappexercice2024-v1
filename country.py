#create web app "explore countries"
#import flask and json
import flask
import json


app = flask.Flask(__name__, static_url_path='/static')
json_file_path_short = '/Users/Darell/workspace/ExtensionSchool/python/20.Webapp/countryshortlistvf.json'
#json_file_path_short = '/Users/Darell/workspace/ExtensionSchool/python/20.Webapp/countryshortlistvf.json'

#function to read data from my json file
def read_json(json_file_path_short):
    #print("read_json")
    with open(json_file_path_short, mode='r') as file:
        content = file.read()
    if content: 
        data = json.loads(content)
        return data
    else:
        return None

#read the Json data from the file   
#data = read_json(json_file_path_short)

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
    return get_html("index")

@app.route("/get_json_data", methods=["GET"])
def get_json_data():
    return flask.jsonify(data)        


@app.route("/search", methods=["GET"])
def search():
    try:
        search_input = flask.request.args.get('searchInput')
        #print("Search input: {search_input}")
        found_country = next((country for country in get_json_data if country['Country'].lower() == search_input.lower()), None)

        if found_country:
            return flask.render_template('countryfactsheet.html', country=found_country)
        else:
            return "Country not found. Please add it using the Add functionality."
    except Exception as e:
        print("Error processing search request:", e)
        return "An error occurred while processing the search request."

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
