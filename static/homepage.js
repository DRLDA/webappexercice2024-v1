//1. FUNCTIONS

//Explore all countries and display factsheet
//function exploreAllCountries() {
//    window.location.href = '/allcountryfactsheet';
//}

//fetch json data from flask
function get_json_data() {
    return fetch('/get_json_data')
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
    let searchInput = document.getElementById(`searchInput`).value.toLowerCase();
    console.log(searchInput);
    fetch(`/search?searchInput=${searchInput}`)
    .then(response => response.json())
    .then(data => {
    console.log(data);    
        if(data.length === 0) {
            alert("Country not available. Please add it using the Add Functionality.");
        } else {
            window.location.href = `/countryfactsheet/${searchInput}`;
       }
    });
}