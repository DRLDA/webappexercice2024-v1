//1. FUNCTIONS

//Explore all countries and display factsheet
function exploreAllCountries() {
    window.location.href = '/allcountryfactredirect';
    //    window.location.href = `D:/Code/Flask/Debug/1/webappexercice2024/service/templates/allcountryfactsheets.html`;
    //    file:///D:/Code/Flask/Debug/1/webappexercice2024/service/templates/allcountryfactsheets.html
}

//fetch json data from flask
function get_json_data() {
    /*
     * API Fetch pour effectuer une requête HTTP GET vers l'URL http://127.0.0.1:5000/get_json_data
     */

    fetch('http://127.0.0.1:5000/get_json_data')
        .then(response => {
            console.log(response);
            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.status}`);
            }
            return response.json();
        })
        .catch(error => {
            console.error('Error fetching JSON data:', error);
            throw error; // Rethrow the error to handle it in the calling code
        });
    return fetch('/get_json_data')
        .then(response => response.json());
}

//search country and display factsheet
function searchCountry() {
    //Recuperation de l'élement HTML avec id searchInput avec une conversion en minuscule a
    let searchInput = document.getElementById(`searchInput`).value.toLowerCase();
    //console.log(searchInput);  
    //Lancement d'une requête GET vers une URL spécifique avec la valeur searchinput
    fetch(`http://127.0.0.1:5000/search?searchInput=${searchInput}`, {
            method: 'GET'
        })
        // promesse qui traite la réponse d'une requete http avec conversion de la réposne en json
        .then(response => response.json(), )
        // Promess json qui traite les data json récupérées à partir de la réponse de la requetre

    .then(data => {
        console.log(data);
        if (!data.success) {
            alert("Pays non disponible Country not available. Please add it using the Add Functionality.");
        } else {
            //window.location.href = `/countryfactsheet/${searchInput}`;
            sessionStorage.setItem("currentSearch", JSON.stringify(data.data))
                // window.location.href = `D:/Code/Flask/Debug/1/webappexercice2024/service/templates/countryfactsheet.html`;
            window.location.href = `/searchspecificcountryredirect`;
        }
    });
}

//Add new country in records
function addCountry() {
    let countryName = document.getElementById(`addCountryInput`).value;
    fetch(`http://127.0.0.1:5000/addcountry`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "countryName": countryName
            })
        })
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                alert("Error while saving new Country. Try again later!");
            } else {
                sessionStorage.setItem("currentSearch", JSON.stringify(data.data))
                window.location.href = `D:/Code/Flask/Debug/1/webappexercice2024/service/templates/countryfactsheet.html`;
            }
        });
}