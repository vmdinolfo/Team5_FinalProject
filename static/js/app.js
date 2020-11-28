// console.log because we can
console.log("app.js");

// assign variables for button
var predictor_button = d3.select("predictorButton");

// select the form
var form = d3.select("#form");

// event handlers for clicking button or pressing enter
predictor_button.on("click", runEnter);
form.on("submit", runEnter);

// function to run for both events for search form (button click or pressing enter)
function runEnter() {

    // prevent the page from refreshing
    d3.event.preventDefault();

    // select input elements
    var genderInputElement = d3.select("#gender.form-check-input:checked");
    var hypertensionInputElement = d3.select("#hypertension.form-check-input:checked");
    var heartDiseaseInputElement = d3.select("#heartDisease.form-check-input:checked");
    var everMarriedInputElement = d3.select("#everMarried.form-check-input:checked");
    var smokingStatusInputElement = d3.select("#smokingStatusInput");
    var residenceTypeInputElement = d3.select("#residenceTypeInput");
    var workTypeInputElement = d3.select("#workTypeInput");
    var ageInputElement = d3.select("#ageInput.form-control");
    var bmiInputElement = d3.select("#bmiInput.form-control");
    var glucoseInputElement = d3.select("#glucoseInput.form-control");


    // get value from input elements
    var genderInputValue = genderInputElement.property("value");
    var hypertensionInputValue = hypertensionInputElement.property("value");
    var heartDiseaseInputValue = heartDiseaseInputElement.property("value");
    var everMarriedInputValue = everMarriedInputElement.property("value");
    var smokingStatusInputValue = smokingStatusInputElement.property("value");
    var residenceTypeInputValue = residenceTypeInputElement.property("value");
    var workTypeInputValue = workTypeInputElement.property("value");
    var ageInputValue = ageInputElement.property("value");
    var bmiInputValue = bmiInputElement.property("value");
    var glucoseInputValue = glucoseInputElement.property("value");

    console.log(`Gender Value Selected: ${genderInputValue}`);
    console.log(`Hypertension Value Selected: ${hypertensionInputValue}`);
    console.log(`Heart Disease Value Selected: ${heartDiseaseInputValue}`);
    console.log(`Ever Married Value Selected: ${everMarriedInputValue}`);
    console.log(`Smoking Status Value Selected: ${smokingStatusInputValue}`);
    console.log(`Residence Type Value Selected: ${residenceTypeInputValue}`);
    console.log(`Work Type Value Selected: ${workTypeInputValue}`);
    console.log(`Age Value Entered: ${ageInputValue}`);
    console.log(`BMI Value Entered: ${bmiInputValue}`);
    console.log(`Glucose Value Entered: ${glucoseInputValue}`);

    var values_to_send = [genderInputValue, hypertensionInputValue, heartDiseaseInputValue, everMarriedInputValue, smokingStatusInputValue, residenceTypeInputValue, workTypeInputValue, ageInputValue, bmiInputValue, glucoseInputValue]
    console.log(`Values to send to model: ${values_to_send}`);
}